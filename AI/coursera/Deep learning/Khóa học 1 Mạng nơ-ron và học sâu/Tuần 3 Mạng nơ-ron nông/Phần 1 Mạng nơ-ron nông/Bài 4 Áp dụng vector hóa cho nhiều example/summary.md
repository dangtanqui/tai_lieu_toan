# Bài 4 — Vector hóa nhiều training examples

## Vấn đề

- Bài trước: tính ŷ cho **1 example** tại một thời điểm
- Cần lặp for i = 1..m → **chậm**, không hiệu quả

## Cách vector hóa

Xếp m examples vào **các cột** của ma trận X (nₓ × m):

| Biến đơn | Biến vector hóa |
|---|---|
| x⁽ⁱ⁾ | **X** (nₓ × m) |
| z⁽ˡ⁾⁽ⁱ⁾ | **Z⁽ˡ⁾** (nₗ × m) |
| a⁽ˡ⁾⁽ⁱ⁾ | **A⁽ˡ⁾** (nₗ × m) |

## Bốn phương trình vector hóa

```
Z⁽¹⁾ = W⁽¹⁾X + b⁽¹⁾
A⁽¹⁾ = g(Z⁽¹⁾)
Z⁽²⁾ = W⁽²⁾A⁽¹⁾ + b⁽²⁾
A⁽²⁾ = g(Z⁽²⁾)
```

- **b** được broadcast tự động sang mọi cột (nhờ Python broadcasting)

## Cách đọc ma trận A

| Chiều | Ý nghĩa |
|---|---|
| **Ngang** (cột) | Các training examples (1 → m) |
| **Dọc** (hàng) | Các hidden units (1 → n₁) |

- Góc trên-trái = activation của hidden unit 1, example 1
- Quét ngang = cùng unit, khác examples
- Quét dọc = khác units, cùng example

## Ký hiệu kết hợp

- **a⁽²⁾⁽ⁱ⁾**: ngoặc vuông = layer 2, ngoặc tròn = example i

## Ý chính

- Vector hóa đúng **rất quan trọng** trong deep learning
- Kết quả tương tự logistic regression — chỉ cần thay x → X
