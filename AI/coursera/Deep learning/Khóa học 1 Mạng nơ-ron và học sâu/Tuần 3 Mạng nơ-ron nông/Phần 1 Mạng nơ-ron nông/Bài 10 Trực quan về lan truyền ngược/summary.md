# Bài 10 — Trực quan lan truyền ngược (tùy chọn)

## Computation graph — Logistic Regression

**Forward:** z → a → Loss L(a, y)

**Backward (chain rule):**
- da = ∂L/∂a
- **dz = da · g'(z)** ← quy tắc chuỗi
- dw = dz · x, db = dz

- Với sigmoid: dz = **a − y** (đã tích hợp sẵn trong công thức)

## Mạng nơ-ron = logistic regression × 2 lần

**Forward:** z⁽¹⁾ → a⁽¹⁾ → z⁽²⁾ → a⁽²⁾ → Loss

**Backward (từ phải sang trái):**
1. dZ⁽²⁾ = A⁽²⁾ − Y
2. dW⁽²⁾ = dZ⁽²⁾ · A⁽¹⁾ᵀ, db⁽²⁾ = dZ⁽²⁾
3. dZ⁽¹⁾ = W⁽²⁾ᵀ · dZ⁽²⁾ * g⁽¹⁾'(Z⁽¹⁾)
4. dW⁽¹⁾ = dZ⁽¹⁾ · Xᵀ, db⁽¹⁾ = dZ⁽¹⁾

## Đối chiếu với logistic regression

| Logistic Regression | Neural Network |
|---|---|
| dw = dz · x | dW⁽²⁾ = dZ⁽²⁾ · A⁽¹⁾ᵀ |
| — | dW⁽¹⁾ = dZ⁽¹⁾ · A⁽⁰⁾ᵀ (= Xᵀ) |

- A⁽¹⁾ đóng vai trò **x** cho layer output
- Thêm transpose vì W lưu dạng ma trận (w là row vector)

## Kiểm tra kích thước

- **d(foo)** luôn cùng kích thước với **foo**
- dZ⁽¹⁾: n₁×1 = W⁽²⁾ᵀ (n₁×n₂) × dZ⁽²⁾ (n₂×1) * g'(Z⁽¹⁾) (n₁×1)

## Vector hóa backprop

- Xếp dZ, dA theo cột (m examples) → công thức giữ nguyên, thêm **1/m**
- Video tùy chọn — có thể triển khai đúng mà không cần hiểu hết calculus
