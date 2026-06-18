## Ví dụ
- Nhận dạng chữ viết tay 0 vs 1: ảnh 8×8 (64 pixel) → 2 hidden layers (25, 15 nơ-ron) → 1 output

## Forward propagation
- Chuỗi: \(x \to a^{[1]} \to a^{[2]} \to a^{[3]}\) (trái → phải)
- \(a^{[0]} = x\); mỗi layer tính từ activation layer trước
- Output mạng: \(f(x) = a^{[3]}\) (cùng ký hiệu như logistic regression)

## Threshold
- \(a^{[3]} \geq 0.5 \Rightarrow \hat{y} = 1\), ngược lại \(\hat{y} = 0\)

## Kiến trúc
- Số nơ-ron giảm dần về output layer là lựa chọn phổ biến
- **Back propagation** (huấn luyện) — học tuần sau

## Inference
- Tải tham số mạng đã huấn luyện → chạy forward propagation trên dữ liệu mới
