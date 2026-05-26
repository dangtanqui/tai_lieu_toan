import numpy as np

# Ma trận hệ số
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])


print(np.linalg.inv(A))
