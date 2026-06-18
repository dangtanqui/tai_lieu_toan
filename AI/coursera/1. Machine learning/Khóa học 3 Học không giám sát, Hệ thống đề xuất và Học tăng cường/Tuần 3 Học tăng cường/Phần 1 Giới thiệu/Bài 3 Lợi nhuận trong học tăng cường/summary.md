## Return (lợi nhuận tích lũy)

- Tổng phần thưởng có **chiết khấu** — phần thưởng sớm hơn đáng giá hơn
- Analogy: $5 ngay chân hay $10 sau 30 phút đi bộ?

## Công thức

\[
\text{Return} = R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots
\]

- **γ** (gamma): **hệ số chiết khấu** (discount factor), thường gần 1 (0.9, 0.99, 0.999)
- Ví dụ khóa học dùng **γ = 0.5** để minh họa rõ

## Ví dụ: luôn đi trái (bắt đầu state 4)

- Thưởng: 0, 0, 0, 100 → Return = 0 + 0.5×0 + 0.5²×0 + 0.5³×100 = **12.5**

| State bắt đầu | Return (luôn trái) |
|---------------|-------------------|
| 1 | 100 |
| 2 | 50 |
| 3 | 25 |
| 4 | 12.5 |
| 5 | 6.25 |
| 6 | 40 |

## Luôn đi phải → return thấp hơn hầu hết state

- Từ state 4: return = **10** (so với 12.5 khi đi trái)

## Chính sách hỗn hợp

- State 2,3,4 → trái; state 5 → phải (gần thưởng 40)
- Return: 100, 50, 25, 12.5, **20**, 40

## Phần thưởng âm

- γ khuyến khích **hoãn** phần thưởng âm (tương tự lãi suất trong tài chính)
- target RL: tối đa hóa **return**
