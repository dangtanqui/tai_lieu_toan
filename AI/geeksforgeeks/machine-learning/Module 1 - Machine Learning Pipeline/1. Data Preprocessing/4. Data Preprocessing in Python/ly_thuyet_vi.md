Data preprocessing là bước đầu tiên trong mọi phân tích dữ liệu hoặc machine learning pipeline. Nó liên quan đến việc làm sạch, chuyển đổi và tổ chức dữ liệu thô để đảm bảo dữ liệu chính xác, nhất quán và sẵn sàng cho model hóa. Nó có ảnh hưởng lớn đến việc xây dựng model như:

* Dữ liệu rõ ràng và có cấu trúc tốt cho phép models tìm hiểu các mẫu có ý nghĩa thay vì nhiễu.
* Dữ liệu được xử lý đúng cách sẽ ngăn chặn thông tin đầu vào sai lệch, dẫn đến predictions đáng tin cậy hơn.
* Dữ liệu được sắp xếp giúp việc tạo đầu vào hữu ích cho model trở nên đơn giản hơn, nâng cao hiệu suất của model.
* Dữ liệu có tổ chức hỗ trợ Phân tích dữ liệu khám phá (EDA) tốt hơn, làm cho các model và xu hướng trở nên dễ hiểu hơn.

![data_cleaning](https://media.geeksforgeeks.org/wp-content/uploads/20251212113640777958/data_cleaning.webp "Click to enlarge")

Triển khai từng bước
----------------------------

Hãy triển khai nhiều quá trình tiền xử lý features khác nhau,

### Bước 1: Nhập thư viện và tải Dataset

Chúng ta chuẩn bị môi trường với các thư viện như [Pandas](https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/), [Numpy](https://www.geeksforgeeks.org/numpy/python-numpy/), [Học hỏi](https://www.geeksforgeeks.org/machine-learning/learning-model-building-scikit-learn-python-machine-learning-library/), [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) và [Sinh ra ở biển](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) để thao tác dữ liệu, các phép toán số, trực quan hóa và scaling. Tải dataset để xử lý trước.

> Có thể tải xuống mẫu dataset từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20250115110111213229/diabetes.csv).

```python
import pandas as pd
import numpy as np from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Geeksforgeeks/Data/diabetes.csv')
df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-132400](https://media.geeksforgeeks.org/wp-content/uploads/20250829133434412896/Screenshot-2025-08-29-132400.webp "Click to enlarge")

### Bước 2: Kiểm tra cấu trúc dữ liệu và kiểm tra Missing Values

Chúng ta hiểu kích thước, loại dữ liệu của dataset và xác định mọi dữ liệu không đầy đủ (thiếu) cần xử lý.

* ****df.info():**** In bản tóm tắt ngắn gọn bao gồm số lượng mục nhập không rỗng và kiểu dữ liệu của mỗi cột.
* ****df.isnull().sum():**** Trả về số missing values trên mỗi cột.

```python
df.info()
print(df.isnull().sum())
```

****Đầu ra:****

![Screenshot-2025-08-29-132349.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133538216025/Screenshot-2025-08-29-132349.webp)

![Screenshot-2025-08-29-132333.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133538354485/Screenshot-2025-08-29-132333.webp)

### Bước 3: Tóm tắt thống kê và trực quan hóa Outliers

Nhận các bản tóm tắt bằng số như giá trị trung bình, trung vị, tối thiểu/tối đa và phát hiện các điểm bất thường (outliers). Outliers có thể làm lệch models nếu không được xử lý.

* ****df.describe():**** Tính toán số lượng, giá trị trung bình, độ lệch tiêu chuẩn, tối thiểu/tối đa và tứ phân vị cho các cột số.
* ****Boxplots:**** Trực quan hóa mức lan truyền và phát hiện outliers bằng cách sử dụng boxplot() của matplotlib.

```python
df.describe()
fig, axs = plt.subplots(len(df.columns), 1, figsize=(7, 18), dpi=95) for i, col in enumerate(df.columns):
axs[i].boxplot(df[col], vert=False)
axs[i].set_ylabel(col)
plt.tight_layout()
plt.show()
```

****Đầu ra:****

![boxplot-data-preprocessing](https://media.geeksforgeeks.org/wp-content/uploads/20250829133635752868/boxplot-data-preprocessing.webp "Click to enlarge")

### Bước 4: Loại bỏ Outliers bằng phương pháp Interquartile Range (IQR)

Loại bỏ các giá trị cực trị vượt quá phạm vi hợp lý để cải thiện độ bền của model.

* IQR = Q3 (phân vị thứ 75) – Q1 (phân vị thứ 25).
* Giá trị dưới Q1 - 1,5IQR hoặc trên Q3 + 1,5IQR là outliers.
* Tính giới hạn dưới và trên cho từng cột riêng biệt.
* Lọc các điểm dữ liệu để chỉ giữ những điểm trong giới hạn.

```python
q1, q3 = np.percentile(df['Insulin'], [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
clean_df = df[(df['Insulin'] >= lower) & (df['Insulin'] <= upper)]
```

> ****Lưu ý:**** Trong thực tế, việc loại bỏ outlier phải được áp dụng trên tất cả các cột số có liên quan để đảm bảo quá trình tiền xử lý nhất quán.

### Bước 5: Phân tích tương quan

Hiểu mối quan hệ giữa features và biến mục tiêu (Kết quả). Mối tương quan giúp đánh giá tầm quan trọng của feature.

* ****df.corr():**** Tính toán các hệ số tương quan theo cặp giữa các cột.
* Heatmap thông qua seaborn hiển thị rõ ràng ma trận tương quan.
* Sắp xếp các mối tương quan bằng corr\['Outcome'\].sort\_values() làm nổi bật features tương quan nhất với mục tiêu.

```python
corr = df.corr()
plt.figure(dpi=130)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.show()
print(corr['Outcome'].sort_values(ascending=False))
```

****Đầu ra:****

![seashore.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133737344121/seashore.webp)

### Bước 6: Trực quan hóa phân phối biến mục tiêu

Kiểm tra xem các nhóm mục tiêu (Tiểu đường và Không tiểu đường) có cân bằng hay không, ảnh hưởng đến model training và đánh giá.

* ****plt.pie():**** Biểu đồ hình tròn để hiển thị tỷ lệ của từng loại trong biến mục tiêu 'Kết quả'.

```python
plt.pie(clean_df['Outcome'].value_counts(),
labels=['Diabetes', 'Not Diabetes'],
autopct='%.f%%', shadow=True)
plt.title('Outcome Proportionality')
plt.show()
```

****Đầu ra:****

![pie](https://media.geeksforgeeks.org/wp-content/uploads/20250829133842061194/pie.webp "Click to enlarge")

### Bước 7: Tách Features và Biến mục tiêu

Chuẩn bị riêng các biến độc lập (features) và biến phụ thuộc (đích) để lập model.

* ****df.drop(columns=\[...\]):**** Bỏ cột mục tiêu khỏi features.
* Lựa chọn cột trực tiếp df\['Outcome'\] chọn cột mục tiêu.

```python
X = df.drop(columns=['Outcome'])
y = df['Outcome']
```

### Bước 8: Feature Scaling: Normalization và Standardization

Chia tỷ lệ features thành phạm vi hoặc phân bố chung, quan trọng đối với nhiều ML algorithms nhạy cảm với cường độ feature.

****1\. Normalization (Scaling tối thiểu):**** Thay đổi tỷ lệ features trong khoảng từ 0 đến 1. Tốt cho algorithms như k-NN và neural networks.

* ****Lớp:**** MinMaxScaler từ sklearn.
* ****.fit\_transform():**** Tìm hiểu tối thiểu/tối đa từ dữ liệu và áp dụng scaling.

```python
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
print(X_normalized[:5])
```

****Đầu ra:****

![Screenshot-2025-08-29-132258](https://media.geeksforgeeks.org/wp-content/uploads/20250829133922543007/Screenshot-2025-08-29-132258.webp "Click to enlarge")

****2\. Standardization:**** Biến đổi features thành có giá trị trung bình = 0 và độ lệch chuẩn = 1, hữu ích cho features được phân phối chuẩn.

* ****Lớp:**** StandardScaler từ sklearn.

```python
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
print(X_standardized[:5])
```

****Đầu ra:****

![Screenshot-2025-08-29-132251](https://media.geeksforgeeks.org/wp-content/uploads/20250829134002498787/Screenshot-2025-08-29-132251.webp "Click to enlarge")

Thuận lợi
----------

* Làm sạch và sắp xếp dữ liệu thô để phân tích tốt hơn.
* Loại bỏ nhiễu và dữ liệu không liên quan, mang lại predictions chính xác hơn.
* Xử lý outliers và features dự phòng, giúp giảm overfitting.
* Dữ liệu Scaling giúp models training nhanh hơn bằng cách giảm thời gian tính toán.
* Chuyển đổi dữ liệu sang các định dạng phù hợp với machine learning models.

Câu đố được đề xuất
----------

Mục đích chính của data preprocessing là gì?

- [ ] A. Triển khai model
    
- [ ] B. Làm sạch, chuyển đổi và sắp xếp dữ liệu thô
    
- [ ] C. Tăng kích thước dataset
    
- [ ] D. Chỉ hiển thị biến mục tiêu

Chức năng nào giúp xác định missing values trong mỗi cột?

- [ ] A. Df.describe()
    
- [ ] B. B. Df.info()
    
- [ ] C. Df.isnull().sum()
    
- [ ] D. Df.corr()

Trong phương thức IQR, outliers là các giá trị:

- [ ] A. Bằng số trung vị
    
- [ ] B. Lớn hơn giá trị trung bình
    
- [ ] C. Giảm xuống dưới Q1 − 1,5IQR hoặc cao hơn Q3 + 1,5IQR
    
- [ ] D. Không có variance

Normalization (Scaling tối thiểu-tối đa) làm gì?

- [ ] A. Chuyển dữ liệu văn bản sang dạng số
    
- [ ] B. Thay đổi tỷ lệ features trong khoảng từ 0 đến 1
    
- [ ] C. Loại bỏ missing values
    
- [ ] D. Phát hiện mối tương quan

Một lợi thế chính của data preprocessing là gì?

- [ ] A. Đảm bảo model accuracy hoàn hảo
    
- [ ] B. Loại bỏ nhu cầu về EDA
    
- [ ] C. Loại bỏ tất cả features
    
- [ ] D. Giảm overfitting
