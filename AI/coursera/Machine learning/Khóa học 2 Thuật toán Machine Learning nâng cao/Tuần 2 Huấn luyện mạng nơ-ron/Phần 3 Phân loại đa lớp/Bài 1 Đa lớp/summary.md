## Phân loại đa lớp (multiclass)

- y có thể là nhiều hơn 2 giá trị rời rạc (không phải số bất kỳ)
- Ví dụ: nhận dạng chữ số 0–9; chẩn đoán 3–5 loại bệnh; phát hiện nhiều loại lỗi trên viên thuốc

## So với phân loại nhị phân

- Nhị phân: ước lượng P(y = 1 | x)
- Đa lớp: ước lượng P(y = 1 | x), P(y = 2 | x), … cho từng lớp
- Ranh giới quyết định chia không gian đặc trưng thành nhiều vùng (không chỉ 2)

## Thuật toán

- **Softmax regression** — tổng quát hóa logistic regression cho đa lớp
- Gắn softmax vào lớp đầu ra mạng nơ-ron để huấn luyện phân loại đa lớp
