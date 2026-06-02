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
    "1. classification algorithms.txt": "01_classification_algorithms",
    "2. logistic regression.txt": "02_logistic_regression",
    "3. k-nearest neighbors (knn).txt": "03_knn",
    "4. nave bayes algorithm.txt": "04_naive_bayes",
    "5. decision tree algorithm.txt": "05_decision_tree",
    "6. support vector machine (svm).txt": "06_svm",
    "7. random forest algorithm.txt": "07_random_forest",
    "8. confusion matrix.txt": "08_confusion_matrix",
    "9. stochastic gradient descent.txt": "09_stochastic_gradient_descent",
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
    for r in results:
        print(f"  {r['slug']}: {len(r['images'])} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
