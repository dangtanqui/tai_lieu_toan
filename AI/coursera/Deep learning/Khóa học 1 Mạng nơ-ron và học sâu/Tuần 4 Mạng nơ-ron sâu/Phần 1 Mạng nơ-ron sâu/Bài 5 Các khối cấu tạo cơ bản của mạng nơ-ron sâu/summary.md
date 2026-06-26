# Bài 5 — Các khối cấu tạo cơ bản của mạng nơ-ron sâu

## Một lớp = hai hàm

### Forward function

- **Input:** \(a^{[l-1]}\), \(W^{[l]}\), \(b^{[l]}\)
- **Output:** \(a^{[l]}\) và **cache** (lưu \(z^{[l]}\) cho backprop)

\[
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}, \quad a^{[l]} = g(z^{[l]})
\]

### Backward function

- **Input:** \(da^{[l]}\), cache
- **Output:** \(da^{[l-1]}\), \(dW^{[l]}\), \(db^{[l]}\)

## Luồng toàn mạng

```
Forward:  a⁰=x → a¹ → a² → … → aᴸ=ŷ  (cache z¹…zᴸ)
Backward: daᴸ → daᴸ⁻¹ → … → da¹     (tính dWˡ, dbˡ)
Update:   Wˡ := Wˡ - α·dWˡ,  bˡ := bˡ - α·dbˡ
```

## Một iteration gradient descent

1. Forward prop từ \(a^{[0]}\) → \(\hat{y}\)
2. Tính loss
3. Back prop → tất cả gradient
4. Cập nhật \(W, b\) mọi lớp

## Chi tiết cache

- Lưu \(z^{[l]}\) cho backward; bài tập có thể cache thêm \(W^{[l]}, b^{[l]}\)
- Mỗi lớp: **forward** + **backward** nối bằng cache → Bài 6 có công thức cụ thể
