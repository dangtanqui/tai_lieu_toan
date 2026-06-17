## Dot product (vector · vector)
- \(z = a \cdot w = \sum_i a_i w_i\)
- Ví dụ: \([1,2] \cdot [3,4] = 1×3 + 2×4 = 11\)

## Cách viết tương đương
- \(z = a^T w\) (a chuyển thành row vector, w là column vector)

## Vector × ma trận
- \(Z = a^T W\): mỗi cột của \(Z\) = dot product \(a^T\) với cột tương ứng của \(W\)
- Ví dụ: \(a^T=[1,2]\), \(W=\begin{bmatrix}3&5\\4&6\end{bmatrix}\) → \(Z=[11, 17]\)

## Ma trận × ma trận
- \(Z = A^T W\): mỗi **hàng** của \(A^T\) nhân với toàn bộ \(W\) → một hàng của \(Z\)
- Phần tử \((i,j)\) = dot product hàng \(i\) của \(A^T\) với cột \(j\) của \(W\)

## Transpose
- Đổi **cột** thành **hàng** (`A.T` trong NumPy)
- Ma trận → nghĩ theo **cột** (vectors)
- Transpose → nghĩ theo **hàng**
