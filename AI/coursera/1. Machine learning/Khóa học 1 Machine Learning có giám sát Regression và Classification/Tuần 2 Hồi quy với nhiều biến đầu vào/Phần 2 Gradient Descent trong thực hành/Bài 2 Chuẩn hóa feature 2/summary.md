## 3 cách Feature Scaling

**1. Chia max**
- x_scaled = x / max(x)

**2. Mean normalization**
- x_scaled = (x − μ) / (max − min)
- Center quanh 0, range ~[−1, 1]

**3. Z-score normalization**
- x_scaled = (x − μ) / σ
- μ = mean, σ = standard deviation

## Rule of thumb
- target: features trong khoảng **~[−1, 1]** (linh hoạt)
- x ∈ [−3, 3] hoặc [−0.3, 0.3] → OK
- x ∈ [−100, 100] hoặc [−0.001, 0.001] → **nên scale**
- Nhiệt độ 98.6–105°F → nên scale

## Lưu ý
- Hầu như **không hại** khi scale — khi nghi ngờ thì scale
