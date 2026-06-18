# Bài 4 — Learning curve

## Trục hoành: m_train (kích thước training set)

- **J_cv**: giảm khi có thêm dữ liệu huấn luyện
- **J_train**: tăng khi m_train tăng — khó khớp hoàn hảo mọi ví dụ
- J_cv thường cao hơn J_train (fit trên train nên tốt hơn trên cv)

## High bias (underfit)

- J_train và J_cv đều cao, plateau sớm
- Gap lớn so với baseline (human-level)
- **Thêm dữ liệu không giúp nhiều** — model quá đơn giản
- Trước khi thu thập thêm data, kiểm tra bias

## High variance (overfit)

- J_train thấp, J_cv cao hơn nhiều
- Kéo dài learning curve sang phải: J_cv có thể hạ dần, tiến gần J_train
- **Thêm dữ liệu thường giúp nhiều**

## Cách vẽ

- Huấn luyện trên 100, 200, 300… ví dụ; plot J_train và J_cv
- Tốn compute nhưng hình dung mental model hữu ích
