## Phân loại đa nhãn (multi-label) vs đa lớp (multi-class)

- **Đa lớp**: mỗi ảnh thuộc **một** lớp (chữ số 0–9)
- **Đa nhãn**: mỗi ảnh có thể có **nhiều nhãn** cùng lúc

## Ví dụ: xe tự lái

- Hỏi đồng thời: có xe? có xe buýt? có người đi bộ?
- y = vector 3 số (có/không cho từng loại)

## Hai cách xây mô hình

1. **Ba mạng riêng** — mỗi mạng phân loại nhị phân một nhãn (hợp lý)
2. **Một mạng, 3 đầu ra** — lớp cuối 3 nơ-ron, mỗi nơ-ron dùng **sigmoid** (3 bài toán nhị phân song song)

## Phân biệt

- Đa lớp → softmax (xác suất cộng = 1)
- Đa nhãn → sigmoid từng đầu ra (độc lập, không cần cộng = 1)
