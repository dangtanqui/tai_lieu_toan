## Vì sao thay sigmoid?

- Sigmoid giới hạn đầu ra trong (0, 1) — phù hợp xác suất, nhưng không phù hợp mọi đặc trưng ẩn
- Ví dụ "awareness": có thể là giá trị không âm bất kỳ, không chỉ 0/1

## Ba hàm kích hoạt phổ biến

| Hàm | Công thức | feature |
|-----|-----------|----------|
| **Sigmoid** | \(g(z) = \frac{1}{1+e^{-z}}\) | Đầu ra 0–1 |
| **ReLU** | \(g(z) = \max(0, z)\) | 0 khi z < 0; bằng z khi z ≥ 0 |
| **Linear** | \(g(z) = z\) | Không biến đổi; đôi khi gọi là "không dùng kích hoạt" |

- **ReLU** (rectified linear unit): lựa chọn phổ biến nhất cho lớp ẩn
- Tuần này còn gặp thêm **softmax** cho phân loại đa lớp
