## Đạo hàm (derivative) — trực giác

- J(w) = w², w = 3 → J = 9
- w tăng ε nhỏ → J tăng khoảng **6ε** → đạo hàm dJ/dw = **6**
- Ý nghĩa: w tăng một chút thì J thay đổi bao nhiêu lần ε

## Liên hệ gradient descent

- Đạo hàm nhỏ → cập nhật w nhỏ (thay w ít ảnh hưởng J)
- Đạo hàm lớn → cập nhật w lớn (thay w ảnh hưởng J nhiều)

## Ví dụ thêm (J = w²)

| w | J | dJ/dw |
|---|---|-------|
| 3 | 9 | 6 |
| 2 | 4 | 4 |
| −3 | 9 | −6 |

- Công thức: d(w²)/dw = **2w** — đạo hàm phụ thuộc giá trị w

## Các hàm khác

| J(w) | dJ/dw (w=2) |
|------|-------------|
| w³ | 3w² = 12 |
| w | 1 |
| 1/w | −1/w² = −¼ |

## SymPy

- Thư viện Python tính đạo hàm tự động: `sp.diff(J, w)`
- Backpropagation cần tính đạo hàm J theo mọi tham số mạng nơ-ron
