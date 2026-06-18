## Lớp đầu ra — chọn theo nhãn y

- **Sigmoid**: phân loại nhị phân (y = 0 hoặc 1) → dự đoán xác suất y = 1
- **Linear**: hồi quy, y có thể âm hoặc dương (vd. biến động giá cổ phiếu)
- **ReLU**: hồi quy, y chỉ không âm (vd. giá nhà)

## Lớp ẩn

- **ReLU** là mặc định cho hầu hết lớp ẩn
- ReLU nhanh hơn sigmoid (không cần lũy thừa)
- ReLU "phẳng" chỉ một phía → gradient descent học nhanh hơn; sigmoid phẳng hai phía → học chậm
- Ngoại lệ: lớp đầu ra phân loại nhị phân vẫn dùng sigmoid

## TensorFlow

```python
Dense(25, activation='relu')   # lớp ẩn
Dense(1, activation='sigmoid') # lớp đầu ra nhị phân
```

- Các hàm khác (tanh, LeakyReLU, swish) tồn tại nhưng ReLU đủ tốt cho đa số bài toán
