## Supervised Learning là gì?
- Học ánh xạ **x → y** (input → output)
- Cho thuật toán **ví dụ kèm đáp án đúng** (cặp x, y) → sau đó dự đoán y cho x mới
- ~**99%** giá trị kinh tế ML hiện nay đến từ supervised learning

## Ví dụ ứng dụng
| Input x | Output y |
|---------|----------|
| Email | Spam / không spam |
| Audio | Bản ghi text (speech recognition) |
| Tiếng Anh | Bản dịch (machine translation) |
| Thông tin quảng cáo + user | Click / không click (online ads) |
| Ảnh + cảm biến | Vị trí xe khác (self-driving) |
| Ảnh sản phẩm | Có lỗi / không (visual inspection) |

## Quy trình
1. **Train:** dữ liệu (x, y) có nhãn
2. **Predict:** x mới → dự đoán y

## Ví dụ chi tiết: Dự đoán giá nhà
- **x** = diện tích (sq ft) · **y** = giá ($)
- Bạn bè có nhà 750 sq ft → model dự đoán giá
- Có thể fit **đường thẳng** (~$150k) hoặc **đường cong** (~$200k)
- Khóa học sẽ dạy cách **chọn model phù hợp** (không chọn theo giá cao nhất)

## Regression
- Loại supervised learning: dự đoán **số liên tục** (giá nhà, nhiệt độ...)
- Vô số giá trị y có thể
