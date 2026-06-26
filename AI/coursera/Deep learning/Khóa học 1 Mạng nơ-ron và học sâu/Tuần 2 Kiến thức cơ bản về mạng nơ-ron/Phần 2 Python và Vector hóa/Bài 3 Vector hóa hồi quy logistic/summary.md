## Vector hóa Forward Propagation

- Mục tiêu: 1 iteration gradient descent trên **toàn bộ m mẫu** — **không for-loop** qua m

## Ma trận dữ liệu

- **X**: \(n_x \times m\) — cột i = \(x^{(i)}\)
- **Z** = \([z^{(1)}, \ldots, z^{(m)}]\): \(1 \times m\)

## Tính Z cho tất cả mẫu

\[
Z = w^T X + b
\]

```python
Z = np.dot(w.T, X) + b   # shape (1, m)
```

- **b** là số thực → Python **broadcast** thành vector 1×m (cộng b vào mỗi cột)

## Tính A (activation)

- **A** = σ(Z) — sigmoid áp dụng **element-wise** cho toàn bộ Z
- Xếp \(a^{(1)}, \ldots, a^{(m)}\) ngang → ma trận **A** (1×m)

## Tóm tắt

| Bước | Vectorized |
|---|---|
| Forward Z | `Z = w.T @ X + b` |
| Forward A | `A = sigmoid(Z)` |

- Video tiếp: vector hóa **backward propagation** (gradient)
