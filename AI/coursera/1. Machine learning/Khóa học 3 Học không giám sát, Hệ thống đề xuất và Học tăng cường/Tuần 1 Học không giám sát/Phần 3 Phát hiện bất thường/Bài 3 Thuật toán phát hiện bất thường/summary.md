## Mô hình p(x) — nhiều feature

Giả định các feature **độc lập** (thường vẫn hoạt động tốt):

```
p(x) = p(x₁) · p(x₂) · ... · p(xₙ) = Π p(xⱼ; μⱼ, σⱼ²)
```

## Thuật toán

1. Chọn feature xⱼ có khả năng phân biệt bất thường
2. Fit μⱼ, σⱼ² trên tập huấn luyện (chỉ ví dụ bình thường)
3. Với x mới: tính p(x); nếu **p(x) < ε** → bất thường

## Công thức từng feature

```
p(xⱼ) = (1 / (√(2π) · σⱼ)) · exp(−(xⱼ−μⱼ)² / (2σⱼ²))
```

- Chỉ cần **một** feature cực đoan → p(xⱼ) rất nhỏ → p(x) nhỏ

## Ví dụ số

| Điểm | p(x) | ε = 0.02 | Kết quả |
|------|------|----------|---------|
| x_test1 (gần tâm) | ≈ 0.4 | > ε | Bình thường |
| x_test2 (xa tập train) | ≈ 0.0021 | < ε | Bất thường |

- Bước tiếp: chọn **ε** và đánh giá hệ thống
