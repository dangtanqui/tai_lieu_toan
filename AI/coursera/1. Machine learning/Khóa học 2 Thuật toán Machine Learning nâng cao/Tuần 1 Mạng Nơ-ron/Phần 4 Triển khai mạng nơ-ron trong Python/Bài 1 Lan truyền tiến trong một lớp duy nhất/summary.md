## Mục tiêu
- Implement **forward propagation** một layer bằng Python/NumPy (không TensorFlow)

## Quy ước ký hiệu code
- `w1_1` = \(w_1^{[1]}\); `a1_1` = \(a_1^{[1]}\)
- Dùng 1D array (single bracket) thay vì ma trận 2D

## Tính từng nơ-ron
- \(z = w \cdot x + b\)
- \(a = g(z)\) với \(g\) = sigmoid
- Lặp cho 3 nơ-ron layer 1 → `np.array([a1_1, a1_2, a1_3])` = \(a^{[1]}\)

## Layer 2
- \(a_2 = g(w_2^{[1]} \cdot a^{[1]} + b_2^{[1]})\)

## Hạn chế
- Hard-code từng nơ-ron — không scale cho mạng lớn
