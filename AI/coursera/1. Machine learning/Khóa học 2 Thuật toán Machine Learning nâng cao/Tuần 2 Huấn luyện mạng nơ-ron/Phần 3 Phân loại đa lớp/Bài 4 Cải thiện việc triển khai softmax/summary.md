## Vấn đề làm tròn số (floating-point)

- Cùng một giá trị, cách tính khác nhau → sai số làm tròn khác nhau
- Ví dụ: `2/10000` trực tiếp chính xác hơn `(1+1/10000) - (1-1/10000)`

## Cách triển khai tốt hơn: `from_logits=True`

- **Không** tính xác suất a rồi mới tính mất mát (2 bước riêng)
- Gộp hàm kích hoạt + mất mát vào một biểu thức → TensorFlow sắp xếp lại cho ổn định hơn
- Lớp đầu ra dùng **linear** (chỉ xuất z/logits); mất mát tự áp softmax + cross-entropy bên trong

## Logistic regression

- Tương tự: `from_logits=True` gộp sigmoid + binary cross-entropy
- Logits = giá trị z trước khi qua hàm kích hoạt

## Softmax

- e^z rất lớn hoặc rất nhỏ gây tràn số — gộp công thức giúp tránh
- Code khó đọc hơn nhưng **nên dùng** phiên bản `from_logits=True`
- Sau khi huấn luyện, cần qua sigmoid/softmax riêng nếu muốn lấy xác suất
