# Bài 1 — Model cây quyết định

## Giới thiệu tuần 4

- **Decision tree** và **tree ensemble**: thuật toán mạnh, dùng rộng rãi, thường thắng ML competition
- Ít được nhắc trong học thuật nhưng rất đáng có trong toolbox

## Ví dụ: phân loại mèo

- Trung tâm nhận nuôi mèo: dự đoán con vật có phải mèo không
- 10 mẫu huấn luyện: 5 mèo, 5 chó
- **Feature** X (categorical, nhị phân):
  - Ear shape: pointy / floppy
  - Face shape: round / not round
  - Whiskers: present / absent
- Nhãn Y: cat (1) hay not cat (0) — bài toán **binary classification**

## Cấu trúc decision tree

- Mô hình sau huấn luyện có dạng cây (định nghĩa CS: root ở trên, leaf ở dưới)
- **Root node**: nút gốc, bắt đầu inference
- **Decision node**: xét một feature → đi trái hoặc phải
- **Leaf node**: dự đoán nhãn cuối cùng
- Ví dụ inference: pointy ears → round face → dự đoán **cat**

## Nhiều cây khác nhau

- Cùng dataset có thể cho nhiều decision tree khác nhau
- Thuật toán học chọn cây làm tốt trên training set và **generalize** tốt trên CV/test
