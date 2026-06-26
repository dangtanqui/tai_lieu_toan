## Gradient Descent

- Mục tiêu: tìm **w, b** sao cho **J(w,b)** nhỏ nhất
- Cost logistic là hàm **lồi (convex)** → một cực tiểu toàn cục (hình “cái bát”)

## Thuật toán

1. Khởi tạo **w, b** (thường = 0; random cũng được với logistic)
2. Lặp: bước theo hướng **dốc xuống nhanh nhất**
3. Hội tụ gần minimum

## Công thức cập nhật

\[
w := w - \alpha \frac{\partial J}{\partial w}, \quad b := b - \alpha \frac{\partial J}{\partial b}
\]

- **α** = **learning rate** — điều khiển kích thước bước
- Trong code: biến **dw**, **db** = lượng cập nhật (đạo hàm)

## Trực giác đạo hàm

| Vị trí w | Độ dốc | Hướng cập nhật |
|---|---|---|
| Bên phải minimum | Dương | Giảm w |
| Bên trái minimum | Âm | Tăng w |

## Ký hiệu vi phân

- Nhiều biến → ký hiệu **∂** (partial derivative); một biến → **d**
- Thực tế cùng ý nghĩa: **độ dốc** của hàm theo từng tham số
