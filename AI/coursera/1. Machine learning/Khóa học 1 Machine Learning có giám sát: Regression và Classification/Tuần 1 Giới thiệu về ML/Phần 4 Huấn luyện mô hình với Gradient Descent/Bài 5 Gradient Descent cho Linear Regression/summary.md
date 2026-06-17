## Derivative cho Linear Regression
```
∂J/∂w = (1/m) · Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾) · x⁽ⁱ⁾
∂J/∂b = (1/m) · Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)
```
- f(x⁽ⁱ⁾) = wx⁽ⁱ⁾ + b
- Derive từ calculus (optional) — chia 2 trong J giúp công thức gọn

## Algorithm đầy đủ
```
repeat until convergence:
  w := w − α · ∂J/∂w
  b := b − α · ∂J/∂b   (simultaneous update)
```

## Convex function — lợi thế lớn
- Squared error + linear regression → J **bowl-shaped**, **convex**
- **Không có** nhiều local minima — chỉ **1 global minimum**
- α chọn đúng → gradient descent **luôn** hội tụ global minimum
