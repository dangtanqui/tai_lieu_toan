#!/usr/bin/env python3
"""Download Tutorialspoint images for *.txt in this folder."""

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
    "1. regression analysis.txt": "01_regression_analysis",
    "2. linear regression.txt": "02_linear_regression",
    "3. simple linear regression.txt": "03_simple_linear_regression",
    "4. multiple linear regression.txt": "04_multiple_linear_regression",
    "5. polynomial regression.txt": "05_polynomial_regression",
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
        if len(data) < 5000:
            continue
        ext = os.path.splitext(urlparse(img_url).path)[1].lower() or ".png"
        rel = f"images/{slug}/img{i:02d}{ext}"
        with open(os.path.join(HERE, rel), "wb") as f:
            f.write(data)
        out.append({"url": img_url, "file": rel})
    return {"page_url": url, "slug": slug, "images": out}


def main() -> int:
    results = []
    for fname in sorted(f for f in os.listdir(HERE) if f.endswith(".txt")):
        with open(os.path.join(HERE, fname), encoding="utf-8", errors="ignore") as f:
            url = f.readline().strip()
        if not url.startswith("http"):
            continue
        slug = MAPPING.get(fname.lower(), slugify(fname))
        results.append(download_page(url, slug))
    with open(os.path.join(HERE, "images_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Done: {len(results)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
