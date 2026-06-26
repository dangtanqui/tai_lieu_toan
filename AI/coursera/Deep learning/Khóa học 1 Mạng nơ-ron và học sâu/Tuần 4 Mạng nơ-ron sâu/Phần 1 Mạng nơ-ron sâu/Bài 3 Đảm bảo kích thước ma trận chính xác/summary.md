# Bài 3 — Đảm bảo kích thước ma trận chính xác

## Công cụ debug

- Viết ra giấy kích thước từng ma trận khi implement — giúp loại bỏ nhiều lỗi

## Ví dụ: mạng 5 lớp

| Lớp \(l\) | \(n^{[l]}\) |
|-----------|-------------|
| 0 (input) | 2 |
| 1 | 3 |
| 2 | 5 |
| 3 | 4 |
| 4 | 2 |
| 5 (output) | 1 |

## Kích thước W và b (một mẫu)

| Tham số | Kích thước |
|---------|------------|
| \(W^{[l]}\) | \(n^{[l]} \times n^{[l-1]}\) |
| \(b^{[l]}\) | \(n^{[l]} \times 1\) |
| \(z^{[l]}, a^{[l]}\) | \(n^{[l]} \times 1\) |

**Ví dụ:** \(W^{[1]}\) là \(3 \times 2\); \(W^{[2]}\) là \(5 \times 3\)

- Backprop: \(dW^{[l]}\) cùng kích thước \(W^{[l]}\); \(db^{[l]}\) cùng kích thước \(b^{[l]}\)

## Vector hóa (m mẫu)

| Đại lượng | Một mẫu | Vector hóa |
|-----------|---------|------------|
| \(Z^{[l]}, A^{[l]}\) | \(n^{[l]} \times 1\) | \(n^{[l]} \times m\) |
| \(W^{[l]}, b^{[l]}\) | Không đổi | Không đổi |
| \(X = A^{[0]}\) | \(n^{[0]} \times 1\) | \(n^{[0]} \times m\) |

- **Broadcasting:** \(b^{[l]}\) tự nhân bản thành \(n^{[l]} \times m\); \(dZ^{[l]}, dA^{[l]}\) cùng kích thước \(Z^{[l]}, A^{[l]}\)
- Luôn kiểm tra \(W^{[l]}: n^{[l]} \times n^{[l-1]}\) — kích thước nhất quán giúp loại lỗi backprop
