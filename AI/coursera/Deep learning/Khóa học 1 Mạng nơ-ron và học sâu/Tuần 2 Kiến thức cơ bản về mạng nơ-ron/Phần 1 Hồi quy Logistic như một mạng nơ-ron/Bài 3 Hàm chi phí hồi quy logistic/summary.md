## Hàm chi phí hồi quy logistic

- Mô hình: \(\hat{y}^{(i)} = \sigma(w^T x^{(i)} + b)\), với \(z^{(i)} = w^T x^{(i)} + b\)
- **(i)** trong ngoặc = mẫu huấn luyện thứ i

## Loss vs Cost

| Khái niệm | Phạm vi | Mục đích |
|---|---|---|
| **Loss** \(L(\hat{y}, y)\) | Một mẫu | Đo lỗi từng ví dụ |
| **Cost** \(J(w,b)\) | Toàn tập | Trung bình loss trên m mẫu |

## Tại sao không dùng bình phương sai?

- **Squared error** với sigmoid → bài toán **non-convex**, nhiều cực tiểu cục bộ
- Gradient descent có thể không tìm được optimum toàn cục

## Hàm loss logistic

\[
L(\hat{y}, y) = -\big[y \log \hat{y} + (1-y)\log(1-\hat{y})\big]
\]

| y | Loss đẩy ŷ về |
|---|---|
| 1 | Gần 1 (càng lớn càng tốt, tối đa 1) |
| 0 | Gần 0 |

## Hàm cost

\[
J(w,b) = -\frac{1}{m}\sum_{i=1}^{m}\big[y^{(i)}\log\hat{y}^{(i)} + (1-y^{(i)})\log(1-\hat{y}^{(i)})\big]
\]

- Huấn luyện = tìm **w, b** **tối thiểu hóa** \(J(w,b)\)
- Hồi quy logistic có thể xem như **mạng nơ-ron rất nhỏ** (1 neuron)
