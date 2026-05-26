import numpy as np

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        det_value = 0
        A_firstrow_deleted = np.delete(A, 0, axis=0)
        for i in range(n):
            a_1i = np.delete(A_firstrow_deleted, i, axis=1)
            det_value += (-1)**i * A[0][i] * det(a_1i)
        return det_value
    

# Dữ liệu
A = np.array([[1, 2, 156, 3],
              [2, 0, 35, 1], 
              [0, 41, 1, 5], 
              [25, 1, 3, 2]
              ]) 

x = np.linalg.det(A)
'''
A_firstrow_deleted = np.delete(A, 0, axis=0)
A11 = np.delete(A_firstrow_deleted, 0, axis=1)
A12 = np.delete(A_firstrow_deleted, 1, axis=1)
A13 = np.delete(A_firstrow_deleted, 2, axis=1)
A14 = np.delete(A_firstrow_deleted, 3, axis=1)

det = A[0][0]*np.linalg.det(A11) - A[0][1]*np.linalg.det(A12) + A[0][2]*np.linalg.det(A13) - A[0][3]*np.linalg.det(A14)
'''

print(x)
print(det(A))