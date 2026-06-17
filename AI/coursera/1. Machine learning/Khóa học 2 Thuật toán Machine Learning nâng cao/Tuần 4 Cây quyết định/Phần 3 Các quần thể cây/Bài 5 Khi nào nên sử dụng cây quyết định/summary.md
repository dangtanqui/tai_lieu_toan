# Bài 5 — Khi nào dùng cây quyết định vs neural network

## Decision tree / tree ensemble

### Phù hợp

- **Tabular / structured data** (dạng bảng spreadsheet)
- Ví dụ: giá nhà — size, bedrooms, floors, age
- Classification lẫn regression trên dữ liệu có cấu trúc

### Ưu điểm

- **Huấn luyện nhanh** → vòng lặp phát triển ML nhanh hơn
- Cây nhỏ (vài chục node) → **interpretable**, in ra xem logic quyết định
- Ensemble lớn (100 cây × hàng trăm node) → khó đọc trực tiếp

### Khuyến nghị

- Dùng **XGBoost** cho hầu hết ứng dụng tabular
- Chỉ dùng một cây đơn khi ngân sách tính toán rất hạn chế

### Không nên

- **Unstructured data**: ảnh, video, audio, text

## Neural network

### Phù hợp

- Mọi loại dữ liệu: tabular, unstructured, mixed
- Unstructured → **neural network** là lựa chọn ưu tiên

### Ưu điểm

- **Transfer learning** / pre-training quan trọng khi dataset nhỏ
- Ghép nhiều model: train end-to-end bằng **gradient descent**

### Nhược điểm

- Huấn luyện chậm hơn decision tree
- Decision tree chỉ train **từng cây một**, khó nối nhiều cây thành hệ thống lớn

## Tóm tắt

| | Decision tree / ensemble | Neural network |
|--|------------------------|----------------|
| Tabular data | Rất tốt | Cạnh tranh |
| Unstructured | Không khuyến nghị | Ưu tiên |
| Tốc độ train | Nhanh | Chậm hơn |
| Interpretability | Cao (cây nhỏ) | Thấp hơn |

## Kết khóa học

- Đã học neural network + decision tree + tips thực tế
- Khóa 3: **unsupervised learning** (không cần nhãn Y)
