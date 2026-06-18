## Phát hiện bất thường là gì?

> Học từ dữ liệu **sự kiện bình thường** (không nhãn), rồi **cảnh báo** khi gặp sự kiện bất thường.

## Ví dụ: động cơ máy bay

- Feature: x₁ = nhiệt, x₂ = độ rung, ...
- Training: m động cơ **bình thường** (lỗi rất hiếm)
- Test x_test: giống dữ liệu cũ → OK; lệch xa → **cần kiểm tra**

## Kỹ thuật: density estimation

1. Học mô hình **p(x)** — vùng nào có xác suất cao/thấp
2. Với x_test: nếu **p(x_test) < ε** → **bất thường**; ngược lại → bình thường

## Ứng dụng

| Lĩnh vực | Cách dùng |
|----------|-----------|
| **Gian lận** | Mô hình hành vi user; bật kiểm tra bảo mật thêm |
| **Sản xuất** | Phát hiện linh kiện lỗi trước khi giao khách |
| **Data center** | Máy bất thường (hack, hỏng ổ cứng...) |
| **Viễn thông** | Trạm phát sóng hoạt động lạ |

- Rất phổ biến trong thực tế dù ít được nhắc đến trong học thuật
