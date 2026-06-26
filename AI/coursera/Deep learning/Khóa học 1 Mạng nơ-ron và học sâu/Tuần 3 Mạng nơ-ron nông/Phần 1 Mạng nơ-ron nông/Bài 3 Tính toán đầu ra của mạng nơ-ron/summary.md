# Bài 3 — Tính toán đầu ra mạng nơ-ron

## Mỗi node = 2 bước tính toán

Giống logistic regression, lặp lại cho từng node:

1. **z** = wᵀx + b
2. **a** = sigmoid(z)

## Ví dụ node đầu tiên (hidden layer 1)

- z⁽¹⁾₁ = (w⁽¹⁾₁)ᵀx + b⁽¹⁾₁
- a⁽¹⁾₁ = sigmoid(z⁽¹⁾₁)
- Ký hiệu: **l** (superscript) = số layer, **i** (subscript) = số node

## Vector hóa layer 1

Thay vì for-loop qua 4 node:

- **Z⁽¹⁾** = W⁽¹⁾X + b⁽¹⁾ (ma trận 4×3 × vector 3×1 + 4×1)
- **A⁽¹⁾** = sigmoid(Z⁽¹⁾) — áp dụng **element-wise**

| Ma trận | Kích thước |
|---|---|
| W⁽¹⁾ | 4 × 3 (stack 4 vector w thành hàng) |
| Z⁽¹⁾, A⁽¹⁾ | 4 × 1 |

**Quy tắc:** các node trong cùng layer → **xếp chồng theo chiều dọc**

## Layer 2 (output)

- Z⁽²⁾ = W⁽²⁾A⁽¹⁾ + b⁽²⁾ → kích thước 1×1
- A⁽²⁾ = sigmoid(Z⁽²⁾) = **ŷ**
- Tương tự logistic regression với W⁽²⁾ thay cho wᵀ

## Bốn phương trình tổng hợp

```
Z⁽¹⁾ = W⁽¹⁾A⁽⁰⁾ + b⁽¹⁾    (A⁽⁰⁾ = X)
A⁽¹⁾ = g(Z⁽¹⁾)
Z⁽²⁾ = W⁽²⁾A⁽¹⁾ + b⁽²⁾
A⁽²⁾ = g(Z⁽²⁾) = ŷ
```

## Ý chính

- Hidden layer = **4 logistic regression units** song song
- Output layer = **1 logistic regression unit**
- Bước tiếp: vector hóa qua **nhiều training examples**
