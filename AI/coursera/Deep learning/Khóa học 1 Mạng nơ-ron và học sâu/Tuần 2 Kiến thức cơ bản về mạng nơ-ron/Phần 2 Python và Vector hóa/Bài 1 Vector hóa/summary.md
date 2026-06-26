## Vector hóa (Vectorization)

- **Vector hóa** = loại bỏ **for-loop tường minh** trong code
- Kỹ năng then chốt trong kỷ nguyên deep learning với tập dữ liệu lớn

## Ví dụ: z = wᵀx + b

| Cách | Code | Tốc độ |
|---|---|---|
| Không vector hóa | `for i: z += w[i]*x[i]` | Chậm |
| Vector hóa | `z = np.dot(w, x) + b` | Nhanh |

## Benchmark (1 triệu chiều)

- `np.dot(a, b)`: ~**1.5 ms**
- For-loop: ~**400–500 ms** → chậm hơn **~300 lần**
- Chênh lệch có thể là phút vs giờ khi scale lên

## SIMD

- CPU/GPU có lệnh **SIMD** (Single Instruction Multiple Data)
- Hàm NumPy built-in tận dụng **song song hóa** tốt hơn for-loop Python

## Quy tắc

> **Tránh for-loop** khi có thể — dùng hàm NumPy/vectorized operations

- Demo chạy trên CPU; GPU cũng hưởng lợi tương tự (GPU mạnh hơn cho SIMD)
