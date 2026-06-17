## Classification là gì?
- Loại supervised learning thứ hai (sau **regression**)
- Dự đoán **category / class** — tập hữu hạn nhãn, không phải số bất kỳ

## Regression vs Classification
| | Regression | Classification |
|---|------------|----------------|
| Output | Số liên tục (vô hạn) | Nhãn rời rạc (hữu hạn) |
| Ví dụ | Giá nhà: $150k, $183k... | Benign (0) / Malignant (1) |
| Lưu ý | — | 0, 1, 2 là **nhãn**, không phải số thực (không có 0.5, 1.7) |

## Ví dụ: Phát hiện ung thư vú
- **x** = kích thước khối u · **y** = benign (0) hoặc malignant (1)
- Phát hiện sớm → cứu sống bệnh nhân
- Có thể **> 2 class:** benign, malignant type 1, type 2...

## Nhiều input (features)
- Trước: chỉ **kích thước u**
- Thêm: **tuổi** bệnh nhân → 2 input
- Thực tế dùng nhiều hơn: độ dày khối u, đồng nhất kích thước/hình dạng tế bào...
- Model tìm **đường biên** (boundary) phân tách benign / malignant

## Category không nhất thiết là số
- Mèo / chó
- Spam / không spam
- Benign / malignant

## Tóm tắt Supervised Learning
- Học x → y từ đáp án đúng
- **Regression:** dự đoán số
- **Classification:** dự đoán nhãn
