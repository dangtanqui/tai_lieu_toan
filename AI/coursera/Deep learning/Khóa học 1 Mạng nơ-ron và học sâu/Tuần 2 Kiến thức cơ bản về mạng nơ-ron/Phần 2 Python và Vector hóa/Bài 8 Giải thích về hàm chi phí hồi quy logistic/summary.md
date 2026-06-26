## Giải thích hàm chi phí logistic (Optional)

- Video tùy chọn: **chứng minh** vì sao dùng loss/cost đã giới thiệu

## Mô hình xác suất

- \(\hat{y} = P(y=1 \mid x)\)
- \(P(y=1 \mid x) = \hat{y}\); \(P(y=0 \mid x) = 1 - \hat{y}\)

## Gộp một công thức

\[
P(y \mid x) = \hat{y}^{\,y} \cdot (1-\hat{y})^{\,1-y}
\]

| y | Kết quả |
|---|---|
| 1 | \(\hat{y}\) |
| 0 | \(1 - \hat{y}\) |

## Log-likelihood

\[
\log P(y \mid x) = y\log\hat{y} + (1-y)\log(1-\hat{y})
\]

- Đây là **âm loss** đã định nghĩa: \(L = -\log P(y \mid x)\)

## Maximum Likelihood Estimation (MLE)

- Giả sử mẫu **IID** → xác suất toàn tập = tích \(\prod_i P(y^{(i)} \mid x^{(i)})\)
- **Tối đa hóa log-likelihood** ≡ **tối thiểu hóa** \(\sum_i L(\hat{y}^{(i)}, y^{(i)})\)
- Thêm **1/m** chỉ để scale — không đổi optimum

## Kết luận

> Minimize \(J(w,b)\) = **MLE** cho mô hình logistic regression (giả định IID)
