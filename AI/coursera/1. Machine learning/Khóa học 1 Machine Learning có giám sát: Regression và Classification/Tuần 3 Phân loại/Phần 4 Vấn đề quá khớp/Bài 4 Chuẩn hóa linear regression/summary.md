## Gradient Descent + Regularization (linear regression)

**Update wⱼ:**
```
wⱼ := wⱼ · (1 − αλ/m)  −  α · (1/m) · Σ(f⁽ⁱ⁾ − y⁽ⁱ⁾) · xⱼ⁽ⁱ⁾
         ↑ thu nhỏ w          ↑ update GD thường
```

**Update b:** giữ nguyên như trước (không regularize b)

## Trực giác
- Mỗi iteration: wⱼ nhân số **hơi < 1** (vd: 0.9998) rồi mới GD
- → w **co nhỏ dần** → regularization hoạt động

## Derivative ∂J/∂wⱼ
- Thêm hạng: **+ (λ/m)·wⱼ** so với bản không regularize

## Kết quả
- Nhiều feature + ít mẫu → regularization giúp linear regression **ổn định hơn**
