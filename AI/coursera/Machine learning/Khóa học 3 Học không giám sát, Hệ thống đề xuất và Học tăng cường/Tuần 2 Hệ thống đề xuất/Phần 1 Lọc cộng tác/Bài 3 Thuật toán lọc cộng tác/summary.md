## Ý tưởng: học feature từ dữ liệu

- Không có feature sẵn → **học** \(x^{(i)}\) cho từng phim từ đánh giá của nhiều user
- Chỉ khả thi vì có **nhiều user** đánh giá cùng item (khác với linear regression 1 user)

## Học feature cho một phim

- Cho trước \(w^{(j)}, b^{(j)}\) của mọi user, tối ưu \(x^{(i)}\):

\[J(x^{(i)}) = \frac{1}{2} \sum_{j: r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2 + \frac{\lambda}{2} \sum_k (x_k^{(i)})^2\]

## Cost function tổng hợp — Collaborative Filtering

- Gộp cost học \(w, b\) và cost học \(x\) thành một:

\[J = \sum_{(i,j): r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2 + \text{regularization}\]

- Tối ưu đồng thời **\(w, b, x\)** bằng gradient descent
- **Collaborative filtering**: nhiều user cùng đánh giá → suy ra feature phim → dự đoán cho user khác

## Tóm tắt

| Tham số | Ý nghĩa |
|---------|---------|
| \(w^{(j)}, b^{(j)}\) | Sở thích user \(j\) |
| \(x^{(i)}\) | Đặc trưng (ẩn) của phim \(i\) |
| Dự đoán | \(w^{(j)} \cdot x^{(i)} + b^{(j)}\) |
