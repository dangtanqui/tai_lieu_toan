# Bài 2 — Đánh giá một model

## Vấn đề với nhiều đặc trưng

- Đa thức bậc 4 khớp 5 điểm huấn luyện nhưng **overfit** — khó vẽ f(x) khi có nhiều feature
- Cần cách đánh giá có hệ thống thay vì chỉ nhìn đồ thị

## Chia train / test

- Chia dữ liệu: ~70% **training set**, ~30% **test set** (hoặc 80/20)
- Ký hiệu: m_train, m_test; test: (x_test, y_test)
- Huấn luyện trên training set, đánh giá trên test set

## Regression

- Fit: minimize J(w,b) (squared error + regularization)
- **J_test(w,b)**: lỗi trung bình trên test set — **không** gồm regularization
- **J_train(w,b)**: lỗi trên training set — cũng không gồm regularization
- Model overfit: J_train thấp, J_test cao → generalization kém

## Classification

- Fit logistic regression như thường lệ
- J_test, J_train: logistic loss trung bình trên test/train
- Cách phổ biến hơn: **tỷ lệ misclassification** — phần trăm ví dụ bị phân loại sai
- Dự đoán: ŷ = 1 nếu f(x) ≥ 0.5, ngược lại 0
