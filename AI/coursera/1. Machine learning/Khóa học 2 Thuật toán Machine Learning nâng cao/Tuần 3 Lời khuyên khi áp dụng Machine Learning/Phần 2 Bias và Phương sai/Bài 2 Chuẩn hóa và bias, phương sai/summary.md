# Bài 2 — Regularization và bias, variance

## Lambda lớn (ví dụ 10.000)

- Ép w ≈ 0 → f(x) ≈ hằng số b
- **High bias**, underfit; J_train và J_cv đều cao

## Lambda nhỏ / bằng 0

- Đa thức bậc 4 không regularization → overfit
- J_train thấp, J_cv cao → **high variance**

## Lambda trung bình

- Model vừa phải; J_train và J_cv đều thấp

## Chọn Lambda bằng cross-validation

- Thử nhiều giá trị Lambda (0, 0.01, 0.02… nhân đôi dần)
- Fit từng lần → tính J_cv → chọn Lambda có J_cv thấp nhất
- Báo cáo generalization: J_test với Lambda đã chọn

## Đồ thị J_train, J_cv theo Lambda

- Lambda nhỏ (trái): high variance — J_train thấp, J_cv cao
- Lambda lớn (phải): high bias — cả hai cao
- J_train tăng khi Lambda tăng (regularization mạnh hơn → fit train kém hơn)
- J_cv có điểm tối ưu ở giữa
- Tương tự mirror của đồ thị theo bậc đa thức d
