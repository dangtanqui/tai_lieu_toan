## Đồ thị tính toán (Computation Graph)

- Mạng nơ-ron tổ chức tính toán theo **forward pass** (tính output) và **backward pass** (tính gradient)
- **Computation graph** giải thích vì sao chia theo hai bước này

## Ví dụ: J = 3(a + bc)

| Bước | Phép tính | Biến trung gian |
|---|---|---|
| 1 | u = b × c | u |
| 2 | v = a + u | v |
| 3 | J = 3v | J |

- Ví dụ số: a=5, b=3, c=2 → u=6, v=11, **J=33**

## Hướng tính toán

```
a, b, c  →  u  →  v  →  J     (forward: trái → phải)
a, b, c  ←  u  ←  v  ←  J     (backward: phải → trái, tính đạo hàm)
```

## Ứng dụng

- Hữu ích khi có biến output đặc biệt cần **tối ưu** (với logistic: **J** = cost function)
- Forward: tính giá trị J; Backward: tính đạo hàm ∂J/∂(tham số)
- Video tiếp: lan truyền ngược trên đồ thị
