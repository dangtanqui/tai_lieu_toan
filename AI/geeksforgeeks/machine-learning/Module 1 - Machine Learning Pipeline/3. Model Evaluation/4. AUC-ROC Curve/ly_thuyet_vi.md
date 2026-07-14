Đường cong AUC-ROC là một biểu đồ được sử dụng để kiểm tra xem classification model nhị phân hoạt động tốt như thế nào. Nó giúp chúng ta hiểu model phân biệt rõ ràng các trường hợp dương tính như người mắc bệnh với các trường hợp tiêu cực như người không mắc bệnh ở các ngưỡng khác nhau. Nó cho thấy model có khả năng phân biệt sự khác biệt giữa hai lớp bằng cách vẽ đồ thị tốt như thế nào:

* ****Tỷ lệ dương tính thực sự (TPR):**** Tần suất model dự đoán chính xác các trường hợp dương tính còn được gọi là Độ nhạy hoặc Recall.
* ****Tỷ lệ dương tính giả (FPR):**** Tần suất model dự đoán sai một trường hợp âm tính là dương tính.
* ****Độ đặc hiệu:**** Đo tỷ lệ âm tính thực tế mà model xác định chính xác. Nó được tính là 1 - FPR.

`A better model has a higher AUC (Area Under the Curve), which indicates a stronger ability to distinguish between classes.`

![111](https://media.geeksforgeeks.org/wp-content/uploads/20250804094411616734/111.webp "Click to enlarge")

Các thuật ngữ này có nguồn gốc từ [****confusion matrix****](https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/) cung cấp các giá trị sau:

* ****Dương tính thực sự (TP)****: Các trường hợp dương tính được dự đoán chính xác
* ****Âm tính thực sự (TN)****: Các trường hợp âm tính được dự đoán chính xác
* ****Dương tính giả (FP)****: Dự đoán không chính xác là dương tính
* ****Âm tính giả (FN)****: Dự đoán không chính xác là âm tính

![file](https://media.geeksforgeeks.org/wp-content/uploads/20250804094513029606/file.webp "Click to enlarge")

* [****Đường cong ROC****](https://www.geeksforgeeks.org/machine-learning/how-to-plot-roc-curve-in-python/) : Nó vẽ biểu đồ TPR so với FPR ở các ngưỡng khác nhau. Nó thể hiện sự cân bằng giữa độ nhạy và độ đặc hiệu của bộ classification.
* [****AUC(Diện tích dưới đường cong)****](https://www.geeksforgeeks.org/r-language/how-to-calculate-auc-area-under-curve-in-r/): đo diện tích dưới đường cong ROC. Giá trị AUC cao hơn cho thấy hiệu suất model tốt hơn vì nó cho thấy khả năng phân biệt giữa các lớp cao hơn. Giá trị AUC là 1,0 biểu thị hiệu suất hoàn hảo trong khi 0,5 cho thấy đó là đoán ngẫu nhiên.

Hoạt động của AUC-ROC
------------------

Đường cong AUC-ROC giúp chúng ta hiểu được mức độ phân biệt giữa classification model giữa hai lớp. Hãy tưởng tượng chúng ta có 6 điểm dữ liệu và trong số này:

* ****3 thuộc loại tích cực: ***** Loại 1 dành cho người mắc bệnh.
* ****3 thuộc loại tiêu cực: **** Loại 0 dành cho người không mắc bệnh.

![AUC-ROC-Curve](https://media.geeksforgeeks.org/wp-content/uploads/20250206150241961244/AUC-ROC-Curve.webp "Click to enlarge")

Bây giờ model sẽ cung cấp cho mỗi điểm dữ liệu một xác suất dự đoán thuộc về Lớp 1. AUC đo lường khả năng của model trong việc gán xác suất dự đoán cao hơn cho lớp dương so với lớp âm. Đây là cách nó hoạt động:

1. ****Chọn ngẫu nhiên một cặp ****: Chọn một điểm dữ liệu từ lớp dương (Lớp 1) và một điểm dữ liệu từ lớp âm (Lớp 0).
2. ****Kiểm tra xem điểm dương có xác suất dự đoán cao hơn hay không ****: Nếu model gán xác suất cho điểm dữ liệu dương cao hơn điểm âm để xếp hạng chính xác.
3. ****Lặp lại cho tất cả các cặp****: Chúng ta thực hiện việc này cho tất cả các cặp ví dụ tích cực và tiêu cực có thể có.

Khi nào nên sử dụng AUC-ROC
-------------------

AUC-ROC có hiệu quả khi:

* Dataset được cân bằng và model cần được đánh giá trên tất cả các ngưỡng.
* Kết quả dương tính giả và âm tính giả có tầm quan trọng như nhau.

> Trong trường hợp datasets mất cân bằng cao, AUC-ROC có thể cho kết quả quá lạc quan. Trong những trường hợp như vậy, Đường cong Precision-Recall phù hợp hơn khi tập trung vào lớp dương.

Hiệu suất Model với AUC-ROC:

* ****AUC cao (gần 1)****: model phân biệt hiệu quả giữa trường hợp tích cực và tiêu cực.
* ****AUC thấp (gần 0)****: model gặp khó khăn trong việc phân biệt giữa hai lớp.
* ****AUC khoảng 0,5****: model không học bất kỳ mẫu có ý nghĩa nào, tức là nó đang đoán ngẫu nhiên.

Nói tóm lại, AUC cung cấp cho bạn ý tưởng tổng thể về việc model của bạn hoạt động tốt như thế nào trong việc sắp xếp các mặt tích cực và tiêu cực mà không bị ảnh hưởng bởi ngưỡng bạn đặt cho classification. AUC cao hơn có nghĩa là model của bạn đang hoạt động tốt.

Thực hiện bằng cách sử dụng hai models khác nhau
-----------------------------------------

### 1\. Cài đặt thư viện

Chúng ta sẽ nhập [Numpy](https://www.geeksforgeeks.org/python/introduction-to-numpy/), [Pandas](https://www.geeksforgeeks.org/pandas/pandas-tutorial/), [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) và [Học hỏi](https://www.geeksforgeeks.org/machine-learning/learning-model-building-scikit-learn-python-machine-learning-library/).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt from sklearn.datasets import make_classification from sklearn.model_selection import train_test_split from sklearn.linear_model import LogisticRegression from sklearn.ensemble import RandomForestClassifier from sklearn.metrics import roc_curve, auc
```

### 2\. Tạo dữ liệu và phân tách dữ liệu

Sử dụng tỷ lệ phân chia 80-20, algorithm tạo dữ liệu classification nhị phân nhân tạo với 20 features, chia nó thành các bộ training và testing và gán một hạt giống ngẫu nhiên để đảm bảo khả năng tái tạo.

```python
X, y = make_classification(
n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)
```

### 3\. Training models khác nhau

Để training [Random Forest](https://www.geeksforgeeks.org/dsa/random-forest-classifier-using-scikit-learn/) và [Logistic Regression](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/) models, chúng ta sử dụng hạt giống ngẫu nhiên cố định để nhận được kết quả giống nhau mỗi khi chạy mã. Đầu tiên chúng ta training logistic regression model bằng training data. Sau đó, sử dụng cùng training data và hạt giống ngẫu nhiên, chúng ta training Random Forest model với 100 cây.

```python
logistic_model = LogisticRegression(random_state=42)
logistic_model.fit(X_train, y_train)
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)
```

### 4\. Predictions

Sử dụng test data và Logistic Regression model đã được training, mã sẽ dự đoán xác suất của lớp dương. Theo cách tương tự, bằng cách sử dụng test data, nó sử dụng Random Forest model đã được training để tạo ra xác suất dự kiến ​​cho lớp tích cực.

```python
y_pred_logistic = logistic_model.predict_proba(X_test)[:, 1]
y_pred_rf = random_forest_model.predict_proba(X_test)[:, 1]
```

### 5\. Tạo một khung dữ liệu

Bằng cách sử dụng test data, mã sẽ tạo một DataFrame có tên test\_df với các cột được gắn label "Đúng", "Logistic" và "RandomForest", thêm labels thực và xác suất được dự đoán từ Random Forest và Logistic Regression models.

```python
test_df = pd.DataFrame(
{'True': y_test, 'Logistic': y_pred_logistic, 'RandomForest': y_pred_rf})
```

### 6\. Vẽ đường cong ROC cho models

Vẽ đường cong ROC và tính AUC cho cả Logistic Regression và Random Forest. Đường cong ROC so sánh models dựa trên Tỷ lệ dương tính thực và Tỷ lệ dương tính giả, trong khi đường đứt nét màu đỏ hiển thị đoán ngẫu nhiên.

```python
plt.figure(figsize=(7, 5))
for model in ['Logistic', 'RandomForest']:
fpr, tpr, _ = roc_curve(test_df['True'], test_df[model])
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, label=f'{model} (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'r--', label='Random Guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves for Two Models')
plt.legend()
plt.show()
```

****Đầu ra:****

![roc-Geeksforgeeks](https://media.geeksforgeeks.org/wp-content/uploads/20231206153808/roc.png "Click to enlarge")

Biểu đồ tính toán đường cong AUC và ROC cho mỗi model, tức là Random Forest và Logistic Regression, sau đó vẽ đường cong ROC. Đường cong ROC để đoán ngẫu nhiên cũng được biểu thị bằng đường đứt nét màu đỏ và labels, tiêu đề và chú giải được đặt để trực quan hóa.

AUC-ROC dành cho Model nhiều lớp
-------------------------------

Đối với classification nhiều lớp, AUC-ROC được mở rộng bằng cách sử dụng phương pháp Một đấu với Tất cả (OvA). Mỗi lớp được coi là lớp tích cực một lần và các lớp còn lại được nhóm thành lớp tiêu cực. Ví dụ: nếu bạn có các lớp A, B, C, D, bạn sẽ nhận được bốn đường cong ROC cho mỗi lớp:

* Loại A so với (B, C, D)
* Lớp B so với (A, C, D)
* Lớp C so với (A, B, D)
* Lớp D so với (A, B, C)

### Các bước sử dụng AUC-ROC cho Models đa lớp

****1\. Chuyển đổi một đấu với tất cả:**** Coi mỗi lớp là lớp tích cực và tất cả các lớp khác được kết hợp thành lớp tiêu cực.

****2\. Training Trình classification nhị phân cho mỗi Lớp: ***** Lắp model riêng biệt cho từng kết hợp giữa lớp và phần còn lại.

****3\. Tính AUC-ROC cho mỗi lớp:****

* Vẽ đường cong ROC cho mỗi lớp
* Tính giá trị AUC cho từng đường cong

****4\. So sánh hiệu suất:**** Điểm AUC cao hơn có nghĩa là model có khả năng phân biệt loại đó tốt hơn với các loại khác.

Triển khai AUC-ROC trong Classification đa lớp
------------------------------------------------------

### 1\. Nhập thư viện

Chương trình tạo dữ liệu đa lớp nhân tạo, chia nó thành các bộ training và testing, sau đó sử dụng kỹ thuật [Trình classification một vs Restclassifier](https://www.geeksforgeeks.org/machine-learning/one-vs-rest-strategy-for-multi-class-classification/) để training các bộ classification cho cả Random Forest và Logistic Regression. Nó vẽ đồ thị hai đường cong ROC đa lớp models để chứng minh chúng phân biệt tốt như thế nào giữa các lớp khác nhau.

```python
import numpy as np
import matplotlib.pyplot as plt from sklearn.datasets import make_classification from sklearn.model_selection import train_test_split from sklearn.preprocessing import label_binarize from sklearn.multiclass import OneVsRestClassifier from sklearn.linear_model import LogisticRegression from sklearn.ensemble import RandomForestClassifier from sklearn.metrics import roc_curve, auc from itertools import cycle
```

### 2\. Tạo dữ liệu và phân chia

Ba lớp và 20 features tạo nên dữ liệu đa lớp tổng hợp do mã tạo ra. Sau khi nhị phân hóa label, dữ liệu được chia thành các bộ training và testing theo tỷ lệ 80-20.

```python
X, y = make_classification(
n_samples=1000, n_features=20, n_classes=3, n_informative=10, random_state=42)
y_bin = label_binarize(y, classes=np.unique(y))
X_train, X_test, y_train, y_test = train_test_split(
X, y_bin, test_size=0.2, random_state=42)
```

### 3\. Training Models

Chương trình training hai models nhiều lớp, tức là Random Forest model với 100 công cụ ước tính và Logistic Regression model với phương pháp Một đấu với Phần còn lại. Với dữ liệu training set, cả models đều được trang bị.

```python
logistic_model = OneVsRestClassifier(LogisticRegression(random_state=42))
logistic_model.fit(X_train, y_train)
rf_model = OneVsRestClassifier(
RandomForestClassifier(n_estimators=100, random_state=42))
rf_model.fit(X_train, y_train)
```

### 4\. Vẽ đường cong AUC-ROC

Các đường cong ROC và điểm AUC cho mỗi lớp được tính toán và vẽ đồ thị cho cả models. Một đường đứt nét biểu thị khả năng đoán ngẫu nhiên, giúp trực quan hóa mức độ phân tách của mỗi model giữa nhiều lớp.

```python
fpr = dict()
tpr = dict()
roc_auc = dict()
models = [logistic_model, rf_model]
plt.figure(figsize=(6, 5))
colors = cycle(['aqua', 'darkorange'])
for model, color in zip(models, colors):
for i in range(model.classes_.shape[0]):
fpr[i], tpr[i], _ = roc_curve(
y_test[:, i], model.predict_proba(X_test)[:, i])
roc_auc[i] = auc(fpr[i], tpr[i])
plt.plot(fpr[i], tpr[i], color=color, lw=2,
label=f'{model.__class__.__name__} - Class {i} (AUC = {roc_auc[i]:.2f})')
plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass ROC Curve with Logistic Regression and Random Forest')
plt.legend(loc="lower right")
plt.show()
```

****Đầu ra:****

![multi-Geeksforgeeks](https://media.geeksforgeeks.org/wp-content/uploads/20231206155921/multi.png "Click to enlarge")

* Đường cong Random Forest và Logistic Regression models ROC và điểm AUC được tính theo mã cho từng hạng.
* Sau đó, các đường cong ROC đa lớp được vẽ biểu thị khả năng phân biệt đối xử của từng lớp và có một đường biểu thị khả năng đoán ngẫu nhiên.
* Sơ đồ kết quả cung cấp đánh giá đồ họa về hiệu suất classification của models.

Câu đố được đề xuất
----------

AUC-ROC hữu ích trong việc đánh giá loại models nào?

- [ ] A. Giảm kích thước models
    
- [ ] B. Classification models
    
- [ ] C. Regression models
    
- [ ] D. Clustering models

Đường cong ROC thể hiện điều gì để đánh giá classification model?

- [ ] A. Accuracy so với tính đặc hiệu
    
- [ ] B. Precision vs Accuracy
    
- [ ] C. Tỷ lệ dương tính thật và tỷ lệ dương tính giả
    
- [ ] D. Precision vs Recall

Giá trị AUC là 0,5 cho biết điều gì đối với classification model?

- [ ] A. Hiệu suất xuất sắc
    
- [ ] B. Model là overfitting
    
- [ ] C. Classification hoàn hảo
    
- [ ] D. Giống như đoán ngẫu nhiên
