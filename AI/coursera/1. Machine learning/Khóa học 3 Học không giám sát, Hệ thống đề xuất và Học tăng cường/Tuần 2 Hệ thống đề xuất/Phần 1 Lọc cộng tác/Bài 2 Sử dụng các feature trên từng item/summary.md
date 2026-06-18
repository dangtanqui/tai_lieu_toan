## Mô hình khi có feature của item

- Mỗi phim có vector feature \(x^{(i)}\), ví dụ: \(x_1\) = mức lãng mạn, \(x_2\) = mức hành động
- \(n\) = số feature; dự đoán điểm user \(j\) cho phim \(i\):

\[\hat{y}^{(i,j)} = w^{(j)} \cdot x^{(i)} + b^{(j)}\]

- Giống **linear regression**, nhưng mỗi user có bộ tham số \(w^{(j)}, b^{(j)}\) riêng

## Ví dụ trực quan

- Alice thích phim lãng mạn → \(w^{(1)} = [5, 0]\), \(b^{(1)} = 0\)
- Phim "Cute Puppies" có \(x^{(3)} = [0.99, 0]\) → dự đoán \(\approx 4.95\) sao — hợp lý

## Hàm cost cho một user

- \(m^{(j)}\) = số phim user \(j\) đã đánh giá
- Chỉ tính lỗi trên các cặp \((i,j)\) có \(r(i,j) = 1\):

\[J(w^{(j)}, b^{(j)}) = \frac{1}{2m^{(j)}} \sum_{i: r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2 + \frac{\lambda}{2m^{(j)}} \sum_k (w_k^{(j)})^2\]

## Học cho tất cả user

- Cost tổng = tổng cost của \(n_u\) user → tối ưu bằng **gradient descent**
- Có thể bỏ hệ số \(1/m^{(j)}\) vì \(m^{(j)}\) chỉ là hằng số
- **Hạn chế**: cần feature mô tả item — nếu không có thì sao? → bài tiếp theo
