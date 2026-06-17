## Ba bước huấn luyện (giống logistic regression)

1. **Đặc tả hàm dự đoán** — kiến trúc mạng quyết định cách tính f(x) từ x và tham số W, b
2. **Hàm mất mát & hàm chi phí** — mất mát trên một mẫu; chi phí J = trung bình mất mát trên toàn tập
3. **Tối ưu hóa** — gradient descent (hoặc thuật toán nhanh hơn) để giảm J

## Hàm mất mát phân loại nhị phân

- **Binary cross-entropy**: \(-y \log f(x) - (1-y) \log(1-f(x))\)
- y = nhãn thật; f(x) = đầu ra mạng nơ-ron
- "Binary" = phân loại 2 lớp; "cross-entropy" = tên thống kê của công thức trên

## Hàm mất mát hồi quy

- **Mean squared error**: \(\frac{1}{2}(f(x) - y)^2\)

## Gradient descent trên mạng nơ-ron

- Cập nhật từng \(w_{l,j}\), \(b_l\): trừ learning rate × đạo hàm riêng của J
- TensorFlow dùng **backpropagation** để tính các đạo hàm riêng này tự động trong `fit`
- Thư viện deep learning đã trưởng thành — hầu hết dùng TensorFlow/PyTorch thay vì tự code từ đầu, nhưng vẫn nên hiểu cơ chế bên trong
