## Huấn luyện mạng nơ-ron trong TensorFlow

- Tuần 2: huấn luyện mạng nơ-ron từ tập dữ liệu có nhãn (X, Y)
- Ví dụ: nhận dạng chữ viết tay 0/1 — kiến trúc 25 → 15 → 1 nơ-ron

## Ba bước huấn luyện

1. **Xây mô hình** — ghép các lớp (lớp ẩn sigmoid + lớp đầu ra)
2. **Biên dịch (compile)** — chọn hàm mất mát: **binary cross-entropy**
3. **Huấn luyện (fit)** — `model.fit(X, Y, epochs=100)`; **epoch** = số bước gradient descent

## Lưu ý

- Hiểu logic phía sau code giúp debug khi huấn luyện không như mong đợi
- TensorFlow tự tính đạo hàm và cập nhật tham số bên trong `fit`
