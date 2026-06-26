## Hồi quy Logistic

- Thuật toán **phân loại nhị phân**: nhãn **y** chỉ là 0 hoặc 1
- **ŷ** (y hat) = ước lượng xác suất \(P(y=1 \mid x)\)

## Mô hình

- Tham số: **w** ∈ \(\mathbb{R}^{n_x}\), **b** ∈ \(\mathbb{R}\)
- Hồi quy tuyến tính \(\hat{y} = w^T x + b\) **không phù hợp** — output có thể < 0 hoặc > 1

| Cách | Công thức | Vấn đề |
|---|---|---|
| Linear | \(\hat{y} = w^T x + b\) | Không giới hạn [0,1] |
| Logistic | \(\hat{y} = \sigma(w^T x + b)\) | Output là xác suất |

## Hàm sigmoid

\[
\sigma(z) = \frac{1}{1 + e^{-z}}, \quad z = w^T x + b
\]

- z lớn → σ(z) ≈ 1; z âm lớn → σ(z) ≈ 0
- Đi qua 0.5 khi z = 0

## Ký hiệu tham số

- Khóa này tách **w** và **b** (không dùng \(x_0=1\) gộp vào **θ** như một số khóa ML khác)
- Mục tiêu: học **w, b** để **ŷ** ước lượng tốt xác suất y = 1
- Bước tiếp: định nghĩa **hàm chi phí** để cập nhật tham số
