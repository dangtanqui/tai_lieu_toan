Điều chỉnh Hyperparameter là quá trình chọn các giá trị tối ưu cho hyperparameters của machine learning model. Chúng thường được đặt trước khi quá trình training thực tế bắt đầu và kiểm soát các khía cạnh của chính quá trình học tập. Điều chỉnh hiệu quả giúp model học các mẫu tốt hơn, tránh overfitting hoặc underfitting và đạt được accuracy cao hơn trên dữ liệu không nhìn thấy.

Kỹ thuật điều chỉnh Hyperparameter
-----------------------------------

Models có thể có nhiều hyperparameters và việc tìm ra sự kết hợp tốt nhất của parameters có thể được coi là một vấn đề tìm kiếm. Hai chiến lược tốt nhất để điều chỉnh Hyperparameter là:

![397349273.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251222173603532083/397349273.webp)

![397349272.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103915201685/397349272.webp)

![397349274.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103914899123/397349274.webp)

### ****1\. GridSearchCV****

[GridSearchCV](https://www.geeksforgeeks.org/machine-learning/performing-feature-selection-with-gridsearchcv-in-sklearn/) là một kỹ thuật mạnh mẽ để điều chỉnh hyperparameter. Nó training model bằng cách sử dụng tất cả các kết hợp có thể có của các giá trị hyperparameter được chỉ định để tìm ra thiết lập hoạt động tốt nhất. Nó chậm và sử dụng nhiều năng lượng máy tính, khiến nó khó sử dụng với datasets lớn hoặc nhiều cài đặt. Nó hoạt động bằng các bước dưới đây:

* Tạo một mạng lưới các giá trị tiềm năng cho mỗi hyperparameter.
* Training model cho mọi kết hợp trong lưới.
* Đánh giá từng model bằng cross-validation.
* Chọn sự kết hợp cho điểm cao nhất.

Ví dụ: nếu chúng ta muốn điều chỉnh hai [Hyperparameters](https://www.geeksforgeeks.org/machine-learning/how-to-optimize-logistic-regression-performance/) C và phạt [Bộ classification Logistic Regression](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/) model với các bộ giá trị sau:  
C = \[0,1, 0,2, 0,3, 0,4, 0,5\]  
phạt = \[0,01, 0,1, 0,5, 1,0\]

![GridSearchCV](https://media.geeksforgeeks.org/wp-content/uploads/Hyp_tune.png "Click to enlarge")

Kỹ thuật tìm kiếm lưới sẽ xây dựng nhiều phiên bản của model với tất cả các kết hợp có thể có của C và Alpha, dẫn đến tổng cộng 5 \* 4 = 20 models khác nhau. Sự kết hợp hoạt động tốt nhất sau đó sẽ được chọn.

****Ví dụ:**** Điều chỉnh Logistic Regression bằng GridSearchCV

Đoạn mã sau minh họa cách sử dụng GridSearchCV . Trong mã dưới đây:

* Chúng ta tạo dữ liệu mẫu bằng cách sử dụng make\_classification.
* Chúng ta xác định một phạm vi giá trị `C` bằng thang logarit.
* GridSearchCV thử tất cả các kết hợp từ param\_grid và sử dụng cross-validation 5 lần.
* Nó trả về hyperparameter (`C`) tốt nhất và điểm validation tương ứng của nó

```python
from sklearn.linear_model import LogisticRegression from sklearn.model_selection import GridSearchCV
import numpy as np from sklearn.datasets import make_classification
X, y = make_classification(
n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)
c_space = np.logspace(-5, 8, 15)
param_grid = {
'C': c_space,
'penalty': ['l1', 'l2'] }
logreg = LogisticRegression(solver='liblinear')
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)
logreg_cv.fit(X, y)
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))
```

****Đầu ra:****

> Đã điều chỉnh Logistic Regression Parameters: {'C': 0,006105402296585327}  
> Điểm tốt nhất là 0,853

Điều này thể hiện accuracy cao nhất mà model đạt được bằng cách sử dụng kết hợp hyperparameter C = 0,0061. Điểm tốt nhất là 0,853 có nghĩa là model đạt được 85,3% accuracy trên dữ liệu validation trong quá trình tìm kiếm lưới.

### ****2\. RandomizedSearchCV****

Như tên gợi ý, [RandomizedSearchCV](https://www.geeksforgeeks.org/machine-learning/comparing-randomized-search-and-grid-search-for-hyperparameter-estimation-in-scikit-learn/) chọn các kết hợp hyperparameters ngẫu nhiên từ các phạm vi nhất định thay vì kiểm tra từng kết hợp đơn lẻ như GridSearchCV.

* Trong mỗi lần lặp, nó thử kết hợp ngẫu nhiên các giá trị hyperparameter mới.
* Nó ghi lại hiệu suất của model cho mỗi lần kết hợp.
* Sau vài lần thử, nó sẽ chọn được tập hợp có hiệu suất tốt nhất.

****Ví dụ:**** Điều chỉnh Decision Tree bằng RandomizedSearchCV

Đoạn mã sau minh họa cách sử dụng RandomizedSearchCV. Trong ví dụ này:

* Chúng ta xác định một phạm vi giá trị cho mỗi [Hyperparameter](https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/), ví dụ: max\_deep, min\_samples\_leaf, v.v.
* Các kết hợp ngẫu nhiên được chọn và đánh giá bằng cross-validation 5 lần.
* Sự kết hợp và điểm tốt nhất được in.

```python
import numpy as np from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)
from scipy.stats import randint from sklearn.tree import DecisionTreeClassifier from sklearn.model_selection import RandomizedSearchCV
param_dist = {
"max_depth": [3, None],
"max_features": randint(1, 9),
"min_samples_leaf": randint(1, 9),
"criterion": ["gini", "entropy"] }
tree = DecisionTreeClassifier()
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)
tree_cv.fit(X, y)
print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))
```

****Đầu ra:****

> Đã điều chỉnh Decision Tree Parameters: {'tiêu chí': 'entropy', 'max\_deep': Không có, 'max\_features': 6, 'min\_samples\_leaf': 6}  
> Điểm tốt nhất là 0,8

Điểm 0,842 có nghĩa là model đã hoạt động với accuracy là 84,2% trên validation set với hyperparameters theo sau.

### ****3\. Tối ưu hóa Bayes ****

Tìm kiếm lưới và Tìm kiếm ngẫu nhiên có thể không hiệu quả vì chúng thử mù quáng nhiều kết hợp hyperparameter, ngay cả khi một số rõ ràng là không hữu ích. [Tối ưu hóa Bayes](https://www.geeksforgeeks.org/artificial-intelligence/bayesian-optimization-in-machine-learning/) có cách tiếp cận thông minh hơn. Nó coi việc điều chỉnh hyperparameter giống như một vấn đề tối ưu hóa toán học và học hỏi từ các kết quả trong quá khứ để quyết định nên thử điều gì tiếp theo.

* Xây dựng model (chức năng thay thế) theo xác suất để dự đoán hiệu suất dựa trên hyperparameters.
* Cập nhật model này sau mỗi lần đánh giá.
* Sử dụng model để chọn bộ tốt nhất tiếp theo để thử.
* Lặp lại cho đến khi tìm được sự kết hợp tối ưu. Hàm thay thế models:

> P(điểm(y)∣hyperparameters(x))P(\\text{điểm}(y) \\mid \\text{hyperparameters}(x))P(điểm(y)∣hyperparameters(x))

Ở đây hàm thay thế models mối quan hệ giữa hyperparameters xxx và điểm số yyy. Bằng cách cập nhật model này lặp đi lặp lại với mỗi đánh giá mới, tối ưu hóa Bayes sẽ đưa ra các quyết định sáng suốt hơn. Chất thay thế phổ biến models được sử dụng trong tối ưu hóa Bayes bao gồm:

* Quy trình Gaussian
* Random Forest Regression
* Công cụ ước tính Parzen có cấu trúc cây (TPE)

****Thuận lợi****
------------------

* Việc tìm ra sự kết hợp tối ưu của hyperparameters có thể tăng cường đáng kể độ bền và độ bền của model accuracy.
* Điều chỉnh giúp ngăn chặn cả overfitting và underfitting, mang lại model cân bằng tốt.
* Bằng cách chọn hyperparameters hoạt động tốt trên dữ liệu validation, model có thể khái quát hóa tốt hơn những dữ liệu không nhìn thấy được.
* Nó cũng giúp sử dụng các tài nguyên tính toán như thời gian và bộ nhớ hiệu quả hơn bằng cách tránh các thử nghiệm không cần thiết.
* Điều chỉnh phù hợp có thể làm cho model đơn giản hơn, dễ hiểu và dễ giải thích hơn.

****Thử thách****
------------------

* Không gian hyperparameter lớn hơn làm tăng số lượng kết hợp để khám phá, khiến quá trình tính toán trở nên tốn kém và tốn thời gian, đặc biệt đối với models phức tạp.
* Sử dụng kiến ​​thức có sẵn giúp thu hẹp không gian tìm kiếm, nâng cao cả hiệu suất và hiệu quả của việc điều chỉnh hyperparameter.
* Điều chỉnh động hyperparameters trong training, chẳng hạn như lập lịch learning rate hoặc dừng sớm, có thể cải thiện hiệu suất model.

Câu đố được đề xuất
----------

Mục tiêu chính của việc điều chỉnh hyperparameter là gì?

- [ ] A. Giảm thời gian training
    
- [ ] B. Tăng kích thước dataset
    
- [ ] C. Thay đổi model parameters sau training
    
- [ ] D. Cải thiện hiệu suất model bằng cách tối ưu hóa hyperparameters

Sự khác biệt chính giữa GridSearchCV và RandomizedSearchCV là gì?

- [ ] A. GridSearchCV chọn ngẫu nhiên hyperparameters, trong khi RandomizedSearchCV kiểm tra tất cả các kết hợp
    
- [ ] B. GridSearchCV chỉ hoạt động với Decision Trees
    
- [ ] C. Cả hai đều thực hiện tìm kiếm toàn diện
    
- [ ] D. GridSearchCV kiểm tra mọi kết hợp có thể, trong khi RandomizedSearchCV thử kết hợp ngẫu nhiên

Hãy tưởng tượng bạn đang điều chỉnh model với 50 hyperparameters. GridSearchCV sẽ yêu cầu testing hàng triệu kết hợp. Phương pháp điều chỉnh nào sẽ khám phá không gian tìm kiếm khổng lồ này một cách hiệu quả nhất trong khi học hỏi từ các thử nghiệm trước đó?

- [ ] A. Giữ lại Validation
    
- [ ] B. K-Fold Cross Validation
    
- [ ] C. RandomizedSearchCV
    
- [ ] D. Tối ưu hóa Bayes

Hyperparameters thường được xác định ở giai đoạn nào của quy trình làm việc machine learning?

- [ ] A. Trước khi quá trình training bắt đầu
    
- [ ] B. Sau khi đánh giá model
    
- [ ] C. Trong prediction
    
- [ ] D. Sau feature selection

Ưu điểm chính của Tối ưu hóa Bayes so với Tìm kiếm lưới và Tìm kiếm ngẫu nhiên là gì?

- [ ] A. Nó tránh được cross-validation
    
- [ ] B. Nó sử dụng ít hyperparameters hơn
    
- [ ] C. Nó học hỏi từ những đánh giá trước đó để hướng dẫn tìm kiếm trong tương lai
    
- [ ] D. Nó kiểm tra tất cả các kết hợp nhanh hơn
