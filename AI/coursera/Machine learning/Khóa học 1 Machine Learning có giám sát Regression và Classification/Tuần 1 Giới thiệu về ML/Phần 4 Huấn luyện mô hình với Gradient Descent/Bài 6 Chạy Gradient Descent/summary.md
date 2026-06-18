## Demo chạy GD
- Khởi tạo w, b (vd: w=−0.1, b=900) → mỗi bước J giảm, đường f(x) fit tốt hơn
- Hội tụ → **global minimum** → đường thẳng fit data tốt nhất
- Dự đoán: nhà 1250 sq ft → ~$250,000

## Batch Gradient Descent
- Mỗi bước dùng **toàn bộ** training set (m mẫu) tính derivative
- "Batch" = cả batch data mỗi update
- (Có biến thể dùng subset — học sau)

## Hoàn thành Tuần 1
- Model ML **đầu tiên:** linear regression + gradient descent
- Lab: code GD, plot J giảm theo iteration, contour plot

## Tuần 2 preview
- Nhiều **features** (không chỉ diện tích)
- Fit **đường cong** (nonlinear)
- Tips thực tế cho ứng dụng
