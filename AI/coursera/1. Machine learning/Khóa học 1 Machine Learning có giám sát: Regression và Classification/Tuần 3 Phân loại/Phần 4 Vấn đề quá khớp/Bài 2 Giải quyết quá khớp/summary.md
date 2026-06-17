## 3 cách giảm overfitting

**1. Thu thập thêm dữ liệu**
- Công cụ **hiệu quả nhất**
- Không lúc nào cũng có thêm data

**2. Giảm số feature (feature selection)**
- Bỏ bớt đa thức bậc cao hoặc chọn feature quan trọng (diện tích, phòng ngủ, tuổi...)
- Nhược điểm: **mất thông tin**
- Course 2: thuật toán chọn feature tự động

**3. Regularization (chuẩn hóa)**
- **Không xóa** feature — chỉ **thu nhỏ** wⱼ (không ép = 0)
- w nhỏ → đường cong **ít lượn** → ít overfit
- Thường chỉ regularize **w**, không regularize **b**

## Trực giác
- Overfit: wⱼ thường **rất lớn**
- Gán w = 0 ≡ bỏ feature; regularization = giảm nhẹ hơn
