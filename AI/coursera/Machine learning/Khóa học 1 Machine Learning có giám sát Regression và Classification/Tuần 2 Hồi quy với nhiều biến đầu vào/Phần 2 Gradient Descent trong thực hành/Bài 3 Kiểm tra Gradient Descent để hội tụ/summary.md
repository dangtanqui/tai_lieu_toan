## Learning Curve
- Plot **J vs số iteration** (không phải vs w/b)
- Mỗi điểm = J sau N lần update

## GD chạy tốt khi
- J **giảm** mỗi iteration
- J **flatten** → đã converge
- Số iteration cần: **không đoán trước được** (30 đến 100k)

## Dấu hiệu lỗi
- J **tăng** → α quá lớn hoặc bug code

## Auto convergence test
- Nếu J giảm < ε (vd: 0.001) / iteration → dừng
- Thực tế: **xem graph** đáng tin hơn
