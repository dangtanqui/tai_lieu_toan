## Gradient Descent — một mẫu

- Đồ thị: z → a = σ(z) → L(a, y)
- Mục tiêu: cập nhật **w, b** để giảm loss

## Công thức đạo hàm (1 mẫu)

| Biến code | Công thức |
|---|---|
| **da** | \(-\frac{y}{a} + \frac{1-y}{1-a}\) |
| **dz** | \(a - y\) |
| **dw₁** | \(x_1 \cdot dz\) |
| **dw₂** | \(x_2 \cdot dz\) |
| **db** | \(dz\) |

- **dz = a − y** đến từ chain rule: dL/da × da/dz

## Cập nhật tham số

\[
w_j := w_j - \alpha \cdot dw_j, \quad b := b - \alpha \cdot db
\]

## Computation graph

- Forward: z = wᵀx + b → a = σ(z) → L
- Backward: tính da → dz → dw, db
- Chuẩn bị cho mở rộng sang **mạng nơ-ron đầy đủ**

## Video tiếp

- Mở rộng lên **m mẫu** huấn luyện (toàn bộ tập dữ liệu)
