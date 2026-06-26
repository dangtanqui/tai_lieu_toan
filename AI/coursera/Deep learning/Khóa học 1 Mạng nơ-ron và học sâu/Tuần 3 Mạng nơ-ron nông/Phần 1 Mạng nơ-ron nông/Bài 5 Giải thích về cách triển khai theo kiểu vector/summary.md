# Bài 5 — Giải thích vector hóa

## Tại sao W⁽¹⁾X cho đúng kết quả?

Với từng example riêng lẻ:
- W⁽¹⁾x⁽¹⁾ → cột z⁽¹⁾⁽¹⁾
- W⁽¹⁾x⁽²⁾ → cột z⁽¹⁾⁽²⁾
- W⁽¹⁾x⁽³⁾ → cột z⁽¹⁾⁽³⁾

Xếp x⁽¹⁾, x⁽²⁾, x⁽³⁾ thành cột của **X** → W⁽¹⁾X cho **Z⁽¹⁾** với các cột tương ứng.

- Bỏ qua **b** trong chứng minh (broadcasting vẫn đúng khi cộng lại)

## Đối xứng giữa các layer

| Layer 1 | Layer 2 |
|---|---|
| Z⁽¹⁾ = W⁽¹⁾A⁽⁰⁾ + b⁽¹⁾ | Z⁽²⁾ = W⁽²⁾A⁽¹⁾ + b⁽²⁾ |
| A⁽¹⁾ = g(Z⁽¹⁾) | A⁽²⁾ = g(Z⁽²⁾) |

- Các layer thực hiện **cùng một phép tính**, chỉ khác chỉ số
- Mạng sâu hơn = lặp 2 bước này **nhiều lần hơn**

## Nguyên tắc vector hóa

> Nếu xếp input theo cột → output cũng xếp theo cột

- Áp dụng cho z, a ở mọi layer
- Chiều ngang = examples; chiều dọc = units/features

## Chuyển sang activation functions

- Tuần này dùng **sigmoid** — không phải lựa chọn tốt nhất
- Bài tiếp: các **hàm kích hoạt** thay thế (ReLU, tanh, ...)
