## Tìm item tương tự

- Sau khi học, mỗi item có vector feature \(x^{(i)}\)
- Feature học được **khó diễn giải** trực tiếp, nhưng tập hợp chúng mô tả item tốt
- Độ tương tự giữa item \(k\) và item \(i\):

\[\text{distance} = \sum_{l=1}^{n} \left(x_l^{(k)} - x_l^{(i)}\right)^2\]

- Chọn top 5–10 item có khoảng cách **nhỏ nhất** → "phim tương tự"

## Hạn chế của Collaborative Filtering

### Cold Start Problem
- **Item mới**: ít user đánh giá → khó xếp hạng chính xác
- **User mới**: ít đánh giá → đề xuất kém (mean normalization giúp một phần)

### Không dùng được side information
- Không tận dụng: thể loại, diễn viên, ngân sách phim
- Không tận dụng: tuổi, giới tính, vị trí, trình duyệt web của user
- Ví dụ: user Chrome vs Firefox vs Safari có hành vi rất khác nhau

## Hướng tiếp theo

- **Content-based filtering** giải quyết nhiều hạn chế trên — kỹ thuật state-of-the-art trong thương mại
