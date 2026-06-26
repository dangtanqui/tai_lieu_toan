## Câu hỏi cốt lõi

- Ý tưởng deep learning đã có **hàng thập kỷ** — tại sao **mới gần đây** bùng nổ?
- Ba lực chính: **dữ liệu**, **quy mô mạng**, **tính toán nhanh** (+ đổi mới thuật toán)

## Đồ thị hiệu suất vs lượng dữ liệu

- Trục X: lượng **dữ liệu có nhãn** (training examples có cả x và y)
- Ký hiệu: **m** = số mẫu huấn luyện (training set size)
- Trục Y: hiệu suất (độ chính xác spam, click ad, vị trí xe…)

| Thuật toán | Hành vi khi tăng dữ liệu |
|------------|--------------------------|
| **SVM, logistic regression** | Cải thiện rồi **plateau** — không tận dụng được big data |
| Mạng nơ-ron nhỏ | Tương tự, plateau sớm |
| Mạng nơ-ron **rất lớn** | Hiệu suất **tiếp tục tăng** với nhiều dữ liệu |

## Scale — động lực chính

- **Scale** = quy mô mạng (nhiều hidden units, parameters, connections) **+** quy mô dữ liệu
- Cách tin cậy để cải thiện NN: **train mạng lớn hơn** hoặc **thêm dữ liệu** (đến giới hạn)
- 10–20 năm qua: xã hội số hóa → lượng dữ liệu tăng vọt (web, app, IoT, camera điện thoại)

## Vùng dữ liệu nhỏ vs lớn

| Vùng | Đặc điểm |
|------|----------|
| **Ít dữ liệu** (trái) | Thứ hạng thuật toán không rõ; phụ thuộc **feature engineering** thủ công — SVM có thể thắng NN |
| **Big data** (phải, m lớn) | Mạng nơ-ron lớn **nhất quán vượt trội** các phương pháp khác |

## Đổi mới thuật toán

- Nhiều cải tiến nhằm làm NN **chạy nhanh hơn**
- Ví dụ: **Sigmoid** → **ReLU**
  - Sigmoid: gradient ≈ 0 ở vùng bão hòa → học chậm (vanishing gradient)
  - ReLU: gradient = 1 khi input dương → gradient descent nhanh hơn nhiều
- Thuật toán nhanh hơn → train được mạng lớn hơn trên cùng phần cứng

## Vòng lặp thử nghiệm

```
Ý tưởng → Code → Chạy thử → Đánh giá → Sửa kiến trúc → lặp lại
```

- Train **10 phút – 1 ngày**: thử nhiều ý tưởng, tìm kiến trúc tốt nhanh
- Train **1 tháng**: vòng lặp chậm → năng suất kém hơn rất nhiều
- Tính toán nhanh (CPU/GPU) → cộng đồng nghiên cứu **lặp nhanh**, liên tục đổi mới

## Triển vọng tương lai

- Ba lực vẫn mạnh: thêm dữ liệu số, phần cứng chuyên dụng (**GPU**), cộng đồng thuật toán
- Deep learning sẽ **tiếp tục cải thiện** trong nhiều năm tới
