Data cleaning là quá trình chuẩn bị dữ liệu thô bằng cách phát hiện và sửa lỗi để có thể sử dụng hiệu quả cho việc phân tích. Đây là bước nền tảng trong data preprocessing nhằm đảm bảo datasets phù hợp cho các nhiệm vụ phân tích, thống kê và machine learning.

* Dữ liệu thô thường nhiễu, không đầy đủ và không nhất quán, điều này có thể tác động tiêu cực đến accuracy của model.
* Datasets sạch cũng rất quan trọng trong [EDA](https://www.geeksforgeeks.org/data-analysis/what-is-exploratory-data-analysis/) (Phân tích dữ liệu khám phá), giúp nâng cao khả năng diễn giải dữ liệu để có thể thực hiện các hành động phù hợp dựa trên thông tin chi tiết.

![data_cleaning_process.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260428110714078703/data_cleaning_process.webp)

![common_data_anomalies.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260428110713933000/common_data_anomalies.webp)

![data_cleaning_techniques.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260428110713725499/data_cleaning_techniques.webp)

![benefits_of_data_cleaning.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260428110713254070/benefits_of_data_cleaning.webp)

---------------------

Các vấn đề về chất lượng dữ liệu có thể phát sinh do lỗi của con người, lỗi hệ thống hoặc sự cố trong quá trình thu thập và tích hợp dữ liệu. Một số thách thức về chất lượng dữ liệu phổ biến nhất bao gồm:

* ****Missing values:**** Bản ghi không đầy đủ có thể làm giảm sức mạnh thống kê và đưa bias vào phân tích.
* ****Bản ghi trùng lặp:**** Các mục nhập lặp lại có thể thể hiện quá mức một số quan sát nhất định dẫn đến kết quả bị sai lệch.
* ****Loại dữ liệu không chính xác:**** Các định dạng không khớp, chẳng hạn như văn bản được lưu trữ trong trường số có thể gây ra lỗi tính toán và lỗi phân tích.
* ****Outliers và các điểm bất thường:**** Giá trị cực cao hoặc thấp có thể làm sai lệch các biện pháp thống kê và ảnh hưởng đến hiệu suất của model.
* ****Định dạng không nhất quán:**** Các biến thể trong định dạng ngày, cách viết hoa văn bản hoặc đơn vị đo lường có thể gây ra sự cố khi hợp nhất hoặc so sánh datasets.
* ****Lỗi chính tả và lỗi đánh máy:**** Lỗi trong trường văn bản có thể dẫn đến việc phân nhóm, classification hoặc diễn giải dữ liệu classification không chính xác

Quá trình Data Cleaning
---------------------

### 1\. Đánh giá chất lượng dữ liệu

Bước đầu tiên trong data cleaning là đánh giá chất lượng dữ liệu của bạn. Điều này liên quan đến việc kiểm tra:

* ****Missing Values:**** Xác định mọi giá trị trống hoặc null trong dataset. Missing values có thể do nhiều nguyên nhân khác nhau như thu thập dữ liệu không đầy đủ, lỗi nhập dữ liệu hoặc mất dữ liệu trong quá trình truyền.
* ****Giá trị không chính xác:**** Kiểm tra các giá trị nằm ngoài phạm vi mong đợi hoặc không nhất quán với loại dữ liệu.
* ****Sự không nhất quán trong Định dạng Dữ liệu:**** Xác minh rằng định dạng dữ liệu nhất quán trong toàn bộ dataset.

![quadrilaterals](https://media.geeksforgeeks.org/wp-content/uploads/20260130165440782166/quadrilaterals.webp "Click to enlarge")

Sau khi đánh giá chất lượng dữ liệu, một số vấn đề có thể được xác định trong dataset:

* Hàng 1 và 6 là trùng lặp cho thấy dữ liệu có thể bị trùng lặp có thể làm sai lệch kết quả phân tích.
* Hàng 7 thiếu giá trị trong cột "Tên", giá trị này có thể ảnh hưởng đến tính toán hoặc tóm tắt.
* Cột "Ngày" sử dụng định dạng "YYYY-MM-DD", nhưng điều quan trọng là phải duy trì tính nhất quán này trên tất cả các mục nhập.
* Điểm 100 ở hàng 7 có thể là outlier tùy thuộc vào hệ thống tính điểm, điều này có thể làm sai lệch phân tích thống kê.

### 2\. Xóa dữ liệu không liên quan

Việc xóa dữ liệu không liên quan hoặc trùng lặp đảm bảo dataset sạch sẽ, chính xác và có ý nghĩa, ngăn ngừa phân tích sai lệch và cải thiện chất lượng tổng thể.

* Xác định các mục trùng lặp bằng cách sử dụng các kỹ thuật như sắp xếp, nhóm hoặc băm.
* Loại bỏ các bản ghi trùng lặp để đảm bảo mỗi điểm dữ liệu là duy nhất và được trình bày chính xác.
* Phát hiện các quan sát dư thừa không thêm thông tin mới vào dataset.
* Loại bỏ các biến hoặc cột không liên quan đến phân tích và không cung cấp thông tin chi tiết hữu ích.

![imperfect_dataframe](https://media.geeksforgeeks.org/wp-content/uploads/20260130165752196818/imperfect_dataframe.webp "Click to enlarge")

Trong DataFrame được loại bỏ trùng lặp, các hàng 1 và 6 trùng lặp đã bị xóa để đảm bảo mỗi bản ghi là duy nhất

### 3\. Sửa lỗi cấu trúc

Lỗi cấu trúc xảy ra khi định dạng dữ liệu, quy ước đặt tên hoặc loại biến không nhất quán có thể ảnh hưởng đến phân tích accuracy. Việc khắc phục những vấn đề này đảm bảo việc trình bày dữ liệu thống nhất và đáng tin cậy.

* Chuẩn hóa các định dạng dữ liệu để duy trì tính nhất quán về ngày, giờ và các loại dữ liệu khác trên dataset.
* Sửa lỗi đặt tên không nhất quán trong tên cột, tên biến hoặc labels để đảm bảo tính rõ ràng và thống nhất.
* Đảm bảo trình bày dữ liệu nhất quán, chẳng hạn như sử dụng cùng đơn vị đo lường hoặc cùng thang đo để xếp hạng.

![dataframe_with_standardized_date_fromat](https://media.geeksforgeeks.org/wp-content/uploads/20260130170123079847/dataframe_with_standardized_date_fromat.webp "Click to enlarge")

### 4\. Xử lý dữ liệu bị thiếu

Dữ liệu bị thiếu có thể tạo ra bias và làm giảm độ tin cậy của phân tích. Việc đánh địa chỉ missing values đúng cách sẽ giúp duy trì tính toàn vẹn của dataset của bạn.

* Xác định missing values bằng cách sử dụng các phương pháp thống kê như giá trị trung bình, trung vị hoặc chế độ để lấp đầy khoảng trống.
* Xóa các bản ghi bằng missing values khi dữ liệu bị thiếu có phạm vi rộng hoặc không thể liệt kê chính xác.
* Áp dụng các kỹ thuật imputation nâng cao như regression, [K-nearest neighbors](https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/) hoặc [Decision trees](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/) để ước tính missing values.

![dataframe_with_handled_missing_values](https://media.geeksforgeeks.org/wp-content/uploads/20260130170400549078/dataframe_with_handled_missing_values.webp "Click to enlarge")

Giá trị còn thiếu trong cột 'Tên' (hàng 7) đã được điền bằng 'Không xác định' để biểu thị dữ liệu không có sẵn, đảm bảo dataset vẫn đầy đủ và nhất quán.

### 5\. Chuẩn hóa dữ liệu

Dữ liệu normalization tổ chức dataset để giảm sự dư thừa và đảm bảo tính nhất quán giúp quản lý và phân tích dễ dàng hơn.

* Chia dữ liệu thành nhiều bảng, mỗi bảng lưu trữ những loại thông tin cụ thể.
* Đảm bảo tính nhất quán trên dataset để hỗ trợ truy vấn hiệu quả và phân tích chính xác.

![normalized_data_scores_](https://media.geeksforgeeks.org/wp-content/uploads/20260130170616483478/normalized_data_scores_.webp "Click to enlarge")

### 6\. Xác định và quản lý Outliers

Outliers là các điểm dữ liệu sai lệch đáng kể so với phần còn lại của dataset và có thể ảnh hưởng đến phân tích accuracy. Việc xử lý chúng đúng cách sẽ đảm bảo những hiểu biết sâu sắc đáng tin cậy hơn.

* Loại bỏ outliers do lỗi hoặc không đại diện cho tổng thể.
* Chuyển đổi outliers cực đoan nhưng hợp lệ để giảm tác động của chúng đến quá trình phân tích.

![dataframe_with_managed_outliers](https://media.geeksforgeeks.org/wp-content/uploads/20260130170736629764/dataframe_with_managed_outliers.webp "Click to enlarge")

--------------------------------

Hãy cùng tìm hiểu từng bước để Làm sạch cơ sở dữ liệu bằng titanic dataset.

> Bạn có thể tải xuống dataset từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20250114171103408125/Titanic-Dataset.csv).

### Bước 1: Nhập thư viện và tải Dataset

Chúng ta sẽ nhập tất cả các thư viện cần thiết, ví dụ [Pandas](https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/) và [Numpy](https://www.geeksforgeeks.org/numpy/python-numpy/).

```python
import pandas as pd
import numpy as np
df = pd.read_csv('Titanic-Dataset.csv')
df.info()
df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-122359.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829123024725201/Screenshot-2025-08-29-122359.webp)

### Bước 2: Kiểm tra các hàng trùng lặp

* ****df.duplicate()****: Trả về một chuỗi boolean cho biết các hàng trùng lặp.

```python
df.duplicated()
```

****Đầu ra:****

![Screenshot-2025-08-29-122420](https://media.geeksforgeeks.org/wp-content/uploads/20250829123121881187/Screenshot-2025-08-29-122420.webp "Click to enlarge")

### Bước 3: Xác định kiểu dữ liệu cột

* Khả năng hiểu danh sách bằng thuộc tính .dtype để phân tách các cột classification và cột số.
* ****dtype đối tượng:**** Thường được sử dụng cho văn bản hoặc dữ liệu classification.

```python
cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']
print('Categorical columns:', cat_col)
print('Numerical columns:', num_col)
```

****Đầu ra:****

![Screenshot-2025-08-29-123218](https://media.geeksforgeeks.org/wp-content/uploads/20250829123250706621/Screenshot-2025-08-29-123218.webp "Click to enlarge")

### Bước 4: Đếm các giá trị duy nhất trong các cột classification

* ****df\[cat\_col\].nunique():**** Trả về số lượng giá trị duy nhất trên mỗi cột.

```python
df[cat_col].nunique()
```

****Đầu ra:****

![Screenshot-2025-08-29-122434](https://media.geeksforgeeks.org/wp-content/uploads/20250829123331744443/Screenshot-2025-08-29-122434.webp "Click to enlarge")

### Bước 5: Tính Missing Values theo phần trăm

* ****df.isnull():**** Phát hiện missing values, trả về boolean DataFrame.
* Tính tổng bị thiếu trên các cột, chuẩn hóa theo tổng số hàng và nhân với 100.

```python
round((df.isnull().sum() / df.shape[0]) * 100, 2)
```

****Đầu ra:****

![Screenshot-2025-08-29-122442](https://media.geeksforgeeks.org/wp-content/uploads/20250829123556902755/Screenshot-2025-08-29-122442.webp "Click to enlarge")

### Bước 6: Loại bỏ các cột thiếu dữ liệu hoặc không liên quan

* ****df.drop(columns=\[\])****: Loại bỏ các cột được chỉ định khỏi DataFrame.
* ****df.dropna(subset=\[\])****: Xóa các hàng trong đó các cột được chỉ định có missing values.
* ****fillna()****: Điền vào missing values với giá trị được chỉ định (ví dụ: giá trị trung bình).

```python
df1 = df.drop(columns=['Name', 'Ticket', 'Cabin'])
df1.dropna(subset=['Embarked'], inplace=True)
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
```

### Bước 7: Phát hiện Outliers bằng Box Plot

* ****matplotlib.pyplot.boxplot():**** Hiển thị phân bổ dữ liệu, làm nổi bật trung vị, tứ phân vị và outliers.
* ****plt.show()****: Hiển thị cốt truyện.

```python
import matplotlib.pyplot as plt
plt.boxplot(df1['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()
```

****Đầu ra:****

![boxplot](https://media.geeksforgeeks.org/wp-content/uploads/20250829123644973970/boxplot.webp "Click to enlarge")

### Bước 8: Tính toán ranh giới Outlier và loại bỏ chúng

* Tính toán trung bình và độ lệch chuẩn (std) bằng cách sử dụng df\['Age'\].mean() và df\['Age'\].std().
* Xác định giới hạn là giá trị trung bình ± 2 \* std để phát hiện outlier.
* Lọc các hàng DataFrame trong giới hạn bằng cách sử dụng chỉ mục Boolean.

```python
mean = df1['Age'].mean()
std = df1['Age'].std()
lower_bound = mean - 2 * std
upper_bound = mean + 2 * std
df2 = df1[(df1['Age'] >= lower_bound) & (df1['Age'] <= upper_bound)]
```

### Bước 9: Báo cáo lại dữ liệu bị thiếu nếu có

****fillna()**** áp dụng lại trên dữ liệu đã lọc để xử lý mọi missing values còn lại.

```python
df3 = df2.fillna(df2['Age'].mean())
df3.isnull().sum()
```

****Đầu ra:****

![Screenshot-2025-08-29-122505](https://media.geeksforgeeks.org/wp-content/uploads/20250829123734990016/Screenshot-2025-08-29-122505.webp "Click to enlarge")

### Bước 10: Tính lại giới hạn Outlier và xóa Outliers khỏi dữ liệu đã cập nhật

* ****mean = df3\['Age'\].mean()****: Tính giá trị trung bình (trung bình) của cột Tuổi trong DataFrame df3.
* ****std = df3\['Age'\].std()****: Tính độ lệch chuẩn (chênh lệch hoặc variance) của cột Tuổi trong df3.
* ****dưới\_bound = trung bình - 2 \* std****: Xác định giới hạn dưới cho các giá trị Tuổi có thể chấp nhận được, đặt thành hai độ lệch chuẩn dưới giá trị trung bình.
* ****upper\_bound = giá trị trung bình + 2 \* std****: Xác định giới hạn trên cho các giá trị Tuổi được chấp nhận, được đặt thành hai độ lệch chuẩn trên giá trị trung bình.
* ****df4 = df3\[(df3\['Age'\] >= low\_bound) & (df3\['Age'\] <= Upper\_bound)\]****: Tạo một DataFrame df4 mới bằng cách chỉ chọn các hàng có giá trị Tuổi nằm giữa giới hạn dưới và giới hạn trên, loại bỏ một cách hiệu quả các độ tuổi outlier nằm ngoài phạm vi này.

```python
mean = df3['Age'].mean()
std = df3['Age'].std()
lower_bound = mean - 2 * std
upper_bound = mean + 2 * std print('Lower Bound :', lower_bound)
print('Upper Bound :', upper_bound)
df4 = df3[(df3['Age'] >= lower_bound) & (df3['Age'] <= upper_bound)]
```

****Đầu ra:****

![Screenshot-2025-08-29-122513](https://media.geeksforgeeks.org/wp-content/uploads/20250829123816594942/Screenshot-2025-08-29-122513.webp "Click to enlarge")

### Bước 11: Dữ liệu validation và xác minh

Dữ liệu validation và việc xác minh liên quan đến việc đảm bảo rằng dữ liệu chính xác và nhất quán bằng cách so sánh dữ liệu đó với các nguồn bên ngoài hoặc kiến ​​thức chuyên môn.

* Đối với machine learning prediction, chúng ta tách features độc lập và nhắm mục tiêu
* Ở đây chúng ta sẽ coi 'Pclass', 'Giới tính', 'Tuổi', 'SibSp', 'Parch', 'Fare' và 'Embarked' là features độc lập.
* Sống sót dưới dạng biến mục tiêu vì PassengerId sẽ không ảnh hưởng đến tỷ lệ sống sót

```python
X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df3['Survived']
```

### Bước 12: Định dạng dữ liệu

Định dạng dữ liệu bao gồm việc chuyển đổi dữ liệu thành định dạng hoặc cấu trúc tiêu chuẩn mà algorithms hoặc models được sử dụng để phân tích có thể dễ dàng xử lý. Ở đây chúng ta sẽ thảo luận về các kỹ thuật định dạng dữ liệu thường được sử dụng, tức là Scaling và Normalization.

****1\. Min-Max Scaling:**** Scaling liên quan đến việc chuyển đổi các giá trị của features thành một phạm vi cụ thể. Min-Max scaling thay đổi tỷ lệ các giá trị thành một phạm vi được chỉ định, thường là từ 0 đến 1. Nó duy trì phân bố ban đầu và đảm bảo rằng giá trị tối thiểu ánh xạ tới 0 và giá trị tối đa ánh xạ tới 1.

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X
x1[num_col_] = scaler.fit_transform(x1[num_col_])
x1.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-122526](https://media.geeksforgeeks.org/wp-content/uploads/20250829123857272411/Screenshot-2025-08-29-122526.webp "Click to enlarge")

****2\. Standardization (Z-score scaling):**** Standardization biến đổi các giá trị thành giá trị trung bình bằng 0 và độ lệch chuẩn là 1. Nó tập trung dữ liệu xung quanh giá trị trung bình và chia tỷ lệ dựa trên độ lệch chuẩn. Standardization làm cho dữ liệu phù hợp hơn với algorithms giả định phân phối Gaussian hoặc yêu cầu features có giá trị trung bình bằng 0 và đơn vị variance.

> Z = (X - μ) / σ

Ở đâu,

* X = Dữ liệu
* μ = Giá trị trung bình của X
* σ = Độ lệch chuẩn của X

> Bạn có thể tải xuống mã nguồn từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20260323182359138538/Data-Cleaning.ipynb).

Chiến lược Data Cleaning
---------------

* ****Hiểu dữ liệu:**** Biết nguồn, cấu trúc và miền của dữ liệu để xác định các vấn đề tiềm ẩn về chất lượng và xác định các hành động làm sạch thích hợp.
* ****Ghi lại quy trình:**** Lưu giữ hồ sơ về các quyết định, phương pháp, giả định và quy tắc được áp dụng trong data cleaning.
* ****Ưu tiên các vấn đề quan trọng:**** Tập trung trước tiên vào các vấn đề chính về chất lượng có thể có tác động mang tính hệ thống đến việc phân tích hoặc ra quyết định.
* ****Tự động hóa nếu có thể:**** Sử dụng tập lệnh hoặc công cụ cho các tác vụ dọn dẹp lặp đi lặp lại để nâng cao hiệu quả và tính nhất quán.
* ****Cộng tác với các chuyên gia tên miền:**** Thu hút các bên liên quan hoặc chuyên gia tên miền để validation rằng dữ liệu đã được làm sạch đáp ứng các yêu cầu kinh doanh.
* ****Giám sát và bảo trì:**** Liên tục theo dõi chất lượng dữ liệu và thực hiện dọn dẹp định kỳ để đảm bảo độ tin cậy và accuracy lâu dài.

Thuận lợi
----------

* Loại bỏ các lỗi, sự không nhất quán và dữ liệu không liên quan giúp model học hỏi tốt hơn từ dữ liệu.
* Đảm bảo dữ liệu chính xác, nhất quán và không có sai sót.
* Chuyển đổi dữ liệu sang định dạng thể hiện tốt hơn các mẫu và mối quan hệ cơ bản.
* Cải thiện chất lượng dữ liệu, làm cho nó đáng tin cậy và chính xác hơn.
* Giúp xác định và loại bỏ thông tin nhạy cảm hoặc bí mật, cải thiện bảo mật dữ liệu.

Nhược điểm
-------------

* Tốn nhiều thời gian, đặc biệt đối với datasets lớn và phức tạp.
* Có thể dẫn đến mất thông tin quan trọng nếu không xử lý cẩn thận.
* Đòi hỏi nhiều thời gian, công sức, chuyên môn và đôi khi là các công cụ chuyên dụng.
* Xóa quá nhiều dữ liệu có thể góp phần vào underfitting.

Câu đố được đề xuất
-------------

Mục tiêu chính của data cleaning là gì?

- [ ] A. Tăng kích thước dataset
    
- [ ] B. Làm cho dữ liệu trở nên đầy màu sắc để trực quan hóa
    
- [ ] C. Đảm bảo dữ liệu chính xác, nhất quán và không có sai sót
    
- [ ] D. Trực tiếp training machine learning models

Tại sao dữ liệu thô thường không phù hợp để lập model?

- [ ] A. Nó luôn quá nhỏ
    
- [ ] B. Ồn ào, không đầy đủ và không nhất quán
    
- [ ] C. Nó chỉ chứa các giá trị số
    
- [ ] D. Nó đã được chuẩn hóa rồi

Hàm nào được sử dụng để phát hiện các hàng trùng lặp trong dataset?

- [ ] A. Df.isnull()
    
- [ ] B. Df.describe()
    
- [ ] C. Df.duplicate()
    
- [ ] D. Df.unique()

Phương pháp nào được sử dụng để điền missing values vào dataset?

- [ ] A. Drop()
    
- [ ] B. Duplicated()
    
- [ ] C. Fillna()
    
- [ ] D. Sửa()

Trong phát hiện outlier sử dụng độ lệch trung bình và độ lệch chuẩn, các ranh giới được xác định là

- [ ] A. Trung bình ± tiêu chuẩn
    
- [ ] B. Trung bình ± 2 × tiêu chuẩn
    
- [ ] C. Q1 ± IQR
    
- [ ] D. Trung vị ± variance
