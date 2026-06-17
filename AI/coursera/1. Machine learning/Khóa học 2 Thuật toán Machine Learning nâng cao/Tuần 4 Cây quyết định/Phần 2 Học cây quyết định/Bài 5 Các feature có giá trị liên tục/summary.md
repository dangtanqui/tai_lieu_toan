# Bài 5 — Feature liên tục (continuous)

## Ví dụ: weight (cân nặng)

- Feature số thực: cân nặng (pound) — mèo thường nhẹ hơn chó nhưng có overlap
- Thuật toán xét weight cùng các feature khác; split nếu IG cao nhất

## Cách split feature liên tục

- Chọn **threshold** \(t\): weight ≤ \(t\) hay > \(t\)
- Thử nhiều giá trị \(t\) → chọn \(t\) cho **information gain** cao nhất

## Ví dụ tính IG

| Threshold | IG |
|-----------|-----|
| ≤ 8 lb | 0.24 |
| ≤ 9 lb | **0.61** |
| ≤ 13 lb | 0.40 |

- IG tại t=9 cao hơn mọi feature khác → split tại weight ≤ 9

## Chọn các threshold thử

- Sắp xếp mẫu theo giá trị feature
- Thử **midpoint** giữa các giá trị liên tiếp
- 10 mẫu → thử 9 threshold
- Sau split: xây subtree đệ quy trên hai subset

## Tóm tắt

- Mỗi node: thử nhiều threshold + tính IG như bình thường
- Chọn (feature, threshold) có IG cao nhất
