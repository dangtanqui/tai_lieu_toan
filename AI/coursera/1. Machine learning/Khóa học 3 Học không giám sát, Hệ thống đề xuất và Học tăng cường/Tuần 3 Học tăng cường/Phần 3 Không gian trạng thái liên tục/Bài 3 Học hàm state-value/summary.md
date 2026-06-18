## Ý tưởng Deep RL

- Huấn luyện **neural network** ước lượng **Q(S,A)** → chọn action có Q cao nhất
- Khác supervised learning thuần: input **(S,A)**, output **Q(S,A)** — không map trực tiếp S→A

## Kiến trúc mạng (phiên bản đầu)

- Input **x**: 8 số state + 4 số one-hot action = **12 features**
- Hidden: 64 → 64 neurons
- Output: 1 số = Q(S,A) = target **y**

## Chọn action

- Tính Q(S, nothing), Q(S, left), Q(S, main), Q(S, right) → chọn action có Q **lớn nhất**

## Tạo training set từ Bellman

- Thu thập tuple **(S, A, R(S), S')** khi tương tác simulator
- **X** = (S, A); **Y** = R(S) + γ max_{A'} Q(S', A')
- Ban đầu Q là **đoán ngẫu nhiên** — sẽ cải thiện dần

## Thuật toán DQN (Deep Q-Network)

1. Khởi tạo mạng Q ngẫu nhiên
2. Lặp: chơi Lunar Lander → lưu **10.000 tuple gần nhất** (**replay buffer**)
3. Tạo 10.000 cặp (X,Y) từ Bellman → train mạng **Q_new** (MSE loss)
4. Gán **Q ← Q_new**; lặp lại

- Q(S',A') dùng mạng hiện tại — mỗi vòng ước lượng tốt hơn
- Tiếp theo: cải tiến kiến trúc mạng, ε-greedy, mini-batch, soft update
