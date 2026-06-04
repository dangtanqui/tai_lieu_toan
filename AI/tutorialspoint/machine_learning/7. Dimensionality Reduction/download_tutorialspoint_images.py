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
    "1. dimensionality reduction.txt": "01_dimensionality_reduction",
    "2. feature selection.txt": "02_feature_selection",
    "3. feature extraction.txt": "03_feature_extraction",
    "4. backward elimination.txt": "04_backward_elimination",
    "5. forward feature construction.txt": "05_forward_feature_construction",
    "6. high correlation filter.txt": "06_high_correlation_filter",
    "7. low variance filter.txt": "07_low_variance_filter",
    "8. missing values ratio.txt": "08_missing_values_ratio",
    "9. principal component analysis.txt": "09_principal_component_analysis",
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
        if not os.path.isfile(path):
            continue
        if fname.endswith(".txt"):
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
