## Tiền xử lý

- Chuẩn hóa feature về **mean = 0**
- Nếu scale khác nhau nhiều (diện tích nhà vs số phòng ngủ) → **feature scaling** trước PCA

## Principal Component (thành phần chính)

- Chọn trục \(z\) sao khi **chiếu** (project) dữ liệu lên \(z\), các điểm **phân tán nhiều nhất** (variance lớn nhất)
- Chiếu = đường vuông góc 90° từ điểm xuống trục
- Trục kém: điểm chiếu bị **dồn lại** → mất thông tin

## Công thức chiếu

- Vector đơn vị theo hướng \(z\): ví dụ \([0.71, 0.71]\)
- Điểm \((2, 3)\) chiếu lên \(z\): \((2,3) \cdot (0.71, 0.71) = 3.55\)

## Nhiều thành phần

- \(z_2\) luôn **vuông góc** (\(\perp\)) với \(z_1\); \(z_3\) vuông góc với \(z_1, z_2\)
- 50 feature → 3 principal components → plot 3D

## PCA vs Linear Regression

| | Linear Regression | PCA |
|--|-------------------|-----|
| Loại | Supervised (có \(y\)) | Unsupervised |
| target | Min khoảng cách **theo trục y** | Max variance khi chiếu |
| Feature | \(x\) đặc biệt, \(y\) riêng | Mọi feature **bình đẳng** |

## Reconstruction (tái tạo)

- Từ \(z = 3.55\): \(x_{approx} = z \times [0.71, 0.71] = [2.52, 2.52]\) ≈ \((2, 3)\)
- Mất thông tin nhưng xấp xỉ hợp lý
