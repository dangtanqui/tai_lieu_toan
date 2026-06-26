# Bài 6 — Hàm kích hoạt (Activation Functions)

## Vai trò

- Thay vì a = sigmoid(z), dùng **a = g(z)** với g là hàm kích hoạt tùy chọn
- Mỗi layer có thể dùng **hàm khác nhau**: g⁽¹⁾ ≠ g⁽²⁾

## So sánh các hàm kích hoạt

| Hàm | Công thức | Miền giá trị | Ghi chú |
|---|---|---|---|
| **Sigmoid** | 1/(1+e⁻ᶻ) | (0, 1) | Hầu như không dùng cho hidden |
| **Tanh** | (eᶻ−e⁻ᶻ)/(eᶻ+e⁻ᶻ) | (−1, 1) | Tốt hơn sigmoid cho hidden |
| **ReLU** | max(0, z) | [0, ∞) | **Mặc định** cho hidden layer |
| **Leaky ReLU** | max(0.01z, z) | (−∞, ∞) | Slope nhỏ khi z < 0 |

## Quy tắc chọn

- **Output (binary classification):** sigmoid — vì ŷ cần trong (0, 1)
- **Hidden layer:** ReLU (hoặc tanh) — **không dùng sigmoid**
- **Không chắc?** Dùng ReLU; thử nhiều hàm trên validation set

## Ưu/nhược điểm

| Hàm | Vấn đề |
|---|---|
| Sigmoid / Tanh | Gradient ≈ 0 khi z rất lớn/nhỏ → **chậm học** |
| ReLU | Gradient = 0 khi z < 0, nhưng đủ nhiều unit có z > 0 |
| ReLU / Leaky ReLU | Gradient ≠ 0 trên phần lớn miền z → **học nhanh hơn** |

## Tanh vs Sigmoid

- Tanh = sigmoid **dịch chuyển** — mean activation gần 0 hơn (≈ 0.5)
- Giúp layer tiếp theo học dễ hơn (tương tự chuẩn hóa dữ liệu)

## Lời khuyên thực tế

- Không có công thức chung — **thử nghiệm** trên tập validation
- Deep learning có nhiều lựa chọn thiết kế; kinh nghiệm quan trọng hơn quy tắc cứng
