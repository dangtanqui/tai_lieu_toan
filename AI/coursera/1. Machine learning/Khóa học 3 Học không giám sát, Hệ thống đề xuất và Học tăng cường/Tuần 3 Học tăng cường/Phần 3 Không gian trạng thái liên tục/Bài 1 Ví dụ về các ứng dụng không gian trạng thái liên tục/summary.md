## Discrete vs continuous state space

- **Rời rạc**: Mars Rover — chỉ 1 trong 6 vị trí
- **Liên tục**: vị trí có thể là bất kỳ số thực (ví dụ 2.7 km, 4.8 km trên đoạn 0–6 km)

## Ví dụ state vector

**Xe tự lái (6 số)**
- x, y, θ (hướng), ẋ, ẏ, θ̇

**Trực thăng (12 số)**
- Vị trí: x, y, z
- Hướng: roll φ, pitch θ, yaw ω
- Vận tốc: ẋ, ẏ, ż
- Tốc độ góc: φ̇, θ̇, ω̇

## Continuous-state MDP

- State là **vector số thực**, mỗi thành phần trong miền liên tục
- Policy nhận vector state → chọn action

## Lab tuần này

- **Lunar Lander**: MDP liên tục — hạ cánh tàu mô phỏng trên Mặt Trăng
- Bài tiếp: chi tiết bài toán Lunar Lander
