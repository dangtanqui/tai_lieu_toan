#sử dụng phép nhân element-wise trong quá trình tính toán các lớp ẩn của mạng nơ-ron. 
import numpy as np

# Hàm kích hoạt ReLU
def relu(x):
    return np.maximum(0, x)

# Dữ liệu đầu vào (10 mẫu, mỗi mẫu có 5 đặc trưng)
np.random.seed(0)
X = np.random.rand(10, 5)
print('x=', X)
# Trọng số và bias cho lớp ẩn đầu tiên (5 đặc trưng đầu vào, 5 nơ-ron)
W1 = np.random.rand(5, 5)
b1 = np.random.rand(5)
print('w1=', W1)
print('b1=', b1)
# Tính toán cho lớp ẩn đầu tiên
Z1 = np.dot(X, W1) + b1  # Sử dụng phép nhân ma trận chuẩn và cộng với bias
A1 = relu(Z1)            # Áp dụng hàm kích hoạt ReLU
print('A1=', A1)
# Phép nhân element-wise (ví dụ nhân thêm một mảng hệ số)
elementwise_multiplier = np.random.rand(5)
print('elementwise_multiplier:', elementwise_multiplier)


A1_elementwise = A1 * elementwise_multiplier  # Phép nhân element-wise

print('A1_elementwise')
print(A1_elementwise)

print('A1_elementwise')
A1_elementwise = np.multiply(A1, elementwise_multiplier)  # Phép nhân element-wise
print(A1_elementwise)

# Trọng số và bias cho lớp đầu ra (5 nơ-ron đầu vào, 1 nơ-ron đầu ra)
W2 = np.random.rand(5, 1)
b2 = np.random.rand(1)

# Tính toán cho lớp đầu ra
Z2 = np.dot(A1_elementwise, W2) + b2  # Sử dụng phép nhân ma trận chuẩn và cộng với bias
output = Z2  # Đầu ra cuối cùng

print("Đầu ra của mô hình:", output)


A = np.array([[1, 2, 3], 
              [3, 8, 5]])
x = np.array([2, 3, 4])

print(np.dot(x,x.T))
print(np.dot(x.T,x))

