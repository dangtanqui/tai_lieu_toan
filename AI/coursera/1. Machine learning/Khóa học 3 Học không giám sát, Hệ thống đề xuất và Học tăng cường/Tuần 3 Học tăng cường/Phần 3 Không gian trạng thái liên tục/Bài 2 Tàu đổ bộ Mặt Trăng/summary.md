## Bài toán Lunar Lander

- Điều khiển tàu đổ bộ mô phỏng: bắn động cơ để hạ cánh an toàn giữa hai cờ vàng
- Thất bại → va chạm mặt trăng (crash)

## Actions (4 hành động)

| Tên | Ý nghĩa |
|-----|---------|
| **nothing** | Không làm gì (trọng lực kéo xuống) |
| **left** | Động cơ trái → đẩy tàu sang phải |
| **main** | Động cơ chính (hướng xuống) |
| **right** | Động cơ phải → đẩy tàu sang trái |

## State vector (8 thành phần)

- **Liên tục**: x, y, ẋ, ẏ, θ, θ̇
- **Nhị phân**: l, r — chân trái/phải có chạm đất không (0/1)

## Reward function (phức tạp, thiết kế có chủ ý)

| Sự kiện | Reward |
|---------|--------|
| Hạ cánh thành công | +100 đến +140 |
| Tiến gần bệ đáp | dương; xa bệ → âm |
| Crash | −100 |
| Hạ cánh mềm | +100 |
| Mỗi chân chạm đất | +10 |
| Bắn main engine | −0.3 |
| Bắn left/right | −0.03 |

## target

- Học **π(S)** tối đa return; **γ ≈ 0.985**
- Thiết kế reward dễ hơn gán action đúng cho mọi state
- Tiếp theo: **Deep Q-Network (DQN)** với neural network
