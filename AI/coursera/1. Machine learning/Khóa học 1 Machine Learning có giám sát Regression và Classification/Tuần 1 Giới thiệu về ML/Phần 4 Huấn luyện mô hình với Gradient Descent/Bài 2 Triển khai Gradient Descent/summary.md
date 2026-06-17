## Công thức Gradient Descent
```
w := w − α · ∂J/∂w
b := b − α · ∂J/∂b
```
- **α (alpha)** = learning rate — số dương nhỏ (vd: 0.01)
- **∂J/∂w, ∂J/∂b** = derivative — hướng + độ lớn bước đi

## Learning rate α
- **α lớn** → bước lớn, aggressive
- **α nhỏ** → bước nhỏ, chậm nhưng ổn định

## Lặp cho đến convergence
- **Converge** = w, b gần như không đổi nữa → đạt local minimum

## Simultaneous Update (quan trọng!)
**Đúng:** tính temp_w, temp_b từ w, b **cũ** → rồi mới gán w, b

**Sai:** update w trước → dùng w mới tính b → không phải gradient descent chuẩn

## Lưu ý
- Derivative từ calculus — **không cần biết calculus** để làm khóa học
- `:=` = assignment (gán), khác `=` toán học
