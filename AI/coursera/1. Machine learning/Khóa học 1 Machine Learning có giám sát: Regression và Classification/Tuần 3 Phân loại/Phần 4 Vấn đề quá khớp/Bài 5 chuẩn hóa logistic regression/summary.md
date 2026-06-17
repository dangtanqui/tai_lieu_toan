## Regularized Logistic Regression

**Cost:**
```
J = −(1/m)·Σ[y·log(f) + (1−y)·log(1−f)]  +  (λ/2m)·Σwⱼ²
```

**Update wⱼ:** giống linear regression regularized
```
∂J/∂wⱼ có thêm hạng (λ/m)·wⱼ
```
- **f(x) = g(w·x + b)** — sigmoid, không phải tuyến tính

## Hiệu quả
- Nhiều feature / đa thức bậc cao → ranh giới **đơn giản hơn**, ít overfit
- Vẫn generalize tốt trên mẫu mới

## Lab
- Bật regularization, chọn **λ** trong plot tương tác

## Kết thúc Course 1
- Đã học: **linear regression** + **logistic regression** + **overfitting/regularization**
- Đủ để xây ứng dụng có giá trị thực tế
