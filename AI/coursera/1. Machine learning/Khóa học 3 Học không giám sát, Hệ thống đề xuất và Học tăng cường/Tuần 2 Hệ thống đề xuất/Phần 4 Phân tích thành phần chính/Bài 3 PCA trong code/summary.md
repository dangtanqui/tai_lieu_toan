## Quy trình với scikit-learn

1. **Feature scaling** (nếu scale khác nhau nhiều)
2. `PCA(n_components=k).fit(X)` — tự **mean normalization**
3. `explained_variance_ratio_` — % variance mỗi trục giữ được
4. `transform(X)` — chiếu dữ liệu lên \(z_1, z_2, \ldots\)

## Ví dụ code

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)
print(pca.explained_variance_ratio_)  # [0.992] → giữ 99.2% variance
Z = pca.transform(X)
```

## Giải thích variance ratio

- 1 component: 99.2% variance → 1 số gần như đủ
- 2 components trên data 2D: `[0.992, 0.008]` — tổng = 1 (100%)
- Giảm 2D → 2D: không mất gì, reconstruction chính xác

## Ứng dụng PCA

| Ứng dụng | Mức độ dùng hiện nay |
|----------|---------------------|
| **Visualization** | ✅ Phổ biến nhất |
| Nén dữ liệu (50 → 10 feature) | Ít hơn (storage/network rẻ hơn) |
| Tăng tốc supervised learning | Hiếm (deep learning không cần) |

## Lời khuyên

- Dataset mới → PCA xuống 2–3 chiều → plot → hiểu cấu trúc
- Thử optional lab để thay đổi `n_components` và quan sát projection
