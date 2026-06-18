## Quy trình Supervised Learning
1. Đưa **training set** (x + y) vào algorithm
2. Algorithm tạo ra **function f** (model)
3. f nhận x mới → output **ŷ** (prediction)

## Ký hiệu mới
| Ký hiệu | Ý nghĩa |
|---------|---------|
| **f** | Model / function (trước gọi hypothesis) |
| **ŷ** (y-hat) | Dự đoán / ước lượng của model |
| **y** | Giá trị thật (target trong training set) |
| **w, b** | Tham số quyết định đường thẳng |

**Lưu ý:** ŷ có thể khác y — giá thật của nhà chỉ biết khi bán.

## Công thức Linear Regression
```
f_w,b(x) = w·x + b    (hoặc viết gọn: f(x) = wx + b)
```
- **w, b** là số → chọn w, b → xác định đường thẳng fit data
- Đường thẳng = prediction ŷ cho mỗi x

## Tên gọi
- **Linear regression** — fit đường thẳng
- **Univariate linear regression** — chỉ **1 feature** (diện tích)
- Sau này: nhiều feature (phòng ngủ...), hàm phi tuyến (đường cong)

## Vì sao bắt đầu từ đường thẳng?
- Đơn giản, dễ làm việc → nền tảng cho model phức tạp hơn
