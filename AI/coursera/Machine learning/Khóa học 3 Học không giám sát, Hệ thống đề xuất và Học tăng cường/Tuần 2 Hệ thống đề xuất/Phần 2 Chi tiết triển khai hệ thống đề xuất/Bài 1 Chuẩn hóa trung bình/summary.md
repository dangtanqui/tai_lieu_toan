## Vấn đề với user mới

- User chưa đánh giá gì (ví dụ Eve) → regularization đẩy \(w^{(j)} = [0,0], b^{(j)} = 0\)
- Dự đoán mọi phim = **0 sao** — không hữu ích

## Mean Normalization

1. Tính **trung bình điểm** mỗi phim \(\mu_i\) (chỉ trên user đã đánh giá)
2. Thay \(y^{(i,j)}\) bằng \(y^{(i,j)} - \mu_i\)
3. Học \(w, b, x\) như bình thường trên dữ liệu đã chuẩn hóa
4. Khi dự đoán: **cộng lại** \(\mu_i\):

\[\hat{y}^{(i,j)} = w^{(j)} \cdot x^{(i)} + b^{(j)} + \mu_i\]

## Kết quả

- User mới → dự đoán ban đầu ≈ **điểm trung bình** của phim (hợp lý hơn 0 sao)
- Tối ưu hóa cũng **hội tụ nhanh hơn**

## Chuẩn hóa hàng vs cột

| Cách | Mục đích |
|------|----------|
| **Chuẩn hóa hàng** (theo phim) | User mới, ít đánh giá — **nên dùng** |
| Chuẩn hóa cột (theo user) | Phim mới chưa ai đánh giá — ít quan trọng hơn |

- Trong lab thực hành: chuẩn hóa hàng là đủ
