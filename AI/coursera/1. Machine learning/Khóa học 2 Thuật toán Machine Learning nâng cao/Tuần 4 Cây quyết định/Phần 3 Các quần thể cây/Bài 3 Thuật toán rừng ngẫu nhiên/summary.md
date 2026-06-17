# Bài 3 — Random forest

## Bagged decision tree

- Lặp \(B\) lần (\(B\) thường ~64–128, ~100):
  1. **Sampling with replacement** → tập mới size \(m\)
  2. Huấn luyện decision tree trên tập đó
- Inference: **majority vote** qua \(B\) cây
- \(B\) lớn hơn không hại nhưng > ~100 → diminishing returns, chậm hơn
- Gọi là **bagging** (b = bag)

## Random forest — cải tiến

- Vấn đề bagging: nhiều cây vẫn split cùng feature gần root
- Tại mỗi node: thay vì xét cả \(n\) feature, chọn ngẫu nhiên **subset \(k < n\)** feature
- Trong subset đó: chọn feature có **information gain** cao nhất
- \(k\) thường = \(\sqrt{n}\) khi \(n\) lớn (vài chục–hàng trăm feature)

## Tại sao robust hơn?

- Bagging đã khám phá nhiều biến thể nhỏ của data
- Random feature subset → cây đa dạng hơn
- Thay đổi nhỏ thêm vào training set ít làm lệch kết quả tổng thể

## So sánh

- **Random forest** mạnh và robust hơn một decision tree đơn
- Còn thuật toán mạnh hơn nữa: **boosted decision tree** (XGBoost)
