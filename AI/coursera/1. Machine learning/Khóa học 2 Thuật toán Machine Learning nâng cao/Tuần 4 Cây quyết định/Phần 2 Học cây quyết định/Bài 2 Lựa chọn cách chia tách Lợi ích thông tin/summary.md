# Bài 2 — Lựa chọn cách chia tách: Information gain

## Chọn feature tại root

So sánh 3 lựa chọn split trên 10 mẫu (5 mèo, 5 chó):

| Feature | Entropy trái | Entropy phải |
|---------|-------------|-------------|
| Ear shape | H(0.8) ≈ 0.72 | H(0.2) ≈ 0.72 |
| Face shape | H(4/7) ≈ 0.99 | H(1/3) ≈ 0.92 |
| Whiskers | H(0.75) | H(0.33) |

## Weighted average entropy

- Trọng số theo tỷ lệ mẫu vào mỗi nhánh: \(w^{\text{left}}\), \(w^{\text{right}}\)
- Ví dụ ear shape: \(\frac{5}{10} H(0.8) + \frac{5}{10} H(0.2)\)

## Information gain

\[
\text{IG} = H(p_1^{\text{root}}) - \left[ w^{\text{left}} H(p_1^{\text{left}}) + w^{\text{right}} H(p_1^{\text{right}}) \right]
\]

- Root: \(p_1 = 0.5\) → \(H(0.5) = 1\)
- Ear shape: IG = **0.28**
- Face shape: IG = 0.03
- Whiskers: IG = 0.12
- Chọn feature có **information gain** cao nhất → **ear shape**

## Tại sao dùng reduction thay vì entropy trung bình?

- Tiêu chí dừng: nếu IG quá nhỏ → không split thêm (tránh overfitting)
- Ký hiệu: \(p_1^{\text{left/right/root}}\), \(w^{\text{left/right}}\)
