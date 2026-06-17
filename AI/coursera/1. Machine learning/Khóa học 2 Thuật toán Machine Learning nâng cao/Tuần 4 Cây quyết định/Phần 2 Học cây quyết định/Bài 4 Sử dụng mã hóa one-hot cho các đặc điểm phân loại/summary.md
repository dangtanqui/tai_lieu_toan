# Bài 4 — One-hot encoding cho feature phân loại

## Vấn đề

- Feature categorical có **> 2 giá trị** (ví dụ ear shape: pointy, floppy, **oval**)
- Split trực tiếp → 3 nhánh con (phức tạp hơn)

## One-hot encoding

- Feature có \(k\) giá trị → tạo **k binary feature** (0/1)
- Ear shape (k=3):
  - `pointy_ears`: có tai nhọn?
  - `floppy_ears`: có tai cụp?
  - `oval_ears`: có tai oval?
- Mỗi hàng: **đúng 1** feature = 1 (hot), còn lại = 0 → tên **one-hot**

## Ví dụ

- Mèo tai nhọn: [1, 0, 0]
- Chó tai oval: [0, 0, 1]

## Lợi ích

- Quay về setting mỗi feature chỉ 2 giá trị → thuật toán decision tree không cần sửa
- **One-hot** cũng dùng được cho **neural network**, logistic/linear regression (cần input số)
- Ví dụ: 3 one-hot (ear) + 1 (face) + 1 (whiskers) = 5 feature cho mạng nơ-ron
