## Phương trình Bellman

\[
Q(S,A) = R(S) + \gamma \max_{A'} Q(S', A')
\]

- **S**: state hiện tại; **A**: action vừa chọn
- **R(S)**: phần thưởng **tức thì** (immediate reward)
- **S'**: state tiếp theo sau action A
- **A'**: action có thể chọn ở S'

## Trạng thái terminal

- Q(S,A) = **R(S)** (không có S' → bỏ hạng thứ hai)

## Ví dụ: Q(2, phải)

- S'=3; max Q(3,·) = max(25, 6.25) = 25
- Q(2, phải) = 0 + 0.5 × 25 = **12.5** ✓

## Ví dụ: Q(4, trái)

- S'=3; Q(4, trái) = 0 + 0.5 × 25 = **12.5** ✓

## Trực giác

- Return = phần thưởng **ngay** + γ × return **tối ưu** từ state kế tiếp
- Return tối đa từ S' = max_{A'} Q(S', A')

## Ứng dụng

- Phương trình Bellman là nền tảng để **tính Q** và xây thuật toán RL
- Bài tiếp: MDP **ngẫu nhiên** (stochastic)
