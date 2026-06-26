## Đạo hàm trên Computation Graph

- Ví dụ J = 3(a + bc), với a=5, b=3, c=2 → v=11, J=33

## Backprop từng bước

| Biến | Công thức | Giá trị |
|---|---|---|
| dJ/dv | J = 3v | 3 |
| dJ/da | dv/da = 1 | 3 |
| dJ/du | dv/du = 1 | 3 |
| dJ/db | dJ/du × du/db, u=bc | 6 |
| dJ/dc | dJ/du × du/dc | 9 |

## Chain rule (quy tắc chuỗi)

\[
\frac{\partial J}{\partial a} = \frac{\partial J}{\partial v} \cdot \frac{\partial v}{\partial a}
\]

- Thay đổi **a** → ảnh hưởng **v** → ảnh hưởng **J**
- Nhân các đạo hàm local dọc theo đồ thị

## Ký hiệu trong code

- **dvar** = đạo hàm của biến output cuối (J) theo biến trung gian
- Ví dụ: `dv` = dJ/dv = 3; `db` = dJ/db = 6

## Nguyên tắc hiệu quả

- Tính **phải → trái** (ngược forward pass)
- Dùng kết quả đạo hàm node gần output để tính node xa hơn
- Áp dụng lại cho logistic regression ở video sau
