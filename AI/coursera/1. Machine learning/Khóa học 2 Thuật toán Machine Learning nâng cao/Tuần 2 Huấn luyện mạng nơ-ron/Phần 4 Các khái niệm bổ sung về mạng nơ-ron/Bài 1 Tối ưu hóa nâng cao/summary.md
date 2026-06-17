## Adam — thuật toán tối ưu nhanh hơn gradient descent

- Gradient descent cố định learning rate α → có thể quá chậm hoặc dao động
- **Adam** (Adaptive Moment Estimation) tự điều chỉnh α cho **từng tham số**

## Ý tưởng

- Tham số liên tục đi cùng hướng → tăng α (bước lớn hơn)
- Tham số dao động qua lại → giảm α (ổn định hơn)

## TensorFlow

```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=...
)
```

- Thử vài giá trị learning rate ban đầu (vd. 10⁻³)
- Adam ít nhạy với lựa chọn α hơn gradient descent thuần
- **De facto standard** — hầu hết practitioner dùng Adam thay gradient descent
