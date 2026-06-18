# Bài 1 — Sử dụng nhiều cây quyết định

## Hạn chế một cây đơn

- **Decision tree** đơn nhạy cảm với thay đổi nhỏ trong dữ liệu
- Đổi 1 mẫu huấn luyện → feature split tại root đổi (ear shape → whiskers) → cả cây khác hoàn toàn
- Thuật toán **không robust**

## Tree ensemble

- Huấn luyện **nhiều decision tree** → gọi là **tree ensemble**
- Inference: mỗi cây dự đoán → **majority vote**
- Ví dụ 3 cây: cat, not cat, cat → kết quả cuối: **cat**
- Một cây sai ít ảnh hưởng vì chỉ 1 phiếu trong nhiều phiếu

## Lợi ích

- Ít phụ thuộc vào bất kỳ cây đơn lẻ nào
- Dự đoán chính xác và ổn định hơn
- Cần **sampling with replacement** để tạo nhiều tập huấn luyện khác nhau cho từng cây
