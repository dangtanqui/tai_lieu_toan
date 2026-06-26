# Bài 1 — Tổng quan về mạng nơ-ron

## Mục tiêu tuần này

- Triển khai **mạng nơ-ron** từ đầu
- Video này là **tổng quan nhanh** — chi tiết kỹ thuật ở các bài sau

## So sánh với Logistic Regression

| Logistic Regression | Mạng nơ-ron |
|---|---|
| z → a (sigmoid) | z → a lặp lại nhiều lần |
| 1 bước tính toán | Nhiều layer xếp chồng |
| Output: ŷ | Output: a⁽²⁾ = ŷ |

## Cấu trúc mạng 2 layer

- **Layer 1 (hidden):** z⁽¹⁾ = W⁽¹⁾x + b⁽¹⁾ → a⁽¹⁾ = sigmoid(z⁽¹⁾)
- **Layer 2 (output):** z⁽²⁾ = W⁽²⁾a⁽¹⁾ + b⁽²⁾ → a⁽²⁾ = ŷ

## Ký hiệu quan trọng

| Ký hiệu | Ý nghĩa |
|---|---|
| **x⁽ⁱ⁾** (ngoặc tròn) | Example thứ i trong tập train |
| **z⁽ˡ⁾, a⁽ˡ⁾** (ngoặc vuông) | Giá trị ở layer l |
| **W⁽ˡ⁾, b⁽ˡ⁾** | Tham số của layer l |

## Lan truyền xuôi và ngược

- **Forward:** x → z⁽¹⁾ → a⁽¹⁾ → z⁽²⁾ → a⁽²⁾ → **Loss L**
- **Backward:** tính da⁽²⁾, dz⁽²⁾ → dW⁽²⁾, db⁽²⁾ → da⁽¹⁾, dz⁽¹⁾ → dW⁽¹⁾, db⁽¹⁾

## Ý chính

- Mạng nơ-ron = **logistic regression lặp lại nhiều lần**
- Không cần nhớ hết ký hiệu ngay — sẽ đi sâu ở các bài tiếp theo
