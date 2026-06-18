## target
- **Minimize J(w,b)** — tìm w, b sao cho J nhỏ nhất
- J đo tổng squared error → J nhỏ = model fit tốt

## Ví dụ đơn giản (b = 0)
- Model: **f_w(x) = w·x** (chỉ 1 tham số w)
- Data: (1,1), (2,2), (3,3)

| w | Đường thẳng | J(w) | Ý nghĩa |
|---|-------------|------|---------|
| **1** | Slope 1, đi qua mọi điểm | **0** | Fit hoàn hảo |
| 0.5 | Slope nhỏ hơn | ~0.58 | Lệch khỏi data |
| 0 | Nằm trên trục x | ~2.33 | Sai nhiều |
| −0.5 | Dốc xuống | ~5.25 | Sai càng nhiều |

## Hai đồ thị liên hệ
- **Trái:** f_w(x) — trục x vs y (đường thẳng thay đổi theo w)
- **Phải:** J(w) — trục w vs J (mỗi w → 1 điểm trên đồ thị cost)
- Thay đổi w → đường khác → J khác

## Cách chọn w tốt
- Chọn w làm **J(w) nhỏ nhất** → w = 1 (line fit data tốt nhất)
- Trường hợp đầy đủ: minimize **J(w,b)** với cả w và b

## Tóm tắt
> Đường càng gần data → J càng nhỏ → linear regression = tìm w (và b) minimize J
