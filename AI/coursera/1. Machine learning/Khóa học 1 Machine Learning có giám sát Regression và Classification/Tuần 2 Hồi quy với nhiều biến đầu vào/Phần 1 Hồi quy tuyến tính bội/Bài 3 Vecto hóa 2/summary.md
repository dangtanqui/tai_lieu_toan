## Cơ chế vectorization
**For loop:** tính từng phần tử tuần tự (t₀, t₁, t₂...)

**Vectorized:** nhân/cộng **song song** toàn bộ vector cùng lúc

## Update parameters
```
# Không vectorize: 16 dòng hoặc for loop
w_j := w_j − α · d_j

# Vectorize:
w := w − α · d    # 1 dòng, parallel
```

## Khi nào quan trọng?
- 16 features → chênh ít
- Hàng nghìn features + dataset lớn → **phút vs giờ**

## NumPy
- Arrays, `np.dot()`, lab tự time so sánh tốc độ
