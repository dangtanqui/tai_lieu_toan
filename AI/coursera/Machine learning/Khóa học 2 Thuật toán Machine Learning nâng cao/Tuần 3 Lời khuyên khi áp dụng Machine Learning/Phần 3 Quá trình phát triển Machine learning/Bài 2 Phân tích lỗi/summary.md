# Bài 2 — Error analysis

## Quy trình

- Lấy ví dụ bị **misclassify** trên cross-validation set (ví dụ 100/500)
- Xem tay, nhóm theo loại lỗi phổ biến

## Ví dụ spam (100 lỗi)

| Loại lỗi | Số lượng |
|---|---|
| Pharma spam | 21 |
| Phishing / đánh cắp mật khẩu | 18 |
| Spam ảnh nhúng | … |
| Email routing bất thường | 7 |
| Lỗi chính tả cố ý | 3 |

## Kết luận từ phân tích

- Sửa lỗi chính tả chỉ giải quyết ~3% lỗi → ưu tiên thấp
- Pharma/phishing chiếm tỷ lệ lớn → đáng đầu tư

## Hành động tiếp theo

- Thu thêm data **đúng loại** (pharma spam, phishing)
- Feature mới (tên thuốc, URL đáng ngờ…)
- Một category có thể thuộc nhiều nhóm (overlap)

## Thực hành

- Tập cv lớn (5000 lỗi): lấy mẫu ngẫu nhiên ~100–200 ví dụ
- Dễ làm khi con người đánh giá được (email); khó hơn với dự đoán click quảng cáo
- Kết hợp bias/variance + error analysis để sàng lọc ý tưởng
