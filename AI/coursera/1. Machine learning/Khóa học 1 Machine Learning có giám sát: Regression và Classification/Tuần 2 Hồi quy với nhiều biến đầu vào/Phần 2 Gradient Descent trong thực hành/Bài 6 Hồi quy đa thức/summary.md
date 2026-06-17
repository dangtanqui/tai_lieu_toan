## Polynomial Regression
- Vẫn là **linear regression** nhưng features = powers của x
- Fit **đường cong**, không chỉ đường thẳng

## Ví dụ features
- x, x², x³ (quadratic, cubic)
- x, √x (ít steep hơn, không quay xuống)

## Lưu ý quan trọng
- x²: 1→1M · x³: 1→1B → **bắt buộc feature scaling** khi dùng GD

## Chọn features?
- Thử nhiều model, đo performance (học Course 2)
- Hiện tại: biết có **lựa chọn** features

## Lab
- Code polynomial regression (x, x², x³)
- **Scikit-learn** — thư viện ML phổ biến (biết dùng + vẫn nên hiểu implement tay)
