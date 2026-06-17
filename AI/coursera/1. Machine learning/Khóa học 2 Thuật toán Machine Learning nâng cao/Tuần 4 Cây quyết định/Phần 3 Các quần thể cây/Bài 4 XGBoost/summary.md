# Bài 4 — XGBoost

## Boosting vs bagging

- **Bagging**: mỗi cây huấn luyện trên tập random độc lập, vote
- **Boosting**: cây sau tập trung vào mẫu cây trước **dự đoán sai**
- Ý tưởng "deliberate practice": luyện phần yếu thay vì lặp toàn bộ

## Thuật toán boosted tree

1. Cây 1: bagging bình thường
2. Cây 2 trở đi: khi sampling, **tăng xác suất** chọn mẫu bị misclassify bởi ensemble trước đó
3. Lặp \(B\) lần; mỗi lần xét mẫu ensemble (cây 1…\(b-1\)) còn làm kém

## XGBoost (eXtreme Gradient Boosting)

- Implementation **boosted tree** phổ biến nhất hiện nay
- Nhanh, dễ dùng, thắng nhiều Kaggle competition
- Built-in **regularization** chống overfitting
- Default tốt cho splitting criteria và stopping criteria
- Thay vì sampling thật: gán **weight** khác nhau cho từng mẫu (hiệu quả hơn)

## Code cơ bản

```python
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

- Regression: `XGBRegressor`
