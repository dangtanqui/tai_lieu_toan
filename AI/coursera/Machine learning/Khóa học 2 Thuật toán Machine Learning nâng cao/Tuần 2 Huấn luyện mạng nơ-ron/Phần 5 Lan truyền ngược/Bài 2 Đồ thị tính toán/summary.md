## Đồ thị tính toán (computation graph)

- Chia tính toán thành các nút nhỏ nối bằng mũi tên
- Ví dụ: a = wx + b, J = ½(a − y)² với w=2, b=8, x=−2, y=2

## Lan truyền xuôi (forward prop) — trái → phải

1. c = w×x = −4
2. a = c + b = 4
3. d = a − y = 2
4. J = ½d² = **2**

## Lan truyền ngược (backprop) — phải → trái

- Tính đạo hàm J theo từng biến trung gian và tham số
- dJ/dd = 2 → dJ/da = 2 → dJ/dc = 2, dJ/db = 2 → dJ/dw = **−4**
- Kiểm tra: w tăng 0.001 → J giảm ~4×0.001 ✓

## Quy tắc chuỗi (chain rule)

- dJ/da = (dJ/dd) × (dd/da) = 2 × 1 = 2
- dJ/dw = (dJ/dc) × (dc/dw) = 2 × (−2) = −4

## Hiệu quả

- n nút, p tham số → backprop tính mọi đạo hàm trong ~**n + p** bước
- So với thử từng tham số riêng: **n × p** bước — chênh lệch lớn với mạng thực tế
