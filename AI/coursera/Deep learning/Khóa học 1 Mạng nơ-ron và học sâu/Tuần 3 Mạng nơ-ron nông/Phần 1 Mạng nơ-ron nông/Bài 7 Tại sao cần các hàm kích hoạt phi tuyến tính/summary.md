# Bài 7 — Tại sao cần hàm kích hoạt phi tuyến tính

## Câu hỏi cốt lõi

Nếu đặt **a = z** (hàm kích hoạt tuyến tính / identity), mạng nơ-ron còn ý nghĩa không?

## Chứng minh: linear activation → chỉ là hàm tuyến tính

Với a⁽¹⁾ = z⁽¹⁾ = W⁽¹⁾x + b⁽¹⁾ và a⁽²⁾ = z⁽²⁾ = W⁽²⁾a⁽¹⁾ + b⁽²⁾:

- a⁽²⁾ = W⁽²⁾(W⁽¹⁾x + b⁽¹⁾) + b⁽²⁾
- = **(W⁽²⁾W⁽¹⁾)x + (W⁽²⁾b⁽¹⁾ + b⁽²⁾)**
- = **W'x + b'** — vẫn chỉ là hàm **tuyến tính**!

## Hệ quả

| Tình huống | Kết quả |
|---|---|
| Hidden layer dùng hàm tuyến tính | **Vô dụng** — bỏ hidden layer đi |
| Nhiều layer nhưng đều tuyến tính | Vẫn chỉ tính **một hàm tuyến tính** |
| Hidden tuyến tính + output sigmoid | Không mạnh hơn logistic regression |

> **Tổ hợp hai hàm tuyến tính = một hàm tuyến tính**

## Ngoại lệ duy nhất: output layer cho regression

- Khi **y là số thực** (dự đoán giá nhà) → có thể dùng **linear activation** ở output
- Hidden layer **vẫn phải phi tuyến** (ReLU, tanh, ...)
- Giá nhà ≥ 0 → có thể dùng **ReLU** ở output thay vì linear

## Ý chính

- Hàm kích hoạt **phi tuyến** là **bắt buộc** để mạng học được hàm phức tạp
- Không có nó, thêm bao nhiêu layer cũng vô ích
