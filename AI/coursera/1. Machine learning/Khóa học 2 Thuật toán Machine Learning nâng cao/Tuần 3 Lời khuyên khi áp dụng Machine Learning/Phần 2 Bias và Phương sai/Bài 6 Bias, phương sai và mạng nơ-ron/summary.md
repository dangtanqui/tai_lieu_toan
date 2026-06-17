# Bài 6 — Bias, variance và neural network

## Bias-variance tradeoff (trước deep learning)

- Model đơn giản → high bias; phức tạp → high variance
- Phải cân bằng bậc đa thức / Lambda

## Neural network thay đổi cuộc chơi

- Mạng lớn + dataset vừa/phải = **low bias machine** — gần như luôn fit được training set
- Có thể giảm bias và variance **tuần tự** thay vì tradeoff cứng

## Recipe huấn luyện NN

1. Train → đo J_train so với baseline → cao = **high bias** → tăng kích thước mạng (thêm layer/units)
2. J_train tốt → đo J_cv → J_cv >> J_train = **high variance** → thu thêm data
3. Lặp đến khi J_cv ổn

## Mạng lớn hơn

- Mạng lớn + regularization phù hợp thường ≥ mạng nhỏ
- Hầu như không hại performance; chỉ tốn compute (GPU)
- Giới hạn: quy mô mạng, lượng data có thể thu thập

## Regularization cho NN

- Cost + (λ/2m) Σ w² (tổng mọi trọng số; thường không regularize b)
- TensorFlow: `kernel_regularizer=l2(0.01)` trên từng layer

## Thực tế

- Với mạng đủ lớn thường **chiến variance** hơn bias
- Deep learning + big data giải phóng khỏi tradeoff cổ điển (có điều kiện)
