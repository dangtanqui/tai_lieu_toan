## Gradient Descent cho Logistic Regression
```
wⱼ := wⱼ − α · (1/m) · Σ (f⁽ⁱ⁾ − y⁽ⁱ⁾) · xⱼ⁽ⁱ⁾
b   := b   − α · (1/m) · Σ (f⁽ⁱ⁾ − y⁽ⁱ⁾)
```
- Công thức **giống** linear regression

## Khác biệt quan trọng
- **Linear regression:** f(x) = w·x + b
- **Logistic regression:** f(x) = **g(w·x + b)** (sigmoid)
- Cùng công thức update nhưng **f khác** → 2 thuật toán khác nhau

## Lưu ý thực hành
- **Simultaneous update** w và b
- Có thể **vectorize** để nhanh hơn
- **Feature scaling** vẫn giúp GD hội tụ nhanh
- Theo dõi **learning curve** như linear regression
- **Scikit-learn** có sẵn hàm train logistic regression
