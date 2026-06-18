## Phân phối Gaussian (Normal)

- **Gaussian** = **Normal** = **bell curve** — cùng một khái niệm
- Tham số: **μ** (mean), **σ²** (variance); **σ** = độ lệch chuẩn

## Công thức p(x)

```
p(x) = (1 / (√(2π) · σ)) · exp(−(x−μ)² / (2σ²))
```

- Diện tích dưới đường cong = 1
- σ nhỏ → đường cong **cao, hẹp**; σ lớn → **thấp, rộng**
- Đổi μ → dịch trái/phải; đổi σ → thay đổi độ rộng

## Ước lượng từ dữ liệu

```
μ = (1/m) Σ x⁽ⁱ⁾
σ² = (1/m) Σ (x⁽ⁱ⁾ − μ)²
```

- Gọi là **maximum likelihood estimate**
- Dùng 1/m (không phải 1/(m−1)) — khác biệt nhỏ trong thực tế

## Liên hệ anomaly detection

- x gần μ → **p(x) cao** (bình thường)
- x xa μ → **p(x) thấp** (bất thường)
- Bài tiếp: mở rộng sang **nhiều feature**
