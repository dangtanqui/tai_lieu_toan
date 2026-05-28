#!/usr/bin/env bash
# Tải PNG minh họa từ Google ML Crash Course (pdflatex).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BASE="https://developers.google.com/static/machine-learning/crash-course"

fetch() {
  local url="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
  if [[ -f "$dest" ]]; then
    echo "skip: $dest"
    return
  fi
  echo "get: $dest"
  curl -fsSL "$url" -o "$dest"
}

LOGISTIC="$ROOT/2. Học máy ứng dụng/1. Mô hình học máy/2. Hồi quy logistic/images/logistic-regression"
fetch "$BASE/logistic-regression/images/sigmoid_function_with_axes.png" "$LOGISTIC/sigmoid_function_with_axes.png"
fetch "$BASE/logistic-regression/images/linear_to_logistic.png" "$LOGISTIC/linear_to_logistic.png"

CLASS="$ROOT/2. Học máy ứng dụng/1. Mô hình học máy/3. Phân loại/images/classification"
for f in auc_1-0 auc_0-5 no_slider_data prauc auc_0-65 auc_0-93 auc_abc \
  auc_0-77 auc_0-508 auc_0-623 auc_0-31 auc_0-32 auc_0-65; do
  fetch "$BASE/classification/images/${f}.png" "$CLASS/${f}.png"
done

echo "Done."
