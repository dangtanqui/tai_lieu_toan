## TensorFlow
- Framework phổ biến cho deep learning (PyTorch cũng phổ biến; khóa học dùng TensorFlow)

## Ví dụ: rang cà phê
- Input \(x\): nhiệt độ + thời gian rang → dự đoán cà phê ngon (1) hay không (0)
- Layer 1: `Dense(units=3, activation='sigmoid')` → \(a_1\) (3 số)
- Layer 2: `Dense(units=1, activation='sigmoid')` → \(a_2\) (xác suất)
- Threshold 0.5 → \(\hat{y} \in \{0, 1\}\)

## Ví dụ: chữ viết tay
- \(x\) = numpy array pixel → Layer 1 (25 units) → Layer 2 (15 units) → Layer 3 (1 unit)
- Mỗi bước: \(a^{[l]} = \text{Layer}_l(a^{[l-1]})\)

## Dense layer
- **Dense** = layer mạng nơ-ron đã học (fully connected)

## Forward propagation
- Tạo layer → áp dụng lên input/activation trước → lặp qua các layer
