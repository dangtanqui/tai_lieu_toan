Feature Engineering là quá trình chọn, tạo hoặc sửa đổi features giống như các biến hoặc dữ liệu đầu vào để giúp machine learning models học các mẫu hiệu quả hơn. Nó liên quan đến việc chuyển đổi dữ liệu thô thành đầu vào có ý nghĩa để cải thiện hiệu suất và model accuracy.

![feature-engineering](https://media.geeksforgeeks.org/wp-content/uploads/20250701114435618562/feature-engineering.webp "Click to enlarge")

Bước này có thể bao gồm việc xử lý các danh mục missing values, encoding, số scaling, tạo features mới hoặc kết hợp các danh mục hiện có. Nó giúp biến dữ liệu lộn xộn trong thế giới thực thành dạng mà models có thể hiểu và sử dụng để predictions tốt hơn.

### Tầm quan trọng của Feature Engineering

* ****Cải thiện accuracy****: Việc chọn đúng features giúp model học tốt hơn, dẫn đến predictions chính xác hơn.
* ****Giảm overfitting****: Sử dụng features ít hơn, quan trọng hơn giúp model tránh việc ghi nhớ dữ liệu và hoạt động tốt hơn trên dữ liệu mới.
* ****Tăng cường khả năng diễn giải****: features được lựa chọn kỹ lưỡng giúp bạn dễ hiểu hơn về cách model tạo ra predictions của nó.
* ****Nâng cao hiệu quả****: Tập trung vào features chính sẽ tăng tốc quá trình training và prediction của model, tiết kiệm thời gian và tài nguyên.

Các quy trình liên quan đến Feature Engineering
-----------------------------------------

Hãy xem các features khác nhau có liên quan đến feature engineering:

![processes](https://media.geeksforgeeks.org/wp-content/uploads/20250701123223591115/processes.webp "Click to enlarge")

****1\. Tạo Feature****: Việc tạo Feature liên quan đến việc tạo features mới từ kiến ​​thức miền hoặc bằng cách quan sát các mẫu trong dữ liệu. Nó có thể là:

* ****Dành riêng cho miền****: Được tạo dựa trên kiến ​​thức ngành như các quy tắc kinh doanh.
* ****Dựa trên dữ liệu****: Bắt nguồn bằng cách nhận dạng các mẫu trong dữ liệu.
* ****Tổng hợp****: Được hình thành bằng cách kết hợp features hiện có.

****2\. Chuyển đổi Feature****: Chuyển đổi điều chỉnh features để cải thiện việc học model:

* ****Normalization & Scaling****: Điều chỉnh phạm vi của features cho nhất quán.
* ****Encoding****: Chuyển đổi dữ liệu classification sang dạng số, tức là one-hot encoding.
* ****Các phép biến đổi toán học****: Giống như các phép biến đổi logarit cho dữ liệu bị lệch.

****3\. Feature Extraction****: Chuyển đổi features hiện có thành dạng trình bày có chiều thấp hơn hoặc nhiều thông tin hơn (ví dụ: PCA).

* ****Giảm kích thước****: Các kỹ thuật như PCA giảm features trong khi vẫn giữ được thông tin quan trọng.
* ****Tổng hợp & Kết hợp****: Tính tổng hoặc lấy trung bình features để đơn giản hóa model.

****4\. Feature Selection****: Feature selection liên quan đến việc chọn một tập hợp con features có liên quan để sử dụng:

* ****Phương pháp lọc****: Dựa trên các biện pháp thống kê như tương quan.
* ****Các phương pháp trình bao bọc****: Chọn dựa trên hiệu suất của model.
* ****Các phương pháp nhúng****: Feature selection được tích hợp trong model training.

****5\. Feature Scaling****: Scaling đảm bảo rằng tất cả features đều đóng góp như nhau cho model:

* ****Min-Max scaling****: Thay đổi tỷ lệ các giá trị thành một phạm vi cố định như 0 đến 1.
* ****scaling tiêu chuẩn****: Chuẩn hóa features để có giá trị trung bình là 0 và variance 1

Các bước trong Feature Engineering
----------------------------

Feature engineering có thể khác nhau tùy theo vấn đề cụ thể nhưng các bước chung là:

1. ****Data Cleaning:**** Xác định và sửa các lỗi hoặc sự không nhất quán trong dataset để đảm bảo chất lượng và độ tin cậy của dữ liệu.
2. ****Chuyển đổi dữ liệu:**** Chuyển đổi dữ liệu thô sang định dạng phù hợp để lập model bao gồm scaling, normalization và encoding.
3. ****Feature Extraction:**** Tạo features mới bằng cách kết hợp hoặc lấy thông tin từ những thông tin hiện có để cung cấp đầu vào có ý nghĩa hơn cho model.
4. ****Feature Selection:**** Chọn features phù hợp nhất cho model bằng cách sử dụng các kỹ thuật như phân tích tương quan, thông tin lẫn nhau và regression từng bước.
5. ****Feature Lặp lại:**** Liên tục tinh chỉnh features dựa trên hiệu suất của model bằng cách thêm, xóa hoặc sửa đổi features để cải thiện.

Các kỹ thuật phổ biến trong Feature Engineering
----------------------------------------

****1\. One-Hot Encoding****: [One-Hot Encoding](https://www.geeksforgeeks.org/machine-learning/ml-one-hot-encoding/) chuyển đổi các biến classification thành các chỉ báo nhị phân, cho phép machine learning models sử dụng chúng.

```python
import pandas as pd
data = {'Color': ['Red', 'Blue', 'Green', 'Blue']} df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['Color'], prefix='Color')
print(df_encoded)
```

**Đầu ra**

|   | Color_Blue | Color_Green | Color_Red |
| - | ---------- | ----------- | --------- |
| 0 | False      | False       | True      |
| 1 | True       | False       | False     |
| 2 | False      | True        | False     |
| 3 | True       | False       | False     |

****2\. Binning****: [Thùng](https://www.geeksforgeeks.org/machine-learning/binning-in-data-mining/) chuyển đổi các biến liên tục thành các thùng rời rạc, biến chúng thành các classification để phân tích dễ dàng hơn.

```python
import pandas as pd
data = {'Age': [23, 45, 18, 34, 67, 50, 21]} df = pd.DataFrame(data)
bins = [0, 20, 40, 60, 100]
labels = ['0-20', '21-40', '41-60', '61+']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
print(df)
```

**Đầu ra**

|   | Age | Age_Group |
| - | --- | --------- |
| 0 | 23  | 21-40     |
| 1 | 45  | 41-60     |
| 2 | 18  | 0-20      |
| 3 | 34  | 21-40     |
| 4 | 67  | 61+       |
| 5 | 50  | 41-60     |
| 6 | 21  | 21-40     |

****3\. Văn bản Data Preprocessing****: Liên quan đến việc xóa dữ liệu văn bản [Từ dừng](https://www.geeksforgeeks.org/nlp/removing-stop-words-nltk-python/), [Nhét đầy](https://www.geeksforgeeks.org/machine-learning/introduction-to-stemming/) và [Vector hóa](https://www.geeksforgeeks.org/nlp/vectorization-techniques-in-nlp/) để chuẩn bị cho machine learning models.

```python
import nltk from nltk.corpus import stopwords from nltk.stem import PorterStemmer from sklearn.feature_extraction.text import CountVectorizer
texts = ["This is a sample sentence.", "Text data preprocessing is important."]
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
vectorizer = CountVectorizer()
def preprocess_text(text):
words = text.split()
words = [stemmer.stem(word)
for word in words if word.lower() not in stop_words]
return " ".join(words)
cleaned_texts = [preprocess_text(text) for text in texts]
X = vectorizer.fit_transform(cleaned_texts)
print("Cleaned Texts:", cleaned_texts)
print("Vectorized Text:", X.toarray())
```

****Đầu ra:****

![output](https://media.geeksforgeeks.org/wp-content/uploads/20250701113324922110/output.webp "Click to enlarge")

****4\. Tách Feature****: Chia một feature thành nhiều features phụ, khám phá những hiểu biết sâu sắc có giá trị và cải thiện hiệu suất model.

```python
import pandas as pd
data = {'Full_Address': [
'123 Elm St, Springfield, 12345', '456 Oak Rd, Shelbyville, 67890']} df = pd.DataFrame(data)
df[['Street', 'City', 'Zipcode']] = df['Full_Address'].str.extract(
r'([0-9]+\s[\w\s]+),\s([\w\s]+),\s(\d+)')
print(df)
```

**Đầu ra**

|   | Full_Address                   | Street     | City        | Zipcode |
| - | ------------------------------ | ---------- | ----------- | ------- |
| 0 | 123 Elm St, Springfield, 12345 | 123 Elm St | Springfield | 12345   |
| 1 | 456 Oak Rd, Shelbyville, 67890 | 456 Oak Rd | Shelbyville | 67890   |

Công cụ dành cho Feature Engineering
-----------------------------

* ****Công cụ tính năng****: Tự động tạo feature từ dữ liệu có cấu trúc với khả năng tích hợp thư viện dễ dàng.
* ****TPOT****: Sử dụng algorithms di truyền để tối ưu hóa pipelines và feature selection.
* ****DataRobot****: Tự động hóa quy trình làm việc của ML với sự hỗ trợ cho nhiều loại dữ liệu và làm việc nhóm.
* ****Alteryx****: Cung cấp giao diện kéo và thả để chuẩn bị dữ liệu và feature engineering.
* ****H2O.ai:**** Cung cấp các công cụ cho feature engineering, scaling, encoding và trực quan hóa.

Câu đố được đề xuất
----------

Feature Engineering giúp giảm overfitting như thế nào?

- [ ] A. Bằng cách tăng kích thước dataset
    
- [ ] B. Bằng cách sử dụng features ít hơn nhưng quan trọng hơn
    
- [ ] C. Bằng cách thay thế training dataset
    
- [ ] D. Bằng cách loại bỏ tất cả các phép biến đổi dữ liệu

Mục đích của việc tạo Feature trong Feature Engineering là gì?

- [ ] A. Scaling biến số thành một phạm vi chung
    
- [ ] B. Chia datasets thành bộ training và testing
    
- [ ] C. Tạo features mới bằng cách sử dụng các mẫu hoặc kiến thức về miền
    
- [ ] D. Loại bỏ machine learning models hoạt động kém hiệu quả

Phương pháp nào thay đổi tỷ lệ các giá trị feature thành một phạm vi cố định, chẳng hạn như 0 đến 1?

- [ ] A. Tối thiểu-Tối đa scaling
    
- [ ] B. Scaling tiêu chuẩn
    
- [ ] C. Feature extraction
    
- [ ] D. Đóng thùng

Bước nào trong feature engineering tập trung vào việc chọn features phù hợp nhất?

- [ ] A. Feature Selection
    
- [ ] B. Feature Scaling
    
- [ ] C. Tách Feature
    
- [ ] D. Phép biến đổi Feature

Mục đích của việc lặp lại Feature là gì?

- [ ] A. Triển khai machine learning models đã training vào sản xuất
    
- [ ] B. Tạo và gắn label datasets cho model training
    
- [ ] C. Tổ chức và lưu trữ dữ liệu trong hệ thống cơ sở dữ liệu
    
- [ ] D. Tinh chỉnh liên tục features dựa trên hiệu suất model
