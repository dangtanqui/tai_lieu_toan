import numpy as np
x = np.array([1, 5, 3,  2,5])
y = np.array([3, 2, 1, 2, 6])
print("x + 5: ", x + 5)
print("x - 5: ", x - 5)
print("x * 5: ", x * 5)

print(x, '+', y, '=', x+y)
print(x, '-', y, '=', x-y)
print(x, '*', y, '=', x*y)
print(x, '/', y, '=', x/y)

print("Tích vô hướng của hai vector:", np.dot(x, y))
print("Tích vô hướng của hai vector:", x@y)

print("Tích Hadamard của hai vector:",  np.multiply(x, y))
print("Tích Hadamard của hai vector:",  x*y)
print("chuẩn Norm của vector:", np.linalg.norm(x))
norm = lambda x: np.sqrt(np.sum(np.square(x)))
print("chuẩn Norm của vector:", norm(x))

