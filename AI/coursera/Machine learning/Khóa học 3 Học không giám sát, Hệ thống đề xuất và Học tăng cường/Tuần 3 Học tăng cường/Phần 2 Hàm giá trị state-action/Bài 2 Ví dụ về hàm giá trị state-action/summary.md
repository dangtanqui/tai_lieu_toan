## Optional Lab — thử nghiệm Q(S,A)

- Jupyter notebook cho phép thay đổi tham số Mars Rover và xem Q, return, policy thay đổi
- Tham số cố định: 6 states, 2 actions; terminal reward trái=100, phải=40; γ=0.5

## Thay đổi terminal reward phải

- Giảm reward state 6 xuống **10** → Q(5, trái)=6.25 > Q(5, phải)=5
- **Chính sách tối ưu**: luôn đi trái từ mọi state

## Thay đổi γ (hệ số chiết khấu)

| γ | Hiệu ứng |
|---|----------|
| **0.9** | Kiên nhẫn hơn → từ state 5 vẫn đi trái (65.61 > 36) |
| **0.3** | Rất vội → từ state 4 chọn phải (thưởng 40 gần hơn 100 xa) |

- Q(5, phải) với γ=0.9: 36 = 0.9 × 40 ✓

## Bài học

- **Reward** và **γ** cùng quyết định Q, return tối ưu và policy
- Return tối ưu từ state = max của hai giá trị Q(S,·)
- Tiếp theo: **phương trình Bellman**
