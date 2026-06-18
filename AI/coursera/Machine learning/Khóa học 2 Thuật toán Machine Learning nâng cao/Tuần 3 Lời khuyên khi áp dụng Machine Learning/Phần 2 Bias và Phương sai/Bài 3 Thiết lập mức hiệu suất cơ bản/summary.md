# Bài 3 — Baseline level of performance

## Ví dụ: speech recognition

- J_train = 10.8% error, J_cv = 14.8% error
- Nhìn số tuyệt đối có vẻ high bias — nhưng chưa đủ

## Human-level performance

- Người cũng sai ~10.6% (audio nhiễu, không nghe được)
- J_train chỉ kém human 0.2% → thực ra fit train khá tốt
- J_cv − J_train = 4% → vấn đề chính là **variance**

## Baseline level of performance

- Mức lỗi hợp lý có thể đạt được
- Cách thiết lập:
  - **Human-level performance** (audio, ảnh, text)
  - Thuật toán đối thủ / triển khai cũ
  - Ước lượng từ kinh nghiệm
- Đôi khi baseline > 0% (dữ liệu nhiễu không thể hoàn hảo)

## Cách đọc số liệu

- **Gap 1**: J_train − baseline → lớn = **high bias**
- **Gap 2**: J_cv − J_train → lớn = **high variance**
- Có thể đồng thời high bias **và** high variance (cả hai gap lớn)

## Ý nghĩa

- Không hỏi "J_train có cao không?" mà hỏi "J_train cao **so với baseline** không?"
