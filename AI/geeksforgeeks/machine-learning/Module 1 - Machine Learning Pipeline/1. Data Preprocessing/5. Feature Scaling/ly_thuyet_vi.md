[Feature engineering](https://www.geeksforgeeks.org/machine-learning/what-is-feature-engineering/) được thiết kế tốt là quá trình tạo, chuyển đổi hoặc chọn features quan trọng từ dữ liệu thô để cải thiện hiệu suất model. Những features này giúp model nắm bắt các mẫu và mối quan hệ hữu ích trong dữ liệu.

![feature_engineering](https://media.geeksforgeeks.org/wp-content/uploads/20260317163613238130/feature_engineering.webp "Click to enlarge")

* Features được thiết kế tốt giúp model học các mẫu phức tạp hiệu quả hơn.
* Loại bỏ tiếng ồn và thông tin không liên quan sẽ cải thiện model prediction accuracy.
* Tập trung vào features có ý nghĩa giúp model khái quát hóa tốt hơn và giảm overfitting.
* Features rõ ràng và giàu thông tin giúp model dễ hiểu và diễn giải hơn.

1\. Scaling tối đa tuyệt đối
----------------------------

Scaling tối đa tuyệt đối là phương pháp feature scaling trong đó mỗi giá trị được chia cho giá trị tuyệt đối tối đa của feature đó. Phép biến đổi này định lại tỷ lệ dữ liệu sao cho các giá trị nằm trong phạm vi từ −1 đến 1.

* ****Nhạy cảm với Outliers:**** Giá trị cực cao có thể ảnh hưởng đến giá trị tối đa và làm giảm chất lượng scaling.
* ****Tốt nhất cho dữ liệu sạch:**** Hoạt động tốt hơn khi dataset không chứa outliers mạnh.

### ****Scaling Công thức:****

> Xscaled\=Ximax(∣X∣)X\_{\\rm {scaled }}=\\frac{X\_{i}}{\\rm{max}\\left(|X|\\right)}Xscaled​\=max(∣X∣)Xi​ ​

### ****Triển khai****

>  Dataset có thể được tải xuống từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20250114174407596134/SampleFile.csv).

****Bước 1: Nhập thư viện và Dataset****

```python
import pandas as pd
import numpy as np
df = pd.read_csv('Housing.csv')
df = df.select_dtypes(include=np.number)
df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-163245](https://media.geeksforgeeks.org/wp-content/uploads/20250829163533984164/Screenshot-2025-08-29-163245.webp "Click to enlarge")

****Bước 2: Áp dụng Scaling tối đa tuyệt đối****

* ****np.max(np.abs(df), axis=0)****: Tính giá trị tuyệt đối tối đa cho mỗi cột.
* ****df / max\_abs****: Chia mỗi giá trị cho giá trị tuyệt đối tối đa của cột của nó để chia tỷ lệ dữ liệu.
* ****scaled\_df.head()****: Hiển thị một vài hàng đầu tiên của dataset được chia tỷ lệ.

```python
max_abs = np.max(np.abs(df), axis=0)
scaled_df = df / max_abs
scaled_df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-163253](https://media.geeksforgeeks.org/wp-content/uploads/20250829163652707844/Screenshot-2025-08-29-163253.webp "Click to enlarge")

2\. Tối thiểu-Tối đa Scaling
-------------------

Min-Max Scaling định lại tỷ lệ features bằng cách trừ giá trị tối thiểu và chia cho chênh lệch giữa giá trị tối đa và tối thiểu. Điều này thường ánh xạ các giá trị feature vào phạm vi từ 0 đến 1 trong khi vẫn giữ nguyên phân phối ban đầu.

### ****Scaling Công thức:****

> Xscaled\=Xi−XminXmax−XminX\_{\\rm {scaled }}=\\frac{X\_{i}-X\_{\\text {min}}}{X\_{\\rm{max}} - X\_{\\rm{min}}}Xscaled​\=Xmax​−Xmin​Xi​−Xmin​ ​

### ****Triển khai****

* ****MinMaxScaler():**** Tạo đối tượng chia tỷ lệ cho Min-Max scaling.
* ****scaler.fit\_transform(df):**** Tính toán các giá trị tối thiểu và tối đa cũng như chia tỷ lệ dataset trong khoảng từ 0 đến 1.

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
scaled_df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-163300](https://media.geeksforgeeks.org/wp-content/uploads/20250829163729653530/Screenshot-2025-08-29-163300.webp "Click to enlarge")

3\. Normalization (Vectơ Normalization)
----------------------------------------

Normalization chia tỷ lệ từng mẫu dữ liệu sao cho độ dài vectơ của nó (chuẩn Euclid) trở thành 1. Nó tập trung vào hướng của các điểm dữ liệu thay vì độ lớn của chúng, khiến nó hữu ích trong các tác vụ như văn bản classification và clustering.

### Công thức Scaling:

> Xscaled\=Xi∥X∥X\_{\\text{scaled}} = \\frac{X\_i}{\\| X \\|}Xscale\=∥X∥Xi​​

****Ở đâu:****

* Xi{X\_i}Xi​ là từng giá trị riêng lẻ.
* ∥X∥{\\| X \\|}∥X∥ đại diện cho chuẩn Euclide (hoặc độ dài) của vectơ XXX.
* Chuẩn hóa từng mẫu theo chiều dài đơn vị.
* Hữu ích cho các số liệu tương tự dựa trên hướng.

### ****Tôi****thực hiện

* ****Normalizer():**** Tạo một đối tượng chuẩn hóa để chia tỷ lệ dữ liệu.
* ****scaler.fit\_transform(df):**** Chuẩn hóa mỗi hàng để độ dài vectơ của nó trở thành 1.

```python
from sklearn.preprocessing import Normalizer
scaler = Normalizer()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
scaled_df.head()
```

****Đầu ra:****

![Screenshot-2025-08-29-163307](https://media.geeksforgeeks.org/wp-content/uploads/20250829163822864358/Screenshot-2025-08-29-163307.webp "Click to enlarge")

4\. Standardization
-------------------

Standardization chia tỷ lệ features bằng cách trừ giá trị trung bình và chia cho độ lệch chuẩn. Điều này biến đổi dữ liệu sao cho features có giá trị trung bình và đơn vị variance bằng 0, giúp nhiều machine learning models hoạt động tốt hơn.

### Công thức Scaling:

> Xscaled\=Xi−μσX\_{\\rm {scaled }}=\\frac{X\_{i}-\\mu}{\\sigma}Xscaled​\=σXi​−μ​

* Trong đó μ\\muμ = trung bình, σ\\sigmaσ = độ lệch chuẩn.
* Tạo ra features với giá trị trung bình là 0 và variance là 1.
* Hiệu quả đối với dữ liệu có phân phối gần đúng.

### ****Tôi****thực hiện

* ****standardScaler()****: Tạo bộ chia tỷ lệ để chuẩn hóa dữ liệu.
* ****scaler.fit\_transform(df)****: Trừ giá trị trung bình và chia cho độ lệch chuẩn.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
columns=df.columns)
print(scaled_df.head())
```

****Đầu ra:****

![Screenshot-2025-08-29-163316](https://media.geeksforgeeks.org/wp-content/uploads/20250829163856753439/Screenshot-2025-08-29-163316.webp "Click to enlarge")

5\. Scaling mạnh mẽ
------------------

Scaling mạnh mẽ chia tỷ lệ features bằng cách sử dụng phạm vi trung vị và liên tứ phân vị (IQR) thay vì giá trị trung bình và độ lệch chuẩn. Điều này làm cho nó ít nhạy cảm hơn với outliers và dữ liệu bị sai lệch, khiến nó phù hợp với datasets có giá trị cực cao hoặc nhiễu.

### Công thức Scaling:

> Xscaled\=Xi−Xmedian IQRX\_{\\rm {scaled }}=\\frac{X\_{i}-X\_{\\text {median }}}{IQR}Xscaled​\=IQRXi​−Xmedian ​ ​

### ****Tôi****thực hiện

* ****RobustScaler()****: Tạo bộ chia tỷ lệ sử dụng trung vị và IQR cho scaling.
* ****scaler.fit\_transform(df)****: Chia tỷ lệ dữ liệu đồng thời giảm ảnh hưởng của outliers.

```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
columns=df.columns)
print(scaled_df.head())
```

****Đầu ra:****

![Screenshot-2025-08-29-163327](https://media.geeksforgeeks.org/wp-content/uploads/20250829163938677961/Screenshot-2025-08-29-163327.webp "Click to enlarge")

So sánh các kỹ thuật Feature Scaling khác nhau
------------------------------------------------

Chúng ta hãy xem những điểm khác biệt chính giữa năm kỹ thuật feature scaling chính thường được sử dụng trong quá trình tiền xử lý machine learning.

Kiểu

Mô tả phương pháp

Độ nhạy với Outliers

Các trường hợp sử dụng điển hình

Scaling tối đa tuyệt đối

Chia giá trị cho giá trị tuyệt đối tối đa trong mỗi feature

Cao

Dữ liệu thưa thớt, scaling đơn giản

Tối thiểu-Tối đa Scaling (Normalization)

Chia tỷ lệ features thành normalization tối thiểu-tối đa

Cao

Neural networks, đầu vào giới hạn features

Normalization (Định mức vectơ)

Chia tỷ lệ từng vectơ mẫu theo chiều dài đơn vị (chuẩn = 1)

Không áp dụng (mỗi hàng)

Tương tự dựa trên hướng, văn bản classification

Standardization (Điểm Z)

Căn giữa features có nghĩa là 0 và chia tỷ lệ thành đơn vị variance

Vừa phải

Hầu hết ML algorithms, giả định khoảng. Dữ liệu bình thường

Scaling mạnh mẽ

Tâm trên trung vị và thang đo bằng IQR

Thấp

Dữ liệu có outliers, phân phối sai lệch

Thuận lợi
----------

* ****Cải thiện hiệu suất Model:**** Nâng cao accuracy và khả năng dự đoán bằng cách trình bày features ở quy mô tương đương.
* ****Tăng tốc độ hội tụ:**** Giúp training algorithms dựa trên độ dốc nhanh hơn và đáng tin cậy hơn.
* ****Ngăn chặn Feature Bias:**** Tránh sự thống trị của features quy mô lớn, đảm bảo sự đóng góp công bằng từ tất cả features.
* ****Tăng tính ổn định về mặt số:**** Giảm nguy cơ tràn/tràn trong tính toán.
* ****Tạo điều kiện thuận lợi cho khả năng tương thích Algorithm:**** Làm cho dữ liệu phù hợp với models dựa trên khoảng cách và độ dốc như SVM, KNN và neural networks.

Câu đố được đề xuất
----------

Mục tiêu chính của feature engineering là gì?

- [ ] A. Tăng lượng dữ liệu có sẵn cho model training
    
- [ ] B. Tạo và chuyển đổi features có liên quan để cải thiện hiệu suất model
    
- [ ] C. Triển khai trực tiếp machine learning models vào hệ thống sản xuất
    
- [ ] D. Loại bỏ tất cả các biến đầu vào khỏi dataset trước training

Scaling tối đa tuyệt đối chia tỷ lệ các giá trị feature trong khoảng

- [ ] A. 0 và 1
    
- [] B. 0 và 100
    
- [ ] C. \-100 và 100
    
- [ ] D. \-1 và 1

Standardization biến đổi features để có

- [ ] A. Phạm vi -1 đến 1
    
- [ ] B. Giá trị trung bình 0 và độ lệch chuẩn 1
    
- [ ] C. Trung vị 0
    
- [ ] D. Chỉ có giá trị dương

Phương pháp scaling nào phù hợp nhất cho datasets có nhiều outliers?

- [ ] A. Tối thiểu-Tối đa Scaling
    
- [ ] B. Scaling tối đa tuyệt đối
    
- [ ] C. Scaling mạnh mẽ
    
- [ ] D. Vectơ Normalization

Tại sao feature scaling lại quan trọng đối với machine learning models?

- [ ] A. Nó ngăn chặn features quy mô lớn thống trị người khác
    
- [ ] B. Nó xóa features không liên quan
    
- [ ] C. Nó tăng kích thước dataset
    
- [ ] D. Nó loại bỏ missing values
