## PCA là gì?

- **Principal Component Analysis** — thuật toán **học không giám sát**
- Giảm dữ liệu nhiều chiều (10, 50, 1000 feature) → **2–3 feature** để trực quan hóa
- Ứng dụng chính: **visualization** — hiểu dữ liệu, phát hiện bất thường

## Ví dụ trực quan (ô tô)

| Feature | Biến thiên | PCA chọn |
|---------|------------|----------|
| Chiều dài \(x_1\) | Lớn | Giữ thông tin chính |
| Chiều rộng \(x_2\) | Nhỏ (≈ 1.8m) | Bỏ qua phần lớn |
| Chiều cao + chiều dài | Cả hai đều quan trọng | Trục \(z\) kết hợp → "kích thước xe" |

## Trục mới \(z\)

- Không phải trục 3D vật lý — là **tổ hợp tuyến tính** của \(x_1, x_2\)
- Một số \(z\) thay hai số → vẫn giữ thông tin hữu ích

## Ví dụ thực tế

- Dữ liệu 3D nằm trên "bánh kếp" mỏng → PCA → \(z_1, z_2\) (2D)
- 50 feature quốc gia (GDP, HDI, tuổi thọ…) → \(z_1\) ≈ quy mô kinh tế, \(z_2\) ≈ GDP bình quân đầu người
- Plot 2D giúp so sánh Mỹ, Singapore, các nước khác

## Khi nào dùng

- Nhận dataset mới → **visualize trước** để hiểu cấu trúc dữ liệu
