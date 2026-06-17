## Softmax regression

- Tổng quát hóa logistic regression khi y có n giá trị (1, 2, …, n)

## Cách tính (ví dụ 4 lớp)

- Tính \(z_j = w_j \cdot x + b_j\) cho từng lớp j
- \(a_j = \frac{e^{z_j}}{\sum_{k=1}^{n} e^{z_k}}\) — xác suất lớp j
- Tất cả \(a_j\) cộng lại = 1

## Liên hệ logistic regression

- Logistic regression có thể xem như tính \(a_1 = P(y=1)\) và \(a_2 = P(y=0) = 1 - a_1\)
- Softmax với n = 2 tương đương logistic regression

## Hàm mất mát

- Nếu nhãn thật y = j: mất mát = \(-\log a_j\)
- Khuyến khích mô hình gán xác suất cao cho đúng lớp
- Chi phí = trung bình mất mát trên toàn tập huấn luyện
