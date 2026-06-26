#!/usr/bin/env python3
"""Translate Coursera lab notebooks to Vietnamese (_vi.ipynb).

Technical / domain terms stay in English; explanatory prose is translated.
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
SKIP_DIRS = {".ipynb_checkpoints", "archive"}
TRANSLATOR = GoogleTranslator(source="en", target="vi")
CACHE: dict[str, str] = {}
CHUNK_SIZE = 4500
SLEEP_SEC = 0.12

# Terms that must remain in English (longest first for greedy matching).
PROTECT_TERMS: list[str] = [
  # Frameworks & tools
  "DeepLearning.AI", "scikit-learn", "TensorFlow", "tensorflow", "matplotlib",
  "Coursera", "Jupyter", "SymPy", "Keras", "keras", "NumPy", "numpy", "pandas",
  "sklearn", "Python", "python", "Markdown", "markdown", "f-string", "f strings",
  "Code Cell", "code cell", "iPython", "IPython", "Adam", "SGD",
  # Lab structure
  "Practice lab", "Optional lab", "Optional Lab", "Graded Function",
  "Recommender Systems", "Recommender System",
  # ML / DL core (multi-word first)
  "principal component analysis", "Principal Component Analysis",
  "binary cross-entropy", "Binary Crossentropy", "mean squared error",
  "MeanSquaredError", "feature scaling", "Feature Scaling",
  "polynomial regression", "Polynomial Regression",
  "polynomial features", "Polynomial Features",
  "decision boundary", "Decision Boundary",
  "collaborative filtering", "Collaborative Filtering",
  "content-based filtering", "Content-Based Filtering",
  "reinforcement learning", "Reinforcement Learning",
  "unsupervised learning", "Unsupervised Learning",
  "supervised learning", "Supervised Learning",
  "machine learning", "Machine Learning",
  "deep learning", "Deep Learning",
  "gradient boosting", "Gradient Boosting",
  "gradient descent", "Gradient Descent",
  "logistic regression", "Logistic Regression",
  "logistic model", "Logistic model",
  "linear model", "Linear model",
  "linear regression", "Linear Regression",
  "framework", "Framework",
  "Dataset", "dataset",
  "neural network", "Neural Network",
  "random forest", "Random Forest",
  "decision tree", "Decision Tree",
  "anomaly detection", "Anomaly Detection",
  "forward propagation", "Forward Propagation",
  "backpropagation", "Backpropagation", "backprop", "Backprop",
  "training example", "training examples", "Training Example",
  "train example", "train examples", "Train example", "Train examples",
  "training set", "Training Set", "test set", "Test Set",
  "validation set", "Validation Set", "dev set", "Dev Set",
  "learning rate", "Learning Rate",
  "mini-batch", "mini-batches", "Mini-batch", "Mini-batches",
  "batch gradient descent", "Batch gradient descent",
  "one-hot encoding", "One-hot encoding",
  "value function", "Value function", "Q-value", "Q-values",
  "state-action value", "State-action value",
  "cost function", "Cost Function", "loss function", "Loss Function",
  "dot product", "Dot Product",
  "decision tree", "Decision Tree",
  "state-action", "State-action", "Q-learning", "Q-Learning",
  "Bellman equation", "Bellman Equation",
  "Packages", "Package", "Outline", "Exercise", "Congratulations",
  "lab", "Lab", "exercise", "Exercise",
  # Single-word technical terms
  "hyperparameter", "hyperparameters", "Hyperparameter", "Hyperparameters",
  "regularization", "Regularization", "overfitting", "Overfitting",
  "underfitting", "Underfitting", "normalization", "Normalization",
  "standardization", "Standardization", "vectorization", "Vectorization",
  "vectorized", "Vectorized", "broadcasting", "Broadcasting",
  "classification", "Classification", "regression", "Regression",
  "backpropagation", "activation", "activations", "Activation", "Activations",
  "optimizer", "Optimizer", "prediction", "predictions", "Prediction", "Predictions",
  "classifier", "Classifier", "centroid", "centroids", "Centroid", "Centroids",
  "clustering", "Clustering", "recommender", "Recommender",
  "collaborative", "Collaborative", "filtering", "Filtering",
  "parameter", "parameters", "Parameter", "Parameters",
  "feature", "features", "Feature", "Features",
  "label", "labels", "Label", "Labels",
  "target", "targets", "Target", "Targets",
  "training", "Training", "testing", "Testing",
  "dataset", "datasets", "Dataset", "Datasets",
  "gradient", "gradients", "Gradient", "Gradients",
  "weight", "weights", "Weight", "Weights",
  "bias", "biases", "Bias", "Biases",
  "scalar", "scalars", "Scalar", "Scalars",
  "vector", "vectors", "Vector", "Vectors",
  "matrix", "matrices", "Matrix", "Matrices",
  "tensor", "tensors", "Tensor", "Tensors",
  "layer", "layers", "Layer", "Layers",
  "neuron", "neurons", "Neuron", "Neurons",
  "epoch", "epochs", "Epoch", "Epochs",
  "batch", "batches", "Batch", "Batches",
  "softmax", "Softmax", "sigmoid", "Sigmoid",
  "ReLU", "relu", "tanh", "Tanh",
  "dropout", "Dropout", "lambda", "Lambda",
  "accuracy", "Accuracy", "precision", "Precision",
  "recall", "Recall", "cost", "Cost", "loss", "Loss",
  "model", "models", "Model", "Models",
  "policy", "Policy", "reward", "rewards", "Reward", "Rewards",
  "agent", "Agent", "environment", "Environment",
  "K-means", "PCA", "XGBoost", "Dense", "Sequential", "Input",
  "plot", "scatter", "shape", "dtype", "array", "arrays",
  "update", "updates", "Update", "Updates",
  "fit", "Fit",
  "encoding", "encodings", "Encoding", "Encodings",
  "threshold", "thresholds", "Threshold", "Thresholds",
  "component", "components", "Component", "Components",
  "variance", "Variance",
  "notebook", "notebooks", "Notebook", "Notebooks",
  "cell", "cells", "Cell", "Cells",
  "widget", "widgets", "Widget", "Widgets",
  "rating", "ratings", "Rating", "Ratings",
  "item", "items", "Item", "Items",
  "user", "users", "User", "Users",
  "network", "networks", "Network", "Networks",
  "code", "Code",
  "test", "tests", "Test", "Tests",
  "unit", "units", "Unit", "Units",
  "movie", "movies", "Movie", "Movies",
]

# Fix common Google Translate mistakes after translation.
POST_FIXES: list[tuple[str, str]] = [
  (r"\bvectơ\b", "vector"),
  (r"\bVectơ\b", "Vector"),
  (r"\bvô hướng\b", "scalar"),
  (r"\bVô hướng\b", "Scalar"),
  (r"\bthiên vị\b", "bias"),
  (r"\bThiên vị\b", "Bias"),
  (r"\bthông số\b", "parameter"),
  (r"\bThông số\b", "Parameter"),
  (r"\bđặc trưng\b", "feature"),
  (r"\bĐặc trưng\b", "Feature"),
  (r"\btế bào thần kinh\b", "neuron"),
  (r"\bTế bào thần kinh\b", "Neuron"),
  (r"\bđơn vị ẩn\b", "hidden unit"),
  (r"\bđơn vị\b", "unit"),
  (r"\bGói\b", "Packages"),
  (r"\bgói máy học\b", "machine learning package"),
  (r"\bhuấn luyện example\b", "training example"),
  (r"\bHuấn luyện example\b", "Training example"),
  (r"\btrain example\b", "training example"),
  (r"\bTrain example\b", "Training example"),
  (r"\bđào tạo\b", "training"),
  (r"\bĐào tạo\b", "Training"),
  (r"\btrò chơi\b", "movie"),
  (r"\bTrò chơi\b", "Movie"),
  (r"\bnum_phim\b", "num_movies"),
  (r"\btích dot\b", "dot product"),
  (r"\bTích dot\b", "Dot product"),
  (r"\btraning\b", "training"),
  (r"\bTraning\b", "Training"),
  (r"\bđại lượng scalar\b", "scalar"),
  (r"\bđại lượng vô hướng\b", "scalar"),
  (r"\btham số sai lệch\b", "bias parameter"),
  (r"\bthuật ngữ bias\b", "bias term"),
  (r"\bThuật ngữ bias\b", "Bias term"),
  (r"\bthuật ngữ thiên vị\b", "bias term"),
  (r"\bThuật ngữ thiên vị\b", "Bias term"),
  (r"\bđộ lệch\b", "bias"),
  (r"\bĐộ lệch\b", "Bias"),
  (r"\btrọng số\b", "weight"),
  (r"\bTrọng số\b", "Weight"),
  (r"\bma trận vectơ\b", "vector matrix"),
  (r"\bMa trận vectơ\b", "Vector matrix"),
  (r"\bphòng thí nghiệm\b", "lab"),
  (r"\bPhòng thí nghiệm\b", "Lab"),
  (r"\bmodel hậu cần\b", "logistic model"),
  (r"\bModel hậu cần\b", "Logistic model"),
  (r"\bkhung\b", "framework"),
  (r"\bKhung\b", "Framework"),
  (r"\btrain example\b", "training example"),
  (r"\bTrain example\b", "Training example"),
  (r"\bTham số\b", "Parameter"),
  (r"\btham số\b", "parameter"),
  (r"\btrọng số\b", "weight"),
  (r"\bTrọng số\b", "Weight"),
  (r"\bđộ lệch\b", "bias"),
  (r"\bĐộ lệch\b", "Bias"),
  (r"\bHồi quy\b", "Regression"),
  (r"\bbatch mini\b", "mini-batch"),
  (r"\bBatch mini\b", "Mini-batch"),
  (r"\bkỷ nguyên\b", "epoch"),
  (r"\bKỷ nguyên\b", "Epoch"),
  (r"\blô\b", "batch"),
  (r"\bLô\b", "Batch"),
  (r"\bngưỡng\b", "threshold"),
  (r"\bNgưỡng\b", "Threshold"),
  (r"\bmã hóa\b", "encoding"),
  (r"\bMã hóa\b", "Encoding"),
  (r"\bbiến thiên\b", "variance"),
  (r"\bBiến thiên\b", "Variance"),
  (r"\bgiá trị Q\b", "Q-value"),
  (r"\bGiá trị Q\b", "Q-value"),
  (r"\bhàm giá trị\b", "value function"),
  (r"\bHàm giá trị\b", "Value function"),
  # Giọng văn: inclusive "we"
  (r"\bcủa chúng tôi\b", "của chúng ta"),
  (r"\bCủa chúng tôi\b", "Của chúng ta"),
  (r"\bchúng tôi\b", "chúng ta"),
  (r"\bChúng tôi\b", "Chúng ta"),
  (r"\bgiúpchúng tôi\b", "giúp chúng ta"),
  (r"\bgiúpchúng ta\b", "giúp chúng ta"),
  (r"\bcủa mình\b", "của chúng ta"),
  # Recall (Coursera) → tiếng Việt tự nhiên
  (r"\bRecall rằng\b", "Nhớ rằng"),
  (r"\bRecall mà\b", "Nhớ rằng"),
  (r"\bRecall đối với\b", "Nhớ rằng đối với"),
  (r"\bRecall từ\b", "Nhớ rằng từ"),
  (r"\bRecall cuộc\b", "Nhớ rằng cuộc"),
  (r"\bRecall trong\b", "Nhớ rằng trong"),
  (r"\bRecall các\b", "Nhớ rằng các"),
  (r"\bRecall,\b", "Nhớ rằng,"),
  (r"\bRecall\b", "Nhớ rằng"),
  # Dịch sai thường gặp
  (r"\bcập nhật phần mềm\b", "soft update"),
  (r"\bCập nhật phần mềm\b", "Soft update"),
  (r"\bmạng thần kinh\b", "neural network"),
  (r"\bMạng thần kinh\b", "Neural network"),
  (r"\bMạng Target\b", "Target Network"),
  (r"\bmô-đun\b", "module"),
  (r"\bMô-đun\b", "Module"),
  (r"\bsổ ghi chép\b", "notebook"),
  (r"\bSổ ghi chép\b", "Notebook"),
  (r"\bsổ tay\b", "notebook"),
  (r"\bSổ tay\b", "Notebook"),
  (r"\bThư viện phòng tập thể dục\b", "Gym library"),
  (r"\bPhòng tập thể dục\b", "Gym"),
  (r"\bphòng tập thể dục\b", "Gym"),
  (r"\bPhòng tập\b", "Gym"),
  (r"\bphòng tập\b", "Gym"),
  # Thuật ngữ giữ tiếng Anh (user request)
  (r"\bvật phẩm\b", "item"),
  (r"\bVật phẩm\b", "Item"),
  (r"\bvật phẩm/phim\b", "item/movie"),
  (r"\bphim/mục\b", "movie/item"),
  (r"\bmục/phim\b", "item/movie"),
  (r"\bhuấn luyện\b", "training"),
  (r"\bHuấn luyện\b", "Training"),
  (r"\bđược huấn luyện\b", "được training"),
  (r"\bĐược huấn luyện\b", "Được training"),
  (r"\bđã huấn luyện\b", "đã training"),
  (r"\bĐã huấn luyện\b", "Đã training"),
  (r"\bthử nghiệm\b", "test"),
  (r"\bThử nghiệm\b", "Test"),
  (r"\bdữ liệu thử nghiệm\b", "test data"),
  (r"\btập thử nghiệm\b", "test set"),
  (r"\bngười dùng\b", "user"),
  (r"\bNgười dùng\b", "User"),
  (r"\b(\d+)\s+chiếc\b", r"\1 units"),
  (r"\bmột chiếc model\b", "một model"),
  (r"\bMã được\b", "Code được"),
  (r"\bmã được\b", "code được"),
  (r"\btrong mã\b", "trong code"),
  (r"\bTrong mã\b", "Trong code"),
  (r"\bMã\b", "Code"),
  (r"\bmã\b", "code"),
  (r"\bmạng\b", "network"),
  (r"\bMạng\b", "Network"),
  (r"\bMạng \$Q\$\b", "Q-Network"),
  (r"\bmạng \$Q\$\b", "Q-Network"),
  # Thể loại phim → giữ tiếng Anh
  (r"\bPhiêu lưu\b", "Adventure"),
  (r"\bHoạt hình\b", "Animation"),
  (r"\bTrẻ em\b", "Children"),
  (r"\bPhim hài\b", "Comedy"),
  (r"\bHài kịch\b", "Comedy"),
  (r"\bẢo tưởng\b", "Fantasy"),
  (r"\bHành động\b", "Action"),
  (r"\bKhoa học viễn tưởng\b", "Sci-Fi"),
  (r"\bTội phạm\b", "Crime"),
  (r"\bKinh dị\b", "Horror"),
  (r"\bLãng mạn\b", "Romance"),
  (r"\bCỗ máy thời gian\b", "The Time Machine"),
]

# Sửa thứ tự từ (tiếng Anh + tiếng Việt lẫn lộn)
ORDER_FIXES: list[tuple[str, str]] = [
  (r"đề xuất phim model", "model đề xuất phim"),
  (r"phim model", "model phim"),
  (r"vector user", "user vector"),
  (r"vector của user", "user vector"),
  (r"feature vector user", "user feature vector"),
  (r"feature vector movie", "movie feature vector"),
  (r"bộ phim feature vector", "movie feature vector"),
  (r"phim feature vector", "movie feature vector"),
  (r"vector phim", "movie vector"),
  (r"phim vector", "movie vector"),
  (r"bộ phim vector", "movie vector"),
  (r"bộ phim vectors", "movie vectors"),
  (r"phim vectors", "movie vectors"),
  (r"network user", "user network"),
  (r"network phim", "movie network"),
  (r"phim tương tự feature vectors", "movie feature vectors tương tự"),
  (r"phim feature vectors", "movie feature vectors"),
  (r"giữa mỗi phim feature vector", "giữa mỗi movie feature vector"),
  (r"các phim khác feature vectors", "các movie feature vectors khác"),
  (r"chạy phim vectors", "chạy movie vectors"),
  (r"phim vectors thông qua", "movie vectors thông qua"),
  (r"id user", "user id"),
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

  # CamelCase identifiers (BinaryCrossentropy, ...)
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


def apply_order_fixes(text: str) -> str:
  for pattern, replacement in ORDER_FIXES:
    if pattern != replacement:
      text = re.sub(pattern, replacement, text)
  return text


def capitalize_prose(text: str) -> str:
  """Capitalize first letter and letters after sentence endings."""
  if not text or text.lstrip().startswith(("```", "$", "<", "#", "!", "[")):
    return text

  def cap_after_sep(match: re.Match[str]) -> str:
    return match.group(1) + match.group(2).upper()

  # First character of text / line (bullets)
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


QUOTE_RE = re.compile(r'("([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\')')


def _is_latin_literal(s: str) -> bool:
  inner = s[1:-1]
  if not re.search(r"[A-Za-z]", inner):
    return False
  if re.search(r"[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]", inner, re.I):
    return False
  return True


def sync_quoted_from_english(vi_text: str, en_text: str) -> str:
  """Restore quoted movie titles / genre strings from English source."""
  en_matches = list(QUOTE_RE.finditer(en_text))
  vi_matches = list(QUOTE_RE.finditer(vi_text))
  if not en_matches or len(en_matches) != len(vi_matches):
    return vi_text
  out: list[str] = []
  last = 0
  for vm, em in zip(vi_matches, en_matches):
    out.append(vi_text[last : vm.start()])
    if _is_latin_literal(em.group(0)):
      out.append(em.group(0))
    else:
      out.append(vm.group(0))
    last = vm.end()
  out.append(vi_text[last:])
  return "".join(out)


def polish_text(text: str, en_text: str | None = None) -> str:
  if en_text:
    text = sync_quoted_from_english(text, en_text)
  text = apply_post_fixes(text)
  text = apply_order_fixes(text)
  text = capitalize_prose(text)
  return text


def apply_post_fixes(text: str) -> str:
  for pattern, replacement in POST_FIXES:
    text = re.sub(pattern, replacement, text)
  # Restore markdown spacing after translation / segment restore
  text = re.sub(r"^#(?=[A-Za-z])", "# ", text, flags=re.MULTILINE)
  text = re.sub(r"^##(?=[\dA-Za-z])", "## ", text, flags=re.MULTILINE)
  text = re.sub(r"^###(?=[A-Za-z])", "### ", text, flags=re.MULTILINE)
  text = re.sub(r"#<", "# <", text)
  text = re.sub(r"-\[", "- [", text)
  # Leaked segment placeholders (e.g. </sub> eaten by translator)
  text = re.sub(r"ZZS\d+ZZ", "</sub>", text)
  text = re.sub(r"ZZT\d+ZZ", "", text)
  text = re.sub(r"ZZID\d+ZZ", "", text)
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
    out = polish_text(out)
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
    return _placeholder("S", len(store) - 1)

  patterns = [
    r"```[\s\S]*?```",
    r"!\[[^\]]*\]\([^)]+\)",
    r"\[`[^`]*`\]\([^)]+\)",
    r"\[[^\]]+\]\([^)]+\)",
    r"`[^`\n]+`",
    r"\$\$[\s\S]*?\$\$",
    r"\$[^$\n]+\$",
    r"<sub>[\s\S]*?</sub>",
    r"<figure>[\s\S]*?</figure>",
    r"<a\s+name=[^>]+>",
    r"<[^>]+>",
    r"https?://\S+",
    r"\./[\w./-]+",
    r"\bUNQ_[A-Z0-9_]+\b",
    r"\bC[123]_W\d+[^\s]*",
    r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b",  # snake_case identifiers
  ]
  protected = text
  for pat in patterns:
    protected = re.sub(pat, repl, protected)
  return protected, store


def restore_segments(text: str, store: list[str]) -> str:
  for i, seg in enumerate(store):
    text = text.replace(_placeholder("S", i), seg)
  return text


def translate_markdown(source: str) -> str:
  if isinstance(source, list):
    joined = "".join(source)
    return translate_markdown(joined)
  protected, store = protect_segments(source)
  translated = translate_text(protected)
  result = restore_segments(translated, store)
  return polish_text(result)


def translate_code_line(line: str) -> str:
  stripped = line.lstrip()
  if stripped.startswith("#"):
    indent = line[: len(line) - len(stripped)]
    comment = stripped[1:]
    if comment.startswith("!"):
      return line
    upper = comment.upper()
    if "UNQ_" in upper or "GRADED" in upper:
      return line
    if comment.strip().lower().startswith("grade"):
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
      full = "".join(src_text) if isinstance(src_text, list) else src_text
      cell["source"] = translate_markdown(full).splitlines(keepends=True)
      if cell["source"] and not cell["source"][-1].endswith("\n"):
        cell["source"][-1] += "\n"
    elif ctype == "code":
      cell["source"] = translate_code_source(cell.get("source", ""))

  with dst.open("w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
  return dst


def _english_pair(vi_path: Path) -> Path | None:
  if not vi_path.name.endswith("_vi.ipynb"):
    return None
  en = vi_path.with_name(vi_path.name.replace("_vi.ipynb", ".ipynb"))
  return en if en.exists() else None


def fix_existing_notebook(path: Path) -> None:
  """Apply post-fixes to an existing _vi notebook without re-translating."""
  with path.open(encoding="utf-8") as f:
    nb = json.load(f)

  en_path = _english_pair(path)
  en_cells: list[dict] = []
  if en_path:
    with en_path.open(encoding="utf-8") as f:
      en_nb = json.load(f)
      en_cells = en_nb.get("cells", [])

  changed = False
  for idx, cell in enumerate(nb.get("cells", [])):
    src = cell.get("source", "")
    full = "".join(src) if isinstance(src, list) else (src or "")
    if not full:
      continue
    en_full = ""
    if idx < len(en_cells):
      en_src = en_cells[idx].get("source", "")
      en_full = "".join(en_src) if isinstance(en_src, list) else (en_src or "")
    fixed = polish_text(full, en_full or None)
    if fixed != full:
      changed = True
      cell["source"] = fixed.splitlines(keepends=True)
      if cell["source"] and not cell["source"][-1].endswith("\n"):
        cell["source"][-1] += "\n"

  if changed:
    with path.open("w", encoding="utf-8") as f:
      json.dump(nb, f, ensure_ascii=False, indent=1)


def main() -> None:
  parser = argparse.ArgumentParser(description="Translate notebooks to Vietnamese")
  parser.add_argument(
    "--notebook",
    type=Path,
    help="Translate a single notebook (relative to ROOT or absolute path)",
  )
  parser.add_argument(
    "--fix-existing",
    action="store_true",
    help="Apply post-fixes to existing _vi notebooks without re-translating",
  )
  args = parser.parse_args()

  if args.fix_existing:
    targets = sorted(ROOT.rglob("*_vi.ipynb"))
    print(f"Fixing {len(targets)} _vi notebooks")
    for i, path in enumerate(targets, 1):
      if any(part in SKIP_DIRS for part in path.parts):
        continue
      print(f"[{i}/{len(targets)}] {path.relative_to(ROOT)}", flush=True)
      fix_existing_notebook(path)
    print("Done fixing.")
    return

  load_cache()

  if args.notebook:
    src = args.notebook
    if not src.is_absolute():
      src = ROOT / src
    targets = [src]
  else:
    targets = sorted(p for p in ROOT.rglob("*.ipynb") if should_process(p))

  print(f"Found {len(targets)} notebooks")
  for i, src in enumerate(targets, 1):
    try:
      rel = src.relative_to(ROOT)
    except ValueError:
      rel = src
    print(f"[{i}/{len(targets)}] translating: {rel}", flush=True)
    try:
      out = process_notebook(src)
      print(f"  -> {out.name}")
      if i % 5 == 0:
        save_cache()
    except Exception as exc:
      print(f"  ERROR: {exc}", file=sys.stderr)

  save_cache()
  print(f"Done. Cache: {len(CACHE)} entries")


if __name__ == "__main__":
  main()
