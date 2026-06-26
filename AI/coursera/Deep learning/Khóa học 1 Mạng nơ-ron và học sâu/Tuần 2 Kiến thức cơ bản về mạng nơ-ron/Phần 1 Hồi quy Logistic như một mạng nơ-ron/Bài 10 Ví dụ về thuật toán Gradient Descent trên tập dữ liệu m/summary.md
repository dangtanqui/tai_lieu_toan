## Gradient Descent trên m mẫu

\[
J(w,b) = \frac{1}{m}\sum_{i=1}^{m} L(a^{(i)}, y^{(i)}), \quad a^{(i)} = \sigma(w^T x^{(i)} + b)
\]

- Đạo hàm cost = **trung bình** đạo hàm loss từng mẫu

## Thuật toán (pseudo-code)

1. Khởi tạo: J=0, dw₁=dw₂=db=0
2. **For** i = 1…m:
   - z⁽ⁱ⁾ = wᵀx⁽ⁱ⁾ + b; a⁽ⁱ⁾ = σ(z⁽ⁱ⁾)
   - Cộng dồn J, dz⁽ⁱ⁾ = a⁽ⁱ⁾ − y⁽ⁱ⁾
   - dwⱼ += xⱼ⁽ⁱ⁾·dz⁽ⁱ⁾; db += dz⁽ⁱ⁾
3. Chia dw, db, J cho **m**
4. Cập nhật: wⱼ −= α·dwⱼ; b −= α·db

## Ký hiệu code

| Biến | Ý nghĩa |
|---|---|
| dz⁽ⁱ⁾ | Gradient theo mẫu i |
| dw (không superscript) | Tổng tích lũy trên toàn tập |

## Hạn chế

- Cần **2 vòng for**: qua m mẫu + qua n features
- Trong deep learning, for-loop làm code **chậm** trên tập lớn
- Giải pháp tuần sau: **vectorization** — loại bỏ for-loop
