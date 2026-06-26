# Bài 6 — Lan truyền tiến và lan truyền ngược

## Forward function (một lớp)

\[
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}, \quad a^{[l]} = g^{[l]}(z^{[l]})
\]

- Khởi tạo chuỗi với \(a^{[0]} = x\) (hoặc \(A^{[0]} = X\) nếu vector hóa)
- Lặp \(l = 1 \ldots L\)

## Backward function — 4 phương trình cốt lõi

| Bước | Công thức |
|------|-----------|
| \(dz^{[l]}\) | \(da^{[l]} \odot g'^{[l]}(z^{[l]})\) |
| \(dW^{[l]}\) | \(dz^{[l]} \cdot a^{[l-1]T}\) |
| \(db^{[l]}\) | \(dz^{[l]}\) |
| \(da^{[l-1]}\) | \(W^{[l]T} \cdot dz^{[l]}\) |

(\(\odot\) = nhân từng phần tử)

### Vector hóa

\(dW^{[l]} = \frac{1}{m} dz^{[l]} a^{[l-1]T}\); \(db^{[l]} = \frac{1}{m} \text{sum}(dz^{[l]}, \text{axis}=1)\)

## Khởi tạo backward

Phân loại nhị phân (sigmoid + logistic loss), lớp cuối \(L\):

\[
da^{[L]} = \frac{y}{a} - \frac{1-y}{1-a}
\]

- Vector hóa: mỗi cột là một mẫu; \(da^{[0]}\) không dùng cập nhật trọng số

## Lời khuyên

- Ví dụ: 2 lớp **ReLU** + 1 lớp **sigmoid** → forward → loss → backward
- Công thức sẽ rõ hơn khi làm **programming exercise**; "ma thuật" chủ yếu đến từ **dữ liệu**
