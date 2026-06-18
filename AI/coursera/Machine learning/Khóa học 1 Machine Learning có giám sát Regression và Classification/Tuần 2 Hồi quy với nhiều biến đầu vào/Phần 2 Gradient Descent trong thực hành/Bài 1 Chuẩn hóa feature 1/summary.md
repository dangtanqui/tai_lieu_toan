## Feature Scaling — vì sao cần?
- Features khác **scale** → w tương ứng khác độ lớn
- x₁: 300–2000 sq ft · x₂: 0–5 phòng
- w₁ nhỏ (0.1) · w₂ lớn (50) → contour **dẹt, dài** → GD **bounce** chậm

## Giải pháp
- Scale features về **cùng range** (vd: 0–1)
- Contour gần **tròn** → GD đi thẳng tới minimum

## Quy tắc
- Feature range lớn → thường cần w nhỏ
- Feature range nhỏ → thường cần w lớn
