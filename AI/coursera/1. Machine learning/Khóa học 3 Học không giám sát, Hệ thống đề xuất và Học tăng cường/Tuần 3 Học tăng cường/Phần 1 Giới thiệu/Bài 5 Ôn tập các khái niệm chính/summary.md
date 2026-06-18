## Tóm tắt formalism RL

| Khái niệm | Mars Rover |
|-----------|------------|
| **States** | 6 vị trí (1–6) |
| **Actions** | Trái / Phải |
| **Rewards** | 100, 0,…,0, 40 |
| **γ** | 0.5 (ví dụ) |
| **Return** | \(R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots\) |
| **Policy π** | Ánh xạ state → action |

## Áp dụng cho bài toán khác

**Trực thăng tự hành**
- State: vị trí, hướng, tốc độ
- Action: điều khiển cần joystick
- Reward: +1 bay tốt; −1000 khi rơi; γ ≈ 0.99

**Chơi cờ**
- State: vị trí quân cờ
- Action: nước đi hợp lệ
- Reward: +1 thắng, −1 thua, 0 hòa; γ ≈ 0.99–0.999

## Markov Decision Process (MDP)

- Tên chính thức của formalism RL
- **Tính Markov**: tương lai chỉ phụ thuộc **trạng thái hiện tại**, không phụ thuộc lịch sử

## Sơ đồ MDP

- Agent chọn action **a** theo policy **π**
- Môi trường trả về state mới **S** và reward **R**
- Vòng lặp: observe → act → reward → new state

## Bước tiếp theo

- Định nghĩa và học **hàm giá trị state-action Q(S,A)**
