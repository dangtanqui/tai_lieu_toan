## Vấn đề chọn K

- K-means cần **K** làm đầu vào
- Nhiều bài toán: số cụm **mơ hồ** — người khác nhau có thể thấy 2, 3 hoặc 4 cụm

## Elbow method (ít dùng thực tế)

- Chạy K-means với nhiều giá trị K, vẽ J theo K
- Tìm điểm "khuỷu tay" — J giảm nhanh rồi chậm lại
- Hạn chế: nhiều đường cong **giảm mượt**, không có elbow rõ

## Cách KHÔNG nên làm

- **Minimize J** bằng cách tăng K → J luôn giảm khi K lớn hơn

## Cách nên làm: mục đích downstream

| Ví dụ | K = 3 | K = 5 |
|-------|-------|-------|
| Size áo | S, M, L | XS, S, M, L, XL |
| Nén ảnh | Chất lượng vs dung lượng | Trade-off khác |

- Chọn K dựa trên **mục đích sử dụng cụm** (fit áo, chi phí sản xuất, chất lượng ảnh nén...)
- Đánh giá nhiều K rồi quyết định theo trade-off nghiệp vụ
