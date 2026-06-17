## Code
- `Z = np.matmul(A.T, W)` hoặc `A.T @ W`
- `A_out = g(Z)` — sigmoid element-wise

## Ví dụ rang cà phê
- \(A^T = [[200, 17]]\) (1×2)
- \(W\): stack \(w_1, w_2, w_3\) thành 2×3
- \(B\): \([b_1, b_2, b_3]\) (1×3)
- \(Z = A^T W + B\) → 3 giá trị \(z_j^{[1]}\) → sigmoid → \([1, 0, 1]\)

## Hàm dense vectorized
```python
Z = np.matmul(A_in, W) + B
A_out = g(Z)
```

## Convention TensorFlow
- Mỗi example nằm trên **một hàng** của ma trận X (không phải cột)
- Dùng `A_in` thay `A.T` — cùng logic, khác quy ước layout

## Kết quả
- Vài dòng code, chạy nhanh hơn nhiều nhờ phần cứng tối ưu cho matrix multiplication
