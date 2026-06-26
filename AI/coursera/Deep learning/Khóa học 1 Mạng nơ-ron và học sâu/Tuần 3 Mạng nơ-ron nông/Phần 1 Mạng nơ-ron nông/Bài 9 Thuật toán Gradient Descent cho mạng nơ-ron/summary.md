# Bài 9 — Gradient Descent cho mạng nơ-ron

## Tham số và kích thước

| Tham số | Kích thước |
|---|---|
| W⁽¹⁾ | n₁ × n₀ |
| b⁽¹⁾ | n₁ × 1 |
| W⁽²⁾ | n₂ × n₁ |
| b⁽²⁾ | n₂ × 1 |

## Cost function (binary classification)

- **J = (1/m) Σ L(ŷ⁽ⁱ⁾, y⁽ⁱ⁾)** — giống logistic regression
- Loss L dùng công thức cross-entropy như tuần trước

## Vòng lặp gradient descent

1. **Forward prop** → tính ŷ
2. **Backward prop** → tính dW, db
3. **Cập nhật:** W := W − α·dW, b := b − α·db
4. Lặp đến khi hội tụ

## Forward propagation (4 phương trình)

```
Z⁽¹⁾ = W⁽¹⁾X + b⁽¹⁾
A⁽¹⁾ = g⁽¹⁾(Z⁽¹⁾)
Z⁽²⁾ = W⁽²⁾A⁽¹⁾ + b⁽²⁾
A⁽²⁾ = g⁽²⁾(Z⁽²⁾)    ← sigmoid cho binary classification
```

## Backpropagation (6 phương trình)

```
dZ⁽²⁾ = A⁽²⁾ − Y
dW⁽²⁾ = (1/m) · dZ⁽²⁾ · A⁽¹⁾ᵀ
db⁽²⁾ = (1/m) · np.sum(dZ⁽²⁾, axis=1, keepdims=True)
dZ⁽¹⁾ = W⁽²⁾ᵀ · dZ⁽²⁾ * g⁽¹⁾'(Z⁽¹⁾)    ← element-wise *
dW⁽¹⁾ = (1/m) · dZ⁽¹⁾ · Xᵀ
db⁽¹⁾ = (1/m) · np.sum(dZ⁽¹⁾, axis=1, keepdims=True)
```

## Lưu ý triển khai

- **keepdims=True** trong np.sum → tránh mảng rank-1 sai kích thước
- 3 phương trình đầu backprop **giống logistic regression**
- Khởi tạo W **ngẫu nhiên** (không phải 0) — xem Bài 11
