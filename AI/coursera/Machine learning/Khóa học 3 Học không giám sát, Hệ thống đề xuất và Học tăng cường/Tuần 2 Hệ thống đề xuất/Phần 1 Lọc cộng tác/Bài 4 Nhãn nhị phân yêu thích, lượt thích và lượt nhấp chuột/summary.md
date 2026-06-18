## Nhãn nhị phân thay vì điểm sao

- Nhiều ứng dụng dùng nhãn **0/1** (không thích / thích) thay vì 1–5 sao
- `?` = user chưa thấy item → chưa thể đánh giá

## Cách tạo nhãn ngầm (implicit feedback)

| Ứng dụng | y = 1 | y = 0 | y = ? |
|----------|-------|-------|-------|
| Mua hàng | Đã mua sau khi thấy | Không mua | Chưa được hiển thị |
| Mạng xã hội | Like/favorite | Không like | Chưa hiển thị |
| Hành vi | Xem ≥ 30 giây | Xem < 30 giây | Chưa hiển thị |
| Quảng cáo | Click | Không click | Chưa hiển thị quảng cáo |

## Mô hình: giống logistic regression

- Thay linear bằng **sigmoid**:

\[P(y^{(i,j)} = 1) = g\left(w^{(j)} \cdot x^{(i)} + b^{(j)}\right), \quad g(z) = \frac{1}{1+e^{-z}}\]

## Cost function — Binary Cross Entropy

- Thay MSE bằng **binary cross entropy** (giống logistic regression / phân loại neural network):

\[\text{loss} = -y \log f - (1-y) \log(1-f)\]

- Cost tổng: tổng loss trên mọi cặp \((i,j)\) có \(r(i,j)=1\), cộng regularization
- Mở rộng đáng kể phạm vi ứng dụng của collaborative filtering
