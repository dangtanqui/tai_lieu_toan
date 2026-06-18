## Tại sao dùng TensorFlow?

- Collaborative filtering **không** fit vào `Dense` layer + `model.fit` thông thường
- Cần tự viết cost function, dùng **Auto Diff** để tính đạo hàm tự động

## Gradient Tape (Auto Diff)

```python
with tf.GradientTape() as tape:
    f = w * x
    J = (f - y) ** 2
dJ_dw = tape.gradient(J, w)
w.assign_sub(alpha * dJ_dw)
```

- Chỉ cần định nghĩa \(J\) → TensorFlow tính \(\partial J / \partial w\) tự động
- **Auto Diff** (còn gọi Auto Grad) — PyTorch cũng hỗ trợ

## Triển khai Collaborative Filtering

- Optimizer: **Adam** (`keras.optimizers.Adam`)
- Trong `GradientTape`: tính cost \(J(w, b, x, y_{norm}, r, \lambda, \ldots)\)
- `tape.gradient(J, [x, w, b])` → cập nhật bằng `optimizer.apply_gradients`
- Có thể dùng Adam thay gradient descent thuần — mạnh hơn

## Dataset thực tế

- **MovieLens** (Harper & Konstan) — phim thật, đánh giá thật
- Lab cung cấp đầy đủ syntax; không cần tự tính đạo hàm bằng tay
