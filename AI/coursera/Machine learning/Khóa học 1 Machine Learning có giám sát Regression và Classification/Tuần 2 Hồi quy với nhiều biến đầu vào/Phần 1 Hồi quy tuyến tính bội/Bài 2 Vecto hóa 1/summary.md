## Vectorization
- Code **ngắn hơn** + chạy **nhanh hơn** nhiều
- Tận dụng NumPy, CPU/GPU parallel

## So sánh implement f(x) = w·x + b

| Cách | Vấn đề |
|------|--------|
| w₀x₀ + w₁x₁ + ... thủ công | Không scale khi n lớn |
| For loop | Chậm, tuần tự |
| **`np.dot(w, x) + b`** | ✓ 1 dòng, vectorized |

## Indexing
- Toán: w₁, x₁ (bắt đầu từ 1)
- Python/NumPy: w[0], x[0] (bắt đầu từ 0)

## Lợi ích
- n = 100,000 features → vectorization quan trọng
- Dùng thư viện linear algebra hiện đại
