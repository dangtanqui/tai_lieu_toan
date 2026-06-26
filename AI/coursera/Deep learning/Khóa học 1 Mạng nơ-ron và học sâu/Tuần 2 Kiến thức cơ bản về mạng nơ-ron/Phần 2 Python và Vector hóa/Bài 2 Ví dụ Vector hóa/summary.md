## Ví dụ vector hóa thêm

## Ma trận × vector

- u = A·v: không vector hóa = 2 vòng for
- Vector hóa: `u = np.dot(A, v)`

## Hàm element-wise NumPy

| Hàm | Chức năng |
|---|---|
| `np.exp(v)` | e^x từng phần tử |
| `np.log(v)` | log từng phần tử |
| `np.abs(v)` | giá trị tuyệt đối |
| `np.maximum(v, 0)` | max với 0 |
| `v**2` | bình phương |
| `1/v` | nghịch đảo |

## Áp dụng logistic regression

- Thay dw₁, dw₂,… riêng lẻ → **dw** vector `(n_x, 1)`:
  - `dw = np.zeros((n_x, 1))`
  - `dw += x_i * dz_i` (một dòng)
  - `dw /= m`
- Giảm từ **2 for-loop** xuống **1 for-loop** (qua m mẫu)

## Hướng tiếp

- Video sau: vector hóa **toàn bộ** tập m mẫu — không cần for-loop qua training examples
