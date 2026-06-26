# Bài 11 — Khởi tạo ngẫu nhiên

## Vấn đề: khởi tạo W = 0

| | Logistic Regression | Neural Network |
|---|---|---|
| W = 0 | **OK** | **Không được** |

## Tại sao W = 0 gây lỗi?

- W⁽¹⁾ = 0, b⁽¹⁾ = 0 → mọi hidden unit tính **cùng hàm**
- a⁽¹⁾₁ = a⁽¹⁾₂ (đối xứng hoàn toàn)
- Backprop: dz⁽¹⁾₁ = dz⁽¹⁾₂ → dW mọi hàng **giống nhau**
- Sau mỗi cập nhật: hidden units **vẫn đối xứng** (chứng minh quy nạp)
- Kết quả: **n hidden units = 1 hidden unit** — lãng phí

## Giải pháp: Random Initialization

```python
W1 = np.random.randn(2, 2) * 0.01   # Gaussian, nhân số nhỏ
b1 = np.zeros((2, 1))                # b = 0 là OK
W2 = np.random.randn(1, 2) * 0.01
b2 = np.zeros((1, 1))
```

- **W ngẫu nhiên** → phá vỡ đối xứng (symmetry breaking)
- **b = 0** không gây vấn đề đối xứng

## Tại sao nhân 0.01?

- W quá lớn → z quá lớn/nhỏ → sigmoid/tanh **bão hòa** (gradient ≈ 0)
- Gradient descent **rất chậm** ở vùng bão hòa
- 0.01 là giá trị hợp lý cho mạng nông; mạng sâu cần hằng số khác (tuần 4)

## Tóm tắt tuần 3

- Biết cấu trúc mạng 1 hidden layer
- Forward prop + backprop + gradient descent
- Chọn activation function và khởi tạo ngẫu nhiên
- Sẵn sàng cho quiz và programming assignment
