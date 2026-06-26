# Bài 1 — Mạng nơ-ron sâu L lớp

## Tổng quan tuần 4

- Tuần này ghép các ý tưởng đã học (lan truyền tiến/ngược, vector hóa, khởi tạo ngẫu nhiên) để triển khai **mạng nơ-ron sâu**
- Video ngắn hơn; thời gian dành cho bài tập lập trình lớn

## Mạng nông vs mạng sâu

| Mô hình | Số lớp (không tính input) | Đặc điểm |
|---------|---------------------------|----------|
| Logistic regression | 1 | Rất **nông** (shallow) |
| 1 hidden layer | 2 | Vẫn khá nông |
| 2+ hidden layers | 3+ | **Sâu** (deep) |

- **Độ sâu** là vấn đề mức độ, không phải nhị phân
- Mạng sâu có thể học hàm mà mô hình nông **không học được**
- Số lớp ẩn nên coi là **siêu tham số** — thử logistic regression → 1 → 2 lớp ẩn, đánh giá trên tập dev

## Ký hiệu

| Ký hiệu | Ý nghĩa |
|---------|---------|
| \(L\) | Tổng số lớp (hidden + output), **không** tính input |
| \(n^{[l]}\) | Số node/đơn vị ở lớp \(l\) |
| \(a^{[l]}\) | Activation ở lớp \(l\) |
| \(W^{[l]}, b^{[l]}\) | Trọng số và bias tính \(z^{[l]}\) |
| \(a^{[0]} = x\) | Input cũng là activation lớp 0 |
| \(a^{[L]} = \hat{y}\) | Dự đoán đầu ra |

**Ví dụ:** mạng 4 lớp (3 hidden + 1 output), \(n^{[0]}=3\), \(n^{[1]}=5\), \(n^{[2]}=5\), \(n^{[3]}=3\), \(n^{[4]}=1\)

## Ghi chú

- Ký hiệu nhiều — tra **notation sheet** trên website khóa học khi quên
- Bài tiếp theo: lan truyền tiến trong mạng sâu
