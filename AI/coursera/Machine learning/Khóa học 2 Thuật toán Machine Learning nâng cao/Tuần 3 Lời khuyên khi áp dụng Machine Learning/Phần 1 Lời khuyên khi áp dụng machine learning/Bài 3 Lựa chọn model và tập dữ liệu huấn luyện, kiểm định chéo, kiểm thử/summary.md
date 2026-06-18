# Bài 3 — Lựa chọn model, cross-validation, test

## Hạn chế của J_train và J_test

- J_train thường quá lạc quan (gần 0 khi overfit)
- J_test tốt hơn để ước lượng generalization error
- Chọn model bằng J_test **sai**: chọn bậc đa thức d theo test set → J_test lạc quan

## Model selection (cách sai)

- Thử d = 1…10, chọn d có J_test thấp nhất → **không nên** dùng J_test đó báo cáo hiệu suất

## Ba tập: train / cross-validation / test

- Chia ~60% train, ~20% **cross-validation set** (cv / validation / **dev set**), ~20% test
- **J_cv**: lỗi trung bình trên cross-validation set
- Chọn model (bậc đa thức, kiến trúc neural network…) theo **J_cv thấp nhất**
- Báo cáo generalization error cuối cùng: **J_test** — chỉ dùng sau khi đã chốt model

## Quy trình đúng

1. Fit w,b trên training set
2. Chọn hyperparameter/model (d, số layer…) bằng dev set
3. Chỉ khi đã có model cuối mới đánh giá trên test set

## Neural network

- Thử nhiều kiến trúc → chọn theo J_cv (tỷ lệ misclassification nếu classification)
- J_test ước lượng công bằng vì test set chưa tham gia quyết định nào
