## Cost Function (Hàm chi phí)
- Bước đầu tiên để implement linear regression
- Đo model **tốt đến mức nào** → tối ưu để làm tốt hơn

## Parameters w, b
- **Tham số** có thể điều chỉnh khi training
- Còn gọi: **weights** (w), **coefficients**, **bias** (b)
- **w** → độ dốc (slope) · **b** → giao trục y (y-intercept)

| w | b | Đường thẳng |
|---|---|-------------|
| 0 | 1.5 | Ngang, luôn ŷ = 1.5 |
| 0.5 | 0 | Qua gốc, slope = 0.5 |
| 0.5 | 1 | Slope 0.5, cắt trục y tại 1 |

## Mục tiêu
- Chọn w, b sao cho đường thẳng **fit data** (gần các điểm training)
- **ŷ⁽ⁱ⁾** ≈ **y⁽ⁱ⁾** cho nhiều / tất cả mẫu

## Công thức Squared Error Cost
```
Error⁽ⁱ⁾ = ŷ⁽ⁱ⁾ − y⁽ⁱ⁾ = f(x⁽ⁱ⁾) − y⁽ⁱ⁾

J(w,b) = (1/2m) · Σᵢ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)²
```
- **J(w,b)** = cost function (squared error cost)
- Chia **m** → trung bình (không phụ thuộc kích thước dataset)
- Chia thêm **2** → convention, tính toán sau gọn hơn

## Tóm tắt
- J **lớn** → model kém · J **nhỏ** → model tốt
- Cuối cùng: tìm w, b **minimize J(w,b)**
- Phổ biến nhất cho regression
