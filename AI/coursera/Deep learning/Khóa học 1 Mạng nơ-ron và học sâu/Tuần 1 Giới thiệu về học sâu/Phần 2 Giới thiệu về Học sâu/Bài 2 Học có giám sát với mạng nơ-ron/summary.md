## Học có giám sát (Supervised Learning)

- Hầu hết **giá trị kinh tế** từ mạng nơ-ron đến từ **supervised learning**
- Có input **x** → học hàm ánh xạ tới output **y**
- Ví dụ: feature nhà → giá nhà

## Ứng dụng tiêu biểu

| Ứng dụng | Input x | Output y |
|----------|---------|----------|
| **Quảng cáo trực tuyến** | Thông tin ad + user | Có click không? (lucrative nhất) |
| **Computer vision** | Ảnh | Nhãn 1–1000 (photo tagging) |
| **Nhận dạng giọng nói** | Audio | Bản ghi text |
| **Dịch máy** | Câu tiếng Anh | Câu tiếng Trung |
| **Xe tự lái** | Ảnh + radar | Vị trí xe khác trên đường |

- Thành công = **chọn đúng x và y** cho bài toán, gắn vào hệ thống lớn hơn (xe tự lái)

## Kiến trúc mạng theo loại dữ liệu

| Loại dữ liệu | Kiến trúc | Viết tắt |
|--------------|-----------|----------|
| Bất động sản, quảng cáo | Standard NN | — |
| Ảnh | Convolutional NN | **CNN** |
| Audio, ngôn ngữ (chuỗi thời gian) | Recurrent NN | **RNN** |
| Xe tự lái (ảnh + radar) | **Hybrid** / custom | — |

- **Sequence data**: audio = chuỗi 1D theo thời gian; ngôn ngữ = từng từ/từng ký tự
- RNN phiên bản phức tạp hơn cho NLP, dịch máy

## Structured vs Unstructured Data

| | **Structured** | **Unstructured** |
|---|----------------|------------------|
| Định nghĩa | Database, cột có ý nghĩa rõ | Audio, ảnh, text thô |
| Ví dụ | Diện tích nhà, tuổi user, thông tin ad | Pixel ảnh, từng từ trong văn bản |
| Lịch sử | Máy tính xử lý tốt từ trước | Rất khó — con người giỏi hơn |

- Deep learning giúp máy tính **hiểu unstructured data** tốt hơn nhiều so vài năm trước
- Media hay đưa tin thành công trên unstructured (nhận diện mèo) vì dễ cảm nhận
- Nhưng **giá trị kinh tế ngắn hạn** cũng lớn trên structured: quảng cáo, gợi ý lợi nhuận, phân tích database

## Ghi chú khóa học

- Kỹ thuật trong khóa áp dụng cho **cả hai** loại dữ liệu
- Ví dụ giải thuật thiên về unstructured; ứng dụng thực tế nên cân nhắc cả hai

## Ý tưởng then chốt

- Mạng nơ-ron đã **biến đổi supervised learning**, tạo giá trị kinh tế khổng lồ
- Ý tưởng kỹ thuật đã có **hàng thập kỷ** — tại sao mới bùng nổ gần đây? → bài tiếp theo
