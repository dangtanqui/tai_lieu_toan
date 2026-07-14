Confusion matrix là một bảng đơn giản được sử dụng để đo lường mức độ hoạt động của classification model. Nó so sánh predictions do model tạo ra với kết quả thực tế và cho biết model đúng hay sai ở đâu. Điều này giúp bạn hiểu model đang mắc lỗi ở đâu để bạn có thể cải thiện. Nó chia predictions thành bốn loại:

* ****Dương tính thực sự (TP):**** model đã dự đoán chính xác một kết quả dương tính, tức là kết quả thực tế là dương tính.
* ****Âm tính thực sự (TN):**** model đã dự đoán chính xác một kết quả âm tính, tức là kết quả thực tế là âm tính.
* ****Dương tính giả (FP):**** model dự đoán không chính xác một kết quả dương tính, tức là kết quả thực tế là âm tính. Nó còn được gọi là lỗi Loại I.
* ****Âm tính giả (FN):**** model dự đoán không chính xác một kết quả âm tính, tức là kết quả thực tế là dương tính. Nó còn được gọi là lỗi Loại II.

![predicted_condition_2_](https://media.geeksforgeeks.org/wp-content/uploads/20250530174111874391/predicted_condition_2_.webp "Click to enlarge")

Nó cũng giúp tính toán các thước đo chính như ****accuracy****, ****precision**** và ****recall**** để đưa ra ý tưởng tốt hơn về hiệu suất, đặc biệt là khi dữ liệu mất cân bằng.

Số liệu dựa trên dữ liệu Confusion Matrix
--------------------------------------

### 1\. Accuracy

[Accuracy](https://www.geeksforgeeks.org/data-analysis/techniques-to-evaluate-accuracy-of-classifier-in-data-mining/) hiển thị số lượng predictions mà model đã lấy được trong số tất cả predictions. Nó đưa ra ý tưởng về hiệu suất tổng thể nhưng có thể gây hiểu nhầm khi một lớp chiếm ưu thế hơn lớp kia. Ví dụ: model dự đoán chính xác lớp đa số trong hầu hết thời gian có thể có accuracy cao nhưng vẫn không nắm bắt được các chi tiết quan trọng về các lớp khác. Nó có thể được tính bằng công thức dưới đây:

> Accuracy\=TP+TNTP+TN+FP+FN\\text{Accuracy} = \\frac {TP+TN}{TP+TN+FP+FN}Accuracy\=TP+TN+FP+FNTP+TN​

### 2\. Precision

[Precision](https://www.geeksforgeeks.org/machine-learning/precision-and-recall-in-machine-learning/) tập trung vào chất lượng predictions tích cực của model. Nó cho chúng ta biết có bao nhiêu predictions "tích cực" thực sự đúng. Điều quan trọng là trong các tình huống cần giảm thiểu kết quả dương tính giả, chẳng hạn như phát hiện email spam hoặc lừa đảo. Công thức của precision là:

> Precision\=TPTP+FP\\text{Precision} = \\frac{TP}{TP+FP}Precision\=TP+FPTP​

### 3\. Recall

[Recall](https://www.geeksforgeeks.org/machine-learning/precision-recall-curve-ml/) đo lường khả năng dự đoán tích cực của model. Nó cho thấy tỷ lệ các trường hợp dương tính thực sự được phát hiện trong số tất cả các trường hợp dương tính thực tế. Recall cao là điều cần thiết khi thiếu các trường hợp dương tính gây hậu quả nghiêm trọng như trong các xét nghiệm y tế.

> Recall\=TPTP+FN\\text{Recall} = \\frac{TP}{TP+FN}Recall\=TP+FNTP​

### 4\. Điểm F1

[Điểm F1](https://www.geeksforgeeks.org/r-language/precision-recall-and-f1-score-using-r/) kết hợp precision và recall thành một số liệu duy nhất để cân bằng sự đánh đổi của chúng. Nó mang lại cảm giác tốt hơn về hiệu suất tổng thể của model, đặc biệt đối với datasets mất cân bằng. Sẽ rất hữu ích khi cả kết quả dương tính giả và âm tính giả đều quan trọng mặc dù nó giả định precision và recall đều quan trọng như nhau nhưng trong một số trường hợp, cái này có thể quan trọng hơn cái kia.

> Điểm F1\=2⋅Precision⋅RecallPrecision+Recall\\text{F1-Điểm} = \\frac {2 \\cdot Precision \\cdot Recall}{Precision + Recall}F1-Điểm\=Precision+Thu hồi2⋅Precision⋅Recall​

### 5\. Tính đặc hiệu

[Tính đặc hiệu](https://www.geeksforgeeks.org/r-language/calculate-sensitivity-specificity-and-predictive-values-in-caret/) là một số liệu quan trọng khác trong việc đánh giá classification models, đặc biệt là ở classification nhị phân. Nó đo lường khả năng của model trong việc xác định chính xác các trường hợp tiêu cực. Độ đặc hiệu còn được gọi là Công thức tỷ lệ âm tính thực được đưa ra bởi:

> Độ đặc hiệu\=TNTN+FP\\text{Độ đặc hiệu} = \\frac{TN}{TN+FP}Độ đặc hiệu\=TN+FPTN​

### ****6\. Lỗi loại 1 và loại 2****

Lỗi [Loại 1 và Loại 2](https://www.geeksforgeeks.org/data-science/type-i-and-type-ii-errors/) là:

* ****Lỗi loại 1****: Xảy ra khi model dự đoán sai một trường hợp dương nhưng trường hợp thực tế lại là âm. This is also known as a ****false positive****. Lỗi Loại 1 ảnh hưởng đến ****precision**** của model đo accuracy của predictions dương.

> Loại 1 Lỗi\=FPFP+TN\\text{Lỗi loại 1} = \\frac{\\text{FP}}{\\text{FP} + \\text{TN}}Loại 1 Lỗi\=FP+TNFP​

* ****Lỗi loại 2****: Điều này xảy ra khi model không dự đoán được trường hợp dương tính ngay cả khi nó thực sự dương tính. Điều này còn được gọi là ****âm tính giả****. Lỗi Loại 2 tác động đến ****recall**** của model để đo lường mức độ model xác định tất cả các trường hợp dương tính thực tế tốt như thế nào.

> Loại 2 Lỗi\=FNTP+FN\\text{Lỗi loại 2} = \\frac{FN}{TP+FN}Lỗi loại 2\=TP+FNFN​

****Ví dụ:**** Một xét nghiệm chẩn đoán được sử dụng để phát hiện một căn bệnh cụ thể ở bệnh nhân.

* ****Lỗi loại 1 (Dương tính giả):**** Điều này xảy ra khi xét nghiệm dự đoán một bệnh nhân mắc bệnh (kết quả dương tính) nhưng bệnh nhân thực sự khỏe mạnh (trường hợp âm tính).
* ****Lỗi loại 2 (Âm tính giả):**** Điều này xảy ra khi xét nghiệm dự đoán bệnh nhân khỏe mạnh (kết quả âm tính) nhưng bệnh nhân thực sự mắc bệnh (trường hợp dương tính).

Confusion Matrix cho Classification nhị phân
------------------------------------------

Confusion matrix 2x2 được hiển thị bên dưới cho image recognition có hình ảnh Chó hoặc hình ảnh Không phải chó:

Dự đoán

Dự đoán

Thật sự

Tích cực thực sự (TP)

Âm tính giả (FN)

Thật sự

Dương tính giả (FP)

Âm tính thực sự (TN)

* ****Dương thực thực sự (TP):**** Đó là tổng số có cả giá trị dự đoán và giá trị thực tế là Dog.
* ****True Negative (TN):**** Đó là tổng số có cả giá trị dự đoán và giá trị thực tế không phải là Dog.
* ****Dương tính giả (FP):**** Đó là tổng số có prediction là Chó trong khi thực tế không phải là Chó.
* ****Phủ định giả (FN):**** Đó là tổng số có prediction không phải là Chó trong khi thực tế thì đó là Chó.

#### Ví dụ: Confusion Matrix cho chó Image Recognition có số

Chỉ mục

1

2

3

4

5

6

7

8

9

10

Thật sự

Chó

Chó

Chó

Không phải chó

Chó

Không phải chó

Chó

Chó

Không phải chó

Không phải chó

Dự đoán

Chó

Không phải chó

Chó

Không phải chó

Chó

Chó

Chó

Chó

Không phải chó

Không phải chó

Kết quả

TP

FN

TP

TN

TP

FP

TP

TP

TN

TN

* Số lượng chó thực tế = 6 
* Số lượng chó không phải thực tế = 4
* Số lượng dương thực sự = 5
* Số lượng dương tính giả = 1
* Số âm thực sự = 3
* Số âm tính sai = 1

Dự đoán

Chó

Không phải chó

  

Thật sự

Chó

Tích cực thực sự  
(TP =5)

Âm tính giả  
(FN =1)

Không phải chó

Dương tính giả  
(FP=1)

Phủ định thực sự  
(TN=3)

Triển khai Confusion Matrix cho classification nhị phân bằng Python
-------------------------------------------------------------------------

****Bước 1: Nhập các thư viện cần thiết****

```python
import numpy as np from sklearn.metrics import confusion_matrix,classification_report
import seaborn as sns
import matplotlib.pyplot as plt
``` 

****Bước 2: Tạo mảng NumPy cho labels thực tế và dự đoán****

* ****thực tế:**** đại diện cho labels thực tế hoặc classification thực tế của các mặt hàng. Trong trường hợp này, đây là danh sách gồm 10 mục trong đó mỗi mục là 'Chó' hoặc 'Không phải Chó'.
* ****được dự đoán:**** đại diện cho labels được dự đoán hoặc classification được tạo bởi model.

```python
actual
= np.array(
['Dog','Dog','Dog','Not Dog','Dog','Not Dog','Dog','Dog','Not Dog','Not Dog'])
predicted = np.array(
['Dog','Not Dog','Dog','Not Dog','Dog','Dog','Dog','Dog','Not Dog','Not Dog'])
```

Thực tế \= np.array(

\['Chó','Chó','Chó','Không phải chó','Chó','Không phải chó','Chó','Chó','Không phải chó','Không phải chó'\])

Dự đoán \= np.array(

\['Dog','Not Dog','Dog','Not Dog','Dog','Dog','Dog','Dog','Not Dog','Not Dog'\])

****Bước 3: Tính confusion matrix****

* ****confusion\_matrix:**** Hàm này từ sklearn.metrics tính toán confusion matrix, một bảng được sử dụng để đánh giá hiệu suất của classification algorithm. Nó so sánh thực tế và dự đoán để tạo ra ma trận

```python
cm = confusion_matrix(actual,predicted)
```

Cm \= nhầm lẫn\_matrix(thực tế, dự đoán)

****Bước 4: Vẽ sơ đồ confusion matrix với sự trợ giúp của bản đồ nhiệt seaborn****

* ****sns.heatmap:**** Chức năng này từ [****Sinh vật biển****](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) được sử dụng để tạo bản đồ nhiệt của confusion matrix.
* ****annot=True:**** Hiển thị các giá trị số trong mỗi ô của bản đồ nhiệt.

```python
sns.heatmap(cm,
annot=True,
fmt='g',
xticklabels=['Dog','Not Dog'],
yticklabels=['Dog','Not Dog'])
plt.ylabel('Actual', fontsize=13)
plt.title('Confusion Matrix', fontsize=17, pad=20)
plt.gca().xaxis.set_label_position('top')
plt.xlabel('Prediction', fontsize=13)
plt.gca().xaxis.tick_top()
plt.gca().figure.subplots_adjust(bottom=0.2)
plt.gca().figure.text(0.5, 0.05, 'Prediction', ha='center', fontsize=13)
plt.show()
```

****Đầu ra****:

![confusion-Matrix](https://media.geeksforgeeks.org/wp-content/uploads/20240708120829/confusion-Matrix.PNG "Click to enlarge")

****Bước 5: Báo cáo classification dựa trên số liệu nhầm lẫn****

```python
print(classification_report(actual, predicted))
```

Print(classification\_report(thực tế, dự đoán))

****Đầu ra****:

![classification-repot](https://media.geeksforgeeks.org/wp-content/uploads/20250508120735058346/classification-repot.png "Click to enlarge")

Confusion Matrix Dành cho Classification đa lớp
-----------------------------------------------

Trong [****classification đa lớp****](https://www.geeksforgeeks.org/machine-learning/multiclass-classification-using-scikit-learn/), confusion matrix được mở rộng để chứa nhiều lớp.

* ****Các hàng**** đại diện cho các lớp thực tế (sự thật cơ bản).
* ****Cột**** đại diện cho các lớp được dự đoán.
* Mỗi ô trong ma trận hiển thị tần suất một lớp thực tế cụ thể được dự đoán là một lớp khác.

Ví dụ: trong bài toán 3 lớp, confusion matrix sẽ là một bảng 3x3 trong đó mỗi hàng và cột tương ứng với một trong các lớp. Nó tóm tắt hiệu suất của model trên tất cả các loại ở định dạng nhỏ gọn. Hãy xem xét ví dụ dưới đây:

### Ví dụ: Confusion Matrix cho Hình ảnh Classification (Mèo, Chó, Ngựa)

Thực tế\\Dự đoán

Dự đoán con mèo

Con chó được dự đoán

Dự Đoán Ngựa

****Mèo thật******

Chính xác

Classification sai

Classification sai

****Chó thật****

Classification sai

Chính xác

Classification sai

****Ngựa thật****

Classification sai

Classification sai

Chính xác

> ****Lưu ý:**** Trong classification nhiều lớp, các giá trị ngoài đường chéo thể hiện sự classification sai.

Đối với một lớp nhất định, một phiên bản bị classification sai đóng vai trò là Âm tính giả (FN) cho lớp thực tế và Âm tính giả (FP) cho lớp được dự đoán. Do đó, FP và FN được xác định trên mỗi lớp chứ không phải trên mỗi ô.

****Ví dụ về số:****

Khi đánh giá từng lớp một (một so với phần còn lại), các số liệu confusion matrix như TP, FP, FN và TN được tính riêng cho từng lớp. Hãy xem xét tình huống trong đó model xử lý 30 hình ảnh:

Dự đoán con mèo

Con chó được dự đoán

Dự Đoán Ngựa

Mèo thật

8

1

1

Con chó thật

2

10

0

Ngựa thật

0

2

8

Trong kịch bản này:

* ****Mèo:**** 8 con đã được xác định chính xác, 1 con bị xác định nhầm là chó và 1 con bị xác định nhầm là ngựa.
* ****Chó:**** 10 con đã được xác định chính xác, 2 con bị xác định nhầm là mèo.
* ****Ngựa:**** 8 con được xác định chính xác, 2 con bị xác định nhầm là chó.

Để tính toán âm bản thực sự, chúng ta cần biết tổng số hình ảnh là mèo, chó hoặc ngựa NOT. Giả sử có 10 hình ảnh như vậy và model đã classification chính xác tất cả chúng là "không phải mèo", "không phải chó" và "không phải ngựa". Vì thế:

* ****Phủ định thực sự (TN) Đếm:**** 10 cho mỗi lớp vì model đã xác định chính xác từng hình ảnh không phải mèo/chó/ngựa là không thuộc lớp đó

Triển khai Confusion Matrix cho classification nhiều lớp bằng Python
------------------------------------------------------------------------------

****Bước 1: Nhập các thư viện cần thiết****

```python
import numpy as np from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
```

****Bước 2: Tạo mảng NumPy cho labels thực tế và dự đoán****

* ****y\_true:**** Danh sách labels thực sự.
* ****y\_pred:**** Danh sách labels được dự đoán bởi model.
* ****classes:**** Danh sách tên lớp: 'Mèo', 'Chó' và 'Ngựa'

```python
y_true = ['Cat'] * 10 + ['Dog'] * 12 + ['Horse'] * 10 y_pred = ['Cat'] * 8 + ['Dog'] + ['Horse'] + ['Cat'] * 2 + ['Dog'] * 10 + ['Horse'] * 8 + ['Dog'] * 2 classes = ['Cat', 'Dog', 'Horse']
```

****Bước 3: Tạo và trực quan hóa Confusion Matrix****

* ****ConfusionMatrixDisplay:**** Tạo đối tượng hiển thị cho confusion matrix.
* ****confusion\_matrix=cm:**** Chuyển confusion matrix (`cm`) để hiển thị.
* ****display\_labels=classes:**** Đặt labels (\['Cat' , 'Dog' , 'Horse'\]) hoặc confusion matrix.

```python
cm = confusion_matrix(y_true, y_pred, labels=classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix', fontsize=15, pad=20)
plt.xlabel('Prediction', fontsize=11)
plt.ylabel('Actual', fontsize=11)
plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.tick_top()
plt.gca().figure.subplots_adjust(bottom=0.2)
plt.gca().figure.text(0.5, 0.05, 'Prediction', ha='center', fontsize=13)
plt.show()
```

****Đầu ra:****

![confusion-Matrix](https://media.geeksforgeeks.org/wp-content/uploads/20240708132251/confusion-Matrix.PNG "Click to enlarge")

****Bước 4: In Báo cáo Classification****

```python
print(classification_report(y_true, y_pred, target_names=classes))
```

Print(classification\_report(y\_true, y\_pred, target\_names\=classes))

****Đầu ra:****

![Classification-report](https://media.geeksforgeeks.org/wp-content/uploads/20250508121024203815/Classification-report.png "Click to enlarge")

Confusion matrix cung cấp thông tin chi tiết rõ ràng về các số liệu quan trọng như accuracy, precision và recall bằng cách phân tích predictions đúng và không chính xác.

Câu đố được đề xuất
----------

Confusion matrix giúp phân tích gì trong machine learning?

- [ ] A. Kiến trúc Model
    
- [ ] B. Hiệu suất Model trên training data
    
- [ ] C. Đánh giá Model về nhiệm vụ classification
    
- [ ] D. Feature selection

Giá trị nào trong confusion matrix đại diện cho predictions dương chính xác?

- [ ] A. Đúng Phủ định
    
- [ ] B. Sai Phủ định
    
- [ ] C. Dương tính giả
    
- [ ] D. Tích cực thực sự

Model có recall cao nhưng precision thấp có thể gặp vấn đề gì?

- [ ] A. Nhiều tiêu cực thực sự
    
- [ ] B. Quá nhiều kết quả dương tính giả
    
- [ ] C. Quá nhiều âm tính giả
    
- [ ] D. Accuracy thấp

Thành phần nào của confusion matrix chịu trách nhiệm giảm recall của model khi giá trị của nó tăng lên?

- [ ] A. Tích cực thực sự
    
- [ ] B. Đúng Phủ định
    
- [ ] C. Dương tính giả
    
- [ ] D. Âm tính giả
