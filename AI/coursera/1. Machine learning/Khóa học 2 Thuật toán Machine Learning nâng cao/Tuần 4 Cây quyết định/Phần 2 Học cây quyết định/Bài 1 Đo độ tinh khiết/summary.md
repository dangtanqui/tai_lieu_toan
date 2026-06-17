# Bài 1 — Đo độ tinh khiết

## Entropy — đo impurity

- **Pure**: tập toàn mèo hoặc toàn chó → impurity thấp
- **Impure**: hỗn hợp mèo/chó → impurity cao
- \(p_1\): tỷ lệ mẫu nhãn dương (cat)
- \(p_0 = 1 - p_1\): tỷ lệ nhãn âm

## Công thức

\[
H(p_1) = -p_1 \log_2(p_1) - p_0 \log_2(p_0)
\]

- Dùng log base 2 để đỉnh hàm = 1
- \(p_1 = 0.5\) (50-50) → entropy = **1** (impure nhất)
- \(p_1 = 0\) hoặc \(1\) → entropy = **0** (pure)
- Quy ước: \(0 \log 0 = 0\)

## Ví dụ trực giác

| Tập mẫu | \(p_1\) | Entropy |
|---------|---------|---------|
| 3 mèo, 3 chó | 0.5 | 1.0 |
| 5 mèo, 1 chó | ~0.83 | ~0.65 |
| 6 mèo, 0 chó | 1.0 | 0 |
| 2 mèo, 4 chó | ~0.33 | ~0.92 |

## Tiêu chí khác

- **Gini criteria**: hàm tương tự entropy, cũng dùng được trong thư viện
- Khóa học tập trung vào **entropy**
