## Cách 1: forward prop thủ công
- Tạo từng layer → tính \(a_1 = \text{Layer1}(x)\) → \(a_2 = \text{Layer2}(a_1)\)

## Cách 2: Sequential model
- `model = Sequential([Dense(3, sigmoid), Dense(1, sigmoid)])`
- TensorFlow tự nối các layer tuần tự

## Huấn luyện (preview)
- `model.compile(...)` + `model.fit(X, Y)` — chi tiết tuần sau
- X: ma trận m×n features; Y: mảng nhãn

## Inference
- `model.predict(X_new)` — tự chạy forward propagation qua toàn mạng

## Convention code
- Thường viết layer trực tiếp trong `Sequential([...])` thay vì gán biến riêng
- Ví dụ chữ viết tay: 3 Dense layers (25 → 15 → 1 units, sigmoid)

## Lưu ý
- Hiểu cơ chế bên dưới thư viện quan trọng hơn chỉ gọi vài dòng code
