## Ý tưởng Regularization
- Phạt w lớn → ép wⱼ **gần 0** → giảm ảnh hưởng feature bậc cao
- Ví dụ: thêm **1000·w₃² + 1000·w₄²** vào cost → w₃, w₄ ≈ 0 → gần như bỏ x³, x⁴

## Cost function (linear regression)
```
J = (1/2m)·Σ(f⁽ⁱ⁾ − y⁽ⁱ⁾)²  +  (λ/2m)·Σwⱼ²
     ↑ MSE gốc                    ↑ hạng regularization
```
- **λ (lambda):** tham số regularization — cần chọn như α
- Thường **không** penalize b

## Cân bằng 2 mục tiêu
- Hạng 1: fit data tốt
- Hạng 2: giữ w nhỏ → ít overfit

## Chọn λ
| λ | Kết quả |
|---|---------|
| **0** | Overfit (đường lượn sóng) |
| **Rất lớn** | Underfit (gần đường ngang, f ≈ b) |
| **Vừa phải** | Fit tốt, ít overfit |
