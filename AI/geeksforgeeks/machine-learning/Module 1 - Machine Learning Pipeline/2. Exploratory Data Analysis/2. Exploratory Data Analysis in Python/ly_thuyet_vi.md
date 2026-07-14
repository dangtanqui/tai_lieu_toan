EDA là một bước thiết yếu trong phân tích dữ liệu tập trung vào việc tìm hiểu các mẫu, mối quan hệ và phân phối trong dataset bằng các phương pháp thống kê và trực quan hóa. Các thư viện Python như pandas, NumPy, Plotly, matplotlib và seaborn giúp quá trình này trở nên hiệu quả và sâu sắc. Một số kỹ thuật EDA phổ biến là:

* ****Kiểm tra dữ liệu:**** Kiểm tra kích thước của dataset, cách tổ chức, loại dữ liệu chứa và các giá trị tóm tắt cơ bản.
* ****Xử lý dữ liệu bị thiếu và trùng lặp:**** Tìm và sửa các giá trị trống hoặc các hàng lặp lại để giữ cho dữ liệu luôn sạch sẽ.
* ****Phân tích đơn biến:**** Nghiên cứu từng biến một để hiểu sự phân bố, xu hướng và outliers của nó.
* ****Phân tích hai biến:**** So sánh hai biến để xem chúng có liên quan như thế nào.
* ****Phân tích đa biến:**** Phân tích ba biến trở lên cùng nhau để hiểu mối quan hệ sâu sắc hơn.

Các bước chính để phân tích dữ liệu thăm dò (EDA)
---------------------------------------------

### Bước 1: Nhập thư viện cần thiết

Chúng ta cần cài đặt các thư viện [Pandas](https://www.geeksforgeeks.org/pandas/pandas-tutorial/), [NumPy](https://www.geeksforgeeks.org/numpy/python-numpy/), [Matplotlib](https://www.geeksforgeeks.org/data-visualization/data-visualization-using-matplotlib/) và [Sinh ra ở biển](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) trong python để tiếp tục.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')
```

Nhập pandas dưới dạng pd

Nhập numpy dưới dạng np

Nhập matplotlib.pyplot dưới dạng plt

Nhập khẩu seaborn dưới dạng sns

Nhập cảnh báo dưới dạng wr

Wr.filterwarnings('bỏ qua')

### Bước 2: Đọc Dataset

Hãy đọc dataset bằng pandas.

> Tải xuống dataset từ [Liên kết](https://media.geeksforgeeks.org/wp-content/uploads/20250731152112425017/WineQT.csv) này

```python
df = pd.read_csv("/content/WineQT.csv")
print(df.head())
```

Df \= pd.read\_csv("/content/WineQT.csv")

In(df.head())

****Đầu ra:****

![eda1](https://media.geeksforgeeks.org/wp-content/uploads/20250508155447619651/eda1.webp "Click to enlarge")

### Bước 3: Phân tích dữ liệu

****1\. Df.shape():**** Hàm này được sử dụng để hiểu số lượng hàng (quan sát) và số cột (features) trong dataset. Điều này cung cấp cái nhìn tổng quan về kích thước và cấu trúc của dataset.

```python
df.shape
```

Df.shape

****Đầu ra:****

> (1143, 13)

****2\. Df.info():**** Hàm này giúp chúng ta hiểu dataset bằng cách hiển thị số lượng bản ghi trong mỗi cột, loại dữ liệu, liệu có giá trị nào bị thiếu hay không và dataset sử dụng bao nhiêu bộ nhớ.

```python
df.info()
```

Df.info()

****Đầu ra:****

![eda2](https://media.geeksforgeeks.org/wp-content/uploads/20250508155610060367/eda2.webp "Click to enlarge")

****3\. Df.describe().T****: Phương pháp này đưa ra bản tóm tắt thống kê về DataFrame (Transpose) hiển thị các giá trị như số đếm, giá trị trung bình, độ lệch chuẩn, mức tối thiểu và tứ phân vị cho mỗi cột số. Nó giúp tóm tắt xu hướng trung tâm và sự lan truyền của dữ liệu.

```python
df.describe().T
```

Df.describe().T

****Đầu ra:****

![describe](https://media.geeksforgeeks.org/wp-content/uploads/20250731152213452639/describe.webp "Click to enlarge")

4\. ****df.columns.tolist():**** Thao tác này chuyển đổi tên cột của DataFrame thành danh sách Python giúp dễ dàng truy cập và thao tác với tên cột.

```python
df.columns.tolist()
```

Df.columns.tolist()

****Đầu ra:****

![eda4](https://media.geeksforgeeks.org/wp-content/uploads/20250508155820778813/eda4.webp "Click to enlarge")

### Bước 4 : Kiểm tra Missing Values

****df.isnull().sum():**** Thao tác này sẽ kiểm tra missing values trong mỗi cột và trả về tổng số giá trị null trên mỗi cột giúp chúng ta xác định bất kỳ khoảng trống nào trong dữ liệu của mình.

```python
df.isnull().sum()
```

Df.isnull().sum()

****Đầu ra:****

![eda5](https://media.geeksforgeeks.org/wp-content/uploads/20250508155944227795/eda5.webp "Click to enlarge")

### Bước 5: Kiểm tra các giá trị trùng lặp

****df.duplicate().sum():**** Trả về số hàng trùng lặp trong dataset.

```python
df.duplicated().sum()
```

Df.duplicate().sum()

****Đầu ra:****

![eda6](https://media.geeksforgeeks.org/wp-content/uploads/20250508160112148527/eda6.webp "Click to enlarge")

### Bước 6: Phân tích đơn biến

Trong [Phân tích đơn biến](https://www.geeksforgeeks.org/data-analysis/univariate-bivariate-and-multivariate-data-and-its-analysis/), việc vẽ biểu đồ phù hợp có thể giúp chúng ta hiểu rõ hơn về dữ liệu, khiến việc trực quan hóa dữ liệu trở nên quan trọng.

1\. Bar Plot để đánh giá số lượng rượu và tỷ lệ chất lượng của nó.

```python
quality_counts = df['quality'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(quality_counts.index, quality_counts, color='deeppink')
plt.title('Count Plot of Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()
```

Chất lượng\_counts \= df\['quality'\].value\_counts()

​

Plt.figure(figsize\=(8, 6))

Plt.bar(chất lượng\_counts.index, chất lượng\_counts, color\='deeppink')

Plt.title('Đếm batch chất lượng')

Plt.xlabel('Chất lượng')

Plt.ylabel('Đếm')

Plt.show()

****Đầu ra:****

![eda7](https://media.geeksforgeeks.org/wp-content/uploads/20250508160319714718/eda7.webp "Click to enlarge")

Ở đây, biểu đồ số lượng này hiển thị số lượng rượu cùng với tỷ lệ chất lượng của nó.

2\. Biểu đồ mật độ hạt nhân giúp trực quan hóa việc phân bổ dữ liệu và xác định các mẫu như độ lệch và mật độ.

```python
sns.set_style("darkgrid")
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
plt.figure(figsize=(14, len(numerical_columns) * 3)) for idx, feature in enumerate(numerical_columns, 1):
plt.subplot(len(numerical_columns), 2, idx)
sns.histplot(df[feature], kde=True)
plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")
plt.tight_layout()
plt.show()
```

Sns.set\_style("darkgrid")

​

Số\_columns \= df.select\_dtypes(include\=\["int64", "float64"\]).columns

​

Plt.figure(figsize\=(14, len(numerical\_columns) \* 3))

Đối với idx, feature trong liệt kê (số\_columns, 1):

Plt.subplot(len(số\_columns), 2, idx)

Sns.histplot(df\[feature\], kde\=True)

Plt.title(f"{feature} | Độ lệch: {round(df\[feature\].skew(), 2)}")

​

Plt.tight\_layout()

Plt.show()

****Đầu ra:****

![eda8](https://media.geeksforgeeks.org/wp-content/uploads/20250508160409495815/eda8.webp "Click to enlarge")

Features trong dataset có độ lệch ****0**** cho thấy sự phân bố đối xứng. Độ lệch > 0 biểu thị độ lệch dương (phải), trong khi độ lệch < 0 biểu thị độ lệch âm (trái). Trong phân bố lệch phải, phần đuôi kéo dài hơn về bên phải, điều này cho thấy sự hiện diện của các giá trị cực cao.

3\. [Âm mưu bầy đàn](https://www.geeksforgeeks.org/python/swarmplot-using-seaborn-in-python/) để hiển thị outlier trong dữ liệu

```python
plt.figure(figsize=(10, 8))
sns.swarmplot(x="quality", y="alcohol", data=df, palette='viridis')
plt.title('Swarm Plot for Quality and Alcohol')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.show()
```

Plt.figure(figsize\=(10, 8))

​

Sns.swarmplot(x\="quality", y\="alcohol", data\=df, bảng\='viridis')

​

Plt.title('Âm mưu bầy đàn về chất lượng và rượu')

Plt.xlabel('Chất lượng')

Plt.ylabel('Rượu')

Plt.show()

****Đầu ra:****

![eda9](https://media.geeksforgeeks.org/wp-content/uploads/20250508160909098036/eda9.webp "Click to enlarge")

Biểu đồ này hiển thị sơ đồ nhóm cho cột 'Chất lượng' và 'Rượu'. Mật độ điểm cao hơn ở một số khu vực nhất định cho thấy nơi tập trung hầu hết các điểm dữ liệu. Các điểm bị cô lập và cách xa các cụm này biểu thị outliers làm nổi bật các giá trị không đồng đều trong dataset.

### Bước 7: Phân tích hai biến

Trong [Phân tích hai biến](https://www.geeksforgeeks.org/data-analysis/univariate-bivariate-and-multivariate-data-and-its-analysis/), hai biến được phân tích cùng nhau để xác định các mẫu, sự phụ thuộc hoặc tương tác giữa chúng. Phương pháp này giúp hiểu được những thay đổi trong một biến có thể ảnh hưởng đến một biến khác như thế nào.

1\. Biểu đồ cặp để hiển thị phân phối của các biến riêng lẻ

```python
sns.set_palette("Pastel1")
plt.figure(figsize=(10, 6))
sns.pairplot(df)
plt.suptitle('Pair Plot for DataFrame')
plt.show()
```

Sns.set\_palette("Pastel1")

​

Plt.figure(figsize\=(10, 6))

​

Sns.pairplot(df)

​

Plt.suptitle('Sơ đồ cặp cho DataFrame')

Plt.show()

****Đầu ra:****

![eda10](https://media.geeksforgeeks.org/wp-content/uploads/20250508160949661677/eda10.webp "Click to enlarge")

* Nếu đồ thị là đường chéo, biểu đồ của đồ thị mật độ hạt nhân thể hiện sự phân bố của các biến riêng lẻ.
* Nếu biểu đồ phân tán nằm trong tam giác phía dưới, nó sẽ hiển thị mối quan hệ giữa các cặp biến.
* Nếu các ô phân tán ở trên và dưới đường chéo là hình ảnh phản chiếu biểu thị tính đối xứng.
* Nếu biểu đồ biểu đồ tập trung hơn, nó thể hiện vị trí của các đỉnh.
* Độ lệch được phát hiện bằng cách quan sát xem biểu đồ có đối xứng hay lệch sang trái hay phải hay không.

2\. [Âm mưu vĩ cầm](https://www.geeksforgeeks.org/data-visualization/violin-plot-for-data-analysis/) để kiểm tra mối quan hệ giữa rượu và Chất lượng.

```python
df['quality'] = df['quality'].astype(str)
plt.figure(figsize=(10, 8))
sns.violinplot(x="quality", y="alcohol", data=df, palette={
'3': 'lightcoral', '4': 'lightblue', '5': 'lightgreen', '6': 'gold', '7': 'lightskyblue', '8': 'lightpink'}, alpha=0.7)
plt.title('Violin Plot for Quality and Alcohol')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.show()
```

Df\['quality'\] \= df\['quality'\].astype(str)

​

Plt.figure(figsize\=(10, 8))

​

Sns.violinplot(x\="quality", y\="alcohol", data\=df, pallet\={

'3': 'lightcoral', '4': 'lightblue', '5': 'lightgreen', '6': 'gold', '7': 'lightskyblue', '8': 'lightpink'}, alpha\=0.7)

​

Plt.title('Âm mưu vĩ cầm cho chất lượng và rượu')

Plt.xlabel('Chất lượng')

Plt.ylabel('Rượu')

Plt.show()

****Đầu ra:****

![violin](https://media.geeksforgeeks.org/wp-content/uploads/20250731151918776977/violin.webp "Click to enlarge")

* Nếu chiều rộng rộng hơn, nó hiển thị mật độ cao hơn gợi ý nhiều điểm dữ liệu hơn.
* Đồ thị đối xứng thể hiện sự phân bố cân bằng.
* Đỉnh hoặc chỗ phình ra trong biểu đồ violin thể hiện giá trị phổ biến nhất trong phân bố.
* Đuôi dài hơn cho thấy sự biến đổi lớn.
* Đường trung tuyến là đường giữa bên trong ô violin. Nó giúp hiểu được xu hướng trung tâm.

3\. Sơ đồ hộp để kiểm tra mối quan hệ giữa rượu và chất lượng

```python
sns.boxplot(x='quality', y='alcohol', data=df)
```

Sns.boxplot(x\='quality', y\='alcohol', data\=df)

****Đầu ra:****

![box-plot](https://media.geeksforgeeks.org/wp-content/uploads/20250728152858175356/box-plot.png "Click to enlarge")

Hộp đại diện cho [IQR](https://www.geeksforgeeks.org/dsa/interquartile-range-iqr/) tức là hộp càng dài thì độ variance càng lớn.

* Đường trung tuyến trong hộp thể hiện xu hướng trung tâm.
* [Râu](https://www.geeksforgeeks.org/data-visualization/box-and-whisker-plot-meaning-uses-and-example/) mở rộng từ hộp đến các giá trị nhỏ nhất và lớn nhất trong phạm vi được chỉ định.
* Các điểm riêng lẻ ngoài râu tượng trưng cho outliers.
* Hộp nhỏ gọn cho thấy độ variance thấp trong khi hộp kéo dài cho thấy độ variance cao hơn.

### Bước 8: Phân tích đa biến

Nó liên quan đến việc tìm kiếm sự tương tác giữa ba hoặc nhiều biến trong dataset cùng một lúc. Cách tiếp cận này tập trung vào việc xác định các model, mối quan hệ và tương tác phức tạp nhằm cung cấp sự hiểu biết về cách nhiều biến số hành xử và ảnh hưởng lẫn nhau.

Ở đây, chúng ta sẽ trình bày phân tích đa biến bằng [Sơ đồ ma trận tương quan](https://www.geeksforgeeks.org/python/plotting-correlation-matrix-using-python/).

```python
plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
plt.title('Correlation Heatmap')
plt.show()
```

Plt.figure(figsize\=(15, 10))

​

Sns.heatmap(df.corr(), annot\=True, fmt\='.2f', cmap\='Pastel2', linewidths\=2)

​

Plt.title('Bản đồ nhiệt tương quan')

Plt.show()

****Đầu ra:****

![eda13](https://media.geeksforgeeks.org/wp-content/uploads/20250508161201512231/eda13.webp "Click to enlarge")

Các giá trị gần +1 cho thấy mối tương quan dương mạnh mẽ, -1 cho thấy mối tương quan âm mạnh mẽ và 0 cho thấy không có tương quan tuyến tính.

* Màu tối hơn biểu thị mối tương quan chặt chẽ, trong khi màu sáng biểu thị mối tương quan yếu hơn.
* Biến tương quan dương di chuyển cùng hướng. Khi cái này tăng thì cái kia cũng tăng.
* Biến tương quan âm di chuyển theo hướng ngược nhau. Sự gia tăng của một biến có liên quan đến việc giảm biến khác.

Câu đố được đề xuất
----------

Hàm nào trong EDA được sử dụng để kiểm tra số hàng và số cột trong dataset?

- [ ] A. Df.info()
    
- [ ] B. Df.describe()
    
- [ ] C. Df.shape
    
- [ ] D. Df.columns

Df.describe().T cung cấp những gì trong EDA?

- [ ] A. Chỉ có missing values
    
- [ ] B. Danh sách tên cột
    
- [ ] C. Thống kê tổng hợp cột số
    
- [ ] D. Kích thước tệp của dataset

Biểu đồ nào được sử dụng trong phân tích đơn biến để hiểu sự phân bố và độ lệch của các cột số?

- [ ] A. Âm mưu bầy đàn
    
- [ ] B. Âm mưu đàn violin
    
- [ ] C. Biểu đồ mật độ hạt nhân
    
- [ ] D. Bản đồ nhiệt

Mục đích chính của Phân tích dữ liệu thăm dò (EDA) là gì?

- [ ] A. Để triển khai machine learning models
    
- [ ] B. Để hiểu các mẫu, xu hướng và mối quan hệ trong dữ liệu
    
- [ ] C. Chỉ xóa các giá trị trùng lặp
    
- [ ] D. Để tăng kích thước dataset
