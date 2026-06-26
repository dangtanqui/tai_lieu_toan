# Bài 7 — Tham số so với siêu tham số

## Phân biệt

| Loại | Ví dụ | Cách học |
|------|-------|----------|
| **Tham số** (parameters) | \(W, b\) | Gradient descent |
| **Siêu tham số** (hyperparameters) | \(\alpha\), số iteration, \(L\), \(n^{[l]}\), hàm activation | **Bạn** chọn thủ công |

- Siêu tham số **điều khiển** giá trị cuối cùng của \(W, b\)
- Deep learning có **rất nhiều** siêu tham số (khóa 2: momentum, mini-batch size, regularization…)

## Quy trình tinh chỉnh — thực nghiệm

```
Ý tưởng (vd. α=0.01) → Implement → Chạy → Quan sát J
→ Điều chỉnh (vd. α=0.05) → Lặp lại
```

- \(\alpha\) quá nhỏ: học chậm
- \(\alpha\) quá lớn: \(J\) **phân kỳ**
- Không biết trước giá trị tốt nhất → **thử nhiều giá trị**

## Lưu ý thực tế

- Intuition từ lĩnh vực này (CV, NLP…) **không luôn** chuyển sang lĩnh vực khác
- Giá trị tốt nhất có thể **thay đổi theo thời gian** (dữ liệu, phần cứng)
- Nên **kiểm tra lại** siêu tham số định kỳ (vài tháng) khi làm dài hạn
- Đánh giá trên **validation/cross-validation set**

## Tóm tắt

- Áp dụng deep learning là quá trình **thực nghiệm** (empirical)
- Khóa 2 sẽ dạy cách khám phá không gian siêu tham số **có hệ thống**
- Hiện tại đã đủ công cụ cho bài tập lập trình tuần 4
