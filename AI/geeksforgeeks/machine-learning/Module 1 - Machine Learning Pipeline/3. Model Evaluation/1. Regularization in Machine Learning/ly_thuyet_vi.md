Regularization là một kỹ thuật được sử dụng trong machine learning để ngăn chặn overfitting, điều này khiến models hoạt động kém trên dữ liệu không nhìn thấy. Bằng cách thêm hình phạt cho độ phức tạp, regularization khuyến khích models đơn giản hơn và dễ khái quát hơn.

* ****Ngăn chặn overfitting:**** Thêm các ràng buộc vào model để giảm nguy cơ ghi nhớ tiếng ồn trong training data.
* ****Cải thiện tính khái quát hóa: ***** Khuyến khích models đơn giản hơn hoạt động tốt hơn trên dữ liệu mới, chưa được nhìn thấy.

![420046945](https://media.geeksforgeeks.org/wp-content/uploads/20251209153305862042/420046945.webp "Click to enlarge")

Các loại Regularization
--------------

Chủ yếu có 3 loại kỹ thuật regularization, mỗi loại áp dụng hình phạt theo những cách khác nhau để kiểm soát độ phức tạp của model và cải thiện tính tổng quát.

### 1\. Lasso Regression

Regression model sử dụng kỹ thuật L1 Regularization được gọi là [LASSO (Toán tử lựa chọn và co rút tuyệt đối nhỏ nhất)](https://www.geeksforgeeks.org/machine-learning/what-is-lasso-regression/) regression. Nó cộng giá trị tuyệt đối của độ lớn của hệ số như một số hạng phạt vào loss function(L). Hình phạt này có thể thu nhỏ một số hệ số về 0, giúp chỉ chọn features quan trọng và bỏ qua những hệ số ít quan trọng hơn.

> Chi phí\=1n∑i\=1n(yi−yi^)2+λ∑j\=1m∣wj∣\\rm{Cost} = \\frac{1}{n}\\sum\_{i=1}^{n}(y\_i-\\hat{y\_i})^2 +\\lambda \\sum\_{j=1}^{m}{|w\_j|}Chi phí\=n1​∑i\=1n​(yi​−yi​^​)2+λ∑j\=1m​∣wj​∣

Ở đâu

*mmm: Số lượng Features
* Nnn: Số lượng ví dụ
* Yiy\_i yi​: Giá trị mục tiêu thực tế
* Y^i\\hat{y}\_iy^​i​: Giá trị mục tiêu dự đoán

> ****Lưu ý****: Các công thức này áp dụng cho models tuyến tính. Trong neural networks, số lượng weights lớn hơn nhiều so với số lượng features, nhưng các nguyên tắc regularization tương tự (L1, L2) vẫn được áp dụng trên tất cả weights.

Hãy xem cách triển khai điều này bằng python:

* ****X, y = make\_regression(n\_samples=100, n\_features=5, noise=0.1, Random\_state=42)****: Tạo regression dataset với 100 mẫu, 5 features và một số nhiễu.
* ****X\_train, X\_test, y\_train, y\_test = train\_test\_split(X, y, test\_size=0.2, Random\_state=42)****: Chia dữ liệu thành các bộ 80% training và 20% testing.
* ****lasso = Lasso(alpha=0.1)****: Tạo Lasso regression model với cường độ alpha regularization được đặt thành 0,1.

```python
from sklearn.linear_model import Lasso from sklearn.model_selection import train_test_split from sklearn.datasets import make_regression from sklearn.metrics import mean_squared_error
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42) X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print("Coefficients:", lasso.coef_)
```

****Đầu ra:****

![regularization1](https://media.geeksforgeeks.org/wp-content/uploads/20250521170718703437/regularization1.PNG "Click to enlarge")

Đầu ra hiển thị lỗi prediction của model và tầm quan trọng của features với một số hệ số giảm xuống 0 do L1 regularization.

### 2\. Sườn núi Regression

Regression model sử dụng kỹ thuật L2 regularization được gọi là [Sườn núi regression](https://www.geeksforgeeks.org/machine-learning/what-is-ridge-regression/). Nó cộng độ lớn bình phương của hệ số như một số hạng phạt đối với loss function(L). Nó xử lý đa cộng tuyến bằng cách thu hẹp các hệ số của features tương quan, giảm variance của chúng và ngăn chặn bất kỳ feature đơn lẻ nào thống trị model.

> Chi phí\=1n∑i\=1n(yi−y^i)2+λ∑j\=1mwj2\\rm{Cost} = \\frac{1}{n}\\sum\_{i=1}^{n}(y\_i-\\hat{y}\_i)^2 + \\lambda \\sum\_{j=1}^{m}{w\_j^2}Chi phí\=n1​∑i\=1n​(yi​−y^​i​)2+λ∑j\=1m​wj2​

Ở đâu,

* Nnn: Số lượng ví dụ hoặc điểm dữ liệu
* Mmm: Số lượng biến dự đoán features
* Yiy\_iyi​: Giá trị mục tiêu thực tế cho ví dụ thứ ithith
* Y^i\\hat{y}\_iy^​i​​: Giá trị mục tiêu dự đoán cho ví dụ thứ i
* Wiw\_iwi​: Các hệ số của features
* λ\\lambdaλ: Regularization parameter kiểm soát sức mạnh của regularization

Hãy xem cách triển khai điều này bằng python:

* ****ridge = Ridge(alpha=1.0)****: Tạo Ridge regression model với cường độ alpha regularization được đặt thành 1.0.

```python
from sklearn.linear_model import Ridge from sklearn.datasets import make_regression from sklearn.model_selection import train_test_split from sklearn.metrics import mean_squared_error
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42) X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred = ridge.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Coefficients:", ridge.coef_)
```

****Đầu ra****:

![regualrization2](https://media.geeksforgeeks.org/wp-content/uploads/20250521170802215020/regualrization2.PNG "Click to enlarge")

Đầu ra hiển thị MSE hiển thị hiệu suất model. MSE thấp hơn có nghĩa là accuracy tốt hơn. Các hệ số phản ánh feature weights được chính quy hóa.

### 3\. Lưới đàn hồi Regression

[Lưới đàn hồi Regression](https://www.geeksforgeeks.org/machine-learning/implementation-of-elastic-net-regression-from-scratch/) là sự kết hợp của cả L1 và L2 regularization. Nó kết hợp cả hình phạt L1 (giá trị tuyệt đối) và L2 (giá trị bình phương) trên các hệ số. Với sự trợ giúp của hyperparameter bổ sung để kiểm soát tỷ lệ của L1 và L2 regularization.

> Chi phí\=1n∑i\=1n(yi−y^i)2+λ((1−α)∑j\=1m∣wj∣+α∑j\=1mwj2)\\rm{Cost} = \\frac{1}{n}\\sum\_{i=1}^{n}(y\_i-\\hat{y}\_i)^2 + \\lambda \\left( (1-\\alpha)\\sum\_{j=1}^{m}|w\_j| + \\alpha \\sum\_{j=1}^{m}{w\_j^2} \\right)Chi phí\=n1​∑i\=1n​(yi​−y^​i​)2+λ((1−α)∑j\=1m​∣wj​∣+α∑j\=1m​wj2​)

Ở đâu

* Nnn: Số lượng ví dụ (điểm dữ liệu)
* Mmm: Số lượng features (biến dự đoán)
* Yiy\_iyi​:​ Giá trị mục tiêu thực tế cho ví dụ ithi^{th}ith
* Y^i\\hat{y}\_iy^​i​​: Giá trị mục tiêu dự đoán cho ví dụ thứ i
* Wiwiwi: Các hệ số của features
* λ\\lambdaλ: Regularization parameter kiểm soát sức mạnh của regularization
* α\\alphaα: Trộn parameter trong đó 0≤α≤10 \\leq \\alpha \\leq 10≤α≤1 và α\\alphaα\= 1 tương ứng với Lasso (L1L\_1L1​) regularization, α\\alphaα\= 0 tương ứng với Ridge (L2L\_2L2​) regularization và Giá trị giữa 0 và 1 cung cấp sự cân bằng của cả L1 và L2 regularization

Hãy xem cách triển khai điều này bằng python:

* ****model = ElasticNet(alpha=1.0, l1\_ratio=0.5)**** : Tạo một Lưới đàn hồi model với cường độ regularization alpha=1.0 và tỷ lệ trộn L1/L2 0,5.

```python
from sklearn.linear_model import ElasticNet from sklearn.datasets import make_regression from sklearn.model_selection import train_test_split from sklearn.metrics import mean_squared_error
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42) X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = ElasticNet(alpha=1.0, l1_ratio=0.5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Coefficients:", model.coef_)
```

****Đầu ra****:

![regularization3](https://media.geeksforgeeks.org/wp-content/uploads/20250521170834658723/regularization3.PNG "Click to enlarge")

Đầu ra hiển thị MSE đo lường khoảng cách giữa predictions so với giá trị thực tế (thấp hơn là tốt hơn) và các hệ số cho thấy tầm quan trọng của feature.

Lợi ích của Regularization
-----------------

Bây giờ, chúng ta hãy xem các lợi ích khác nhau của regularization như sau:

* ****Ngăn chặn Overfitting:**** Regularization giúp models tập trung vào các mẫu cơ bản thay vì ghi nhớ nhiễu trong training data.
* ****Nâng cao hiệu suất:**** Ngăn chặn việc tăng weight quá mức của outliers hoặc features không liên quan giúp cải thiện model accuracy tổng thể.
* ****Ổn định Models:**** Giảm độ nhạy cảm đối với những thay đổi dữ liệu nhỏ nhằm đảm bảo tính nhất quán giữa các tập hợp con dữ liệu khác nhau.
* ****Ngăn chặn sự phức tạp:**** Giữ cho model không trở nên quá phức tạp, điều này rất quan trọng đối với dữ liệu bị hạn chế hoặc bị nhiễu.
* ****Xử lý đa cộng tuyến:**** Giảm độ lớn của các hệ số tương quan giúp cải thiện độ ổn định của model.
* ****Thúc đẩy tính nhất quán:**** Đảm bảo hiệu suất đáng tin cậy trên các datasets khác nhau giúp giảm nguy cơ thay đổi hiệu suất lớn.

> Tìm hiểu thêm về sự khác biệt giữa các kỹ thuật regularization tại đây: [****Lasso vs Ridge vs Elastic Net****](https://www.geeksforgeeks.org/machine-learning/lasso-vs-ridge-vs-elastic-net-ml/)

Câu đố được đề xuất
----------

Regularization trong machine learning là gì?

- [ ] A. Một kỹ thuật ngăn chặn overfitting bằng cách thêm hình phạt vào model
    
- [ ] B. Phương pháp giảm kích thước dataset
    
- [ ] C. Bước tiền xử lý cho missing values
    
- [ ] D. Một cách để cải thiện tốc độ training

Ridge Regression (L2 regularization) xử lý hiện tượng đa cộng tuyến như thế nào?

- [ ] A. Bằng cách đặt một số hệ số về 0
    
- [ ] B. Bằng cách giảm độ lớn của tất cả các hệ số
    
- [ ] C. Bằng cách loại bỏ features
    
- [ ] D. Bằng cách bỏ qua features tương quan

Điều khiển alpha parameter trong regularization models trong scikit học được gì?

- [ ] A. Kích thước của dataset
    
- [ ] B. Sức mạnh của regularization
    
- [ ] C. Số features
    
- [ ] D. Loại prediction

Kỹ thuật regularization nào có thể thu nhỏ một số hệ số feature chính xác về 0?

- [ ] A. Lasso Regression
    
- [ ] B. Linear Regression
    
- [ ] C. Sườn Regression
    
- [ ] D. Lưới đàn hồi
