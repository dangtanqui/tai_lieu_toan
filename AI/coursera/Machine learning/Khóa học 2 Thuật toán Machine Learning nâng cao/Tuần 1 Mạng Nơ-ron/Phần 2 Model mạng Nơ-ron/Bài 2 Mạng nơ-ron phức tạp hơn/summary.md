## Đếm layer
- "Mạng 4 layer" = 3 hidden + 1 output (không đếm input layer / layer 0)

## Công thức tổng quát
- \(a_j^{[l]} = g(w_j^{[l]} \cdot a^{[l-1]} + b_j^{[l]})\)
- \(a^{[l-1]}\) = output layer trước; \(g\) = **activation function** (hiện tại: sigmoid)

## Activation function
- \(g\) còn gọi là activation function vì nó sinh ra giá trị **activation**
- Tuần sau: các hàm khác ngoài sigmoid

## Ký hiệu thống nhất
- Input vector \(x\) cũng gọi là \(a^{[0]}\)
- Có thể tính activation bất kỳ layer nào từ layer trước
