## Vector hóa Backward Propagation

## dZ — gradient theo z

\[
dZ = A - Y \quad \text{(shape } 1 \times m\text{)}
\]

- \(dz^{(i)} = a^{(i)} - y^{(i)}\) cho mọi i — **một dòng code**

## db và dw

\[
db = \frac{1}{m} \sum dz^{(i)} = \frac{1}{m}\,\text{np.sum}(dZ)
\]

\[
dW = \frac{1}{m}\, X \cdot dZ^T \quad \text{(shape } n_x \times 1\text{)}
\]

- Tương đương \(\frac{1}{m}\sum_i x^{(i)} \cdot dz^{(i)}\)

## Một iteration gradient descent hoàn chỉnh

```python
Z = np.dot(w.T, X) + b
A = sigmoid(Z)
dZ = A - Y
dW = (1/m) * np.dot(X, dZ.T)
db = (1/m) * np.sum(dZ)
w -= alpha * dW
b -= alpha * db
```

## Lưu ý

- **Không for-loop** qua m mẫu trong forward/backward
- Vẫn cần for-loop **ngoài cùng** cho nhiều iteration gradient descent (1000 lần…)
- Kết quả: implementation logistic regression **hiệu quả cao**
