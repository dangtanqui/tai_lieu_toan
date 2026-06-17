## J(w,b) với 2 tham số
- Trở lại model đầy đủ: **f(x) = wx + b**
- Mục tiêu: **minimize J(w,b)**

## 3D Surface Plot
- 1 tham số w → J(w) dạng **chữ U** (2D)
- 2 tham số w, b → J(w,b) dạng **bowl / soup bowl** (3D)
- Mỗi điểm trên surface = 1 cặp (w, b) → 1 giá trị J

## Contour Plot (đồ thị đường đồng mức)
- Cắt ngang surface 3D → các **ellipse/oval**
- Mỗi ellipse = các điểm (w,b) có **cùng J**
- Giống bản đồ địa hình (topographical map)
- Nhìn từ trên xuống → thấy **đáy bowl** = J nhỏ nhất (tâm ellipse nhỏ nhất)
- Tiện visualize J 3D trên mặt phẳng 2D

## Liên hệ
- Cùng (w,b) → 1 đường f(x) bên trái + 1 điểm trên J bên phải
- (w,b) xấu → đường fit kém → J cao (xa tâm)
- (w,b) tốt → đường fit tốt → J thấp (gần tâm)
