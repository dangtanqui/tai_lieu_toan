# Bài 1 — Chẩn đoán bias và variance

## Khái niệm

- **High bias** (underfit): model quá đơn giản — đường thẳng trên dữ liệu cong
- **High variance** (overfit): model quá phức tạp — đa thức bậc cao khớp train nhưng generalize kém
- **Just right**: đa thức bậc 2 trong ví dụ 1D

## Chẩn đoán bằng J_train và J_cv

| Tình huống | J_train | J_cv |
|---|---|---|
| High bias | Cao | Cao (gần J_train) |
| High variance | Thấp | Cao hơn J_train nhiều |
| Just right | Thấp | Thấp (gần J_train) |

## Đồ thị theo bậc đa thức d

- J_train giảm khi d tăng (khớp train tốt hơn)
- J_cv: cao ở d nhỏ (underfit) và d lớn (overfit), thấp nhất ở giữa

## High bias + high variance cùng lúc

- Hiếm với linear regression 1D; có thể xảy ra với neural network
- Dấu hiệu: J_train cao **và** J_cv cao hơn J_train rất nhiều
- Thường chỉ gặp một trong hai

## Tóm tắt

- **Bias**: không làm tốt trên training set
- **Variance**: làm tốt train nhưng tệ hơn nhiều trên cross-validation set
