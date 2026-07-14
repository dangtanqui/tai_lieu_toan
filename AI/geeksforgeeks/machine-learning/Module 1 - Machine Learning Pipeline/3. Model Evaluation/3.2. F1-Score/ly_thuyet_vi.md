Điểm F1 là số liệu được sử dụng để đánh giá hiệu suất của classification model. Nó kết hợp precision và recall thành một giá trị duy nhất và đặc biệt hữu ích khi dataset có các lớp mất cân bằng.

* Kết hợp precision và recall thành một số liệu.
* Hữu ích cho datasets mất cân bằng.
* Điểm F1 cao hơn có nghĩa là hiệu suất tốt hơn.

![f1_score](https://media.geeksforgeeks.org/wp-content/uploads/20260313122802030936/f1_score.webp "Click to enlarge")

Điều kiện tiên quyết
-------------

### 1\. Confusion Matrix

[Confusion matrix](https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/) là bảng được sử dụng để đánh giá hiệu suất của classification model. Nó so sánh labels thực tế với labels dự đoán để cho biết có bao nhiêu predictions đúng hoặc không chính xác.

* ****Dương tính thực sự (TP):**** model dự đoán chính xác loại dương tính.
* ****Âm tính thực sự (TN):**** model dự đoán chính xác lớp âm.
* ****Dương tính giả (FP):**** model dự đoán là dương tính, nhưng lớp thực tế là âm tính.
* ****Âm tính giả (FN):**** model dự đoán âm tính, nhưng lớp thực tế là dương tính.

### 2\. Precision

[Precision](https://www.geeksforgeeks.org/r-language/precision-recall-and-f1-score-using-r/) đo lường xem có bao nhiêu predictions dương do model tạo ra thực sự chính xác. Nó cho chúng ta biết model chính xác đến mức nào khi dự đoán một lớp tích cực.

> Precision\=True PositivesTrue Dương tính+Sai Dương tính\\text{Precision} = \\frac{\\text{Dương tính thật}}{\\text{Dương tính thật} + \\text{Dương tính giả}}Precision\=True Dương tính+Sai PositivesTrue Dương cực​

****Ví dụ:**** Giả sử model dự đoán 5 trường hợp là dương tính. Trong số này, 4 là thực sự tích cực và 1 là tiêu cực. Trong trường hợp này, precision là 80% (4/5).

### 3\. Recall

Recall, còn được gọi là Độ nhạy hoặc Tỷ lệ dương tính thực, đo lường số lượng trường hợp dương tính thực tế được model xác định chính xác. Nó tập trung vào khả năng phát hiện các trường hợp tích cực của model.

> Recall\=True PositivesTrue Dương tính+Sai Tiêu cực\\text{Recall} = \\frac{\\text{Dương tính thực sự}}{\\text{Dương tính thực sự} + \\text{Phủ định sai}}Recall\=True Dương tính+Sai NegativesTrue Dương cực​

****Ví dụ:**** Giả sử có 10 trường hợp dương tính thực tế trong dataset. Nếu model xác định chính xác 4 trong số đó là dương thì recall sẽ trở thành 40% (4/10). Điều này có nghĩa là model chỉ phát hiện được một phần số ca dương tính thực sự.

Kết hợp Precision và Recall
------------------------------

Điểm F1 kết hợp precision và recall thành một số liệu duy nhất sử dụng giá trị trung bình hài hòa. Nó giúp đánh giá model bằng cách cân bằng cả precision và recall.

> F1 Điểm\=2×Precision×RecallPrecision+RecallF\_1 \\text{ Điểm} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}}F1​ Điểm\=2×Precision+RecallPrecision×Recall​

Điểm F1 chỉ cao khi cả precision và recall đều cao. Nếu một trong hai yếu tố này giảm đáng kể thì điểm F1 cũng sẽ giảm.

Tại sao phương tiện hài hòa được sử dụng
-------------------------

[Ý nghĩa hài hòa](https://www.geeksforgeeks.org/maths/harmonic-mean/) được sử dụng thay vì mức trung bình đơn giản vì nó cân bằng precision và recall hiệu quả hơn. Nó đảm bảo rằng cả hai giá trị đều phải cao thì điểm F1 mới cao.

* ****Cân bằng cả hai số liệu:**** Mang lại tầm quan trọng như nhau cho precision và recall.
* ****Phạt các giá trị thấp:**** Nếu precision hoặc recall thấp, điểm F1 cũng trở nên thấp.
* ****Hữu ích cho dữ liệu mất cân bằng:**** Giúp đánh giá models khi một lớp xuất hiện thường xuyên hơn các lớp khác.

Tính điểm F1
--------------------

Điểm F1 có thể được tính cho cả bài toán classification nhị phân và classification đa lớp.

### 1\. Classification nhị phân

Trong [Nhị phân classification](https://www.geeksforgeeks.org/machine-learning/getting-started-with-classification/), chỉ có hai lớp: tích cực và tiêu cực. Điểm F1 được tính bằng cách sử dụng các giá trị từ confusion matrix, giúp xác định các số liệu như precision và recall.

****Ví dụ:**** Hãy xem xét một dataset với tổng số 100 trường hợp. Trong số này, 90 là tích cực và 10 là tiêu cực. Model dự đoán 85 trường hợp là dương tính, trong đó 80 trường hợp thực sự dương tính và 5 trường hợp thực sự âm tính. Confusion matrix sẽ trông như sau:

Ví dụ

Thật sự

Tổng cộng

  

Model Prediction

80

5

85

10

5

15

Tổng cộng

90

10

100

Từ ma trận này chúng ta có thể tính toán:

1. ****Precision**** \= 80 / 85 = 0,94
2. ****Recall**** \= 80 / 90 = 0,88
3. ****Accuracy**** \= (80 + 5) / 100 = 0,85
4. ****Điểm F1**** = 0,91

Điều này cho thấy model hoạt động tốt vì cả precision và recall đều ở mức cao.

### 2\. Classification đa lớp

Trong [Classification đa lớp](https://www.geeksforgeeks.org/machine-learning/multiclass-classification-using-scikit-learn/), nơi có nhiều hơn hai lớp, điểm F1 được tính riêng cho từng lớp thay vì sử dụng một điểm duy nhất cho toàn bộ model. Điều này thường được thực hiện bằng cách sử dụng phương pháp Một đấu với Tất cả (OvR) hoặc Một đấu với Tất cả (OvA). Quá trình này hoạt động như sau:

* ****Coi một lớp là tích cực:**** Đối với mỗi lớp, coi đó là lớp tích cực và tất cả các lớp khác là tiêu cực.
* ****Tính chỉ số cho mỗi lớp:**** Tính điểm precision, recall và F1 bằng cách sử dụng TP, FP và FN cho lớp đó.
* ****Lặp lại cho tất cả các lớp:**** Thực hiện phép tính tương tự cho mọi lớp trong dataset.
* ****Kết hợp các kết quả:**** Điểm F1 riêng lẻ có thể được kết hợp bằng cách sử dụng mức trung bình vi mô, mức trung bình vĩ mô hoặc mức trung bình có weight để có được thước đo hiệu suất tổng thể.

Triển khai Điểm F1 trong Python
-------------------------------

Chúng ta có thể dễ dàng tính điểm F1 trong Python bằng cách sử dụng hàm f1\_score từ mô-đun sklearn.metrics. Hàm này hỗ trợ cả classification nhị phân và đa lớp. Hàm f1\_score chủ yếu sử dụng parameters sau:

* ****y\_true:**** Lớp labels thực tế của dataset.
* ****y\_pred:**** labels dự đoán được tạo bởi model.
* ****trung bình (tùy chọn):**** Chỉ định cách tính điểm F1 khi giải quyết các vấn đề về nhiều lớp hoặc nhiều label.

```python
from sklearn.metrics import f1_score
y_true = [0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0]
y_pred = [0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1]
f1_per_class = f1_score(y_true, y_pred, average=None)
f1_micro = f1_score(y_true, y_pred, average='micro')
f1_macro = f1_score(y_true, y_pred, average='macro')
f1_weighted = f1_score(y_true, y_pred, average='weighted')
print("F1 score per class:", f1_per_class)
print("Micro-average F1 score:", f1_micro)
print("Macro-average F1 score:", f1_macro)
print("Weighted-average F1 score:", f1_weighted)
```

Từ sklearn.metrics nhập f1\_score

​

Y\_true \= \[0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0\]

Y\_pred \= \[0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1\]

​

F1\_per\_class \= f1\_score(y\_true, y\_pred, Average\=None)

F1\_micro \= f1\_score(y\_true, y\_pred, Average\='micro')

F1\_macro \= f1\_score(y\_true, y\_pred, Average\='macro')

F1\_weighted \= f1\_score(y\_true, y\_pred, Average\='weighted')

​

Print("Điểm F1 mỗi lớp:", f1\_per\_class)

Print("Điểm F1 trung bình vi mô:", f1\_micro)

Print("Điểm F1 trung bình vĩ mô:", f1\_macro)

Print("Điểm F1 trung bình có weight:", f1\_weighted)

****Đầu ra:****

![Implementation-of-F1-Score](https://media.geeksforgeeks.org/wp-content/uploads/20250508135804102579/Implementation-of-F1-Score.png "Click to enlarge")

> * ****Trung bình vi mô****: Tính toán các số liệu trên toàn cầu bằng cách đếm tổng số kết quả dương tính thật, âm tính giả và dương tính giả.
> * ****Trung bình vĩ mô****: Tính trung bình điểm F1 cho mỗi lớp mà không tính đến sự mất cân bằng của lớp.
> * ****Trung bình có weight****: Xem xét sự mất cân bằng của lớp bằng cách tính điểm F1 theo số lượng học sinh đúng cho mỗi lớp.

Câu đố được đề xuất
----------

Khi nào Điểm F1 đặc biệt hữu ích?

- [ ] A. Khi chỉ accuracy quan trọng
    
- [ ] B. Trong bài toán regression
    
- [ ] C. Khi có sự mất cân bằng giai cấp
    
- [ ] D. Khi các lớp được cân bằng

Tại sao Điểm F1 được ưu tiên hơn accuracy đơn giản trong datasets mất cân bằng?

- [ ] A. Bởi vì nó bỏ qua các kết quả âm tính giả
    
- [ ] B. Vì nó chỉ xét những mặt tích cực thực sự
    
- [ ] C. Bởi vì nó cân bằng precision và recall bằng cách sử dụng trung bình điều hòa
    
- [ ] D. Bởi vì nó sử dụng giá trị trung bình số học của tất cả các số liệu

Trong classification nhiều lớp, Điểm F1 cho mỗi lớp thường được tính như thế nào?

- [ ] A. Bằng cách so sánh tất cả các lớp cùng một lúc
    
- [ ] B. Bằng cách coi mỗi lớp là dương và phần còn lại là âm (OvR)
    
- [ ] C. Bằng cách bỏ qua những kết quả dương tính giả
    
- [ ] D. Bằng cách lấy trung bình các ma trận nhầm lẫn của tất cả các lớp
