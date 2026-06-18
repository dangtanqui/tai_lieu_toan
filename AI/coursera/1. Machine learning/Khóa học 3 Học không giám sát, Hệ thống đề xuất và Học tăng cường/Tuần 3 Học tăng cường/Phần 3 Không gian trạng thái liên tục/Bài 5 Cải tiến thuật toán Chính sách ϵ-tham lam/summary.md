## Chọn action khi đang học

- Trong bước "chơi Lunar Lander", cần policy tạm dù Q chưa chính xác

## Các lựa chọn

| Cách | Mô tả | Vấn đề |
|------|-------|--------|
| Ngẫu nhiên hoàn toàn | Luôn random | Thường kém |
| **Greedy** | Luôn argmax Q(S,A) | Có thể **không bao giờ thử** action bị khởi tạo Q thấp |
| **ε-greedy** | Phổ biến nhất | Cân bằng khám phá / khai thác |

## ε-greedy policy

- Với xác suất **1−ε**: chọn action **greedy** (max Q)
- Với xác suất **ε**: chọn action **ngẫu nhiên** (exploration)
- Ví dụ: ε = 0.05 → 95% greedy, 5% explore

## Exploration vs exploitation

- **Exploration**: thử action chưa rõ để học thêm
- **Exploitation**: dùng Q hiện tại để tối đa return

## Giảm ε theo thời gian

- Bắt đầu ε = **1.0** (hoàn toàn random) → giảm dần xuống **0.01**
- Lab cung cấp code sẵn

## Lưu ý hyperparameter

- RL **nhạy** hyperparameter hơn supervised learning (sai ε có thể chậm 10–100×)
