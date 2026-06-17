# Bài 2 — Trade-off precision và recall

## Threshold mặc định

- Logistic regression: dự đoán 1 nếu f(x) ≥ **0.5**

## Tăng threshold (vd. 0.7, 0.9)

- Chỉ dự đoán positive khi rất tự tin
- **Precision tăng**, **recall giảm**
- Phù hợp khi false positive tốn kém (điều trị xâm lấn không cần thiết)

## Giảm threshold (vd. 0.3)

- "Nghi ngờ thì dự đoán positive"
- **Precision giảm**, **recall tăng**
- Phù hợp khi bỏ sót bệnh nhân (FN) nguy hiểm hơn

## Precision-recall curve

- Threshold cao → precision cao, recall thấp
- Threshold thấp → precision thấp, recall cao
- Plot curve để chọn điểm cân bằng chi phí FP vs FN

## Chọn threshold

- Không chọn bằng cross-validation — **quyết định thủ công** theo ngữ cảnh ứng dụng

## F1 score

- Trung bình (P+R)/2 **không tốt** — thuật toán recall=100%, precision thấp vẫn có average cao
- **F1 = 2PR / (P + R)** = harmonic mean của P và R
- Nhấn mạnh giá trị thấp hơn — P hoặc R ≈ 0 → F1 rất thấp
- Dùng khi cần **một số** để so sánh nhiều thuật toán tự động
