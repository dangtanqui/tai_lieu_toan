# Bài 3 — Ghép nó lại với nhau

## Thuật toán tổng thể

1. Đặt tất cả mẫu tại **root node**
2. Tính **information gain** cho mọi feature → chọn feature IG cao nhất
3. Split → tạo nhánh trái/phải, gán mẫu theo giá trị feature
4. Lặp đệ quy trên từng nhánh cho đến khi đạt **stopping criteria**:
   - Entropy = 0 (100% một lớp)
   - Vượt **maximum depth**
   - IG < ngưỡng
   - Số mẫu tại node < ngưỡng

## Minh họa

- Root: ear shape → 5 mẫu mỗi nhánh
- Nhánh trái: face shape (IG cao hơn whiskers; ear shape IG = 0 vì đã cùng pointy) → leaf cat / leaf not cat
- Nhánh phải: whiskers → leaf cat / leaf not cat

## Recursive algorithm

- Mỗi subtree = huấn luyện decision tree trên **subset** mẫu tại node đó
- Code gọi chính nó → thuật toán **đệ quy**

## Chọn maximum depth

- Depth lớn → cây phức tạp hơn, dễ **overfitting** (tương tự polynomial bậc cao / mạng lớn)
- Có thể dùng **cross-validation** chọn depth
- Thư viện open-source thường có default tốt

## Inference

- Mẫu mới: bắt đầu tại root → theo decision node → đến leaf → nhận dự đoán
