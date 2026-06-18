## Gradient Descent là gì?
- Algorithm **tự động** tìm w, b minimize J(w,b)
- Dùng **rộng rãi** ML — không chỉ linear regression mà cả neural network / deep learning
- Generalize: minimize J(w₁...wₙ, b) với nhiều tham số

## Ý tưởng (analogy đồi núi)
1. Khởi tạo w, b (thường = 0)
2. Nhìn xung quanh → bước theo hướng **dốc nhất xuống** (steepest descent)
3. Lặp lại → J giảm dần → đến **minimum**

## Local vs Global Minimum
- Một số hàm J có **nhiều đáy** (local minima)
- Điểm khởi tạo khác → có thể hội tụ đáy khác nhau
- Linear regression + squared error → **1 global minimum** (bowl shape) — sẽ học ở bài sau
