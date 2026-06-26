# Bài 8 — Điều này có liên quan gì đến não bộ?

## Kết luận ngắn gọn

> Deep learning và não bộ: **không liên quan nhiều** — dù analogy vẫn phổ biến trong media

## Tại sao analogy tồn tại?

- Forward/backprop khó trực quan → "giống não" là cách giải thích **đơn giản, hấp dẫn**
- Có tương đồng **rất lỏng lẻo** giữa logistic unit (sigmoid) và neuron sinh học

## Neuron sinh học vs artificial neuron

| Artificial | Sinh học |
|------------|----------|
| Tổng có trọng số + activation | Nhận tín hiệu điện từ neuron khác |
| Output số | "Bắn" xung điện qua axon nếu vượt ngưỡng |

**Nhưng:**
- Neuroscientist gần như **không hiểu** một neuron đơn lẻ làm gì
- Neuron thật **phức tạp hơn nhiều** so với logistic regression
- Cách não **học** vẫn là bí ẩn — không rõ có dùng backprop/gradient descent không

## Quan điểm của Andrew Ng

- Deep learning = học mapping \(X \to Y\) linh hoạt trong **supervised learning**
- Analogy não bộ **đang mất dần giá trị** — ít dùng hơn trước
- Computer vision có thể chịu ảnh hưởng từ não nhiều hơn các lĩnh vực khác

## Kết thúc tuần 4

- Đã biết implement forward prop, backprop, gradient descent cho mạng sâu
- Chúc may mắn với **programming exercise**!
