## Mạng nơ-ron đa lớp

- Nhận dạng chữ số 0–9: đổi lớp đầu ra từ 1 → **10 nơ-ron** với **softmax**
- Lan truyền xuôi: lớp ẩn giữ nguyên; lớp 3 tính \(z_1 \ldots z_{10}\) rồi softmax → \(a_1 \ldots a_{10}\)

## feature softmax

- Khác sigmoid/ReLU/linear: mỗi \(a_j\) phụ thuộc **tất cả** \(z_1 \ldots z_n\), không tính độc lập từng nơ-ron
- Phải tính đồng thời toàn bộ vector z

## TensorFlow

1. Xây mô hình: lớp ẩn ReLU + lớp đầu ra `activation='softmax'` (10 units)
2. Compile: **SparseCategoricalCrossentropy** — "sparse" vì mỗi mẫu thuộc đúng 1 lớp; "categorical" vì y là danh mục
3. Fit như bình thường

- Có phiên bản triển khai tốt hơn (ổn định số học) sẽ trình bày ở bài sau
