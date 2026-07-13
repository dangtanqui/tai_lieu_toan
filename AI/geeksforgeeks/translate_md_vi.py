#!/usr/bin/env python3
"""Translate English Markdown files under AI/geeksforgeeks to Vietnamese.

Pipeline:
  1. Protect Markdown structure (code fences, images, links, inline code, math)
  2. Protect domain English terms (customizable PROTECT_TERMS)
  3. Google Translate EN -> VI
  4. Restore protected segments + post-fix common mistranslations
  5. Write sibling file with ``_vi`` suffix (e.g. ly_thuyet.md -> ly_thuyet_vi.md)

Usage:
  # Dịch một file
  python translate_md_vi.py path/to/ly_thuyet.md

  # Dịch tất cả .md dưới thư mục (mặc định = thư mục chứa script)
  python translate_md_vi.py
  python translate_md_vi.py --dir machine-learning

  # Thêm thuật ngữ giữ tiếng Anh (file, mỗi dòng một term)
  python translate_md_vi.py --extra-terms my_terms.txt

  # Ép dịch lại (bỏ qua cache / file _vi đã có)
  python translate_md_vi.py --force
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent
CACHE_FILE = ROOT / ".translate_cache_vi.json"

TRANSLATOR = GoogleTranslator(source="en", target="vi")
CACHE: dict[str, str] = {}
CHUNK_SIZE = 4500
SLEEP_SEC = 0.12

SKIP_DIRS = {".git", ".ipynb_checkpoints", "__pycache__", "node_modules"}
SKIP_NAME_SUFFIXES = ("_vi.md", "_vi.markdown")

# ---------------------------------------------------------------------------
# Thuật ngữ giữ tiếng Anh (có thể mở rộng bằng --extra-terms)
# Multi-word trước; script sort theo độ dài khi protect.
# ---------------------------------------------------------------------------
PROTECT_TERMS: list[str] = [
  # Platforms / tools
  "GeeksforGeeks", "scikit-learn", "TensorFlow", "tensorflow", "PyTorch",
  "matplotlib", "NumPy", "numpy", "pandas", "sklearn", "Python", "python",
  "Keras", "keras", "Jupyter", "Markdown",
  # Multi-word ML
  "principal component analysis", "Principal Component Analysis",
  "reinforcement learning", "Reinforcement Learning",
  "unsupervised learning", "Unsupervised Learning",
  "supervised learning", "Supervised Learning",
  "semi-supervised learning", "Semi-Supervised Learning",
  "machine learning", "Machine Learning",
  "deep learning", "Deep Learning",
  "natural language processing", "Natural Language Processing",
  "computer vision", "Computer Vision",
  "gradient boosting", "Gradient Boosting",
  "gradient descent", "Gradient Descent",
  "logistic regression", "Logistic Regression",
  "linear regression", "Linear Regression",
  "polynomial regression", "Polynomial Regression",
  "random forest", "Random Forest",
  "decision tree", "Decision Tree", "decision trees", "Decision Trees",
  "support vector machine", "Support Vector Machine",
  "support vector machines", "Support Vector Machines",
  "k-nearest neighbors", "K-Nearest Neighbors", "K-nearest neighbor",
  "neural network", "Neural Network", "neural networks", "Neural Networks",
  "convolutional neural network", "Convolutional Neural Network",
  "recurrent neural network", "Recurrent Neural Network",
  "anomaly detection", "Anomaly Detection",
  "feature engineering", "Feature Engineering",
  "feature selection", "Feature Selection",
  "feature extraction", "Feature Extraction",
  "data preprocessing", "Data Preprocessing",
  "data cleaning", "Data Cleaning",
  "missing values", "Missing Values",
  "one-hot encoding", "One-Hot Encoding", "one hot encoding",
  "label encoding", "Label Encoding",
  "cross-validation", "Cross-Validation", "cross validation",
  "train-test split", "Train-Test Split",
  "confusion matrix", "Confusion Matrix",
  "decision boundary", "Decision Boundary",
  "learning rate", "Learning Rate",
  "cost function", "Cost Function", "loss function", "Loss Function",
  "training set", "Training Set", "test set", "Test Set",
  "validation set", "Validation Set",
  "validation", "Validation", "validations", "Validations",
  "training data", "Training Data", "test data", "Test Data",
  "hyperparameter", "hyperparameters", "Hyperparameter", "Hyperparameters",
  "recommender system", "Recommender System",
  "recommender systems", "Recommender Systems",
  "image recognition", "Image Recognition",
  "speech recognition", "Speech Recognition",
  "speech processing", "Speech Processing",
  "language translation", "Language Translation",
  "sentiment analysis", "Sentiment Analysis",
  "self-driving", "Self-Driving",
  "feedback loop", "Feedback Loop",
  "model training", "Model Training",
  "data input", "Data Input",
  # Single-word / short technical
  "overfitting", "Overfitting", "underfitting", "Underfitting",
  "regularization", "Regularization",
  "normalization", "Normalization", "standardization", "Standardization",
  "classification", "Classification", "regression", "Regression",
  "clustering", "Clustering", "tokenization", "Tokenization",
  "parameter", "parameters", "Parameter", "Parameters",
  "feature", "features", "Feature", "Features",
  "label", "labels", "Label", "Labels",
  "dataset", "datasets", "Dataset", "Datasets",
  "training", "Training", "testing", "Testing",
  "prediction", "predictions", "Prediction", "Predictions",
  "accuracy", "Accuracy", "precision", "Precision", "recall", "Recall",
  "bias", "Bias", "variance", "Variance",
  "weight", "weights", "Weight", "Weights",
  "model", "models", "Model", "Models",
  "algorithm", "algorithms", "Algorithm", "Algorithms",
  "pipeline", "pipelines", "Pipeline", "Pipelines",
  "epoch", "epochs", "Epoch", "Epochs",
  "batch", "batches", "Batch", "Batches", "mini-batch", "Mini-batch",
  "optimizer", "Optimizer", "activation", "Activation",
  "dropout", "Dropout", "softmax", "Softmax", "sigmoid", "Sigmoid",
  "ReLU", "CNN", "RNN", "LSTM", "GRU", "SVM", "KNN", "K-NN",
  "PCA", "NLP", "OCR", "AUC", "ROC", "MSE", "RMSE", "MAE",
  "K-Means", "DBSCAN", "XGBoost", "LightGBM",
  "outlier", "outliers", "Outlier", "Outliers",
  "imputation", "Imputation", "scaling", "Scaling",
  "encoding", "Encoding", "tokenizer", "Tokenizer",
]

POST_FIXES: list[tuple[str, str]] = [
  (r"\bhọc máy\b", "Machine Learning"),
  (r"\bHọc máy\b", "Machine Learning"),
  (r"\bHọc Máy\b", "Machine Learning"),
  (r"\bmạng thần kinh\b", "neural network"),
  (r"\bMạng thần kinh\b", "Neural network"),
  (r"\bđặc trưng\b", "feature"),
  (r"\bĐặc trưng\b", "Feature"),
  (r"\bthiên vị\b", "bias"),
  (r"\bThiên vị\b", "Bias"),
  (r"\bbiến thiên\b", "variance"),
  (r"\bBiến thiên\b", "Variance"),
  (r"\btrọng số\b", "weight"),
  (r"\bTrọng số\b", "Weight"),
  (r"\bthông số\b", "parameter"),
  (r"\bThông số\b", "Parameter"),
  (r"\btham số\b", "parameter"),
  (r"\bTham số\b", "Parameter"),
  (r"\bđào tạo\b", "training"),
  (r"\bĐào tạo\b", "Training"),
  (r"\bhuấn luyện\b", "training"),
  (r"\bHuấn luyện\b", "Training"),
  (r"\btập huấn luyện\b", "training set"),
  (r"\bTập huấn luyện\b", "Training set"),
  (r"\btập kiểm tra\b", "test set"),
  (r"\bTập kiểm tra\b", "Test set"),
  (r"\bkiểm tra chéo\b", "cross-validation"),
  (r"\bKiểm tra chéo\b", "Cross-validation"),
  (r"\bđường ống\b", "pipeline"),
  (r"\bĐường ống\b", "Pipeline"),
  (r"\bcác đường ống\b", "pipelines"),
  (r"\bCác đường ống\b", "Pipelines"),
  (r"\bxác thực\b", "validation"),
  (r"\bXác thực\b", "Validation"),
  (r"\bmô hình\b", "model"),
  (r"\bMô hình\b", "Model"),
  (r"\btập dữ liệu\b", "dataset"),
  (r"\bTập dữ liệu\b", "Dataset"),
  (r"\bphân loại\b", "classification"),
  (r"\bPhân loại\b", "Classification"),
  (r"\bhồi quy\b", "regression"),
  (r"\bHồi quy\b", "Regression"),
  (r"\bnhãn\b", "label"),
  (r"\bNhãn\b", "Label"),
  (r"\bđộ chính xác\b", "accuracy"),
  (r"\bĐộ chính xác\b", "Accuracy"),
  (r"\bkỷ nguyên\b", "epoch"),
  (r"\bKỷ nguyên\b", "Epoch"),
  (r"\blô\b", "batch"),
  (r"\bLô\b", "Batch"),
  (r"\bchúng tôi\b", "chúng ta"),
  (r"\bChúng tôi\b", "Chúng ta"),
  (r"\bcủa chúng tôi\b", "của chúng ta"),
  (r"\bCủa chúng tôi\b", "Của chúng ta"),
]

CAMEL_RE = re.compile(r"\b[A-Z][a-zA-Z0-9]*(?:[A-Z][a-z0-9]*)+\b")


def load_cache() -> None:
  global CACHE
  if CACHE_FILE.exists():
    try:
      CACHE = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
      CACHE = {}


def save_cache() -> None:
  try:
    CACHE_FILE.write_text(
      json.dumps(CACHE, ensure_ascii=False, indent=0),
      encoding="utf-8",
    )
  except OSError as exc:
    print(f"  [warn] cache save failed: {exc}", file=sys.stderr)


def _placeholder(kind: str, idx: int) -> str:
  return f"ZZ{kind}{idx}ZZ"


def protect_with_pattern(
  text: str,
  pattern: re.Pattern[str],
  store: list[tuple[str, str]],
) -> str:
  def repl(match: re.Match[str]) -> str:
    original = match.group(0)
    ph = _placeholder("ID", len(store))
    store.append((ph, original))
    return ph

  return pattern.sub(repl, text)


def protect_terms(text: str) -> tuple[str, list[tuple[str, str]]]:
  store: list[tuple[str, str]] = []
  text = protect_with_pattern(text, CAMEL_RE, store)
  for term in sorted(set(PROTECT_TERMS), key=len, reverse=True):
    pat = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)

    def repl(match: re.Match[str], _term: str = term) -> str:
      original = match.group(0)
      ph = _placeholder("T", len(store))
      store.append((ph, original))
      return ph

    text = pat.sub(repl, text)
  return text, store


def restore_terms(text: str, store: list[tuple[str, str]]) -> str:
  for placeholder, term in store:
    text = text.replace(placeholder, term)
  return text


def apply_post_fixes(text: str) -> str:
  for pattern, replacement in POST_FIXES:
    text = re.sub(pattern, replacement, text)
  # Markdown heading / list spacing after MT
  text = re.sub(r"^(#{1,6})(?=[^\s#])", r"\1 ", text, flags=re.MULTILINE)
  text = re.sub(r"-\[", "- [", text)
  # Chỉ dọn term/id placeholder bị MT làm vỡ — KHÔNG xóa ZZS (segment MD)
  text = re.sub(r"ZZT\d+ZZ", "", text)
  text = re.sub(r"ZZID\d+ZZ", "", text)
  return text


def capitalize_prose(text: str) -> str:
  if not text or text.lstrip().startswith(("```", "$", "<", "#", "!", "[")):
    return text

  def cap_after_sep(match: re.Match[str]) -> str:
    return match.group(1) + match.group(2).upper()

  text = re.sub(
    r"(^|\n)(\s*[-*]\s+)([a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ])",
    lambda m: m.group(1) + m.group(2) + m.group(3).upper(),
    text,
    flags=re.MULTILINE,
  )
  if text and text[0].islower():
    text = text[0].upper() + text[1:]
  text = re.sub(
    r"([.!?]\s+)([a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ])",
    cap_after_sep,
    text,
  )
  return text


def polish_text(text: str) -> str:
  text = apply_post_fixes(text)
  text = capitalize_prose(text)
  return text


QUIZ_OPTION_RE = re.compile(
  r"^\*\s+([A-Da-d])\s*\n(?:[ \t]*\n)+[ \t]*(.+?)[ \t]*\n",
  re.MULTILINE,
)

IMG_MD_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
INLINE_PYTHON_RE = re.compile(
  r"(?:^|\n)(?:Python|python)\s*`([^`]+)`",
  re.MULTILINE,
)
CAROUSEL_RE = re.compile(
  r"^(?:Previous\s+)?Pause\s+Next\s+\d+\s*/\s*\d+\s*$",
  re.MULTILINE | re.IGNORECASE,
)

# Sau ) hoặc ] tới statement / method call mới
_CODE_STMT_BREAK = re.compile(
  r"([)\]])[ \t]+(?=(?:[A-Za-z_]\w*(?:\s*=|\[|\.)|print\(|plt\.))"
)
# "x1 = X x1[num] =" hoặc "X = ... Y ="
_CODE_ASSIGN_BREAK = re.compile(
  r"(\b[A-Za-z_]\w*)[ \t]+(?=[A-Za-z_]\w*(?:\[[^\]]*\])?\s*=)"
)


def format_inline_python(code: str) -> str:
  """Tách code GFG (1 dòng / cách đôi) thành nhiều dòng đọc được."""
  code = code.strip()
  protected: list[str] = []

  def _protect(match: re.Match) -> str:
    protected.append(match.group(0))
    return f"__CFG{len(protected) - 1}__"

  # Giữ nguyên "from X import Y"
  code = re.sub(r"from\s+\S+\s+import\s+\S+", _protect, code)
  # Khoảng trắng đôi của GFG = xuống dòng
  code = re.sub(r"[ \t]{2,}", "\n", code)
  # import liên tiếp: "import pandas as pd import numpy as np"
  code = re.sub(r"[ \t]+(?=import\s)", "\n", code)
  # "import matplotlib.pyplot as plt plt.boxplot(...)"
  code = re.sub(r"(as\s+[A-Za-z_]\w*)[ \t]+(?=[A-Za-z_]\w*\.)", r"\1\n", code)
  # Sau ) hoặc ] tới statement / method call mới
  code = _CODE_STMT_BREAK.sub(r"\1\n", code)
  # "x1 = X x1[num] =" → xuống dòng trước assignment kế
  code = _CODE_ASSIGN_BREAK.sub(r"\1\n", code)
  for i, seg in enumerate(protected):
    code = code.replace(f"__CFG{i}__", seg)
  code = re.sub(r"\n{3,}", "\n\n", code)
  return "\n".join(ln.rstrip() for ln in code.splitlines() if ln.strip()).strip()


def normalize_quiz_options(text: str) -> str:
  """Chuẩn hóa đáp án trắc nghiệm GeeksforGeeks thành checkbox tương tác."""

  def repl(match: re.Match[str]) -> str:
    letter = match.group(1).upper()
    answer = match.group(2).strip()
    return f"- [ ] {letter}. {answer}\n"

  return QUIZ_OPTION_RE.sub(repl, text)


def dedupe_images(text: str) -> str:
  """Xóa ảnh trùng liền nhau (cùng URL, kể cả cùng dòng)."""

  def collapse_line(line: str) -> str:
    imgs = list(IMG_MD_RE.finditer(line))
    if len(imgs) < 2:
      return line
    seen_urls: set[str] = set()
    keep: list[str] = []
    last = 0
    for m in imgs:
      keep.append(line[last : m.start()])
      url_m = re.search(r"\(([^)\s]+)", m.group(0))
      url = url_m.group(1) if url_m else m.group(0)
      if url not in seen_urls:
        seen_urls.add(url)
        keep.append(m.group(0))
      last = m.end()
    keep.append(line[last:])
    return "".join(keep)

  lines = [collapse_line(ln) for ln in text.splitlines(keepends=True)]
  text = "".join(lines)

  # Ảnh trùng URL trên các dòng liên tiếp
  out: list[str] = []
  prev_url: str | None = None
  for line in text.splitlines(keepends=True):
    m = IMG_MD_RE.fullmatch(line.strip())
    if m:
      url_m = re.search(r"\(([^)\s]+)", m.group(0))
      url = url_m.group(1) if url_m else None
      if url and url == prev_url:
        continue
      prev_url = url
      out.append(line if line.endswith("\n") else line + "\n")
    else:
      if line.strip():
        prev_url = None
      out.append(line)
  return "".join(out)


def remove_image_captions(text: str) -> str:
  """Bỏ dòng nhãn ngay dưới hình (GFG caption kiểu 'Standardization').

  Giữ lại heading setext thật, ví dụ:
    Advantages
    ----------
  """
  lines = text.splitlines()
  out: list[str] = []
  i = 0
  while i < len(lines):
    out.append(lines[i])
    if IMG_MD_RE.fullmatch(lines[i].strip()):
      j = i + 1
      while j < len(lines) and not lines[j].strip():
        out.append(lines[j])
        j += 1
      if j < len(lines):
        cap = lines[j].strip()
        # Dòng kế tiếp (sau caption) có phải gạch setext heading?
        k = j + 1
        while k < len(lines) and not lines[k].strip():
          k += 1
        next_line = lines[k].strip() if k < len(lines) else ""
        is_setext_heading = bool(re.fullmatch(r"-{3,}|={3,}", next_line))
        is_caption = (
          cap
          and len(cap) <= 60
          and not cap.startswith(("#", "*", "-", ">", "`", "!", "["))
          and "http" not in cap.lower()
          and not re.match(r"^(Python|Output|Step\s+\d|Bước\s+\d)", cap, re.I)
          and not re.search(r"[.!?]$", cap)
          and not is_setext_heading  # Advantages / Suggested Quiz / ...
        )
        if is_caption:
          i = j + 1
          continue
      i = j
      continue
    i += 1
  return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def normalize_inline_python_blocks(text: str) -> str:
  """Python`code...` → fenced ```python block với xuống dòng."""

  def repl(match: re.Match[str]) -> str:
    code = format_inline_python(match.group(1))
    prefix = "\n" if match.group(0).startswith("\n") else ""
    return f"{prefix}```python\n{code}\n```"

  return INLINE_PYTHON_RE.sub(repl, text)


def normalize_gfg_markdown(text: str) -> str:
  """Chuẩn hóa Markdown scraped từ GeeksforGeeks."""
  text = re.sub(CAROUSEL_RE, "", text)
  text = dedupe_images(text)
  text = remove_image_captions(text)
  text = normalize_inline_python_blocks(text)
  text = normalize_quiz_options(text)
  text = re.sub(r"\n{3,}", "\n\n", text)
  return text.strip() + "\n"


LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")


def translate_md_links_only_label(text: str) -> str:
  """Chỉ dịch text trong []; giữ nguyên (url) và cú pháp [..](..).

  Ví dụ:
    [Types of Machine Learning](https://www.geeksforgeeks.org/...)
  -> [Các loại Machine Learning](https://www.geeksforgeeks.org/...)
  """

  def repl(match: re.Match[str]) -> str:
    label, url = match.group(1), match.group(2)
    if not label.strip():
      return match.group(0)
    if label.startswith("`") and label.endswith("`"):
      return match.group(0)
    vi_label = translate_text(label)
    return f"[{vi_label}]({url})"

  return LINK_RE.sub(repl, text)


def protect_segments(text: str) -> tuple[str, list[str]]:
  """Bảo vệ cấu trúc MD trước khi dịch prose.

  Link/image phải đứng trước bare URL để không nuốt dấu ')'.
  """
  store: list[str] = []

  def repl(match: re.Match[str]) -> str:
    store.append(match.group(0))
    return _placeholder("S", len(store) - 1)

  patterns = [
    r"```[\s\S]*?```",
    r"!\[[^\]]*\]\([^)]+\)",
    r"(?<!!)\[[^\]]*\]\([^)]+\)",
    r"`[^`\n]+`",
    r"\$\$[\s\S]*?\$\$",
    r"\$[^$\n]+\$",
    # Chỉ tag HTML thật — KHÔNG khớp toán tử <= >=
    r"</?[a-zA-Z][^>\n]*>",
    r"https?://[^\s)]+",
    r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b",
  ]
  protected = text
  for pat in patterns:
    protected = re.sub(pat, repl, protected)
  return protected, store


def restore_segments(text: str, store: list[str]) -> str:
  for i, seg in enumerate(store):
    text = text.replace(_placeholder("S", i), seg)
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
    if out is None:
      out = text
    out = restore_terms(out, term_store)
    out = polish_text(out)
    CACHE[text] = out
    time.sleep(SLEEP_SEC)
    return out
  except Exception as exc:
    print(f"  [warn] translate failed: {exc!r} -> keep original", file=sys.stderr)
    return text


def translate_markdown(source: str) -> str:
  # 0) Chuẩn hóa GFG (ảnh trùng, nhãn hình, code, quiz)
  source = normalize_gfg_markdown(source)

  # 1) Chỉ dịch label trong [label](url); URL + cú pháp giữ nguyên
  step1 = translate_md_links_only_label(source)

  # 2) Bảo vệ link đã dịch + code/ảnh/math… rồi dịch prose
  protected, store = protect_segments(step1)

  paragraphs = re.split(r"(\n\n+)", protected)
  out_parts: list[str] = []
  for part in paragraphs:
    if not part or part.isspace() or re.fullmatch(r"\n+", part):
      out_parts.append(part)
      continue
    if re.fullmatch(r"(?:\s|ZZS\d+ZZ)+", part):
      out_parts.append(part)
      continue
    if re.fullmatch(r"-{3,}|={3,}", part.strip()):
      out_parts.append(part)
      continue
    out_parts.append(translate_text(part))

  result = "".join(out_parts)
  result = restore_segments(result, store)
  # Dọn placeholder segment còn sót (nếu MT làm hỏng token)
  result = re.sub(r"ZZS\d+ZZ", "", result)
  result = normalize_gfg_markdown(result)
  return polish_text(result)


def is_english_md(path: Path) -> bool:
  name = path.name.lower()
  if not name.endswith((".md", ".markdown")):
    return False
  if any(name.endswith(suf) for suf in SKIP_NAME_SUFFIXES):
    return False
  if any(part in SKIP_DIRS for part in path.parts):
    return False
  return True


def vi_output_path(src: Path) -> Path:
  return src.with_name(f"{src.stem}_vi{src.suffix}")


def process_file(src: Path, force: bool = False) -> str | None:
  """Return 'skip' | 'ok' | None (not an EN md). Never re-translate unless force."""
  if not is_english_md(src):
    return None
  dst = vi_output_path(src)
  if dst.exists() and not force:
    print(f"  [skip] đã dịch: {dst.relative_to(ROOT)}")
    return "skip"

  print(f"  [translate] {src.relative_to(ROOT)} -> {dst.name}")
  en = src.read_text(encoding="utf-8")
  vi = translate_markdown(en)
  dst.write_text(vi, encoding="utf-8")
  save_cache()
  return "ok"


def collect_md_files(base: Path) -> list[Path]:
  files = sorted(p for p in base.rglob("*.md") if is_english_md(p))
  files += sorted(p for p in base.rglob("*.markdown") if is_english_md(p))
  # Deduplicate while preserving order
  seen: set[Path] = set()
  out: list[Path] = []
  for p in files:
    if p not in seen:
      seen.add(p)
      out.append(p)
  return out


def load_extra_terms(path: Path) -> None:
  for line in path.read_text(encoding="utf-8").splitlines():
    term = line.strip()
    if not term or term.startswith("#"):
      continue
    if term not in PROTECT_TERMS:
      PROTECT_TERMS.append(term)


def parse_args() -> argparse.Namespace:
  p = argparse.ArgumentParser(
    description="Dịch Markdown EN -> VI (_vi.md), giữ thuật ngữ chuyên ngành.",
  )
  p.add_argument(
    "paths",
    nargs="*",
    type=Path,
    help="File .md hoặc thư mục (mặc định: toàn bộ dưới ROOT)",
  )
  p.add_argument(
    "--dir",
    type=Path,
    default=None,
    help="Thư mục gốc để quét (mặc định = thư mục script)",
  )
  p.add_argument(
    "--extra-terms",
    type=Path,
    default=None,
    help="File text: mỗi dòng một thuật ngữ giữ tiếng Anh",
  )
  p.add_argument(
    "--force",
    action="store_true",
    help="Ép dịch lại (mặc định: bỏ qua nếu *_vi.md đã có)",
  )
  p.add_argument(
    "--dry-run",
    action="store_true",
    help="Chỉ liệt kê file sẽ dịch, không gọi API",
  )
  return p.parse_args()


def main() -> int:
  args = parse_args()
  if args.extra_terms:
    load_extra_terms(args.extra_terms.resolve())
    print(f"Loaded extra terms from {args.extra_terms} ({len(PROTECT_TERMS)} total)")

  load_cache()
  targets: list[Path] = []

  if args.paths:
    for raw in args.paths:
      path = raw if raw.is_absolute() else (ROOT / raw)
      path = path.resolve()
      if path.is_file():
        targets.append(path)
      elif path.is_dir():
        targets.extend(collect_md_files(path))
      else:
        print(f"  [warn] not found: {path}", file=sys.stderr)
  else:
    base = (ROOT / args.dir).resolve() if args.dir else ROOT
    if not base.exists():
      print(f"Directory not found: {base}", file=sys.stderr)
      return 1
    targets = collect_md_files(base)

  if not targets:
    print("No English Markdown files found.")
    return 0

  print(f"Found {len(targets)} file(s) under {ROOT}")
  if args.dry_run:
    for t in targets:
      print(f"  would translate: {t.relative_to(ROOT)} -> {vi_output_path(t).name}")
    return 0

  n_ok = n_skip = n_err = 0
  for src in targets:
    try:
      status = process_file(src, force=args.force)
      if status == "ok":
        n_ok += 1
      elif status == "skip":
        n_skip += 1
    except Exception as exc:
      n_err += 1
      print(f"  [error] {src}: {exc!r}", file=sys.stderr)

  save_cache()
  print(
    f"Done. dịch mới={n_ok}, bỏ qua (đã có _vi)={n_skip}, lỗi={n_err}"
    f" / tổng={len(targets)}. Cache: {CACHE_FILE.name}"
  )
  return 0 if n_err == 0 else 1


if __name__ == "__main__":
  raise SystemExit(main())
