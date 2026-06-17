## Overfitting (quá khớp) & Underfitting (thiếu khớp)

| | Underfitting | Vừa đủ | Overfitting |
|---|-------------|--------|-------------|
| Thuật ngữ | **High bias** | — | **High variance** |
| Fit training | Kém | Tốt | Rất tốt (có thể J = 0) |
| Dữ liệu mới | Kém | Tốt | Kém |
| Ví dụ (giá nhà) | Đường thẳng | Đa thức bậc 2 | Đa thức bậc 4, lượn sóng |

## Generalization (khả năng tổng quát)
- Model tốt = dự đoán tốt trên **mẫu chưa thấy**

## Classification
- Underfit: ranh giới **thẳng** quá đơn giản
- Vừa đủ: ellipse (đa thức bậc 2)
- Overfit: ranh giới **quá phức tạp**, ôm sát training

## Mục tiêu
- Tránh cả underfitting lẫn overfitting — model **vừa phải** (như cốc cháo vừa ăn trong truyện Gấu)

## Giải pháp (preview)
- **Regularization** — kỹ thuật quan trọng, dùng rộng rãi
