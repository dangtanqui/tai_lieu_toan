## Học tăng cường (Reinforcement Learning) là gì?

- Một trong **ba trụ cột** của machine learning; ít ứng dụng thương mại hơn supervised learning nhưng đang phát triển mạnh
- Bài toán: từ **trạng thái** (state) s → chọn **hành động** (action) a để điều khiển hệ thống (ví dụ: trực thăng tự hành)

## Ví dụ trực thăng tự hành

- Mỗi 0,1 giây nhận vị trí, hướng, tốc độ → quyết định đẩy hai cần điều khiển
- RL đã giúp trực thăng Stanford học bay **lộn ngược** và nhiều động tác nhào lộn
- **Supervised learning không phù hợp**: khó có nhãn "hành động đúng duy nhất" cho mỗi trạng thái

## Hàm thưởng (reward function)

- Tương tự huấn luyện chó: **"good dog"** / **"bad dog"** thay vì chỉ dẫn từng bước
- Chỉ cần nói **làm gì** (target), không cần nói **làm thế nào**
- Ví dụ trực thăng: +1 mỗi giây bay tốt; −1000 khi rơi

## Ứng dụng khác

| Lĩnh vực | Ví dụ |
|----------|-------|
| Robot | Chó robot vượt chướng ngại vật |
| Mô phỏng | Tàu đổ bộ Mặt Trăng (lab tuần này) |
| Công nghiệp | Tối ưu nhà máy |
| Tài chính | Thực thi lệnh bán cổ phiếu theo thời gian |
| Trò chơi | Cờ, Go, video game |

## Ý tưởng cốt lõi

- Không cần cặp (input, output đúng) cho mọi trạng thái
- Chỉ định nghĩa **khi nào tốt / xấu** → thuật toán tự tìm hành động tốt
