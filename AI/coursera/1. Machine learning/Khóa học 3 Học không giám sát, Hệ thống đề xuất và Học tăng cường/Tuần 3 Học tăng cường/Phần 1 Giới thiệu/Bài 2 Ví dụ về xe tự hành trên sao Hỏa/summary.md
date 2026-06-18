## Ví dụ Mars Rover (6 trạng thái)

- Rover có **6 vị trí** (state 1–6); bắt đầu ở state 4
- **Hành động**: đi **trái** hoặc **phải** mỗi bước
- **Phần thưởng**: state 1 → 100; state 6 → 40; các state khác → 0

## Trạng thái kết thúc (terminal state)

- Đến state 1 hoặc 6 → nhận thưởng rồi **kết thúc** (hết nhiên liệu/thời gian)
- Không nhận thêm phần thưởng sau terminal state

## Ví dụ quỹ đạo

- Từ state 4 đi trái: 4→3→2→1 → thưởng 0,0,0,**100**
- Từ state 4 đi phải: 4→5→6 → thưởng 0,0,**40**
- Có thể đổi ý giữa chừng (ví dụ 4→5 rồi quay lại trái) — hợp lệ nhưng lãng phí thời gian

## Bốn thành phần cốt lõi mỗi bước

| Ký hiệu | Ý nghĩa |
|---------|---------|
| **S** | Trạng thái hiện tại |
| **A** | Hành động chọn |
| **R(S)** | Phần thưởng tại trạng thái S |
| **S'** | Trạng thái tiếp theo sau hành động |

- **R(S)** gắn với trạng thái **trước** khi chuyển, không phải trạng thái đích
- Bài tiếp theo: định nghĩa **return** (lợi nhuận tích lũy có chiết khấu)
