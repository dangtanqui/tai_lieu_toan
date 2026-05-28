#!/usr/bin/env python3
"""Convert .svg files in given directories to .png for pdflatex."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def convert_one(svg: Path) -> bool:
    png = svg.with_suffix(".png")
    if png.exists() and png.stat().st_mtime >= svg.stat().st_mtime:
        print(f"skip (up to date): {png}")
        return True

    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        r = subprocess.run([rsvg, "-w", "1200", str(svg), "-o", str(png)], capture_output=True)
        if r.returncode == 0:
            print(f"rsvg: {png}")
            return True

    inkscape = shutil.which("inkscape")
    if inkscape:
        r = subprocess.run(
            [inkscape, str(svg), "--export-type=png", f"--export-filename={png}"],
            capture_output=True,
        )
        if r.returncode == 0:
            print(f"inkscape: {png}")
            return True

    convert = shutil.which("convert")
    if convert:
        r = subprocess.run(
            [convert, "-density", "300", "-background", "white", str(svg), str(png)],
            capture_output=True,
        )
        if r.returncode == 0:
            print(f"convert: {png}")
            return True

    print(f"FAILED: {svg} (install rsvg-convert, inkscape, or imagemagick)", file=sys.stderr)
    return False


def main() -> int:
    roots = [Path(p) for p in sys.argv[1:]] or []
    if not roots:
        print("usage: svg_to_png.py DIR [DIR ...]", file=sys.stderr)
        return 2

    ok = True
    for root in roots:
        for svg in sorted(root.rglob("*.svg")):
            ok = convert_one(svg) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
