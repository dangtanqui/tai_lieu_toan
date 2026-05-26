import numpy as np

# Dữ liệu mô phỏng: diện tích, số phòng ngủ và giá nhà
# Đặc trưng thứ 2 là gấp đôi của đặc trưng thứ nhất và không cần thiết
#X = np.array([[100, 2], [250, 4], [300, 8], [500, 12], [800, 10]])  # Diện tích (m2) và số phòng ngủ
X = np.array([[100, 2, 2], [250, 4, 4], [300, 8, 8], [500, 12, 12], [800, 10, 10]])  # Diện tích (m2) và số phòng ngủ và số phòng tắm
y = np.array([300, 500, 700, 900, 1100])  # Giá nhà (triệu đồng)

corr_matrix = np.corrcoef(X, rowvar=False)
print("Ma trận tương quan:\n", corr_matrix)

det_corr = np.linalg.det(corr_matrix)

# Kiểm tra định thức để xác định có dữ liệu dư thừa không
if det_corr != 0:
    print("Định thức của ma trận X.T.dot(X) khác 0, không có dữ liệu dư thừa.")
else:
    print("Định thức của ma trận X.T.dot(X) bằng 0, có dữ liệu dư thừa.")

