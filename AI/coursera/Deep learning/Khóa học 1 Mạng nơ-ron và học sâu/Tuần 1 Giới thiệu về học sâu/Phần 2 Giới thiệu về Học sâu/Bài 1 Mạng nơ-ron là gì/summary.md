## Deep learning là gì?

- **Deep learning** = huấn luyện **mạng nơ-ron** (Neural Networks), đôi khi rất lớn
- Bài này trực quan hóa mạng nơ-ron qua ví dụ **dự đoán giá nhà**

## Ví dụ đơn giản: 1 neuron

- Dữ liệu: diện tích nhà → giá nhà
- Hồi quy tuyến tính: đường thẳng có thể cho giá **âm** → không hợp lý
- Giải pháp: uốn cong đường thẳng, **cắt tại 0** khi diện tích nhỏ

```
Input x (diện tích) → [Neuron] → Output y (giá)
```

- Một **neuron** thực hiện: hàm tuyến tính → **max(0, ·)** → giá ước lượng
- Hàm **ReLU** (Rectified Linear Unit): bằng 0 bên trái, đường thẳng bên phải
- "Rectify" = lấy max với 0

## Mạng nơ-ron lớn hơn

- Ghép nhiều neuron như **khối Lego** → mạng lớn hơn
- Thêm feature: số phòng ngủ, mã bưu điện, mức giàu khu vực

| Input | Hidden unit (ví dụ) |
|-------|---------------------|
| Diện tích + #phòng ngủ | Quy mô gia đình phù hợp |
| Mã bưu điện | Mức độ đi bộ được (walkability) |
| Mã bưu điện + giàu có | Chất lượng trường học |
| Family size + walkability + trường học | **Giá nhà** (output) |

## Cách triển khai thực tế

- Chỉ cần cung cấp **input x** và **output y** cho tập huấn luyện
- Các lớp giữa (hidden) — mạng **tự học**, không cần thiết kế thủ công

## Thuật ngữ quan trọng

- **Input layer**: 4 feature (diện tích, phòng ngủ, zip code, wealth)
- **Hidden units**: mỗi node nhận **cả 4 input** — không gán ý nghĩa cố định
- **Densely connected**: mọi input nối tới mọi hidden unit
- Mạng tự quyết định mỗi node đại diện gì

## Điểm mạnh

- Với đủ dữ liệu (x, y), mạng nơ-ron **rất giỏi** học hàm ánh xạ x → y chính xác
- Hữu ích nhất trong **supervised learning**: input x → output y (như dự đoán giá nhà)
