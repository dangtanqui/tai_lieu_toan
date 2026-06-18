## Khối xây dựng cơ bản
- **Layer** = nhóm nơ-ron; mỗi nơ-ron = logistic regression unit với **sigmoid**

## Tính toán một lớp ẩn
- Mỗi nơ-ron: \(a_j^{[1]} = g(w_j^{[1]} \cdot x + b_j^{[1]})\)
- Ví dụ: 3 nơ-ron → vector activation \(a^{[1]} = [0.3,\ 0.7,\ 0.2]\)

## Ký hiệu layer
- Input layer = layer 0; hidden layer = layer 1; output layer = layer 2
- Superscript \([l]\): \(w_j^{[l]}\), \(b_j^{[l]}\), \(a^{[l]}\) — gắn với layer \(l\)

## Output layer
- \(a^{[2]} = g(w_1^{[2]} \cdot a^{[1]} + b_1^{[2]})\) → xác suất cuối (scalar)
- Tùy chọn: threshold 0.5 → dự đoán nhị phân \(\hat{y} \in \{0, 1\}\)

## Nguyên tắc
- Mỗi layer: input vector → nhiều logistic units → output vector → truyền layer tiếp theo
