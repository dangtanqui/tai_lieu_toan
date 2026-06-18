## Khi nào dùng gì?

| Tiêu chí | Anomaly detection | Supervised learning |
|----------|-------------------|---------------------|
| Số ví dụ dương (y=1) | **Rất ít** (0–20) | Nhiều hơn |
| Học từ | Chủ yếu y=0 → mô hình "bình thường" | Cả y=0 và y=1 |
| Anomaly mới | Phát hiện **kiểu chưa từng thấy** | Giả định tương tự train |

## Ví dụ so sánh

| Bài toán | Lựa chọn | Lý do |
|----------|----------|-------|
| **Gian lận tài chính** | Anomaly detection | Kiểu gian lận mới liên tục xuất hiện |
| **Spam email** | Supervised | Spam tương tự spam đã thấy |
| **Lỗi sản xuất mới** | Anomaly detection | Cách hỏng chưa biết trước |
| **Vết xước điện thoại** | Supervised | Lỗi đã biết, đủ ví dụ y=1 |
| **Hack / bảo mật** | Anomaly detection | Hacker tìm cách mới |
| **Dự báo thời tiết** | Supervised | Nhãn lặp lại, đủ dữ liệu |

## Tóm tắt

- **Anomaly detection**: "Khác bình thường" — kể cả kiểu mới
- **Supervised**: "Giống các ví dụ dương đã có"
