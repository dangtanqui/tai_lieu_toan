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
    "1. clustering algorithms.txt": "01_clustering_algorithms",
    "2. centroid-based clustering.txt": "02_centroid_based",
    "3. k-means clustering algorithm.txt": "03_k_means",
    "4. k-medoids clustering.txt": "04_k_medoids",
    "5. mean-shift clustering algorithm.txt": "05_mean_shift",
    "6. hierarchical clustering.txt": "06_hierarchical",
    "7. density based clustering.txt": "07_density_based",
    "8. dbscan clustering.txt": "08_dbscan",
    "9. optics clustering.txt": "09_optics",
    "10. hdbscan clustering.txt": "10_hdbscan",
    "11. birch clustering.txt": "11_birch",
    "12. affinity propagation.txt": "12_affinity_propagation",
    "13. distribution-based clustering.txt": "13_distribution_based",
    "14. agglomerative clustering": "14_agglomerative",
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
        if fname.endswith(".txt") or fname == "14. Agglomerative Clustering":
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
