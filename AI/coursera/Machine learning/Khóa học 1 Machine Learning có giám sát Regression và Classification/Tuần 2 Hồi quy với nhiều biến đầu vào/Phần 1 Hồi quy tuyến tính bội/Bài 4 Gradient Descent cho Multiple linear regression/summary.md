## GD cho Multiple Linear Regression
```
f(x) = w · x + b
J(w, b) — cost function

Update mỗi wⱼ:
wⱼ := wⱼ − α · ∂J/∂wⱼ
b := b − α · ∂J/∂b
```
- ∂J/∂wⱼ giống univariate nhưng dùng **xⱼ⁽ⁱ⁾** thay x⁽ⁱ⁾
- j = 1...n, simultaneous update

## Normal Equation (side note)
- Giải w, b **trực tiếp** bằng linear algebra — không cần iterate
- **Nhược điểm:** chỉ linear regression; chậm khi n lớn; không generalize
- Một số thư viện dùng backend — biết tên thôi, **dùng GD khi tự implement**
