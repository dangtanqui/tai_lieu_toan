# Bài 6 — Cây hồi quy (regression tree)

## Bài toán

- Input: ear shape, face shape, whiskers
- Output Y: **weight** (số) — bài toán **regression**, không phải classification

## Leaf node dự đoán gì?

- Dự đoán = **trung bình** weight các mẫu huấn luyện rơi vào leaf đó
- Ví dụ: 4 mẫu weights 7.2, 7.6, 8.4, 10.2 → dự đoán 8.35 lb

## Chọn split: variance thay entropy

- Classification: giảm **entropy** / tối đa **information gain**
- Regression: giảm **variance** của Y tại mỗi nhánh
- Variance đo mức độ phân tán số (7.2–10.2 → variance thấp; 8.8–20 → variance cao)

## Weighted variance & reduction in variance

- Trọng số \(w^{\text{left}}\), \(w^{\text{right}}\) như classification
- **Reduction in variance** = Var(root) − weighted avg variance sau split
- Root Var = 20.51; split ear shape → reduction = **8.84** (cao nhất) → chọn ear shape

## Quy trình

- Giống classification: chọn split theo reduction in variance lớn nhất, đệ quy, dừng theo criteria
- Cùng feature có thể split ở cả nhánh trái và phải — hợp lệ

## Tree ensemble

- Nhiều cây → kết quả tốt hơn một cây đơn
