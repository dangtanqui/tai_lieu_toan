## Hàm `dense(a_in, W, b)`
- Input: activation layer trước + tham số layer hiện tại
- Stack \(w_1, w_2, \ldots\) thành **ma trận W** (cột = trọng số mỗi nơ-ron)
- Stack \(b_1, b_2, \ldots\) thành vector **b**
- For loop: \(z_j = w_j \cdot a_{in} + b_j\); \(a_j = g(z_j)\)

## Forward prop tổng quát
- \(a^{[1]} = \text{dense}(x, W_1, b_1)\)
- \(a^{[2]} = \text{dense}(a^{[1]}, W_2, b_2)\)
- … → \(f(x) = a^{[L]}\)

## Ký hiệu
- **W** viết hoa = ma trận; **w** viết thường = vector/scalar

## Tại sao quan trọng?
- Hiểu under the hood giúp debug khi TensorFlow chạy chậm, sai kết quả, hoặc lỗi
