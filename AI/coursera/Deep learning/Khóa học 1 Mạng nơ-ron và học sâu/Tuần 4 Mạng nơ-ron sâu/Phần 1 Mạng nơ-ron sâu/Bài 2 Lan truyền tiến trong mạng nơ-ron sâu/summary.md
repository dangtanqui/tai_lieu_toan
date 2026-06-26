# Bài 2 — Lan truyền tiến trong mạng nơ-ron sâu

## Một mẫu huấn luyện

Với mỗi lớp \(l\):

\[
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}, \quad a^{[l]} = g^{[l]}(z^{[l]})
\]

- Lớp 1: \(z^{[1]} = W^{[1]} x + b^{[1]}\), \(a^{[1]} = g(z^{[1]})\)
- Lớp sau: dùng \(a^{[l-1]}\) thay cho \(x\)
- Lớp cuối: \(a^{[L]} = \hat{y}\)

**Mẹo:** thay \(x\) bằng \(a^{[0]}\) → mọi lớp cùng dạng công thức

## Vector hóa (cả tập huấn luyện)

\[
Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}, \quad A^{[l]} = g(Z^{[l]})
\]

- \(X = A^{[0]}\): các mẫu xếp **theo cột**
- \(Z^{[l]}, A^{[l]}\): mỗi cột là một mẫu
- \(\hat{Y} = A^{[L]} = g(Z^{[L]})\)

## Vòng lặp For — ngoại lệ được phép

- Thường tránh For loop, nhưng **lan truyền qua các lớp** bắt buộc lặp \(l = 1 \ldots L\)
- Mạng sâu = lặp lại logic mạng 1 hidden layer **nhiều lần**
- Bài tiếp: kiểm tra **kích thước ma trận** để debug code
