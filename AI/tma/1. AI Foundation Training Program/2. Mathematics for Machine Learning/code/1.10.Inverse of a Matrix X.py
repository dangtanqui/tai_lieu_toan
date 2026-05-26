'''
2x1 + x2 = 4
x1 + 3x2 = 5

Ax = B
x = inv(A)*B
'''
import numpy as np

# Ma trận hệ số
A = np.array([[2, 1],
              [1, 3]])

# Vector hằng số
b = np.array([4, 5])

# Giải hệ phương trình tuyến tính Ax = b
x = np.linalg.inv(A).dot(b)

print("Vector nghiệm x:", x)
