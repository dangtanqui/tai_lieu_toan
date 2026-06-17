## Loss gộp 1 công thức
```
L = −y·log(f) − (1−y)·log(1−f)
```
- y = 1 → chỉ còn −log(f)
- y = 0 → chỉ còn −log(1−f)
- Tương đương công thức 2 nhánh trước đó

## Cost function chuẩn
```
J = −(1/m) · Σ [y⁽ⁱ⁾·log(f⁽ⁱ⁾) + (1−y⁽ⁱ⁾)·log(1−f⁽ⁱ⁾)]
```
- Công thức **mọi người dùng** để train logistic regression

## Nguồn gốc
- Từ **maximum likelihood estimation** (thống kê)
- Không cần học chi tiết — chỉ biết: **lồi**, implement được

## Lab
- Ranh giới fit tốt → **cost thấp hơn**
