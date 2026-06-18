# Bài 2 — Lấy mẫu có hoàn trả (sampling with replacement)

## Khái niệm

- Rút token từ túi → ghi lại → **trả lại** token → rút tiếp
- 4 token (đỏ, vàng, xanh lá, xanh dương), rút 4 lần: có thể ra xanh dương 2 lần, không có đỏ
- **Without replacement**: luôn ra cùng 4 token → không đa dạng

## Áp dụng cho ML

- 10 mẫu huấn luyện → "bỏ vào túi" lý thuyết
- Rút có hoàn trả 10 lần → tập mới size 10:
  - Có mẫu **lặp lại**
  - Có thể **thiếu** mẫu gốc
- Tập mới tương tự nhưng khác đủ để huấn luyện cây khác nhau

## Vai trò

- Nền tảng xây **tree ensemble** (bagging, random forest)
