## Khởi tạo centroid

- Luôn đặt **K ≤ m** (số ví dụ huấn luyện)
- Cách phổ biến: **chọn ngẫu nhiên K ví dụ huấn luyện** làm μ₁...μ_K

## Vấn đề local optima

- Khởi tạo khác nhau → cụm khác nhau, chất lượng khác nhau
- Có thể kẹt ở **cực tiểu cục bộ** (local minimum) với J cao

## Giải pháp: chạy nhiều lần

```
For i = 1 to 100:
    Khởi tạo ngẫu nhiên K centroid
    Chạy K-means đến hội tụ
    Tính J
Chọn bộ cụm có J nhỏ nhất
```

- Thường chạy **50–1000** lần; >1000 thường tốn compute, lợi ích giảm dần

## Thực hành

- Hầu như **luôn** dùng nhiều khởi tạo ngẫu nhiên
- Chọn kết quả có **distortion J thấp nhất**
