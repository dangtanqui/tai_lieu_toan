## Lưu ý về vector trong NumPy

- **Broadcasting** linh hoạt nhưng dễ gây **bug khó tìm** nếu không hiểu shape

## Rank-1 array — tránh dùng

```python
a = np.random.randn(5)    # shape (5,) — KHÔNG phải cột hay hàng
a.T == a                  # transpose không đổi!
np.dot(a, a.T)            # trả về số, không phải ma trận
```

## Nên dùng

| Cách tạo | Shape | Loại |
|---|---|---|
| `np.random.randn(5, 1)` | (5, 1) | **Cột vector** |
| `np.random.randn(1, 5)` | (1, 5) | **Hàng vector** |

- `a.T` của cột vector → hàng vector (2 dấu ngoặc khi in)
- `np.dot(a, a.T)` → ma trận **outer product** đúng

## Best practices

1. **Không dùng** rank-1 array `(n,)`
2. Luôn dùng `(n, 1)` hoặc `(1, n)`
3. Thêm **assert** kiểm tra shape: `assert(a.shape == (5, 1))`
4. Dùng `.reshape(n, 1)` khi cần sửa shape

## Tóm tắt

> Vector hóa mạnh nhưng cần kiểm soát **dimension** — assertion + reshape giúp code sạch, ít bug
