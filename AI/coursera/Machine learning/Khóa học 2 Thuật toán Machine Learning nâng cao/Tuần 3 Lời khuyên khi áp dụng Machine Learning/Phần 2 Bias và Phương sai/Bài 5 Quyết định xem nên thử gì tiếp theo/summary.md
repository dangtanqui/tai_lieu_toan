# Bài 5 — Quyết định nên thử gì (bias/variance)

## Sáu hướng cải thiện và mapping

| Hướng | High variance | High bias |
|---|---|---|
| Thu thêm training data | ✓ | ✗ |
| Giảm số feature | ✓ | |
| Thêm feature | | ✓ |
| Thêm đặc trưng đa thức | | ✓ |
| Giảm Lambda | | ✓ |
| Tăng Lambda | ✓ | |

## Giải thích ngắn

- **Thêm data**: giúp variance (overfit trên tập nhỏ); không giúp bias
- **Giảm feature**: giảm độ linh hoạt → giảm variance
- **Thêm feature / polynomial**: model mạnh hơn → giảm bias
- **Giảm Lambda**: ít regularization → fit train tốt hơn → giảm bias
- **Tăng Lambda**: model mượt hơn → giảm variance
- **Giảm kích thước training set không giúp bias** — chỉ làm J_cv tệ hơn

## Tóm tắt

- **Variance**: thêm data hoặc đơn giản hoá model (ít feature, tăng Lambda)
- **Bias**: model mạnh hơn (thêm feature, polynomial, giảm Lambda)

## Lưu ý

- Bias/variance học nhanh nhưng thành thạo cần thực hành lâu dài
- Diagnostic quan trọng nhất khi huấn luyện ML
