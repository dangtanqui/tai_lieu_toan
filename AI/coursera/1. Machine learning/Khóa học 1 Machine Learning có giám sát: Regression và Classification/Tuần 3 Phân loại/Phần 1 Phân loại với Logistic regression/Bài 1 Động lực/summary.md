## Classification (phân loại)
- Tuần 2: **regression** — dự đoán số
- Tuần 3: **classification** — output chỉ thuộc **tập nhỏ** giá trị rời rạc

## Ví dụ
- Email spam / không spam
- Giao dịch gian lận / hợp lệ
- Khối u ác tính / lành tính

## Binary classification
- Chỉ **2 lớp** (nhị phân)
- Ký hiệu: **0 / 1** (false/true, negative/positive)
- **Negative (0):** không có đặc tính cần tìm (vd: không spam)
- **Positive (1):** có đặc tính (vd: spam)
- Negative/positive **không** = xấu/tốt

## Vì sao không dùng linear regression?
- Output có thể **bất kỳ số nào** (< 0, > 1) — không phù hợp nhãn 0/1
- Thêm 1 mẫu xa → đường thẳng **dịch chuyển** → **decision boundary** sai
- Ngưỡng 0.5 không ổn định

## Giải pháp
- **Logistic regression** — tên có "regression" nhưng dùng cho **classification**
- Output luôn trong khoảng **(0, 1)**
