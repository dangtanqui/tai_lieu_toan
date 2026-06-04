#!/usr/bin/env python3
"""Download images from machinelearningcoban.com gradient descent pages."""

from __future__ import annotations

import os
import re
import json
import urllib.request
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")

PAGES = [
    ("https://machinelearningcoban.com/2017/01/12/gradientdescent/", "01_gradient_descent_part1"),
    ("https://machinelearningcoban.com/2017/01/16/gradientdescent2/", "02_gradient_descent_part2"),
]

BAD = ["logo", "icon", "sprite", "ads", "gravatar", "facebook", "twitter"]


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
        if full not in seen and not any(b in full.lower() for b in BAD):
            seen.add(full)
            srcs.append(full)
    os.makedirs(os.path.join(IMAGES_DIR, slug), exist_ok=True)
    out = []
    for i, img_url in enumerate(srcs, 1):
        try:
            data = fetch(img_url)
        except Exception:
            continue
        if len(data) < 2000:
            continue
        ext = os.path.splitext(urlparse(img_url).path)[1].lower()
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
            ext = ".png"
        rel = f"images/{slug}/img{i:02d}{ext}"
        with open(os.path.join(HERE, rel), "wb") as f:
            f.write(data)
        out.append({"url": img_url, "file": rel})
    return {"page_url": url, "slug": slug, "images": out}


def main() -> int:
    results = [download_page(url, slug) for url, slug in PAGES]
    with open(os.path.join(HERE, "images_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    for r in results:
        print(f"  {r['slug']}: {len(r['images'])} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
