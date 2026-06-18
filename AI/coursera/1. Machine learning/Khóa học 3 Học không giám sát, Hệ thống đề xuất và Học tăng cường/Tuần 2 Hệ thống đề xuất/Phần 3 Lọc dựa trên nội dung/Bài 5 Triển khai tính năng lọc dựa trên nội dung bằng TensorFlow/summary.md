## Cấu trúc code TensorFlow/Keras

### User network & Item network
```python
user_nn = Sequential([Dense(...), Dense(...), Dense(32)])
item_nn = Sequential([Dense(...), Dense(...), Dense(32)])
```
- Lớp ẩn: **ReLU**; output: 32 units

### Pipeline
1. `user_vec = user_nn(user_features)` → **L2 normalize** \(v_u\)
2. `item_vec = item_nn(item_features)` → **L2 normalize** \(v_m\)
3. `output = Dot(axes=1)([user_vec, item_vec])` — lớp dot product đặc biệt
4. `Model(inputs=[user_features, item_features], outputs=output)`

## L2 Normalization

- `tf.nn.l2_normalize(v, axis=1)` — chuẩn hóa vector về **độ dài 1**
- Giúp thuật toán hoạt động **tốt hơn** (không đề cập ở bài trước)

## Huấn luyện

- Loss: **Mean Squared Error**
- Khác collaborative filtering: dùng `Sequential` + `Dense` + `Dot` layer thay viết cost thủ công

## Tóm tắt

| Thành phần | Vai trò |
|------------|---------|
| User NN | \(x_u \rightarrow v_u\) |
| Item NN | \(x_m \rightarrow v_m\) |
| L2 norm | Ổn định dot product |
| Dot layer | Dự đoán \(\hat{y} = v_u \cdot v_m\) |
