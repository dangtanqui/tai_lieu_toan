# Bài 3 — Thêm dữ liệu

## Thu data có mục tiêu

- Không nhất thiết thu "mọi thứ" — tốn chậm, đắt
- Error analysis chỉ ra subset yếu → thu thêm **đúng loại đó** (pharma spam, phishing…)
- Dữ liệu chưa gán nhãn: nhờ labeler lọc nhanh ví dụ liên quan

## Data augmentation

- Biến đổi ví dụ (X, y) có sẵn → ví dụ mới cùng nhãn y
- **Ảnh/OCR**: xoay, phóng/thu, đổi contrast, mirror (một số chữ), random warping
- **Speech**: cộng nhiễu nền (đám đông, xe), giả lập sóng điện thoại kém
- Distortion phải **đại diện test set** — nhiễu pixel ngẫu nhiên vô nghĩa thường vô ích

## Data synthesis

- Tạo ví dụ hoàn toàn mới (không sửa từ ví dụ cũ)
- **Photo OCR**: render text bằng nhiều font/màu trên máy tính → ảnh chữ synthetic
- Tốn effort viết code nhưng có thể tạo hàng loạt data
- Phổ biến nhất trong computer vision

## Data-centric vs model-centric

- Vài thập kỷ qua: giữ data cố định, cải thiện thuật toán
- Thuật toán hiện đại đã khá tốt → đôi khi **engineering data** hiệu quả hơn
- Thu thập có chọn lọc, augmentation, synthesis đều là data-centric approach
