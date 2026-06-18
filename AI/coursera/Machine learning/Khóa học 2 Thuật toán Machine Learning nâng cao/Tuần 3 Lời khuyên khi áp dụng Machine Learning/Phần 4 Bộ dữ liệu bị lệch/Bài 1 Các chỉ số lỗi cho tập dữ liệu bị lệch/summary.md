# Bài 1 — Chỉ số lỗi cho tập dữ liệu bị lệch

## Skewed dataset

- Tỷ lệ positive/negative rất lệch (xa 50-50)
- **Accuracy** gây hiểu lầm

## Ví dụ: bệnh hiếm

- Model 1% error nghe hay — nhưng chỉ 0.5% bệnh nhân mắc bệnh
- Thuật toán luôn in y=0 → accuracy 99.5%, **vô dụng** làm chẩn đoán
- Khó so sánh các model chỉ bằng accuracy

## Confusion matrix

| | Actual 1 | Actual 0 |
|---|---|---|
| Pred 1 | **TP** (true positive) | **FP** (false positive) |
| Pred 0 | **FN** (false negative) | **TN** (true negative) |

## Precision

- Trong số dự đoán positive, bao nhiêu đúng?
- P = TP / (TP + FP)
- Ví dụ: 15/(15+5) = 75%

## Recall

- Trong số thực sự positive, phát hiện được bao nhiêu?
- R = TP / (TP + FN)
- Ví dụ: 15/(15+10) = 60%
- Phát hiện thuật toán luôn dự đoán 0 (recall = 0)

## Yêu cầu

- Cả **precision** và **recall** đều phải đủ cao mới là model hữu ích
