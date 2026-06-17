## Quy tắc kích thước
- \(A^T\) (m×n) × \(W\) (n×p) → \(Z\) (m×p)
- Số **cột** ma trận trái = số **hàng** ma trận phải (để dot product cùng độ dài)

## Cách tính
- \(Z_{ij}\) = dot product hàng \(i\) của \(A^T\) với cột \(j\) của \(W\)

## Ví dụ
- \(A^T\): 3×2, \(W\): 2×4 → \(Z\): 3×4 (12 phần tử)

## Output shape
- Số hàng \(Z\) = số hàng \(A^T\); số cột \(Z\) = số cột \(W\)

## Ứng dụng
- Nền tảng cho **vectorized implementation** của forward propagation
