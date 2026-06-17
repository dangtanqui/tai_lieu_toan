## Lớp Dense (đã học)

- Mỗi nơ-ron nhận **tất cả** kích hoạt từ lớp trước

## Lớp Convolutional (tích chập)

- Mỗi nơ-ron chỉ nhìn **một vùng cục bộ** của đầu vào (không phải toàn bộ pixel)
- Ví dụ ảnh: nơ-ron 1 xem vùng góc trên-trái; nơ-ron 2 xem vùng khác, v.v.
- **CNN** (convolutional neural network) = mạng gồm nhiều lớp tích chập

## Lợi ích

- Tính toán nhanh hơn
- Cần ít dữ liệu huấn luyện hơn / ít overfitting hơn

## Ví dụ EKG (tín hiệu tim)

- 100 điểm thời gian; nơ-ron lớp 1 chỉ xem cửa sổ 20 điểm liên tiếp
- Lớp 2 tiếp tục dùng cửa sổ cục bộ trên kích hoạt lớp 1
- Lớp đầu ra sigmoid: có/không bệnh tim

## Ghi chú

- Không bắt buộc cho bài tập khóa học này
- Nghiên cứu hiện đại (Transformer, LSTM, attention) = phát minh thêm loại lớp mới
