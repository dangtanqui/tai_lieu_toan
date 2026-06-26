# Bài 2 — Biểu diễn mạng nơ-ron

## Các layer trong mạng

| Layer | Vai trò |
|---|---|
| **Input layer** | Chứa features x₁, x₂, x₃ |
| **Hidden layer** | Tính toán trung gian — không có trong tập train |
| **Output layer** | Sinh dự đoán **ŷ** |

## Tại sao gọi là "hidden"?

- Trong **supervised learning**, ta chỉ thấy input x và output y
- Giá trị đúng của các node ở giữa **không được quan sát** trong tập train

## Ký hiệu activation

- **A** = activation — giá trị mỗi layer truyền sang layer tiếp theo
- **a⁽⁰⁾** = x (input features)
- **a⁽¹⁾** = vector 4×1 (4 hidden units)
- **a⁽²⁾** = số thực → **ŷ = a⁽²⁾**

## Quy ước đếm layer

- Mạng trên gọi là **mạng 2 layer** (không đếm input layer)
- Input layer = layer 0; hidden = layer 1; output = layer 2

## Kích thước tham số (ví dụ: 3 features, 4 hidden, 1 output)

| Tham số | Kích thước | Giải thích |
|---|---|---|
| **W⁽¹⁾** | 4 × 3 | 4 hidden units, 3 features |
| **b⁽¹⁾** | 4 × 1 | Bias cho 4 hidden units |
| **W⁽²⁾** | 1 × 4 | 1 output, 4 hidden units |
| **b⁽²⁾** | 1 × 1 | Bias output |

## Ý chính

- Mỗi node = 2 bước: tính **z** rồi áp dụng **hàm kích hoạt** → **a**
- Ký hiệu ngoặc vuông chỉ **layer**, ngoặc tròn chỉ **training example**
