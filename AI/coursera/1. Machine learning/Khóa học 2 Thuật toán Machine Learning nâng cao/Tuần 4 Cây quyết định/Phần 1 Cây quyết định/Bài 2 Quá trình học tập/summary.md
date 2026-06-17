# Bài 2 — Quá trình học tập

## Quy trình xây cây

1. Chọn feature cho **root node** (ví dụ: ear shape) → chia 10 mẫu trái/phải
2. Lặp trên nhánh trái: chọn feature tiếp (ví dụ: face shape) → chia tiếp
3. Nếu nhánh **pure** (100% mèo hoặc 100% chó) → tạo **leaf node**
4. Lặp tương tự trên nhánh phải (ví dụ: split theo whiskers)

## Quyết định quan trọng

### Chọn feature để split

- Mục tiêu: tối đa **purity** (tập con gần all-cat hoặc all-not-cat)
- Ví dụ lý tưởng: feature "cat DNA" → hai nhánh hoàn toàn pure
- Thực tế: so sánh ear shape, face shape, whiskers theo độ pure của nhánh trái/phải
- Sẽ dùng **entropy** để đo impurity

### Khi nào dừng split

- Nhánh đã 100% một lớp
- Đạt **maximum depth** (depth = số bước từ root; root depth = 0)
- **Information gain** quá nhỏ (cải thiện purity không đáng kể)
- Số mẫu tại node dưới ngưỡng → tạo leaf, dự đoán theo đa số
- Giới hạn depth / số mẫu giúp cây nhỏ hơn, giảm **overfitting**

## Lưu ý

- Nhiều tiêu chí dừng do nhiều nhà nghiên cứu bổ sung qua thời gian — thuật toán phức tạp nhưng hiệu quả
- Thư viện open-source giúp chọn tham số mà không cần tự quyết mọi chi tiết
