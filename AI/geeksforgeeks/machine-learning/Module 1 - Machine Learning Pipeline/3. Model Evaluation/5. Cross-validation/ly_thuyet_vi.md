Cross-validation là một kỹ thuật được sử dụng để kiểm tra xem machine learning model hoạt động tốt như thế nào trên dữ liệu không nhìn thấy được trong khi ngăn chặn overfitting. Nó hoạt động bằng cách:

* Chia dataset thành nhiều phần.
* Training model trên một số phần và testing trên phần còn lại.
* Lặp lại quá trình lấy mẫu lại này nhiều lần bằng cách chọn các phần khác nhau của dataset.
* Tính trung bình kết quả từ mỗi bước validation để có hiệu suất cuối cùng.

Kỹ thuật Validation
---------------------

### ****1\. Giữ Validation****

Trong [Giữ lại Validation](https://www.geeksforgeeks.org/software-engineering/introduction-of-holdout-method/), dataset được chia thành các bộ training và testing. Các mức phân chia phổ biến bao gồm 70–30, 80–20 hoặc 75–25 tùy thuộc vào kích thước và vấn đề của dataset. Làm cho nó đơn giản và nhanh chóng để áp dụng.

### ****2\. LOOCV (Bỏ lại một Cross Validation)****

Trong phương pháp này, model được training trên toàn bộ dataset ngoại trừ một điểm dữ liệu được sử dụng cho testing. Quá trình này được lặp lại cho từng điểm dữ liệu trong dataset.

* Tất cả các điểm dữ liệu được sử dụng cho training, dẫn đến bias thấp.
* Testing trên một điểm dữ liệu có thể gây ra variance cao, đặc biệt nếu điểm đó là outlier.
* Việc này có thể rất tốn thời gian đối với datasets lớn vì nó yêu cầu một lần lặp cho mỗi điểm dữ liệu.

### ****3\. Cross-Validation phân tầng ****

Đây là một kỹ thuật đảm bảo mỗi lần của quy trình cross-validation có cùng phân bổ lớp với dataset đầy đủ. Điều này hữu ích cho datasets mất cân bằng trong đó một số lớp được trình bày không đầy đủ.

* Dataset được chia thành k nếp gấp, giữ tỷ lệ lớp nhất quán trong mỗi nếp gấp.
* Trong mỗi lần lặp lại, một nếp gấp được sử dụng cho testing và các nếp gấp còn lại cho training.
* Quá trình này được lặp lại k lần sao cho mỗi lần gấp được sử dụng một lần làm test set.
* Nó giúp classification models khái quát hóa tốt hơn bằng cách duy trì sự biểu diễn lớp cân bằng.

### ****4\. K-Fold Cross Validation****

[K-Fold Cross Validation](https://www.geeksforgeeks.org/r-language/k-fold-cross-validation-in-r-programming/) chia dataset thành __k__ các nếp gấp có kích thước bằng nhau. Model được training trên các nếp gấp __k-1__ và được thử nghiệm trên nếp gấp còn lại. Quá trình này được lặp lại __k__ lần mỗi lần bằng cách sử dụng một cách gấp khác nhau cho testing.

> _****Lưu ý:****_ Giá trị k thường được sử dụng là 10, nhưng việc lựa chọn phụ thuộc vào kích thước dataset và yêu cầu của bài toán.

### 5\. K-Fold Cross Validation lặp đi lặp lại

Phương pháp này lặp lại quy trình K-Fold cross-validation nhiều lần với các lần phân chia ngẫu nhiên khác nhau. Nó giúp giảm tác động của tính ngẫu nhiên trong việc phân tách dữ liệu và cung cấp ước tính hiệu suất mạnh mẽ hơn.

* Dataset được chia thành k lần nhiều lần.
* Mỗi lần lặp lại sử dụng một cách xáo trộn ngẫu nhiên khác nhau.
* Hiệu suất cuối cùng được tính trung bình trên tất cả các lần lặp lại.
* Nó rất hữu ích để cải thiện độ tin cậy trong đánh giá model.

****Ví dụ**** của K Fold Cross Validation
------------------------------------------

Sơ đồ bên dưới hiển thị ví dụ về các tập hợp con training và các tập hợp con đánh giá được tạo trong cross-validation gấp k lần. Ở đây chúng ta có tổng cộng 25 trường hợp.

![222](https://media.geeksforgeeks.org/wp-content/uploads/20250927122541290704/222.webp "Click to enlarge")

* Ở đây ta sẽ lấy k là 5.
* ****Lần lặp thứ nhất:**** 20% dữ liệu đầu tiên \[1–5\] được sử dụng cho testing và 80% còn lại \[6–25\] được sử dụng cho training.
* ****Lần lặp thứ 2:**** 20% \[6–10\] thứ hai được sử dụng cho testing và dữ liệu còn lại \[1–5\] và \[11–25\] được sử dụng cho training.
* Quá trình này tiếp tục cho đến khi mỗi nếp gấp được sử dụng một lần làm test set.

Lặp lại

Quan sát Training Set

Quan sát tập hợp Testing

1

\[5-24\]

\[0-4\]

2

\[0-4, 10-24\]

\[5-9\]

3

\[0-9, 15-24\]

\[10-14\]

4

\[0-14, 20-24\]

\[15-19\]

5

\[0-19\]

\[20-24\]

Mỗi lần lặp lại sử dụng các tập hợp con khác nhau cho testing và training, đảm bảo rằng tất cả các điểm dữ liệu được sử dụng cho cả training và testing.

So sánh giữa phương pháp K-Fold Cross-Validation và phương pháp Hold Out
--------------------------------------------------------------

K-Fold Cross-Validation và Hold Out Method là những kỹ thuật được sử dụng và đôi khi chúng gây nhầm lẫn nên đây là so sánh nhanh giữa chúng:

Feature

K-Fold Cross-Validation

Phương pháp giữ lại

****Chia tách dữ liệu****

Dataset được chia thành k nếp gấp và mỗi nếp gấp được sử dụng một lần làm test set

Dataset được chia một lần, thường thành các bộ training và testing

****Training & Testing****

Model được training và kiểm tra k lần, mỗi lần đóng vai trò là test set một lần

Model được training một lần trên training set và được thử nghiệm một lần trên test set

****Bias & Variance****

Bias thấp hơn, ước tính hiệu suất đáng tin cậy hơn và variance phụ thuộc vào k

Bias cao hơn nếu sự phân chia không mang tính đại diện và kết quả có thể thay đổi đáng kể

****Thời gian thực hiện****

Chậm hơn, đặc biệt đối với datasets lớn vì model được training k lần

Nhanh hơn, chỉ có một chu kỳ training và testing

****Trường hợp sử dụng tốt nhất****

Datasets nhỏ đến trung bình trong đó việc ước tính accuracy là quan trọng

Datasets rất lớn hoặc khi cần đánh giá nhanh

Triển khai Python cho cross-validation k gấp
--------------------------------------------------

### Bước 1: Import các thư viện cần thiết

Chúng ta sẽ nhập các mô-đun thiết yếu từ [Scikit-learn](https://www.geeksforgeeks.org/machine-learning/learning-model-building-scikit-learn-python-machine-learning-library/).

* Cross\_val\_score giúp đánh giá hiệu suất model bằng cross-validation.
* KFold chia dữ liệu thành các phần xác định.
* SVC được sử dụng cho Vector hỗ trợ Classification.
*load\_iris tải mẫu dataset.

```python
from sklearn.model_selection import cross_val_score, KFold from sklearn.svm import SVC from sklearn.datasets import load_iris
```

### Bước 2: Đang tải dataset

Chúng ta sẽ sử dụng Iris dataset một dataset đa lớp tích hợp sẵn với 150 mẫu và 3 loài hoa (Setosa, Versicolor và Virginica).

```python
iris = load_iris() X, y = iris.data, iris.target
```

### Bước 3: Tạo bộ classification SVM

SVC() từ scikit-learn được sử dụng để xây dựng Support Vector Machine model. Ở đây, chúng ta đang sử dụng kernel tuyến tính, phù hợp với dữ liệu có thể phân tách tuyến tính.

```python
svm_classifier = SVC(kernel='linear')
```

### Bước 4: Xác định số lần gấp cho cross-validation

Chúng ta xác định 5 nếp gấp, nghĩa là dataset sẽ được chia thành 5 phần. Model sẽ training 4 phần và kiểm tra 1 phần, lặp lại quy trình này 5 lần để đánh giá cân bằng.

```python
num_folds = 5 kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)
```

### Bước 5: Thực hiện cross-validation gấp k lần

Chúng ta sử dụng cross\_val\_score() để tự động phân chia dữ liệu, training và đánh giá model trên tất cả các màn hình đầu tiên. Nó trả về accuracy cho mỗi lần gấp

```python
cross_val_results = cross_val_score(svm_classifier, X, y, cv=kf)
```

### Bước 6: Các chỉ số đánh giá

Chúng ta in accuracy của từng nếp gấp và accuracy trung bình trên tất cả các nếp gấp để hiểu tính ổn định và tổng quát của model.

```python
print("Cross-Validation Results (Accuracy):") for i, result in enumerate(cross_val_results, 1):
print(f"
Fold {i}: {result * 100:.2f}%")
print(f'Mean Accuracy: {cross_val_results.mean()* 100:.2f}%')
```

****Đầu ra:****

![Cross-validation-accuracy](https://media.geeksforgeeks.org/wp-content/uploads/20250508172030797636/Cross-validation-accuracy.png "Click to enlarge")

Đầu ra hiển thị điểm accuracy từ mỗi lần trong số 5 lần gấp trong quy trình cross-validation gấp K. Accuracy trung bình là mức trung bình của các điểm riêng lẻ này, xấp xỉ 97,33% cho thấy hiệu suất tổng thể của model trên tất cả các màn hình.

Thuận lợi
----------

1. ****Ước tính hiệu suất tốt hơn:**** Cung cấp đánh giá đáng tin cậy hơn so với một train-test split đơn lẻ.
2. ****Giảm overfitting:**** Giúp đảm bảo model khái quát hóa tốt các dữ liệu không nhìn thấy.
3. ****Sử dụng dữ liệu hiệu quả:**** Tất cả các điểm dữ liệu được sử dụng cho cả training và testing ở các lần lặp khác nhau.
4. ****Linh hoạt:**** Hoạt động với các loại datasets và models khác nhau.

Nhược điểm
-------------

1. **** Đắt về mặt tính toán: **** Nó có thể tốn kém về mặt tính toán, đặc biệt khi số lần gấp lớn.
2. ****Tốn thời gian:**** Các phương pháp như LOOCV có thể mất nhiều thời gian đối với datasets với nhiều phiên bản dữ liệu.
3. ****Bias-Variance Sự cân bằng:**** Ít nếp gấp có thể dẫn đến bias cao trong khi quá nhiều nếp gấp có thể dẫn đến variance cao.

Câu đố được đề xuất
----------

Mục đích của cross-validation trong machine learning là gì?

- [ ] A. Làm cho model trở nên phức tạp hơn
    
- [ ] B. Lựa chọn features tốt nhất
    
- [ ] C. Testing model ổn định và giảm overfitting
    
- [ ] D. Cải thiện tốc độ training

Điều nào sau đây là ưu điểm chính của K-Fold Cross-Validation?

- [ ] A. Yêu cầu một train-test split duy nhất để đánh giá
    
- [ ] B. Cung cấp ước tính ổn định hơn bằng cách lấy kết quả trung bình trên các lần gấp
    
- [ ] C. Hoàn thành đánh giá nhanh hơn phương pháp nắm giữ
    
- [ ] D. Chỉ hoạt động tốt khi datasets được cân bằng hoàn hảo

Loại cross-validation nào đảm bảo rằng mỗi lần xếp duy trì sự phân bổ lớp giống như dataset đầy đủ?

- [ ] A. Cross-Validation phân tầng
    
- [ ] B. K-Fold Cross-Validation
    
- [ ] C. Giữ lại Validation
    
- [ ] D. LOOCV

Kỹ thuật cross-validation nào training model trên tất cả dữ liệu ngoại trừ một phiên bản trong mỗi lần lặp?

- [ ] A. Giữ lại Validation
    
- [ ] B. K-Fold Cross-Validation
    
- [ ] C. LOOCV
    
- [ ] D. Validation phân tầng

Tại sao K-Fold Cross-Validation thường được ưa chuộng hơn phương pháp Holdout?

- [ ] A. Sử dụng một phần dữ liệu nhỏ hơn cho model training
    
- [ ] B. Ước tính hiệu suất đáng tin cậy hơn
    
- [ ] C. Chỉ training model một lần trước khi đánh giá
    
- [ ] D. Được thiết kế dành riêng cho datasets rất nhỏ
