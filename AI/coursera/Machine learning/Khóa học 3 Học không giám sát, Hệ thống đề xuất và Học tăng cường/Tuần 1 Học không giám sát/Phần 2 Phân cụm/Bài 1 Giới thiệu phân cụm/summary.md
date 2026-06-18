## Phân cụm là gì?

> Thuật toán **học không giám sát** tự tìm các điểm dữ liệu **tương tự** và gom thành **cụm** (cluster).

## So với học có giám sát

| | Có giám sát | Phân cụm |
|---|-------------|----------|
| Dữ liệu | x + nhãn y | Chỉ có x |
| target | Dự đoán y đúng | Tìm cấu trúc thú vị trong dữ liệu |
| Ví dụ | Logistic regression, mạng nơ-ron | K-means |

- Không có "đáp án đúng" y → thuật toán tự khám phá nhóm điểm giống nhau

## Ứng dụng

- **Tin tức** — gom bài viết tương tự
- **Phân khúc thị trường** — nhóm người học theo nhu cầu
- **Phân tích DNA** — nhóm cá nhân có biểu hiện di truyền tương tự
- **Thiên văn** — nhóm thiên thể thành thiên hà / cấu trúc không gian

## Bước tiếp theo

- Thuật toán phân cụm phổ biến nhất: **K-means**
