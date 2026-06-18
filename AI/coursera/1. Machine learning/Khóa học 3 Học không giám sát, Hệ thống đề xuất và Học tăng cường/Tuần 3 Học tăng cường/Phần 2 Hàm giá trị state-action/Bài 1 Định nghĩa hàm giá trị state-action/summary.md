## Định nghĩa Q(S,A) — hàm giá trị state-action

- **Q(S,A)** = return nếu: bắt đầu ở state S, thực hiện action A **một lần**, rồi hành xử **tối ưu** sau đó
- Còn gọi **Q-function** hoặc **state-action value function**
- Trong tài liệu ngoài khóa học: đôi khi ký hiệu **Q\*** (optimal Q-function) — cùng nghĩa

## Ví dụ (γ = 0.5, chính sách tối ưu: trái ở 2,3,4; phải ở 5)

| State | Q(trái) | Q(phải) |
|-------|---------|---------|
| 2 | **50** | 12.5 |
| 3 | **25** | 6.25 |
| 4 | **12.5** | 10 |
| 5 | 6.25 | **20** |
| 1 | 100 | 100 |
| 6 | 40 | 40 |

- Q(2, phải) = 12.5: đi phải rồi tối ưu — không đánh giá hành động đó "tốt hay xấu"

## Từ Q → chính sách tối ưu

- Return tốt nhất từ state S = **max_A Q(S,A)**
- Chọn action: **π(S) = argmax_A Q(S,A)**

## Lưu ý

- Định nghĩa có vẻ "vòng tròn" (cần biết hành vi tối ưu) — thuật toán sau sẽ giải quyết bằng cách **lặp cải thiện** Q
