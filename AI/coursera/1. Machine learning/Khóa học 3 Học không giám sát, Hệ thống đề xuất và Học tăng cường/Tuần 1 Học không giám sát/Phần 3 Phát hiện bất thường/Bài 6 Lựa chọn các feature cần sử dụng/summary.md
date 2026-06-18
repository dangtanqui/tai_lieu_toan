## Feature quan trọng hơn supervised

- Không có nhãn → khó tự loại feature thừa
- Cần **chọn feature cẩn thận**

## Làm feature gần Gaussian

- Vẽ histogram; nếu không bell-shaped → **biến đổi**:

| Biến đổi | Ví dụ |
|----------|-------|
| log | log(x), log(x + C) |
| Lũy thừa | x^0.4, √x, x^(1/3) |

- Thử vài giá trị C / exponent, chọn phân phối trông Gaussian nhất
- **Áp dụng cùng biến đổi** cho train, CV và test

## Error analysis

- Vấn đề: p(x) **cao** cho cả bình thường lẫn bất thường → không phát hiện được
- Xem ví dụ bị miss trên CV → thêm feature phân biệt (ví dụ: tốc độ gõ phím)

## Feature kết hợp

- Ví dụ data center: CPU cao + traffic thấp = bất thường
- Tạo feature mới: **x₅ = CPU load / network traffic**
- Hoặc (CPU load)² / traffic — thử nghiệm trên CV

## target

- p(x) **lớn** cho bình thường, **nhỏ** cho anomaly trên tập đánh giá
