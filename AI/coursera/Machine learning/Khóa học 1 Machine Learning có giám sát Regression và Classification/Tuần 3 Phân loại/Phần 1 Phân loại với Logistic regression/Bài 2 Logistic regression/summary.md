## Logistic Regression
- Thuật toán **classification** phổ biến nhất
- Fit đường cong **hình chữ S** thay vì đường thẳng

## Hàm Sigmoid (logistic function)
```
g(z) = 1 / (1 + e^(-z))
```
- Output: **0 đến 1**
- z lớn → g(z) ≈ 1 · z âm lớn → g(z) ≈ 0 · z = 0 → g(z) = 0.5

## Model (2 bước)
```
z = w·x + b
f(x) = g(z) = g(w·x + b)
```

## Cách hiểu output
- f(x) = **xác suất** y = 1
- Ví dụ: f(x) = 0.7 → 70% khối u ác tính, 30% lành tính
- Nhãn thực y vẫn chỉ là **0 hoặc 1**
