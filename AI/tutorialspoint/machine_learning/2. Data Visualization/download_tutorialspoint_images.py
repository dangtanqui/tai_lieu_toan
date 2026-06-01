#!/usr/bin/env python3
"""
Download images from Tutorialspoint pages referenced by *.txt in this folder.

Inputs:
  - Each .txt file's first line is the Tutorialspoint URL.
Outputs:
  - images/<slug>/imgXX.<ext>
  - tex/_figures/<slug>.tex (LaTeX snippet; optional reference)

Filters ads/UI assets. See 1. Basic/download_tutorialspoint_images.py for details.
"""

from __future__ import annotations

import os
import re
import sys
import json
import urllib.request
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")
FIG_DIR = os.path.join(HERE, "tex", "_figures")

IMG_EXTS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"[^a-z0-9_]+", "", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name or "page"


def read_first_url(txt_path: str) -> str | None:
    with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
        first = f.readline().strip()
    if first.startswith("http://") or first.startswith("https://"):
        return first
    return None


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/122.0 Safari/537.36"
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def extract_img_srcs(html: str, base_url: str) -> list[str]:
    srcs = re.findall(r"""<img[^>]+src=["']([^"']+)["']""", html, flags=re.I)
    out: list[str] = []
    for src in srcs:
        src = src.strip()
        if not src:
            continue
        out.append(urljoin(base_url, src))
    return out


def looks_like_content_image(url: str) -> bool:
    u = url.lower()
    if not u.endswith(IMG_EXTS):
        return False
    bad_tokens = [
        "logo",
        "icon",
        "sprite",
        "ads",
        "doubleclick",
        "googlesyndication",
        "facebook",
        "twitter",
        "linkedin",
        "tutorix",
        "googleplay",
        "appstore",
        "run-button",
    ]
    if any(t in u for t in bad_tokens):
        return False
    return True


def stable_name(url: str, idx: int) -> str:
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext not in IMG_EXTS:
        ext = ".png"
    return f"img{idx:02d}{ext}"


def download_images_for_page(page_url: str, slug: str) -> dict:
    html_bytes = fetch(page_url)
    html = html_bytes.decode("utf-8", errors="ignore")
    srcs = extract_img_srcs(html, page_url)

    filtered = []
    seen = set()
    for s in srcs:
        if s in seen:
            continue
        seen.add(s)
        if looks_like_content_image(s):
            filtered.append(s)

    page_dir = os.path.join(IMAGES_DIR, slug)
    os.makedirs(page_dir, exist_ok=True)

    downloaded = []
    for i, img_url in enumerate(filtered, start=1):
        try:
            data = fetch(img_url)
        except Exception:
            continue
        if len(data) < 5_000:
            continue
        fname = stable_name(img_url, i)
        out_path = os.path.join(page_dir, fname)
        with open(out_path, "wb") as f:
            f.write(data)
        downloaded.append(
            {
                "url": img_url,
                "file": os.path.relpath(out_path, HERE).replace(os.sep, "/"),
                "bytes": len(data),
            }
        )

    return {"page_url": page_url, "slug": slug, "images": downloaded}


def write_fig_tex(slug: str, images: list[dict]) -> None:
    os.makedirs(FIG_DIR, exist_ok=True)
    tex_path = os.path.join(FIG_DIR, f"{slug}.tex")
    if not images:
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write("% (no images found)\n")
        return

    lines = [
        "% Auto-generated figures for this section\n",
        "\\begin{vidu}[title={Hình minh họa từ nguồn}]\n",
    ]
    for idx, img in enumerate(images, start=1):
        rel_file = img["file"].replace("images/", "")
        lines.append(f"\\tsimg{{{rel_file}}}\n")
        lines.append("\\begin{center}\\footnotesize ")
        lines.append(f"Hình {idx}. Nguồn: \\tsurl{{{img['url']}}}")
        lines.append("\\end{center}\n\n")
    lines.append("\\end{vidu}\n")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> int:
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(FIG_DIR, exist_ok=True)

    mapping = {
        "1. data visualization.txt": "01_data_visualization",
        "2. histograms.txt": "02_histograms",
        "3. density plots.txt": "03_density_plots",
        "4. box and whisker plots.txt": "04_box_whisker_plots",
        "5. correlation matrix plot.txt": "05_correlation_matrix_plot",
        "6. scatter matrix plot.txt": "06_scatter_matrix_plot",
    }

    txt_files = sorted(
        f
        for f in os.listdir(HERE)
        if f.lower().endswith(".txt") or f.lower().endswith(".text")
    )

    results = []
    for fname in txt_files:
        path = os.path.join(HERE, fname)
        url = read_first_url(path)
        if not url:
            continue
        key = fname.strip().lower()
        slug = mapping.get(key, slugify(os.path.splitext(fname)[0]))
        info = download_images_for_page(url, slug)
        results.append(info)

    by_slug: dict[str, list[dict]] = {}
    for r in results:
        by_slug.setdefault(r["slug"], []).extend(r["images"])

    for slug, imgs in by_slug.items():
        seen = set()
        uniq = []
        for img in imgs:
            if img["url"] in seen:
                continue
            seen.add(img["url"])
            uniq.append(img)
        write_fig_tex(slug, uniq)

    with open(os.path.join(HERE, "images_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Downloaded images for {len(results)} pages. Wrote _figures snippets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
