## Broadcasting trong Python/NumPy

- Kỹ thuật tự động **mở rộng** ma trận/vector nhỏ để khớp kích thước khi tính toán
- Dùng trong logistic: `Z = w.T @ X + b` (b scalar → vector 1×m)

## Ví dụ: % calo từ carbs/protein/fat

```python
cal = A.sum(axis=0)              # tổng theo cột (axis=0 = dọc)
percentage = 100 * A / cal.reshape(1, 4)
```

- `axis=0`: sum **dọc**; `axis=1`: sum **ngang**

## Các dạng broadcasting

| Phép toán | Kết quả |
|---|---|
| (m,n) ±×÷ (1,n) | Copy hàng (1,n) thành (m,n) |
| (m,n) ±×÷ (m,1) | Copy cột (m,1) thành (m,n) |
| (m,1) + scalar | Copy scalar thành (m,1) |

## Ví dụ nhanh

- Vector (4,1) + 100 → cộng 100 vào **mỗi phần tử**
- (2,3) + (1,3) → cộng [100,200,300] vào **mỗi hàng**

## Tips

- Dùng `.reshape(1, n)` hoặc `(m, 1)` khi không chắc shape
- `reshape` là O(1), rất rẻ
- MATLAB/Octave: hàm `bsxfun` tương tự (tham khảo nâng cao)
