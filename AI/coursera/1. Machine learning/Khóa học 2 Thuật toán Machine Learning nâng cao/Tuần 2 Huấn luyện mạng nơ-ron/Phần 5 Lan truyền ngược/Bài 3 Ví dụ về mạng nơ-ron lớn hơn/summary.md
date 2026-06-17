## Mạng 2 lớp với ReLU

- Lớp ẩn: a₁ = ReLU(w₁x + b₁); lớp đầu ra: a₂ = ReLU(w₂a₁ + b₂)
- J = ½(a₂ − y)²; tham số w₁=2, b₁=0, w₂=3, b₂=1, x=1, y=5 → J = 2

## Đồ thị tính toán

- t₁ = w₁x → z₁ = t₁ + b₁ → a₁ = g(z₁)
- t₂ = w₂a₁ → z₂ = t₂ + b₂ → a₂ = g(z₂) → J = ½(a₂ − y)²

## Backprop

- Cùng cơ chế phải → trái như mạng 1 lớp
- Kết quả: dJ/dw₁ = 6, dJ/db₂ = 2, … (tính cho mọi tham số)
- Kiểm tra: w₁ tăng 0.001 → J tăng ~6×0.001 ✓

## Autodiff (tự động vi phân)

- TensorFlow/PyTorch dùng computation graph + backprop tự động
- Trước đây researcher phải tính đạo hàm thủ công bằng giấy bút
- **Autodiff** giảm yêu cầu calculus thủ công — chỉ cần hiểu trực giác

## Ứng dụng

- Các đạo hàm từ backprop → đưa vào gradient descent hoặc Adam để huấn luyện
