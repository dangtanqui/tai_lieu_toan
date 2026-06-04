#!/usr/bin/env python3
"""Download Tutorialspoint images for sources in this folder."""

from __future__ import annotations

import os
import re
import json
import urllib.request
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")
IMG_EXTS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")

MAPPING = {
    "1. reinforcement learning algorithms.txt": "01_reinforcement_learning_algorithms",
    "2. exploitation and exploration.txt": "02_exploitation_exploration",
    "3. q-learning.txt": "03_q_learning",
    "4. reinforce algorithm.txt": "04_reinforce",
    "5. sarsa reinforcement learning.txt": "05_sarsa",
    "6. actor-critic reinforcement learning method.txt": "06_actor_critic",
    "7. monte carlo methods for reinforcement learning.txt": "07_monte_carlo",
    "8. temporal difference learning.txt": "08_temporal_difference",
}

BAD = ["logo", "icon", "sprite", "ads", "tutorix", "googleplay", "appstore", "run-button",
       "facebook", "twitter", "linkedin", "doubleclick", "googlesyndication"]


def slugify(n: str) -> str:
    n = re.sub(r"[^a-z0-9_]+", "_", n.strip().lower())
    return re.sub(r"_+", "_", n).strip("_") or "page"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def download_page(url: str, slug: str) -> dict:
    html = fetch(url).decode("utf-8", errors="ignore")
    srcs = []
    seen = set()
    for s in re.findall(r"""<img[^>]+src=["']([^"']+)["']""", html, re.I):
        full = urljoin(url, s.strip())
        if full not in seen and full.lower().endswith(IMG_EXTS) and not any(b in full.lower() for b in BAD):
            seen.add(full)
            srcs.append(full)
    os.makedirs(os.path.join(IMAGES_DIR, slug), exist_ok=True)
    out = []
    for i, img_url in enumerate(srcs, 1):
        try:
            data = fetch(img_url)
        except Exception:
            continue
        if len(data) < 3000:
            continue
        ext = os.path.splitext(urlparse(img_url).path)[1].lower() or ".png"
        rel = f"images/{slug}/img{i:02d}{ext}"
        with open(os.path.join(HERE, rel), "wb") as f:
            f.write(data)
        out.append({"url": img_url, "file": rel})
    return {"page_url": url, "slug": slug, "images": out}


def iter_sources():
    for fname in sorted(os.listdir(HERE)):
        path = os.path.join(HERE, fname)
        if os.path.isfile(path) and fname.endswith(".txt"):
            yield fname, path


def main() -> int:
    results = []
    for fname, path in iter_sources():
        with open(path, encoding="utf-8", errors="ignore") as f:
            url = f.readline().strip()
        if not url.startswith("http"):
            continue
        slug = MAPPING.get(fname.lower(), slugify(fname))
        results.append(download_page(url, slug))
    with open(os.path.join(HERE, "images_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Done: {len(results)} pages")
    for r in results:
        print(f"  {r['slug']}: {len(r['images'])} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
