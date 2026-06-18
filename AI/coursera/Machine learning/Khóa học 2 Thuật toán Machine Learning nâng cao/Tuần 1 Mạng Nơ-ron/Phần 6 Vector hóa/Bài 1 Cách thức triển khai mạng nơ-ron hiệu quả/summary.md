## Vấn đề
- Forward prop từng nơ-ron (for loop) chậm — không scale mạng lớn

## Giải pháp: vectorization
- Dùng **ma trận** + `np.matmul` thay for loop
- \(Z = A_{in} \cdot W + B\); \(A_{out} = g(Z)\) (sigmoid element-wise)

## Lợi ích
- **GPU**/CPU tối ưu cho phép nhân ma trận lớn
- Lý do chính deep learning scale được trong thập kỷ qua

## Thay đổi dữ liệu
- Dùng 2D array (double bracket) thay 1D array
- Tất cả \(A_{in}, W, B, Z, A_{out}\) đều là ma trận
