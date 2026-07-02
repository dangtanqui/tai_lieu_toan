#!/usr/bin/env python3
"""Translate ISL/ISLP PDF parts to editable Vietnamese LaTeX.

Pipeline:
  1. extract   EN + Google-VI PDF -> blocks.json (+ figures/)
  2. translate blocks (VI reference seed + term-protected Google Translate)
  3. export    blocks.json -> main.tex + content.tex
  4. compile   xelatex -> PDF

Edit vi_latex/<part>/blocks.json (field "vi") or content.tex, then:
  python translate_pdf_vi.py --part 1 --export-latex --compile
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import fitz
from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent
EN_DIR = ROOT / "ilovepdf_split"
VI_REF_DIR = ROOT / "vi"
OUT_DIR = ROOT / "vi_latex"
CACHE_FILE = ROOT / ".translate_cache_vi.json"

TRANSLATOR = GoogleTranslator(source="en", target="vi")
CACHE: dict[str, str] = {}
CHUNK_SIZE = 4500
SLEEP_SEC = 0.12

SKIP_BLOCK_RE = re.compile(
  r"^(©|Machine Translated by Google|\d{1,3})$",
  re.I,
)
COPYRIGHT_RE = re.compile(r"©\s*Springer", re.I)

PROTECT_TERMS: list[str] = [
  "An Introduction to Statistical Learning",
  "statistical learning", "Statistical Learning", "Statistical learning",
  "supervised learning", "Supervised Learning", "Supervised learning",
  "unsupervised learning", "Unsupervised Learning", "Unsupervised learning",
  "machine learning", "Machine Learning", "Machine learning",
  "linear regression", "Linear Regression", "Linear regression",
  "logistic regression", "Logistic Regression", "Logistic regression",
  "multiple linear regression", "Multiple Linear Regression",
  "polynomial regression", "Polynomial Regression",
  "ridge regression", "Ridge Regression", "Ridge regression",
  "lasso", "Lasso", "LASSO",
  "elastic net", "Elastic Net", "Elastic net",
  "principal component analysis", "Principal Component Analysis",
  "principal components", "Principal Components",
  "decision tree", "Decision Tree", "Decision Trees", "decision trees",
  "random forest", "Random Forest", "Random forest", "random forests",
  "gradient boosting", "Gradient Boosting",
  "support vector machine", "Support Vector Machine",
  "support vector machines", "Support Vector Machines",
  "K-nearest neighbors", "K-Nearest Neighbors", "K-nearest neighbor",
  "cross-validation", "Cross-Validation", "cross validation", "Cross validation",
  "training set", "Training Set", "training sets", "Training sets",
  "test set", "Test Set", "test sets", "Test sets",
  "validation set", "Validation Set",
  "bias-variance trade-off", "Bias-Variance Trade-Off",
  "bias-variance tradeoff", "Bias-Variance Tradeoff",
  "mean squared error", "Mean Squared Error",
  "false discovery rate", "False Discovery Rate",
  "p-value", "p-values", "P-value", "P-values",
  "feature", "features", "Feature", "Features",
  "predictor", "predictors", "Predictor", "Predictors",
  "response", "responses", "Response", "Responses",
  "outcome", "outcomes", "Outcome", "Outcomes",
  "dataset", "datasets", "Dataset", "Datasets", "data set", "data sets",
  "bias", "variance", "Bias", "Variance",
  "overfitting", "Overfitting", "underfitting", "Underfitting",
  "regularization", "Regularization",
  "classification", "Classification", "regression", "Regression",
  "clustering", "Clustering",
  "bootstrap", "Bootstrap", "bootstrapping", "Bootstrapping",
  "resampling", "Resampling",
  "neural network", "Neural Network", "neural networks", "Neural Networks",
  "deep learning", "Deep Learning",
  "principal component", "Principal Component",
  "scikit-learn", "sklearn", "NumPy", "numpy", "pandas", "matplotlib",
  "Python", "python", "TensorFlow", "tensorflow",
  "ISLR", "ISLP", "ESL",
  "Springer", "Coursera",
  "lab", "Lab", "labs", "Labs",
  "model", "models", "Model", "Models",
  "parameter", "parameters", "Parameter", "Parameters",
  "coefficient", "coefficients", "Coefficient", "Coefficients",
  "estimate", "estimates", "Estimate", "Estimates",
  "estimator", "estimators", "Estimator", "Estimators",
  "hyperparameter", "hyperparameters", "Hyperparameter", "Hyperparameters",
  "PCA", "SVM", "KNN", "K-NN", "ROC", "AUC", "MSE", "RSS", "RSE",
  "Wage", "Auto", "Carseats", "Default", "Portfolio", "Hitters",
  "James", "Witten", "Hastie", "Tibshirani", "Taylor",
  "The Elements of Statistical Learning",
  "generalized additive model", "Generalized Additive Model",
  "generalized additive models", "Generalized Additive Models", "GAM", "GAMs",
  "generalized linear model", "Generalized Linear Model",
  "generalized linear models", "Generalized Linear Models", "GLM",
  "naive Bayes", "Naive Bayes",
  "maximum margin classifier", "Maximum Margin Classifier",
  "support vector classifier", "Support Vector Classifier",
  "hazard function", "Hazard Function", "proportional hazards",
  "survival analysis", "Survival Analysis",
  "matrix completion", "Matrix Completion",
  "text classification", "Text Classification",
  "document classification", "Document Classification",
  "dropout", "Dropout",
  "shrinkage", "Shrinkage",
  "qualitative predictors", "Qualitative Predictors",
  "bagging", "Bagging", "boosting", "Boosting",
  "principal components regression", "Principal Components Regression",
  "partial least squares", "Partial Least Squares", "PLS",
  "K-means", "hierarchical clustering", "Hierarchical Clustering",
  "double descent", "Double Descent",
  "validation set approach", "Validation Set Approach",
  "linear discriminant analysis", "Linear Discriminant Analysis", "LDA",
  "quadratic discriminant analysis", "Quadratic Discriminant Analysis", "QDA",
  "polynomial regression", "Polynomial Regression",
  "local regression", "Local Regression",
  "decision boundary", "Decision Boundary",
  "confusion matrix", "Confusion Matrix",
  "training error", "Training Error", "test error", "Test Error",
  "degrees of freedom", "Degrees of Freedom",
  "predictor", "predictors", "response variable", "Response Variable",
]

POST_FIXES: list[tuple[str, str]] = [
  (r"\bhọc máy thống kê\b", "statistical learning"),
  (r"\bHọc máy thống kê\b", "Statistical learning"),
  (r"\bHọc máy Thống kê\b", "Statistical Learning"),
  (r"\bGiới thiệu về Học máy Thống kê\b", "An Introduction to Statistical Learning"),
  (r"\bđặc trưng\b", "feature"),
  (r"\bĐặc trưng\b", "Feature"),
  (r"\bphản hồi\b", "response"),
  (r"\bPhản hồi\b", "Response"),
  (r"\bbiến dự đoán\b", "predictor"),
  (r"\bBiến dự đoán\b", "Predictor"),
  (r"\bthiên vị\b", "bias"),
  (r"\bThiên vị\b", "Bias"),
  (r"\bbiến thiên\b", "variance"),
  (r"\bBiến thiên\b", "Variance"),
  (r"\btrọng số\b", "weight"),
  (r"\bTrọng số\b", "Weight"),
  (r"\bthông số\b", "parameter"),
  (r"\bThông số\b", "Parameter"),
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
  (r"\bmô hình\b", "model"),
  (r"\bMô hình\b", "Model"),
  (r"\btập dữ liệu\b", "dataset"),
  (r"\bTập dữ liệu\b", "Dataset"),
  (r"\bphân loại\b", "classification"),
  (r"\bPhân loại\b", "Classification"),
  (r"\bhồi quy\b", "regression"),
  (r"\bHồi quy\b", "Regression"),
  (r"\bchúng tôi\b", "chúng ta"),
  (r"\bChúng tôi\b", "Chúng ta"),
  (r"\bcủa chúng tôi\b", "của chúng ta"),
  (r"\bCủa chúng tôi\b", "Của chúng ta"),
  (r"\bvectơ\b", "vector"),
  (r"\bVectơ\b", "Vector"),
  (r"\bma trận\b", "matrix"),
  (r"\bMa trận\b", "Matrix"),
  (r"\blấy mẫu lại\b", "resampling"),
  (r"\bLấy mẫu lại\b", "Resampling"),
  (r"\bRe-Sampling\b", "Resampling"),
  (r"\bre-sampling\b", "resampling"),
  (r"\bK-Hàng xóm gần nhất\b", "K-Nearest Neighbors"),
  (r"\bK-hàng xóm gần nhất\b", "K-nearest neighbors"),
  (r"\bthuật toán K-Nearest\b", "K-Nearest Neighbors"),
  (r"\bthực hành\b", "lab"),
  (r"\bThực hành\b", "Lab"),
  (r"\bphòng thí nghiệm\b", "lab"),
  (r"\bPhòng thí nghiệm\b", "Lab"),
  (r"\bclassification là\b", "được phân loại là"),
  (r"\bClassification là\b", "Được phân loại là"),
  (r"\bđược classification là\b", "được phân loại là"),
  (r"\bĐược classification là\b", "Được phân loại là"),
  (r"\bvấn đề classification\b", "classification problem"),
  (r"\bVấn đề classification\b", "Classification problem"),
  (r"\bchiếc wage\b", "wage"),
  (r"\bchiếc model\b", "model"),
  (r"\bbảng điều khiển\b", "panel"),
  (r"\bBảng điều khiển\b", "Panel"),
  (r"\bCác yếu tố của Statistical Learning\b", "The Elements of Statistical Learning"),
  (r"\bmodels phụ gia tổng quát\b", "generalized additive models"),
  (r"\bModels phụ gia tổng quát\b", "Generalized additive models"),
  (r"\bmodel phụ gia tổng quát\b", "generalized additive model"),
  (r"\bModel hậu cần\b", "logistic model"),
  (r"\bmodel hậu cần\b", "logistic model"),
  (r"\bVịnh ngây thơ\b", "naive Bayes"),
  (r"\bvịnh ngây thơ\b", "naive Bayes"),
  (r"\bcây xanh\b", "trees"),
  (r"\bCây xanh\b", "Trees"),
  (r"\bBộ classification\b", "classifier"),
  (r"\bbộ classification\b", "classifier"),
  (r"\bTài liệu Classification\b", "text classification"),
  (r"\btài liệu classification\b", "text classification"),
  (r"\btrình classification\b", "classifier"),
  (r"\bTrình classification\b", "Classifier"),
  (r"\bPhân tích sinh tồn\b", "survival analysis"),
  (r"\bphân tích sinh tồn\b", "survival analysis"),
  (r"\bChức năng Nguy hiểm\b", "Hazard function"),
  (r"\bchức năng nguy hiểm\b", "hazard function"),
  (r"\bMối nguy hiểm\b", "Hazard"),
  (r"\bmối nguy hiểm\b", "hazard"),
  (r"\bcây sống sót\b", "survival trees"),
  (r"\bCây sống sót\b", "Survival trees"),
  (r"\bHoàn thành matrix\b", "matrix completion"),
  (r"\bhoàn thành matrix\b", "matrix completion"),
  (r"\bclustering nghĩa là K\b", "K-means clustering"),
  (r"\bBỏ học\b", "dropout"),
  (r"\bbỏ học\b", "dropout"),
  (r"\bphương pháp thưa thớt\b", "shrinkage methods"),
  (r"\bPhương pháp thưa thớt\b", "Shrinkage methods"),
  (r"\bLời nói đầu\b", "Lời tựa"),
  (r"\blời nói đầu\b", "lời tựa"),
  (r"\bĐịnh tính Predictors\b", "qualitative predictors"),
  (r"\bđịnh tính predictors\b", "qualitative predictors"),
  (r"\bDựa trên sự thay thế cho ISLR\b", "Là phiên bản Python thay thế cho ISLR"),
  (r"\bEstimate f\b", "ước tính f"),
  (r"\bestimate f\b", "ước tính f"),
  (r"\bTại sao lại là ước tính f\b", "Tại sao ước tính f?"),
  (r"\bChúng ta thực hiện ước tính f\b", "Chúng ta ước tính f"),
  (r"\bĐược giám sát so với\b", "Supervised so với"),
  (r"\bđược giám sát\b", "supervised"),
  (r"\bĐược giám sát\b", "Supervised"),
  (r"\bModel tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bmodel tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bModels tuyến tính tổng quát\b", "generalized linear models"),
  (r"\bđóng bao\b", "bagging"),
  (r"\bĐóng bao\b", "Bagging"),
  (r"\bTăng cường\b", "boosting"),
  (r"\btăng cường\b", "boosting"),
  (r"\bMạng một lớp\b", "single-layer network"),
  (r"\bMạng đa lớp\b", "multi-layer network"),
  (r"\bĐiều chỉnh mạng\b", "network tuning"),
  (r"\bđiều chỉnh mạng\b", "network tuning"),
  (r"\bNội suy và giảm dần kép\b", "interpolation and double descent"),
  (r"\bLan truyền ngược\b", "backpropagation"),
  (r"\blan truyền ngược\b", "backpropagation"),
  (r"\bGiảm dần độ dốc ngẫu nhiên\b", "stochastic gradient descent"),
  (r"\bMức độ phù hợp đa biến\b", "multicollinearity"),
  (r"\bPhân tích biệt thức bậc hai\b", "quadratic discriminant analysis"),
  (r"\bphân tích biệt thức bậc hai\b", "quadratic discriminant analysis"),
  (r"\bPhân tích phân biệt tuyến tính\b", "linear discriminant analysis"),
  (r"\bphân tích phân biệt tuyến tính\b", "linear discriminant analysis"),
  (r"\bBình phương nhỏ nhất một phần\b", "partial least squares"),
  (r"\bLoại bỏ một lần\b", "leave-one-out"),
  (r"\bCài đặt Classification\b", "classification setting"),
  (r"\bcài đặt classification\b", "classification setting"),
  (r"\bđầu ra giám sát\b", "supervising output"),
  (r"\bbiến đầu vào\b", "input variables"),
  (r"\bBiến đầu vào\b", "Input variables"),
  (r"\bbiến đầu ra\b", "output variable"),
  (r"\bBiến đầu ra\b", "Output variable"),
  (r"\blần input\b", "lần đầu"),
  (r"\boutput được classification\b", "output được phân loại"),
  (r"\bđược classification hoặc\b", "được phân loại hoặc"),
  (r"\bđược classification\b", "được phân loại"),
  (r"\bĐược classification\b", "Được phân loại"),
  (r"\bđược advanced training\b", "có training nâng cao"),
  (r"\bđược training nâng cao\b", "có training nâng cao"),
  (r"\bcá thể\b", "individual"),
  (r"\bCá thể\b", "Individual"),
  (r"\bđược training\b", "được training"),
  (r"\btraining nâng cao\b", "advanced training"),
  (r"\bTeger K\b", "Cho một số nguyên dương K"),
  (r"\bTeger k\b", "Cho một số nguyên dương K"),
  (r"\bVịnh Bayes\b", "naive Bayes"),
  (r"\bmaxj\b", "max_j"),
  (r"\bPr\(Y = cam\|X\)", "Pr(Y = orange | X)"),
  (r"\bPr\(Y =1\|X = x0\)", "Pr(Y = 1 | X = x_0)"),
  (r"\bPr\(Y = 1\|X = x0\)", "Pr(Y = 1 | X = x_0)"),
  (r"\b  +", " "),
]

ORDER_FIXES: list[tuple[str, str]] = [
  (r"Regression so với Classification", "Regression versus Classification"),
  (r"Supervised so với Unsupervised Learning", "Supervised versus Unsupervised Learning"),
  (r"khả năng diễn giải Model", "model interpretability"),
  (r"độ chính xác của dự đoán và khả năng diễn giải Model", "prediction accuracy and model interpretability"),
  (r"Models tạo cho Classification", "generative models for classification"),
  (r"model phân biệt bậc hai", "quadratic discriminant model"),
  (r"phân tích phân biệt bậc hai model", "quadratic discriminant analysis model"),
]

CAMEL_RE = re.compile(r"\b[A-Z][a-zA-Z0-9]*(?:[A-Z][a-z0-9]*)+\b")
MATH_INLINE_RE = re.compile(r"\$[^$]+\$|\\\([^)]+\\\)|\\\[[^\]]+\\\]")
HEADING_NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\s+(.+)$")
FIGURE_TABLE_RE = re.compile(r"^(FIGURE|TABLE)\s+\d", re.I)
TOC_DOTS_RE = re.compile(r"\.{4,}")
GARBLED_RE = re.compile(r"[\x00-\x08\x0b-\x1f]")
NUMERIC_AXIS_RE = re.compile(r"^[\d\s.\-+−×=*(),/\\]+$")
ROMAN_PAGE_RE = re.compile(r"^(vii|viii|ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix|xx)$", re.I)
PAGE_HEADER_RE = re.compile(r"^\d{1,3}\s+\d+\.\s+")
PAGE_FOOTER_RE = re.compile(r"^\d+\.\s+.+\s+\d{1,3}$")
SECTION_PAGE_FOOTER_RE = re.compile(r"^\d+\.\d+\s+.+\s+\d{1,3}$")
KNOWN_CHAPTER_TITLES = frozenset({
  "preface", "lời tựa", "introduction", "giới thiệu", "contents", "nội dung",
  "index", "chỉ số", "bibliography", "exercises", "bài tập",
})
CHART_LABEL_WORDS = frozenset({
  "age", "wage", "year", "education", "volume", "direction", "degree",
  "error", "training", "test", "down", "up", "today", "yesterday",
  "z1", "z2", "z3", "lag1", "lag2", "lag3", "lag4", "lag5",
  "mpg", "horsepower", "weight", "displacement", "origin",
})


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
    if "\\" in replacement:
      text = re.sub(pattern, lambda _m, r=replacement: r, text)
    else:
      text = re.sub(pattern, replacement, text)
  text = re.sub(r"ZZT\d+ZZ", "", text)
  text = re.sub(r"ZZID\d+ZZ", "", text)
  return text.strip()


def capitalize_prose(text: str) -> str:
  if not text or text.lstrip().startswith(("$", "\\", "%")):
    return text
  if text and text[0].islower():
    text = text[0].upper() + text[1:]
  text = re.sub(
    r"([.!?]\s+)([a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ])",
    lambda m: m.group(1) + m.group(2).upper(),
    text,
  )
  return text


def polish_text(text: str) -> str:
  text = canonicalize_math_storage(text)
  text = apply_post_fixes(text)
  for pattern, replacement in ORDER_FIXES:
    text = re.sub(pattern, replacement, text)
  text = normalize_math_notation(text)
  text = capitalize_prose(text)
  return text


def map_outside_dollars(text: str, transform) -> str:
  """Apply transform only to prose segments (not inside $...$)."""
  if not text:
    return text
  out: list[str] = []
  i = 0
  while i < len(text):
    if text[i] == "$":
      j = text.find("$", i + 1)
      if j == -1:
        out.append(transform(text[i:]))
        break
      out.append(text[i : j + 1])
      i = j + 1
    else:
      j = text.find("$", i)
      if j == -1:
        out.append(transform(text[i:]))
        break
      out.append(transform(text[i:j]))
      i = j
  return "".join(out)


def canonicalize_math_storage(text: str) -> str:
  """Keep math as plain Pr(...), X_1 in blocks.json — LaTeX only at export."""
  if not text:
    return text
  text = text.replace("\\mid", "|")
  text = re.sub(r"\$\\Pr\(([^)]+)\)\$", r"Pr(\1)", text)
  text = re.sub(r"\$\\max_j\$", "max_j", text)
  text = re.sub(r"\$\\mathrm\{([^}]+)\}\$", r"\1", text)
  text = re.sub(r"\$([A-Za-z])_\{?(\d+)\}?\$", r"\1_\2", text)
  text = re.sub(r"\$x_\{?(\d+)\}?\$", r"x_\1", text)
  text = re.sub(r"\$\$+", "", text)
  return text


def normalize_math_notation(text: str) -> str:
  """Restore subscripts / math symbols mangled by translation."""
  if not text:
    return text

  def transform(segment: str) -> str:
    segment = re.sub(
      r"Pr\(([^)]+)\)",
      lambda m: "Pr(" + _normalize_pr_inner(m.group(1)) + ")",
      segment,
    )
    for letter in ("X", "x", "Y", "N", "K"):
      segment = re.sub(rf"\b{letter}(\d+)\b", rf"{letter}_\1", segment)
    segment = re.sub(r"\bmaxj\b", "max_j", segment)
    return segment

  return map_outside_dollars(text, transform)


def _normalize_pr_inner(inner: str) -> str:
  inner = inner.strip()
  inner = re.sub(r"\s*\|\s*", " | ", inner)
  inner = re.sub(r"([A-Za-z])(\d+)\b", r"\1_\2", inner)
  inner = re.sub(r"\s*=\s*", " = ", inner)
  inner = re.sub(r"\s+", " ", inner)
  return inner.strip()


def protect_segments(text: str) -> tuple[str, list[str]]:
  store: list[str] = []

  def repl(match: re.Match[str]) -> str:
    store.append(match.group(0))
    return _placeholder("S", len(store) - 1)

  patterns = [
    r"\$\$[\s\S]*?\$\$",
    r"\$[^$\n]+\$",
    r"\\\([^)]+\\\)",
    r"\\\[[^\]]+\\\]",
    r"Pr\([^)]+\)",
    r"\\[a-zA-Z]+(?:\{[^}]*\})?",
    r"\b[A-Za-z]_\{?\d+\}?",
    r"\b[A-Za-z]\d+\b",
    r"\([^)]*\|[^)]*\)",
    r"https?://\S+",
    r"doi\.org/\S+",
    r"\b[a-z]+_[a-z0-9_]+\b",
    r"\(\d+\.\d+\)",
    r"\\mathbb\{[^}]+\}",
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
  seg_protected, seg_store = protect_segments(term_protected)
  try:
    if len(seg_protected) <= CHUNK_SIZE:
      out = TRANSLATOR.translate(seg_protected)
    else:
      parts = []
      for i in range(0, len(seg_protected), CHUNK_SIZE):
        chunk = seg_protected[i : i + CHUNK_SIZE]
        parts.append(TRANSLATOR.translate(chunk))
        time.sleep(SLEEP_SEC)
      out = "".join(parts)
    out = restore_segments(out, seg_store)
    out = restore_terms(out, term_store)
    out = polish_text(out)
    CACHE[text] = out
    time.sleep(SLEEP_SEC)
    return out
  except Exception as exc:
    print(f"  [warn] translate failed: {exc!r}", file=sys.stderr)
    return text


def join_block_lines(block: dict) -> str:
  lines: list[str] = []
  for line in block.get("lines", []):
    lines.append("".join(span["text"] for span in line.get("spans", [])))
  parts: list[str] = []
  for line in lines:
    line = line.strip()
    if not line:
      continue
    if parts and parts[-1].endswith("-"):
      parts[-1] = parts[-1][:-1] + line
    else:
      parts.append(line)
  return re.sub(r"\s+", " ", " ".join(parts)).strip()


def _looks_like_dedication_line(text: str) -> bool:
  t = text.strip()
  if re.search(r"\d", t):
    return False
  if re.match(r"^[A-Z][a-z]+,", t):
    return True
  if re.match(r"^[A-Z][a-zA-Z'\-]+ (and |và )[A-Z]", t):
    return True
  if t.endswith(":") and len(t) < 55:
    return True
  return False


def _is_math_fragment(text: str) -> bool:
  t = text.strip()
  if not t or len(t) > 150:
    return False
  if re.fullmatch(r"[xX][\dTt\.]+", t):
    return True
  if re.fullmatch(r"[−\-+*/=.,\d\sA-Za-z\(\)|\\]+", t) and (
    "=" in t or "|" in t or "\\" in t or re.search(r"Pr\(", t)
  ):
    return len(t) < 80
  if re.fullmatch(r"[−\-+Ee\d\s.]+", t) and len(t) < 12:
    return True
  if t in {"K", "j", "J", "Tối đa", "Tối da", "Hàng xóm"}:
    return True
  if re.match(r"^I\s*N\d+$", t, re.I):
    return True
  if re.search(r"\\mathbb|\\hat|\\sum|_\{", t):
    return True
  return False


def real_heading_depth(text: str, max_size: float) -> int | None:
  """1=section, 2=subsection, 3=subsubsection; None = not a TOC heading."""
  t = text.strip()
  if not t or _is_math_fragment(t) or _is_figure_noise(t) or _is_chart_label(t):
    return None
  if PAGE_HEADER_RE.match(t) or PAGE_FOOTER_RE.match(t) or SECTION_PAGE_FOOTER_RE.match(t):
    return None
  if ROMAN_PAGE_RE.match(t):
    return None
  if _looks_like_dedication_line(t):
    return None
  if FIGURE_TABLE_RE.match(t) or TOC_DOTS_RE.search(t):
    return None
  if re.match(r"^(In lần đầu|First [Pp]rinting)", t):
    return None

  m = re.match(r"^(\d+\.\d+\.\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2:
    return 3
  m = re.match(r"^(\d+\.\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2:
    return 2
  m = re.match(r"^(\d+)\s+(.+)$", t)
  if m and len(m.group(2).strip()) > 2 and max_size >= 11:
    return 1

  tl = t.lower()
  if max_size >= 14 and any(k in tl for k in KNOWN_CHAPTER_TITLES):
    return 1

  if (
    max_size >= 12.5
    and len(t) < 70
    and not t.endswith(".")
    and t.count(" ") <= 8
    and not re.search(r"[.!?]", t)
    and re.search(r"[A-Za-zà-ỹ]{3,}", t)
  ):
    return 2

  return None


def classify_block(text: str, max_size: float) -> str:
  text = text.strip()
  if not text:
    return "meta"
  if COPYRIGHT_RE.search(text):
    return "meta"
  if SKIP_BLOCK_RE.match(text):
    return "meta"
  if SECTION_PAGE_FOOTER_RE.match(text):
    return "meta"
  if GARBLED_RE.search(text):
    return "meta"
  if ROMAN_PAGE_RE.match(text):
    return "meta"
  if NUMERIC_AXIS_RE.match(text) and len(text) < 60:
    return "meta"
  if _is_figure_noise(text):
    return "meta"
  if _is_chart_label(text):
    return "meta"
  if re.match(r"^\d+\.\s+\S+$", text) and len(text) < 35:
    return "meta"
  if FIGURE_TABLE_RE.match(text):
    return "caption"
  if TOC_DOTS_RE.search(text) and len(text) > 100:
    return "toc"
  if len(text) > 200 and text.count(". .") + text.count("..") > 8:
    return "toc"
  if _is_math_fragment(text):
    return "math"
  if real_heading_depth(text, max_size) is not None:
    return "heading"
  return "paragraph"


def block_heading_depth(block: dict) -> int | None:
  depth = block.get("heading_depth")
  if depth is not None:
    return depth
  text = (block.get("vi") or block.get("en") or "").strip()
  if not text:
    return None
  return real_heading_depth(text, block.get("max_size", 10))


def _is_figure_noise(text: str) -> bool:
  """Scatter markers / plot junk extracted as text (o, Oooo, Ồ, ...)."""
  t = text.strip()
  if not t:
    return True
  if re.fullmatch(r"[oOỒồ\s]+", t):
    return True
  if len(t) < 20 and re.fullmatch(r"[oO\s]+", t):
    return True
  if re.fullmatch(r"[xX]\d+", t):
    return True
  return False


def _is_chart_label(text: str) -> bool:
  t = text.strip()
  if not t or len(t) > 45:
    return False
  if FIGURE_TABLE_RE.match(t):
    return False
  tl = t.lower()
  vi_chart_phrases = (
    "xuống lên", "hướng đi hôm nay", "phần trăm thay đổi",
    "hai ngày trước", "ba ngày trước", "trình độ học vấn",
    "hôm qua", "xác suất dự đoán",
  )
  if len(t) < 40 and any(tl == p or tl.startswith(p) for p in vi_chart_phrases):
    return True
  if re.match(
    r"^(today|yesterday|lag\d|down up|direction|education|age|wage|year|z\d+)",
    tl,
  ):
    return True
  if re.match(r"^percentage change", tl):
    return True
  words = re.findall(r"[A-Za-z0-9]+", tl)
  if not words:
    return False
  if len(words) <= 3 and all(w in CHART_LABEL_WORDS or w.isdigit() for w in words):
    return True
  if len(t) < 25 and re.match(r"^Z\d+$", t, re.I):
    return True
  return False


def reclassify_block_kinds(pages: list[dict]) -> int:
  changed = 0
  for page in pages:
    for block in page["blocks"]:
      if block.get("kind") == "image":
        continue
      en = block.get("en", "").strip()
      if not en:
        continue
      new_kind = classify_block(en, block.get("max_size", 10))
      new_depth = real_heading_depth(en, block.get("max_size", 10))
      if new_kind == "heading" and new_depth is None:
        new_kind = "paragraph"
      vi = (block.get("vi") or "").strip()
      if vi and (_is_chart_label(vi) or _is_figure_noise(vi)):
        new_kind = "meta"
      if _is_figure_noise(en):
        new_kind = "meta"
      if _is_math_fragment(en) and new_kind == "heading":
        new_kind = "math"
      if vi and _is_math_fragment(vi) and new_kind == "heading":
        new_kind = "math"
      if new_kind != block.get("kind") or new_depth != block.get("heading_depth"):
        block["kind"] = new_kind
        block["heading_depth"] = new_depth
        changed += 1
      elif new_kind == block.get("kind") and new_depth != block.get("heading_depth"):
        block["heading_depth"] = new_depth
        changed += 1
  return changed


def extract_pdf_blocks(pdf_path: Path, lang: str) -> list[dict]:
  doc = fitz.open(pdf_path)
  pages: list[dict] = []
  for page_index, page in enumerate(doc):
    page_blocks: list[dict] = []
    for block_index, block in enumerate(page.get_text("dict")["blocks"]):
      block_id = f"p{page_index + 1}_b{block_index}"
      if block["type"] == 1:
        page_blocks.append(
          {
            "id": block_id,
            "kind": "image",
            "bbox": list(block["bbox"]),
            "image_file": f"figures/{block_id}.png",
          }
        )
        continue

      spans = [
        span
        for line in block.get("lines", [])
        for span in line.get("spans", [])
      ]
      if not spans:
        continue
      text = join_block_lines(block)
      if not text:
        continue
      max_size = max(span.get("size", 10) for span in spans)
      kind = classify_block(text, max_size)
      depth = real_heading_depth(text, max_size) if kind == "heading" else None
      if kind == "heading" and depth is None:
        kind = "paragraph"
      entry: dict = {
        "id": block_id,
        "kind": kind,
        "bbox": list(block["bbox"]),
        "max_size": round(max_size, 1),
        "heading_depth": depth,
      }
      if lang == "en":
        entry["en"] = text
        entry["vi"] = ""
      else:
        entry["vi_ref"] = normalize_vi_ref(text)
        entry["en"] = ""
        entry["vi"] = ""
      page_blocks.append(entry)
    pages.append({"page": page_index + 1, "blocks": page_blocks})
  doc.close()
  return pages


def normalize_vi_ref(text: str) -> str:
  text = re.sub(r"\s+", " ", text).strip()
  return text


def extract_images(pdf_path: Path, pages: list[dict], figures_dir: Path) -> None:
  figures_dir.mkdir(parents=True, exist_ok=True)
  doc = fitz.open(pdf_path)
  for page_info in pages:
    page = doc[page_info["page"] - 1]
    for block in page_info["blocks"]:
      if block.get("kind") != "image":
        continue
      bbox = fitz.Rect(block["bbox"])
      if bbox.width < 20 or bbox.height < 20:
        continue
      pix = page.get_pixmap(clip=bbox, dpi=150)
      out = figures_dir / f"{block['id']}.png"
      pix.save(out)
  doc.close()


def align_vi_reference(en_pages: list[dict], vi_pages: list[dict]) -> None:
  """Seed vi from Google-translated PDF by page + block order."""
  vi_by_page = {p["page"]: p["blocks"] for p in vi_pages}
  for page in en_pages:
    vi_blocks = vi_by_page.get(page["page"], [])
    vi_text_blocks = [b for b in vi_blocks if b.get("kind") != "image"]
    en_text_idx = 0
    for block in page["blocks"]:
      if block.get("kind") == "image" or block.get("kind") == "meta":
        continue
      if en_text_idx >= len(vi_text_blocks):
        break
      vi_ref = vi_text_blocks[en_text_idx].get("vi_ref", "")
      en_text_idx += 1
      if vi_ref and len(vi_ref) > 3:
        block["vi_ref"] = vi_ref


def should_translate_block(block: dict) -> bool:
  if block.get("kind") in {"image", "meta", "toc", "math"}:
    return False
  en = block.get("en", "").strip()
  if _is_figure_noise(en):
    return False
  return bool(en)


def vi_ref_usable(en: str, vi_ref: str, kind: str = "paragraph") -> bool:
  if not vi_ref or len(vi_ref) < 4:
    return False
  if vi_ref.strip().lower() == "machine translated by google":
    return False
  ratio = len(vi_ref) / max(len(en), 1)
  if ratio < 0.35 or ratio > 2.8:
    return False
  if COPYRIGHT_RE.search(vi_ref):
    return False
  if kind == "heading" and not heading_ref_plausible(en, vi_ref):
    return False
  return True


def heading_ref_plausible(en: str, vi_ref: str) -> bool:
  en_num = re.match(r"^(\d+(?:\.\d+)*)", en.strip())
  vi_num = re.match(r"^(\d+(?:\.\d+)*)", vi_ref.strip())
  if en_num and (not vi_num or en_num.group(1) != vi_num.group(1)):
    return False
  en_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", en)}
  if en_words and len(en) < 80:
    vi_lower = vi_ref.lower()
    if not any(w in vi_lower for w in en_words):
      return False
  return True


def translate_blocks(
  pages: list[dict],
  use_vi_ref: bool = True,
  page_range: tuple[int, int] | None = None,
  force: bool = False,
) -> None:
  load_cache()
  total = sum(
    1
    for p in pages
    for b in p["blocks"]
    if should_translate_block(b)
    and _page_in_range(p["page"], page_range)
  )
  done = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if not should_translate_block(block):
        continue
      done += 1
      en = block["en"].strip()
      if block.get("vi", "").strip() and not force:
        print(f"  [{done}/{total}] skip (has vi): {block['id']}")
        continue

      if use_vi_ref and block.get("vi_ref") and vi_ref_usable(
        en, block["vi_ref"], kind=block.get("kind", "paragraph")
      ):
        vi = polish_text(block["vi_ref"])
        block["vi"] = vi
        block["vi_source"] = "google_pdf"
        print(f"  [{done}/{total}] ref: {block['id']}")
      else:
        vi = translate_text(en)
        block["vi"] = vi
        block["vi_source"] = "translator"
        print(f"  [{done}/{total}] tr: {block['id']}")
      if done % 10 == 0:
        save_cache()
  save_cache()


def _page_in_range(page: int, page_range: tuple[int, int] | None) -> bool:
  if page_range is None:
    return True
  return page_range[0] <= page <= page_range[1]


def cleanup_noise_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
) -> int:
  cleaned = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      vi = (block.get("vi") or "").strip()
      if _is_figure_noise(en) or _is_figure_noise(vi):
        block["kind"] = "meta"
        block["vi"] = ""
        cleaned += 1
  return cleaned


def fix_existing_blocks(
  pages: list[dict],
  page_range: tuple[int, int] | None = None,
  reclassify: bool = True,
) -> None:
  if reclassify:
    if page_range is None:
      n = reclassify_block_kinds(pages)
    else:
      subset = [p for p in pages if _page_in_range(p["page"], page_range)]
      n = reclassify_block_kinds(subset)
    print(f"Reclassified {n} blocks.")
  recovered = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      en = (block.get("en") or "").strip()
      if block.get("kind") != "meta" or not en or not _is_math_fragment(en):
        continue
      vi = (block.get("vi") or "").strip()
      if vi and not _is_math_fragment(vi):
        continue
      block["kind"] = "math"
      if not vi:
        block["vi"] = normalize_math_notation(en)
      recovered += 1
  if recovered:
    print(f"Recovered {recovered} math blocks from meta.")
  cleaned = cleanup_noise_blocks(pages, page_range)
  if cleaned:
    print(f"Cleaned {cleaned} figure-noise blocks (o/O/Ồ/X1...).")
  realigned = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      if block.get("kind") != "math":
        continue
      en = (block.get("en") or "").strip()
      vi = (block.get("vi") or "").strip()
      if en and _is_math_fragment(en) and vi and not _is_math_fragment(vi):
        block["vi"] = normalize_math_notation(en)
        realigned += 1
      elif vi and (SECTION_PAGE_FOOTER_RE.match(vi) or PAGE_HEADER_RE.match(vi)):
        if not en or not _is_math_fragment(en):
          block["kind"] = "meta"
          block["vi"] = ""
          realigned += 1
  if realigned:
    print(f"Fixed {realigned} misaligned math/page-header blocks.")
  changed = 0
  for page in pages:
    if not _page_in_range(page["page"], page_range):
      continue
    for block in page["blocks"]:
      vi = block.get("vi", "")
      if not vi:
        continue
      fixed = polish_text(vi)
      if fixed != vi:
        block["vi"] = fixed
        changed += 1
  print(f"Polished {changed} blocks.")


def latex_escape_mixed(text: str) -> str:
  """Escape prose but keep $...$ math segments."""
  text = normalize_math_notation(text)
  text = inject_latex_math_delimiters(text)
  out: list[str] = []
  i = 0
  while i < len(text):
    if text[i] == "$":
      j = text.find("$", i + 1)
      if j == -1:
        out.append(latex_escape(text[i:]))
        break
      out.append(text[i : j + 1])
      i = j + 1
    else:
      j = text.find("$", i)
      if j == -1:
        out.append(latex_escape(text[i:]))
        break
      out.append(latex_escape(text[i:j]))
      i = j
  return "".join(out)


def inject_latex_math_delimiters(text: str) -> str:
  """Wrap Pr(...) and letter_subscript tokens in $...$ if not already."""
  if not text:
    return text

  def transform(segment: str) -> str:
    def pr_repl(m: re.Match[str]) -> str:
      inner = m.group(1)
      inner = re.sub(r"\s*\|\s*", lambda _m: " \\mid ", inner)
      inner = re.sub(r"\b([A-Za-z])_(\d+)\b", r"\1_{\2}", inner)
      inner = re.sub(r"(?<!\\mathrm\{)\borange\b", r"\\mathrm{orange}", inner)
      return f"$\\Pr({inner})$"

    segment = re.sub(r"Pr\(([^)]+)\)", pr_repl, segment)

    def subscript_outside(s: str) -> str:
      for letter in ("X", "Y", "N"):
        s = re.sub(rf"\b{letter}_(\d+)\b", rf"${letter}_{{\1}}$", s)
        s = re.sub(rf"\b{letter}(\d+)\b", rf"${letter}_{{\1}}$", s)
      s = re.sub(r"\bx_(\d+)\b", r"$x_{\1}$", s)
      s = re.sub(r"\bmax_j\b", lambda _m: "$\\max_j$", s)
      s = re.sub(r"\by_i\b", lambda _m: "$y_i$", s)
      return s

    return map_outside_dollars(segment, subscript_outside)

  return map_outside_dollars(text, transform)


def format_math_fragment(text: str) -> str:
  text = normalize_math_notation(text.strip())
  text = re.sub(r"\s*\((\d+\.\d+)\)\s*$", "", text)
  text = text.replace("−", "-")
  text = inject_latex_math_delimiters(text)
  if text.startswith("$") and text.endswith("$"):
    return text
  return f"${text}$"


def latex_escape(text: str) -> str:
  replacements = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
  }
  out = []
  for ch in text:
    out.append(replacements.get(ch, ch))
  return "".join(out)


def translation_stats(pages: list[dict]) -> tuple[int, int]:
  total = 0
  translated = 0
  for page in pages:
    for block in page["blocks"]:
      if block.get("kind") in {"image", "meta"}:
        continue
      total += 1
      if (block.get("vi") or "").strip():
        translated += 1
  return translated, total


def heading_command(block: dict) -> tuple[str, str, bool]:
  """Return (latex_cmd, title, starred). Starred = not in TOC."""
  text = (block.get("vi") or "").strip()
  if not text:
    text = (block.get("en") or "").strip()
  depth = block_heading_depth(block)
  m = HEADING_NUM_RE.match(text)
  if m:
    title = m.group(2).strip()
  else:
    title = text.strip()
  if depth is None:
    return "textbf", title, True
  if depth <= 1:
    return "section", title, False
  if depth == 2:
    return "subsection", title, False
  return "subsubsection", title, False


def block_to_latex(block: dict, part_dir: Path, allow_en_fallback: bool = False) -> str:
  kind = block.get("kind")
  if kind == "image":
    img = part_dir / block.get("image_file", "")
    if not img.exists():
      return f"% missing image {block['id']}\n"
    rel = Path(block["image_file"]).as_posix()
    return (
      "\\begin{figure}[ht]\n"
      "\\centering\n"
      f"\\includegraphics[width=0.9\\linewidth]{{{rel}}}\n"
      "\\end{figure}\n\n"
    )
  if kind == "meta":
    note = (block.get("vi") or block.get("en", "")).strip()
    if not note or _is_figure_noise(note):
      return ""
    return f"% {latex_escape(note)}\n"
  if kind == "toc":
    return f"% [muc luc] {block.get('id', '')}\n"

  if kind == "math":
    en = (block.get("en") or "").strip()
    vi = (block.get("vi") or "").strip()
    if vi and (_is_math_fragment(vi) or re.search(r"Pr\(|\\|=|_[{\d]", vi)):
      text = vi
    else:
      text = en
    if not text:
      return ""
    body = format_math_fragment(text)
    if body.startswith("$") and body.endswith("$"):
      body = body[1:-1]
    return f"\\[{body}\\]\n\n"

  vi = (block.get("vi") or "").strip()
  en = (block.get("en") or "").strip()
  if not vi:
    if allow_en_fallback and en:
      text = en
    elif en:
      return (
        f"% TODO DICH {block['id']}\n"
        f"% EN: {latex_escape(en[:240])}{'...' if len(en) > 240 else ''}\n\n"
      )
    else:
      return ""
  else:
    text = vi

  if kind == "heading":
    cmd, title, starred = heading_command(block)
    star = "*" if starred else ""
    if cmd == "textbf":
      return f"\\textbf{{{latex_escape(title)}}}\n\n"
    return f"\\{cmd}{star}{{{latex_escape(title)}}}\n\n"
  if kind == "caption":
    return f"\\noindent\\textit{{{latex_escape_mixed(text)}}}\n\n"
  return f"{latex_escape_mixed(text)}\n\n"


def export_latex(
  part_dir: Path,
  meta: dict,
  allow_en_fallback: bool = False,
  include_toc: bool = True,
) -> None:
  blocks_path = part_dir / "blocks.json"
  data = json.loads(blocks_path.read_text(encoding="utf-8"))
  pages = data["pages"]
  translated, total = translation_stats(pages)
  missing = total - translated

  if missing > 0 and not allow_en_fallback:
    print(
      f"  [warn] {missing}/{total} blocks chua dich (field 'vi' trong).",
      file=sys.stderr,
    )
    print(
      "  Chay: python translate_pdf_vi.py --part N --translate",
      file=sys.stderr,
    )
  elif missing > 0:
    print(f"  [warn] {missing}/{total} blocks dung ban tieng Anh (fallback).")

  content_lines: list[str] = []
  for page in pages:
    content_lines.append(f"% --- page {page['page']} ---\n")
    for block in page["blocks"]:
      content_lines.append(block_to_latex(block, part_dir, allow_en_fallback))

  content_tex = "".join(content_lines)
  (part_dir / "content.tex").write_text(content_tex, encoding="utf-8")

  title = meta.get("title", "An Introduction to Statistical Learning")
  toc_block = "\\tableofcontents\n\\newpage\n" if include_toc else ""
  main_tex = f"""\\documentclass[12pt,a4paper]{{article}}
\\usepackage[a4paper,margin=2.5cm]{{geometry}}
\\usepackage{{fontspec}}
\\usepackage{{polyglossia}}
\\setdefaultlanguage{{vietnamese}}
\\setotherlanguage{{english}}
\\usepackage{{amsmath,amssymb,amsfonts}}
\\usepackage{{graphicx}}
\\usepackage{{hyperref}}
\\usepackage{{indentfirst}}
\\setcounter{{secnumdepth}}{{3}}
\\setcounter{{tocdepth}}{{2}}

\\title{{{latex_escape(title)} (Tiếng Việt)}}
\\author{{Bản dịch chỉnh sửa từ ISLP}}
\\date{{\\today}}

\\begin{{document}}
\\maketitle
{toc_block}\\input{{content.tex}}
\\end{{document}}
"""
  (part_dir / "main.tex").write_text(main_tex, encoding="utf-8")
  print(f"Wrote {part_dir / 'main.tex'} and content.tex ({translated}/{total} blocks tieng Viet)")


def compile_latex(part_dir: Path, min_translated_ratio: float = 0.05) -> None:
  main = part_dir / "main.tex"
  if not main.exists():
    raise FileNotFoundError(f"Missing {main}; run --export-latex first.")

  blocks_path = part_dir / "blocks.json"
  if blocks_path.exists():
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    translated, total = translation_stats(data["pages"])
    if total and translated / total < min_translated_ratio:
      raise RuntimeError(
        f"Chi co {translated}/{total} blocks da dich. "
        "Chay --translate truoc khi compile."
      )
  pdf = part_dir / "main.pdf"
  for _ in range(2):
    subprocess.run(
      ["xelatex", "-interaction=nonstopmode", "main.tex"],
      cwd=part_dir,
      capture_output=True,
      text=True,
      encoding="utf-8",
      errors="replace",
    )
  if not pdf.exists():
    log = part_dir / "main.log"
    tail = log.read_text(encoding="utf-8", errors="replace")[-2000:] if log.exists() else ""
    print(tail, file=sys.stderr)
    raise RuntimeError("xelatex did not produce main.pdf")
  out_name = part_dir.name + ".pdf"
  shutil.copy2(pdf, part_dir.parent / out_name)
  print(f"PDF: {part_dir.parent / out_name}")


def part_paths(part: int) -> dict[str, Path]:
  name = f"An Introduction to Statistical Learning-{part}.pdf"
  return {
    "en": EN_DIR / name,
    "vi_ref": VI_REF_DIR / name,
    "out": OUT_DIR / f"An Introduction to Statistical Learning-{part}",
  }


def run_extract(part: int) -> Path:
  paths = part_paths(part)
  if not paths["en"].exists():
    raise FileNotFoundError(paths["en"])

  part_dir = paths["out"]
  part_dir.mkdir(parents=True, exist_ok=True)
  figures_dir = part_dir / "figures"

  print(f"Extracting EN: {paths['en'].name}")
  en_pages = extract_pdf_blocks(paths["en"], lang="en")
  extract_images(paths["en"], en_pages, figures_dir)

  if paths["vi_ref"].exists():
    print(f"Extracting VI reference: {paths['vi_ref'].name}")
    vi_pages = extract_pdf_blocks(paths["vi_ref"], lang="vi")
    align_vi_reference(en_pages, vi_pages)
  else:
    print("  [warn] VI reference PDF not found; will translate from EN only.")

  payload = {
    "part": part,
    "title": "An Introduction to Statistical Learning",
    "source_en": str(paths["en"]),
    "source_vi_ref": str(paths["vi_ref"]) if paths["vi_ref"].exists() else None,
    "pages": en_pages,
  }
  blocks_path = part_dir / "blocks.json"
  blocks_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
  print(f"Wrote {blocks_path} ({sum(len(p['blocks']) for p in en_pages)} blocks)")
  return part_dir


def main() -> None:
  parser = argparse.ArgumentParser(
    description="Translate ISL PDF to editable Vietnamese LaTeX",
  )
  parser.add_argument("--part", type=int, default=1, help="PDF part number (default: 1)")
  parser.add_argument("--extract", action="store_true", help="Extract blocks from PDFs")
  parser.add_argument("--translate", action="store_true", help="Translate blocks.json")
  parser.add_argument("--export-latex", action="store_true", help="Export blocks.json to LaTeX")
  parser.add_argument("--compile", action="store_true", help="Compile main.tex to PDF (xelatex)")
  parser.add_argument("--all", action="store_true", help="extract + translate + export + compile")
  parser.add_argument(
    "--fix-existing",
    action="store_true",
    help="Apply post-fixes to existing vi text in blocks.json",
  )
  parser.add_argument(
    "--no-vi-ref",
    action="store_true",
    help="Ignore Google-VI PDF; always use online translator",
  )
  parser.add_argument(
    "--force",
    action="store_true",
    help="Re-translate blocks even if vi is already set",
  )
  parser.add_argument(
    "--page-range",
    type=str,
    default=None,
    help="Only translate/fix pages in range, e.g. 12-20",
  )
  parser.add_argument(
    "--allow-en-fallback",
    action="store_true",
    help="Export/export PDF with English text when vi is missing (not recommended)",
  )
  parser.add_argument(
    "--no-toc",
    action="store_true",
    help="Do not include \\tableofcontents in exported main.tex",
  )
  args = parser.parse_args()

  page_range: tuple[int, int] | None = None
  if args.page_range:
    m = re.match(r"^(\d+)\s*-\s*(\d+)$", args.page_range.strip())
    if not m:
      raise SystemExit("--page-range must look like 12-20")
    page_range = (int(m.group(1)), int(m.group(2)))

  part_dir = part_paths(args.part)["out"]

  if args.all:
    args.extract = args.translate = args.export_latex = args.compile = True

  if not any([args.extract, args.translate, args.export_latex, args.compile, args.fix_existing]):
    parser.print_help()
    print("\nExample: python translate_pdf_vi.py --part 1 --all")
    return

  if args.extract:
    part_dir = run_extract(args.part)

  blocks_path = part_dir / "blocks.json"
  if args.fix_existing:
    if not blocks_path.exists():
      raise FileNotFoundError(blocks_path)
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    fix_existing_blocks(data["pages"], page_range=page_range)
    blocks_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return

  if args.translate:
    if not blocks_path.exists():
      part_dir = run_extract(args.part)
      blocks_path = part_dir / "blocks.json"
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    print(f"Translating part {args.part}...")
    translate_blocks(
      data["pages"],
      use_vi_ref=not args.no_vi_ref,
      page_range=page_range,
      force=args.force,
    )
    blocks_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

  if args.export_latex:
    if not blocks_path.exists():
      raise FileNotFoundError(blocks_path)
    data = json.loads(blocks_path.read_text(encoding="utf-8"))
    export_latex(
      part_dir,
      data,
      allow_en_fallback=args.allow_en_fallback,
      include_toc=not args.no_toc,
    )

  if args.compile:
    compile_latex(
      part_dir,
      min_translated_ratio=0.0 if args.allow_en_fallback else 0.05,
    )


if __name__ == "__main__":
  main()
