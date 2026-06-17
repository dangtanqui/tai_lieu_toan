## Các ví dụ (w, b) → đường f(x) → J

| w | b | Đường f(x) | J |
|---|---|------------|---|
| −0.15 | 800 | Dốc xuống, cắt y=800 | **Cao** — xa minimum |
| 0 | 360 | Ngang (flat line) | Trung bình — vẫn kém |
| (khác) | (khác) | Fit kém hơn ví dụ trước | **Cao hơn** — xa minimum hơn |
| ~tốt | ~tốt | Gần đi qua data | **Thấp** — gần tâm ellipse |

## Nguyên tắc
- Đường fit **kém** → J **cao** (xa đáy bowl)
- Đường fit **tốt** → J **thấp** (gần minimum)
- J = tổng squared error giữa data và đường thẳng

## Lab (optional)
- Code implement cost function
- **Contour plot tương tác:** click chọn (w,b) → xem đường + điểm trên 3D
- Xoay 3D surface plot bằng chuột

## Vấn đề
- **Không nên** tự đọc contour plot để chọn w,b thủ công
- Không scale được với model phức tạp

## Giải pháp → Gradient Descent
- Algorithm **tự động** tìm w, b minimize J
- Một trong những thuật toán **quan trọng nhất** ML
- Dùng cho linear regression và cả model AI lớn
