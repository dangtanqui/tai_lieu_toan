## Bài toán
- Dự đoán áo thun có **top seller** hay không (phân loại nhị phân)
- Đặc trưng: giá, phí ship, marketing, chất lượng vải

## Một nơ-ron
- = logistic regression: \(a = g(w \cdot x + b) = \frac{1}{1 + e^{-wx + b}}\)
- \(a\) = **activation** (mức kích hoạt)

## Mạng nhiều lớp
- 4 đặc trưng → 3 nơ-ron ẩn (affordability, awareness, perceived quality) → 1 đầu ra
- **Layer**: nhóm nơ-ron cùng nhận input tương tự
- **Input layer** → **hidden layer** → **output layer**
- Mỗi nơ-ron lớp sau kết nối **tất cả** đặc trưng lớp trước; mạng tự học trọng số

## Góc nhìn
- Mạng = logistic regression trên **đặc trưng tự học** (thay feature engineering thủ công)
- Không cần quyết định thủ công đặc trưng ẩn — mạng tự học từ dữ liệu

## Thuật ngữ
- **Multilayer perceptron**: mạng nhiều lớp ẩn
- **Architecture**: số lớp ẩn và số nơ-ron mỗi lớp
