# Bài 8 — Đạo hàm hàm kích hoạt

## Tại sao cần?

Khi triển khai **backpropagation**, phải tính đạo hàm (slope) của hàm kích hoạt.

## Sigmoid: g'(z)

- **g'(z) = g(z) · (1 − g(z))**
- Khi đã có **a = g(z)** → **g'(z) = a · (1 − a)**

| z | g(z) | g'(z) |
|---|---|---|
| 10 | ≈ 1 | ≈ 0 |
| −10 | ≈ 0 | ≈ 0 |
| 0 | 0.5 | **0.25** |

## Tanh: g'(z)

- **g'(z) = 1 − (tanh(z))²**
- Khi a = tanh(z) → **g'(z) = 1 − a²**

| z | g'(z) |
|---|---|
| 10 hoặc −10 | ≈ 0 |
| 0 | **1** |

## ReLU: g'(z)

| Điều kiện | g'(z) |
|---|---|
| z < 0 | **0** |
| z > 0 | **1** |
| z = 0 | Không xác định — đặt 0 hoặc 1 đều được |

## Leaky ReLU: g'(z)

| Điều kiện | g'(z) |
|---|---|
| z < 0 | **0.01** |
| z > 0 | **1** |

## Ký hiệu

- **g'(z)** = viết tắt của d/dz g(z) (prime notation)
- ReLU tại z=0: gọi là **sub-gradient** — gradient descent vẫn hoạt động

## Mẹo triển khai

- Tính **a** trước trong forward pass → dùng công thức đơn giản để tính **g'(z)** trong backprop
- Bước tiếp: **gradient descent** cho mạng nơ-ron
