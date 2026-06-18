## Hàm chi phí (distortion)

```
J(c, μ) = (1/m) Σ ||x⁽ⁱ⁾ − μ_{c⁽ⁱ⁾}||²
```

- Trung bình **khoảng cách bình phương** từ mỗi điểm đến centroid cụm được gán
- Còn gọi **distortion function**

## Hai bước = hai phần tối ưu

| Bước | Cố định | Cập nhật | target |
|------|---------|----------|----------|
| Gán điểm | μ | c⁽¹⁾...c⁽ᵐ⁾ | Gán x⁽ⁱ⁾ vào centroid **gần nhất** |
| Di chuyển centroid | c | μ₁...μ_K | Đặt μ_k = **mean** các điểm trong cụm k |

- Mean của các điểm **minimize** tổng khoảng cách bình phương trong cụm

## Đảm bảo hội tụ

- Mỗi lần lặp: J **giảm hoặc giữ nguyên** — nếu J tăng → **lỗi code**
- J ngừng giảm → có thể dừng (đã hội tụ)
- J giảm rất chậm → có thể dừng sớm ("đủ tốt")

## Ứng dụng hàm chi phí

- So sánh nhiều lần chạy với **khởi tạo ngẫu nhiên** khác nhau → chọn bộ cụm có J **nhỏ nhất**
