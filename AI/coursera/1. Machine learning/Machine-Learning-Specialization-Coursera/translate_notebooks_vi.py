#!/usr/bin/env python3
"""Translate Coursera lab notebooks to Vietnamese (_vi.ipynb)."""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".ipynb_checkpoints", "archive"}
TRANSLATOR = GoogleTranslator(source="en", target="vi")
CACHE: dict[str, str] = {}
CHUNK_SIZE = 4500
SLEEP_SEC = 0.15


PROTECT_TERMS = [
    "Python", "python", "Jupyter", "NumPy", "numpy", "TensorFlow", "tensorflow",
    "scikit-learn", "sklearn", "matplotlib", "pandas", "SymPy", "Coursera",
    "f-string", "f strings", "Markdown", "markdown", "code cell", "Code Cell",
    "gradient descent", "Gradient Descent", "logistic regression", "linear regression",
    "neural network", "backpropagation", "softmax", "ReLU", "sigmoid", "overfitting",
    "regularization", "K-means", "PCA", "collaborative filtering", "reinforcement learning",
    "decision tree", "random forest", "XGBoost", "gradient boosting",
]


def protect_terms(text: str) -> tuple[str, list[tuple[str, str]]]:
    store: list[tuple[str, str]] = []
    for term in sorted(PROTECT_TERMS, key=len, reverse=True):
        if term in text:
            placeholder = f"⟪T{len(store)}⟫"
            store.append((placeholder, term))
            text = text.replace(term, placeholder)
    return text, store


def restore_terms(text: str, store: list[tuple[str, str]]) -> str:
    for placeholder, term in store:
        text = text.replace(placeholder, term)
    return text


def translate_text(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text in CACHE:
        return CACHE[text]
    term_protected, term_store = protect_terms(text)
    try:
        if len(term_protected) <= CHUNK_SIZE:
            out = TRANSLATOR.translate(term_protected)
        else:
            parts = []
            for i in range(0, len(term_protected), CHUNK_SIZE):
                chunk = term_protected[i : i + CHUNK_SIZE]
                parts.append(TRANSLATOR.translate(chunk))
                time.sleep(SLEEP_SEC)
            out = "".join(parts)
        out = restore_terms(out, term_store)
        CACHE[text] = out
        time.sleep(SLEEP_SEC)
        return out
    except Exception as exc:
        print(f"  [warn] translate failed: {exc!r} -> keep original", file=sys.stderr)
        return text


def protect_segments(text: str) -> tuple[str, list[str]]:
    """Replace code/math/html segments with placeholders."""
    store: list[str] = []

    def repl(match: re.Match[str]) -> str:
        store.append(match.group(0))
        return f"⟦{len(store) - 1}⟧"

    patterns = [
        r"```[\s\S]*?```",
        r"!\[[^\]]*\]\([^)]+\)",
        r"\[`[^`]*`\]\([^)]+\)",  # links with inline code: [`exp()`](url)
        r"\[[^\]]+\]\([^)]+\)",
        r"`[^`\n]+`",
        r"\$\$[\s\S]*?\$\$",
        r"\$[^$\n]+\$",
        r"<figure>[\s\S]*?</figure>",
        r"<[^>]+>",
        r"https?://\S+",
        r"\./[\w./-]+",
    ]
    protected = text
    for pat in patterns:
        protected = re.sub(pat, repl, protected)
    return protected, store


def restore_segments(text: str, store: list[str]) -> str:
    for i, seg in enumerate(store):
        text = text.replace(f"⟦{i}⟧", seg)
    return text


def translate_markdown(source: str) -> str:
    if isinstance(source, list):
        joined = "".join(source)
        translated = translate_markdown(joined)
        return [translated]
    protected, store = protect_segments(source)
    translated = translate_text(protected)
    return restore_segments(translated, store)


def translate_code_line(line: str) -> str:
    stripped = line.lstrip()
    if stripped.startswith("#"):
        indent = line[: len(line) - len(stripped)]
        comment = stripped[1:]
        if comment.startswith("!") or "UNQ_" in comment or "GRADED" in comment.upper():
            return line
        if comment.strip().startswith("grade"):
            return line
        translated = translate_text(comment.strip())
        return f"{indent}# {translated}"
    return line


def translate_code_source(source: str | list[str]) -> list[str]:
    if isinstance(source, str):
        lines = source.splitlines(keepends=True)
    else:
        lines = []
        for part in source:
            lines.extend(part.splitlines(keepends=True))
    return [translate_code_line(line) for line in lines]


def should_process(path: Path) -> bool:
    if path.name.endswith("_vi.ipynb"):
        return False
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix == ".ipynb"


def process_notebook(src: Path) -> Path:
    dst = src.with_name(f"{src.stem}_vi{src.suffix}")
    with src.open(encoding="utf-8") as f:
        nb = json.load(f)

    for cell in nb.get("cells", []):
        ctype = cell.get("cell_type")
        if ctype == "markdown":
            src_text = cell.get("source", "")
            if isinstance(src_text, list):
                full = "".join(src_text)
            else:
                full = src_text
            cell["source"] = translate_markdown(full).splitlines(keepends=True)
            if cell["source"] and not cell["source"][-1].endswith("\n"):
                cell["source"][-1] += "\n"
        elif ctype == "code":
            cell["source"] = translate_code_source(cell.get("source", ""))

    with dst.open("w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    return dst


def main() -> None:
    targets = sorted(p for p in ROOT.rglob("*.ipynb") if should_process(p))
    print(f"Found {len(targets)} notebooks")
    for i, src in enumerate(targets, 1):
        rel = src.relative_to(ROOT)
        print(f"[{i}/{len(targets)}] translating: {rel}", flush=True)
        try:
            out = process_notebook(src)
            print(f"  -> {out.name}")
        except Exception as exc:
            print(f"  ERROR: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
