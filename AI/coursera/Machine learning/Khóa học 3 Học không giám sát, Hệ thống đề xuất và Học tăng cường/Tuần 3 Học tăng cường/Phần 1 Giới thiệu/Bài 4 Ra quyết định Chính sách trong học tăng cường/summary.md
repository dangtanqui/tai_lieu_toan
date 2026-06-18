## Chính sách (policy) π

- Hàm **π(S)** → hành động **A** tương ứng với mỗi trạng thái S
- target RL: tìm π tối ưu để **tối đa hóa return**

## Các cách chọn hành động (ví dụ Mars Rover)

- Luôn đi về phần thưởng **gần** hơn
- Luôn đi về phần thưởng **lớn** hơn
- Luôn đi trái, trừ khi cách 1 bước đến thưởng nhỏ hơn → đi phải

## Ví dụ chính sách tốt

| State | Hành động |
|-------|-----------|
| 2, 3, 4 | Trái |
| 5 | Phải |

## Thuật ngữ

- **Policy** = thuật ngữ chuẩn trong RL (có thể gọi là "controller")
- π(S) cho biết hành động nào nên thực hiện ở trạng thái S

## Bước tiếp theo

- Ôn tập khái niệm → phát triển thuật toán
- Khái niệm then chốt: **hàm giá trị state-action Q(S,A)**
