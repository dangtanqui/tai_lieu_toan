## Thuật toán K-means

**Bước 0:** Khởi tạo ngẫu nhiên K centroid μ₁, ..., μ_K (cùng chiều với x)

**Bước 1 — Gán cụm:** Với mỗi x⁽ⁱ⁾, đặt c⁽ⁱ⁾ = argmin_k ||x⁽ⁱ⁾ − μ_k||²

**Bước 2 — Cập nhật centroid:**

```
μ_k = (1/|S_k|) * Σ x⁽ⁱ⁾   với i ∈ S_k (các điểm thuộc cụm k)
```

Lặp bước 1–2 đến khi hội tụ.

## Góc cạnh

- Cụm **không có điểm nào** → thường **loại bỏ** cụm đó (còn K−1 cụm)
- Hoặc khởi tạo lại ngẫu nhiên nếu bắt buộc giữ K cụm

## Dữ liệu không tách rời rõ

- K-means vẫn hữu ích khi cụm **chồng lấn** (ví dụ: size áo S/M/L theo chiều cao–cân nặng)
- Centroid cho biết đại diện điển hình cho từng size

## Liên hệ

- K-means thực chất đang **tối ưu một hàm cost** (xem bài tiếp theo)
