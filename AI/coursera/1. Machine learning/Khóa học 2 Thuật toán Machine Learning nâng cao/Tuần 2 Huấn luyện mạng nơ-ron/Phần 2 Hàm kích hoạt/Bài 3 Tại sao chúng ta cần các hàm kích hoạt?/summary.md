## Vấn đề khi dùng linear ở mọi lớp

- Mạng nhiều lớp với **linear activation** ở tất cả nơ-ron = chỉ là **linear regression**
- Hàm tuyến tính của hàm tuyến tính vẫn là hàm tuyến tính → nhiều lớp không thêm sức mạnh

## Ví dụ 2 lớp

- \(a_1 = w_1 x + b_1\), \(a_2 = w_2 a_1 + b_2 = w_2 w_1 x + w_2 b_1 + b_2\)
- Gộp lại: \(a_2 = wx + b\) — tương đương một mô hình tuyến tính

## Trường hợp lớp ẩn linear + đầu ra sigmoid

- Mô hình tương đương **logistic regression** — mạng lớn không giúp gì thêm

## Quy tắc

- **Không** dùng linear ở lớp ẩn
- Dùng **ReLU** (hoặc sigmoid/softmax ở lớp đầu ra tùy bài toán) để mạng học được quan hệ phi tuyến
