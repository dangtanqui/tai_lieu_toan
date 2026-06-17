## Decision Boundary (ranh giới quyết định)
- Ngưỡng thường dùng: **f(x) ≥ 0.5** → dự đoán y = 1

## Chuỗi suy luận
```
f(x) ≥ 0.5  ⟺  g(z) ≥ 0.5  ⟺  z ≥ 0  ⟺  w·x + b ≥ 0
```
- z = 0 là đường ranh giới — gần như trung lập giữa 2 lớp

## 2 features (x₁, x₂)
- w₁=1, w₂=1, b=−3 → ranh giới: **x₁ + x₂ = 3** (đường thẳng)
- Bên phải → y=1 · bên trái → y=0

## Ranh giới phi tuyến
- Dùng **đa thức**: z = w₁x₁² + w₂x₂² + b → ranh giới **hình tròn**
- Thêm bậc cao hơn → ellipse, đường cong phức tạp
- Chỉ x₁, x₂, x₃... (bậc 1) → ranh giới **luôn thẳng**

## Dự đoán nhãn
- f(x) = 0.3, 0.7, 0.65... → cần quy tắc chuyển thành **0 hoặc 1** (ngưỡng 0.5)
