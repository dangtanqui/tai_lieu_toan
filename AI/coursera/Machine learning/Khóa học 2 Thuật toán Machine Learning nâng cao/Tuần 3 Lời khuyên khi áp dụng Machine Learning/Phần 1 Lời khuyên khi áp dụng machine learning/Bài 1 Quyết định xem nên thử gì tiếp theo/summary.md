# Bài 1 — Quyết định xem nên thử gì tiếp theo

## Vấn đề

- Đã có nhiều thuật toán (linear/logistic regression, neural network, decision trees) — cần dùng hiệu quả
- Đội kém kinh nghiệm có thể mất 6 tháng cho việc đội giỏi làm trong vài tuần
- Chìa khóa: quyết định đúng **nên thử gì** ở mỗi bước dự án ML

## Ví dụ: dự đoán giá nhà

- Model regularized linear regression vẫn sai lớn → có thể thử:
  - Thu thập thêm dữ liệu huấn luyện
  - Giảm/tăng số đặc trưng, thêm đặc trưng mới (phòng ngủ, tuổi nhà…)
  - Thêm đặc trưng đa thức (x², x₁x₂…)
  - Giảm/tăng **Lambda** (regularization)
- Mỗi hướng có thể hiệu quả hoặc vô ích tùy bài toán

## Diagnostic

- **Diagnostic** = bài kiểm tra cho biết phần nào của thuật toán hoạt động/không, hướng dẫn cải thiện
- Ví dụ: có đáng bỏ vài tháng thu thập dữ liệu không?
- Diagnostic tốn thời gian triển khai nhưng thường tiết kiệm hàng tháng làm việc vô ích
