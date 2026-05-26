import numpy as np

A = np.array([[1, 2, 3], 
              [3, 7, 8],
              [3, 2, 1]])

B = np.array([[4, 3, 4], 
              [5, 6, 3],
              [1, 2, 5]])



print('1. (A+B)^T = A^T + B^T')
print((A+B).T)
print(A.T + B.T)

print('2.(AB)^T = B^TA^T')
print(np.dot(A,B).T)
print(np.dot(B.T, A.T))



