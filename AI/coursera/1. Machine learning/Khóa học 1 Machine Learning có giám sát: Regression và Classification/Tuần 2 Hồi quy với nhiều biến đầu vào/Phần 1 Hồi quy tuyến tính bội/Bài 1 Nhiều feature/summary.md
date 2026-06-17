## Multiple Linear Regression
- Nhiều **features** (x₁, x₂, ... xₙ) thay vì 1
- Ví dụ nhà: diện tích, phòng ngủ, số tầng, tuổi nhà

## Ký hiệu mới
| Ký hiệu | Ý nghĩa |
|---------|---------|
| **n** | Số features |
| **xⱼ** | Feature thứ j |
| **x⁽ⁱ⁾** | Vector features của mẫu thứ i |
| **xⱼ⁽ⁱ⁾** | Feature j của mẫu i |
| **w** | Vector weights (w₁...wₙ) |
| **b** | Bias (số) |

## Model
```
f(x) = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
     = w · x + b   (dot product)
```

## Ý nghĩa tham số (ví dụ)
- b = 80 → giá cơ bản $80k
- w₁ = 0.1 → mỗi sq ft +$100
- w₂ = 4 → mỗi phòng ngủ +$4k

## Tên gọi
- **Hồi quy tuyến tính bội** (≠ Hồi quy đa biến)
  - Multiple Regression: Có nhiều biến độc lập nhưng chỉ có 1 biến phụ thuộc.
  - Multivariate Regression: Có nhiều biến độc lập và có nhiều biến phụ thuộc (đồng thời dự đoán các kết quả này cùng lúc).
- Khác **không đa biến** (1 feature)
