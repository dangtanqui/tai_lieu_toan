## So sánh hai hướng tiếp cận

| | Collaborative Filtering | Content-Based Filtering |
|--|------------------------|------------------------|
| Cơ sở | User có đánh giá tương tự | **Feature** của user và item |
| Dữ liệu | Ma trận đánh giá thưa | Feature user + feature item |
| Điểm mạnh | Không cần feature sẵn | Dùng thông tin phong phú hơn |

## Feature của user (\(x_u^{(j)}\))

- Tuổi, giới tính (one-hot), quốc gia (one-hot ~200 giá trị)
- 1000 feature: user đã xem phim nào trong top 1000?
- Điểm trung bình theo thể loại (romance, action…) — phụ thuộc đánh giá trước, vẫn hợp lệ

## Feature của item (\(x_m^{(i)}\))

- Năm phát hành, thể loại, đánh giá phê bình
- Điểm trung bình phim, điểm trung bình theo quốc gia/demographic

## Mô hình mới

- Thay \(w^{(j)} \cdot x^{(i)} + b^{(j)}\) bằng:

\[\hat{y}^{(i,j)} = v_u^{(j)} \cdot v_m^{(i)}\]

- \(v_u\): vector sở thích user (tính từ \(x_u\)), \(v_m\): vector mô tả phim (tính từ \(x_m\))
- Hai vector phải **cùng kích thước** (ví dụ 32 số) để dot product
- \(x_u\) và \(x_m\) có thể khác kích thước — không sao
