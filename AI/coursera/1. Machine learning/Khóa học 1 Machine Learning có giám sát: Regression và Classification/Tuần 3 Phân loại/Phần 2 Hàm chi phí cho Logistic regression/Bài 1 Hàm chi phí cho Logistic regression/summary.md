## Squared error không phù hợp
- Dùng cost giống linear regression → đồ thị **không lồi** (non-convex)
- Nhiều **local minimum** → gradient descent không đảm bảo hội tụ global

## Loss function (1 mẫu)
- Ký hiệu: **L(f(x), y)**

| y | Loss |
|---|------|
| **1** | −log(f(x)) |
| **0** | −log(1 − f(x)) |

## Trực giác
- **y = 1:** f(x) gần 1 → loss nhỏ; f(x) gần 0 → loss **rất lớn**
- **y = 0:** f(x) gần 0 → loss nhỏ; f(x) gần 1 → loss **tiến tới vô cùng**

## Cost function
```
J = (1/m) · Σ L(f(x⁽ⁱ⁾), y⁽ⁱ⁾)
```
- Loss mới → J **lồi** (convex) → GD hội tụ **global minimum**
