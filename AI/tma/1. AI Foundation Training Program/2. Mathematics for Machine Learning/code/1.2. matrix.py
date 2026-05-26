#https://codelearn.io/sharing/ma-tran-nang-cao-voi-numpy
import numpy as np
print('#1. ma tran chuyen vi')
A = np.array([[1, 2, 3], 
              [3, 2, 1]])

AT = A.T
#[[1 3]
# [2 2]
# [3 1]]
#print(AT)
'''
x1 = np.dot(AT,A)
x2 = np.dot(A, AT)
print('AT*A =')
print(x1)

print('A*AT =')
print(x2)'''

print(A.T)

print('2. kich thuoc ma tran')
print(A.shape) # (2,3)

A = np.array([[1, 2, 3], 
              [3, 2, 1]])

B = np.array([[2, 1, 2], 
             [1, 3, 0]])

print('3. cong 2 ma tran')
#[[3 3 5]
# [4 5 1]]
print(A+B)

print('4. hieu 2 ma tran')
#[[-1  1  1]
# [ 2 -1  1]]
print(A-B)


print('5. Phép nhân ma trận điểm (element-wise or Hadamard product) dùng toán tử *')
print(A*B)

print('5. Phép nhân ma trận điểm (element-wise or Hadamard product) dung numpy')
print(np.multiply(A,B))

# (1*2 2*1 3*2)   (2 2 6)
# (3*1 2*3 1*0)   (3 6 0)

A = np.array([[1, 2, 3], 
              [3, 2, 1]])
B = np.array([[2, 1], 
              [1, 3],
              [1, 1]])

print('6.Phép nhân ma trận chuẩn (matrix multiplication) dùng toán tử @')
#print(2*A@B)       
#print(A@(2*B))       
print(A@B)

print('6.Phép nhân ma trận chuẩn (matrix multiplication) dùng numpy')
print(np.dot(A,B))

#(1*2+2*1+3*1  1*1+2*3+3*1)   (7 10)
#(3*2+2*1+1*1  3*1+2*3+1*1)   (9 10 )
#https://vi.wikipedia.org/wiki/Ph%C3%A9p_nh%C3%A2n_ma_tr%E1%BA%ADn




print('7. Hạng ma trân')
C = np.array([[1, 3, 0, -1, 0],
             [-1, 0, 1, 1, -1],
             [0, -3, 1, 0, -1],
             [2, 3, -1, -2, 1]]
             )
print(np.linalg.matrix_rank(A))


print('8. Dinh thuc ma tran')
A = np.array([[1, 2, 3], 
              [0, 1, 4],
              [5, 6, 0]])

print(np.linalg.det(A))

print('9. ma tran nghich dao')
A_inv = np.linalg.inv(A)
print(A_inv)

print('10. Chuyển từ mảng một chiều thành ma trận hai chiều')
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(A.reshape(3, 3))

print('11. Chuyển từ ma trận hai chiều về mảng một chiều')
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A.reshape(-1))

print('12. Thay đổi số hàng, số cột của ma trận')
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(A.reshape(3, 4))


print('13. Vết của ma trận, được định nghĩa bằng tổng các phần tử trên đường chéo chính của ma trận đó. ')
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# trace
print(np.trace(A))
print(A.trace())



