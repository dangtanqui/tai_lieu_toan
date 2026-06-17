## Ma trận trong NumPy
- Ma trận = mảng 2D; kích thước = **số hàng × số cột**
- Ví dụ: `np.array([[1,2,3],[4,5,6]])` → 2×3

## Vector hàng vs cột
- `[[200, 17]]` → 1×2 (row vector) — **chuẩn TensorFlow**
- `[[200], [17]]` → 2×1 (column vector)
- `[200, 17]` → 1D array (dùng ở Course 1 với logistic regression)

## Tại sao dùng ma trận?
- TensorFlow thiết kế cho dataset lớn → ma trận hiệu quả hơn 1D array

## Output layer
- \(a_1\) (3 nơ-ron): tensor shape `(1, 3)`, float32
- \(a_2\) (1 nơ-ron): tensor shape `(1, 1)`
- Chuyển tensor ↔ NumPy: `a1.numpy()`

## Tensor
- Kiểu dữ liệu TensorFlow để lưu/tính toán ma trận hiệu quả (trong khóa học ≈ ma trận)
