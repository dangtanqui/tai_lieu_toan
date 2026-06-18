## Hệ thống đề xuất là gì?

- **Hệ thống đề xuất** gợi ý sản phẩm, phim, nhà hàng… dựa trên sở thích người dùng
- Ứng dụng rộng: Amazon, Netflix, giao đồ ăn, mạng xã hội — phần lớn doanh thu đến từ đề xuất
- Ví dụ chạy xuyên suốt: dự đoán **điểm đánh giá phim** (1–5 sao)

## Ký hiệu cơ bản

| Ký hiệu | Ý nghĩa |
|---------|---------|
| \(n_u\) | Số người dùng |
| \(n_m\) | Số item (phim, sản phẩm…) |
| \(r(i,j)\) | = 1 nếu user \(j\) đã đánh giá item \(i\); = 0 nếu chưa |
| \(y(i,j)\) | Điểm đánh giá thực tế của user \(j\) cho item \(i\) |
| `?` | User chưa xem/đánh giá item đó |

## Bài toán cốt lõi

- Ma trận đánh giá **thưa** (sparse): không phải user nào cũng đánh giá mọi item
- target: dự đoán điểm cho các ô trống → đề xuất item user có khả năng cho **5 sao**
- Giả định tạm thời (bài sau): có **feature** mô tả item (ví dụ: mức độ lãng mạn, hành động)
- Sau này sẽ học cách hoạt động **khi không có feature** sẵn
