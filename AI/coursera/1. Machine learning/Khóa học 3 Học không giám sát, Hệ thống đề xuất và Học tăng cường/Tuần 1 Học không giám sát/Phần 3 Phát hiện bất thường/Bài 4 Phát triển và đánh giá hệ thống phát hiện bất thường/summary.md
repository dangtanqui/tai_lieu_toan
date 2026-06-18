## Real-number evaluation

- Cần **số đo** để quyết định thay đổi feature, ε, ... có cải thiện hay không

## Chia dữ liệu (ví dụ 10.000 bình thường + 20 lỗi)

| Tập | Nội dung |
|-----|----------|
| **Train** | ~6.000 engine bình thường (y=0) — học p(x) |
| **CV** | ~2.000 bình thường + ~10 lỗi (y=0/1) — tune ε |
| **Test** | ~2.000 bình thường + ~10 lỗi — đánh giá cuối |

- Vẫn là **unsupervised** khi train (không dùng nhãn)
- Nhãn chỉ dùng cho **CV/test**

## Khi ít anomaly

- Chỉ 2 lỗi → có thể bỏ test set, gộp vào CV
- Rủi ro: **overfit** quyết định vào CV

## Đánh giá

- Dự đoán: y=1 nếu p(x) < ε; y=0 nếu p(x) ≥ ε
- Dữ liệu lệch (ít y=1): dùng **precision, recall, F₁** thay vì accuracy
- Tune ε trên CV: cân bằng phát hiện lỗi vs báo nhầm engine tốt
