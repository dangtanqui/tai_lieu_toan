## Môi trường ngẫu nhiên (stochastic MDP)

- Hành động không luôn đưa đến state mong muốn (trượt, gió, địa hình)
- Ví dụ: lệnh **trái** → 90% sang state 3, 10% sang state 5 (và ngược lại với **phải**)

## Return ngẫu nhiên → Expected return

- Không tối đa hóa return **một lần chạy** mà tối đa hóa **giá trị kỳ vọng** (trung bình nhiều lần thử)

\[
\mathbb{E}\left[R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots\right]
\]

- target: chọn π để tối đa **expected return**

## Bellman cho MDP ngẫu nhiên

\[
Q(S,A) = R(S) + \gamma \cdot \mathbb{E}_{S'}\left[\max_{A'} Q(S', A')\right]
\]

- **S'** ngẫu nhiên → thêm toán tử **kỳ vọng** E

## Lab: misstep probability

- Tham số **misstep** = xác suất đi ngược hướng lệnh
- misstep = 0.1 → Q và return giảm nhẹ
- misstep = 0.4 → kiểm soát kém hơn → Q thấp hơn nhiều

## Tổng kết

- Stochastic MDP: target và Bellman chỉ khác ở **kỳ vọng** trên S'
- Tiếp theo: **không gian trạng thái liên tục**
