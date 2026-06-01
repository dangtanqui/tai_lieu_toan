#!/usr/bin/env python3
"""Download Tutorialspoint images for *.txt in this folder. See 1. Basic/ script."""

from __future__ import annotations

import os
import re
import json
import urllib.request
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")
FIG_DIR = os.path.join(HERE, "tex", "_figures")
IMG_EXTS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")

MAPPING = {
    "1. statistics.txt": "01_statistics",
    "2. mean median mode.txt": "02_mean_median_mode",
    "3. standard deviation.txt": "03_standard_deviation",
    "4. percentiles.txt": "04_percentiles",
    "5. data distribution.txt": "05_data_distribution",
    "6. skewness and kurtosis.txt": "06_skewness_kurtosis",
    "7. bias and variance.txt": "07_bias_variance",
    "8. hypothesis.txt": "08_hypothesis",
}

BAD_TOKENS = [
    "logo", "icon", "sprite", "ads", "doubleclick", "googlesyndication",
    "facebook", "twitter", "linkedin", "tutorix", "googleplay", "appstore", "run-button",
]


def slugify(name: str) -> str:
    name = re.sub(r"[^a-z0-9_]+", "_", name.strip().lower())
    return re.sub(r"_+", "_", name).strip("_") or "page"


def read_first_url(path: str) -> str | None:
    with open(path, encoding="utf-8", errors="ignore") as f:
        first = f.readline().strip()
    return first if first.startswith("http") else None


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/122.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def extract_img_srcs(html: str, base: str) -> list[str]:
    srcs = re.findall(r"""<img[^>]+src=["']([^"']+)["']""", html, re.I)
    return [urljoin(base, s.strip()) for s in srcs if s.strip()]


def looks_like_content(url: str) -> bool:
    u = url.lower()
    return u.endswith(IMG_EXTS) and not any(t in u for t in BAD_TOKENS)


def stable_name(url: str, idx: int) -> str:
    ext = os.path.splitext(urlparse(url).path)[1].lower()
    return f"img{idx:02d}{(ext if ext in IMG_EXTS else '.png')}"


def download_page(page_url: str, slug: str) -> dict:
    html = fetch(page_url).decode("utf-8", errors="ignore")
    seen, filtered = set(), []
    for s in extract_img_srcs(html, page_url):
        if s not in seen and looks_like_content(s):
            seen.add(s)
            filtered.append(s)
    page_dir = os.path.join(IMAGES_DIR, slug)
    os.makedirs(page_dir, exist_ok=True)
    downloaded = []
    for i, img_url in enumerate(filtered, 1):
        try:
            data = fetch(img_url)
        except Exception:
            continue
        if len(data) < 5000:
            continue
        rel = f"images/{slug}/{stable_name(img_url, i)}"
        with open(os.path.join(HERE, rel), "wb") as f:
            f.write(data)
        downloaded.append({"url": img_url, "file": rel.replace(os.sep, "/"), "bytes": len(data)})
    return {"page_url": page_url, "slug": slug, "images": downloaded}


def main() -> int:
    os.makedirs(IMAGES_DIR, exist_ok=True)
    results = []
    for fname in sorted(f for f in os.listdir(HERE) if f.lower().endswith(".txt")):
        url = read_first_url(os.path.join(HERE, fname))
        if not url:
            continue
        slug = MAPPING.get(fname.strip().lower(), slugify(fname))
        results.append(download_page(url, slug))
    with open(os.path.join(HERE, "images_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Downloaded images for {len(results)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
