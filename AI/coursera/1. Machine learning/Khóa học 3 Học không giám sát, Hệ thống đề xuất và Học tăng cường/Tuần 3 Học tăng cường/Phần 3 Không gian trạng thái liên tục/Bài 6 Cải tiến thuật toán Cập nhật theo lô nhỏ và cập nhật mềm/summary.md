## Mini-batch gradient descent

- **Batch GD**: mỗi bước tính gradient trên **toàn bộ** dataset (ví dụ 100M mẫu) → rất chậm
- **Mini-batch**: mỗi bước chỉ dùng **m'** mẫu (ví dụ 1.000) → nhanh hơn nhiều

## So sánh hành vi

- Batch GD: đi thẳng về minimum
- Mini-batch: đường đi **nhiễu** nhưng mỗi bước rẻ → thường **nhanh hơn** với data lớn
- Dùng phổ biến trong supervised learning (Adam + mini-batch)

## Áp dụng DQN

- Replay buffer: 10.000 tuple
- Thay vì train trên cả 10.000 mỗi lần → lấy **1.000** mẫu ngẫu nhiên (mini-batch)
- Mỗi iteration nhanh hơn; hội tụ tổng thể nhanh hơn

## Soft update

- Cập nhật cứng: **W ← W_new** — một bước xui có thể làm Q tệ hơn
- **Soft update** (ví dụ τ = 0.01):

\[
W \leftarrow 0.01 \cdot W_{\text{new}} + 0.99 \cdot W
\]

- Chỉ nhận **1%** trọng số mới mỗi lần → thay đổi **mượt**, hội tụ ổn định hơn
- τ + (1−τ) = 1; τ=1 → quay về cập nhật cứng

## Kết quả

- Mini-batch + soft update + kiến trúc 4-output + ε-greedy → Lunar Lander hoạt động tốt
