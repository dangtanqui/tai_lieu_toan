Phân tích dữ liệu khám phá (Exploratory Data Analysis - EDA) là một bước quan trọng trong phân tích dữ liệu, trong đó chúng ta khám phá, tóm tắt và trực quan hóa dữ liệu để hiểu cấu trúc của nó, phát hiện các mẫu, xác định điểm bất thường, kiểm tra giả định và kiểm tra mối quan hệ giữa các biến trước khi áp dụng bất kỳ machine learning hoặc models thống kê nào.

![exploratory_data_analysis_eda_.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429482180/exploratory_data_analysis_eda_.webp)

![exploratory_data_analysis_eda_2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260622154701023131/exploratory_data_analysis_eda_2.webp)

![recovery_and_file_organization_techniques.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429347465/recovery_and_file_organization_techniques.webp)

Tầm quan trọng
----------

* Cung cấp sự hiểu biết rõ ràng về dataset, bao gồm số lượng features, loại dữ liệu và phân phối dữ liệu.
* Tiết lộ các model và mối quan hệ giữa các biến khác nhau trong dữ liệu.
* Xác định các lỗi và outliers có thể ảnh hưởng đến việc phân tích.
* Nêu bật features quan trọng nhất, hữu ích cho việc xây dựng models.
* Hỗ trợ lựa chọn kỹ thuật lập model phù hợp để có kết quả tốt hơn.

Các loại phân tích dữ liệu thăm dò
----------------------------------

### 1\. Phân tích đơn biến

[Phân tích đơn biến](https://www.geeksforgeeks.org/data-visualization/what-is-univariate-bivariate-multivariate-analysis-in-data-visualisation/) nghiên cứu từng biến một để hiểu các đặc điểm và sự phân bố của nó.

* [****Histograms****](https://www.geeksforgeeks.org/maths/histogram/)****:**** Hiển thị cách phân phối giá trị dữ liệu.
* [****Box plots****](https://www.geeksforgeeks.org/data-analysis/box-plot/)****:**** Giúp phát hiện outliers và hiển thị sự lan truyền dữ liệu.
* [****Bar charts****](https://www.geeksforgeeks.org/data-visualization/bar-graph-meaning-types-and-examples/)****:**** Được sử dụng cho các biến classification.

### 2\. Phân tích hai biến

[Phân tích hai biến](https://www.geeksforgeeks.org/maths/bivariate-analysis/) kiểm tra mối quan hệ giữa hai biến để hiểu cách chúng tương tác hoặc ảnh hưởng lẫn nhau. Các kỹ thuật phổ biến bao gồm:

* [****Scatter plots:****](https://www.geeksforgeeks.org/maths/scatter-plot/) Hiển thị mối quan hệ giữa hai biến số.
* [****Hệ số tương quan:****](https://www.geeksforgeeks.org/maths/pearson-correlation-coefficient/) Đo cường độ của mối quan hệ giữa các biến.
* [****Bảng chéo:****](https://www.geeksforgeeks.org/data-analysis/what-is-cross-tabulation-and-how-does-it-organize-data-in-a-table/) Hiển thị mối quan hệ giữa hai biến classification.
* [****Line graphs:****](https://www.geeksforgeeks.org/maths/line-graph/) So sánh hai biến theo thời gian để xác định xu hướng.
* [****Hiệp phương sai:****](https://www.geeksforgeeks.org/data-analysis/mathematics-covariance-and-correlation/) Hiển thị cách hai biến thay đổi cùng nhau.

### 3\. Phân tích đa biến

[Phân tích đa biến](https://www.geeksforgeeks.org/r-language/multivariate-analysis-in-r/) nghiên cứu ba biến trở lên cùng nhau để hiểu các mối quan hệ phức tạp trong dataset. Các kỹ thuật phổ biến bao gồm:

* [****Pair plots****](https://www.geeksforgeeks.org/python/pairplot-in-matplotlib/): Hiển thị mối quan hệ giữa nhiều biến cùng một lúc.
* [****Phần tích thành phần chính (Principal Component Analysis - PCA)****](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)****:**** Giảm kích thước trong khi vẫn lưu giữ thông tin quan trọng.
* [****Phân tích không gian:****](https://www.geeksforgeeks.org/data-analysis/what-is-spatial-analysis/) Phân tích các model địa lý bằng bản đồ và dữ liệu dựa trên vị trí.

Các bước để thực hiện phân tích dữ liệu thăm dò
----------------------------------------------

EDA bao gồm một tập hợp các bước giúp chúng ta hiểu dữ liệu, tìm mẫu, phát hiện vấn đề và chuẩn bị dữ liệu để phân tích hoặc lập model thêm. Nó có thể được thực hiện bằng các công cụ khác nhau như:

* ****Python:**** [Pandas](https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/) để thao tác dữ liệu, [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) và [Seaborn](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) để trực quan hóa và [Plotly](https://www.geeksforgeeks.org/python/python-plotly-tutorial/) để biểu đồ tương tác.
* ****R****: [ggplot2](https://www.geeksforgeeks.org/r-language/data-visualization-with-r-and-ggplot2/) để trực quan hóa, [dplyr](https://www.geeksforgeeks.org/r-language/dplyr-package-in-r-programming/) để thao tác dữ liệu và [tidyr](https://www.geeksforgeeks.org/r-language/tidyr-package-in-r-programming/) để sắp xếp dữ liệu.

![Steps-in-EDA](https://media.geeksforgeeks.org/wp-content/uploads/20260310144911767918/Steps-in-EDA.webp "Click to enlarge")

### Bước 1: Tìm hiểu vấn đề và dữ liệu

Bước đầu tiên trong bất kỳ dự án phân tích dữ liệu nào là hiểu đầy đủ vấn đề chúng ta đang giải quyết và dữ liệu chúng ta có. Điều này bao gồm việc đặt những câu hỏi như:

* Mục tiêu hoặc vấn đề chúng ta đang cố gắng giải quyết là gì?
* Những biến nào có trong dataset và chúng đại diện cho điều gì?
* Những loại dữ liệu nào có sẵn (số, phân loại, văn bản, v.v.)?
* Có bất kỳ vấn đề hoặc hạn chế nào về chất lượng dữ liệu không?

### Bước 2: Nhập và kiểm tra dữ liệu

Bước tiếp theo là tải dataset vào các công cụ như [Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/) hoặc [R](https://www.geeksforgeeks.org/r-language/r-programming-for-data-science/) và kiểm tra nó. Những kiểm tra này cung cấp sự hiểu biết cơ bản về dataset.

* Tải dataset đúng cách.
* Kiểm tra số hàng và cột.
* Xác định missing values.
* Kiểm tra kiểu dữ liệu của từng biến.
* Tìm kiếm lỗi, giá trị không hợp lệ hoặc điểm dữ liệu bất thường.

### Bước 3: Xử lý dữ liệu bị thiếu

[Thiếu dữ liệu](https://www.geeksforgeeks.org/data-analysis/handling-missing-values-machine-learning/) phổ biến trong nhiều datasets và có thể ảnh hưởng đến chất lượng phân tích. Trong quá trình EDA, điều quan trọng là phải xác định và xử lý missing values đúng cách để tránh kết quả không chính xác.

* Hiểu lý do tại sao dữ liệu bị thiếu, vì điều này giúp lựa chọn phương pháp phù hợp.
* Quyết định xem nên xóa hay điền vào missing values, vì việc xóa có thể gây ra bias trong khi imputation vẫn bảo toàn dữ liệu.
* Sử dụng các phương pháp imputation phù hợp như kỹ thuật trung bình, trung vị, regression hoặc machine learning như [KNN](https://www.geeksforgeeks.org/machine-learning/how-knn-imputer-works-in-machine-learning/) hoặc [Decision trees](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/).
* Hãy xem xét tác động của việc thiếu dữ liệu vì nó vẫn có thể gây ra sự không chắc chắn ngay cả sau imputation.

### Bước 4: Khám phá đặc điểm dữ liệu

Sau khi xử lý dữ liệu bị thiếu, bước tiếp theo là kiểm tra các đặc điểm chính của dataset. Điều này giúp chúng ta hiểu cách dữ liệu được phân phối, phát hiện các giá trị bất thường và xác định các vấn đề tiềm ẩn trước khi phân tích sâu hơn.

* Kiểm tra [Phân phối dữ liệu](https://www.geeksforgeeks.org/data-science/exploring-data-distribution-set-1/) để hiểu cách các giá trị được phân bổ trên dataset.
* Đo [Xu hướng trung tâm](https://www.geeksforgeeks.org/data-science/central-tendency/) bằng cách sử dụng giá trị trung bình, trung vị và chế độ để tìm giá trị điển hình của dữ liệu.
* Đo độ variance bằng [Độ lệch chuẩn](https://www.geeksforgeeks.org/maths/standard-deviation-formula/) để xem các giá trị thay đổi bao nhiêu.
* Phân tích hình dạng phân phối bằng [Độ lệch và độ nhọn.](https://www.geeksforgeeks.org/data-science/difference-between-skewness-and-kurtosis/)
* Xác định outliers hoặc các điểm bất thường có thể ảnh hưởng đến việc phân tích.

### Bước 5: Thực hiện chuyển đổi dữ liệu

Chuyển đổi dữ liệu chuẩn bị cho dataset phân tích và lập model tốt hơn. Tùy thuộc vào dataset, chúng ta có thể cần sửa đổi hoặc chuyển đổi dữ liệu để dữ liệu có định dạng phù hợp để phân tích.

* Scaling hoặc chuẩn hóa các biến số như [Tối thiểu-tối đa scaling](https://www.geeksforgeeks.org/machine-learning/standardscaler-minmaxscaler-and-robustscaler-techniques-ml/) hoặc [Standardization](https://www.geeksforgeeks.org/machine-learning/what-is-standardization-in-machine-learning/).
* Các biến classification Encoding cho machine learning như [One-hot encoding](https://www.geeksforgeeks.org/machine-learning/ml-one-hot-encoding/) hoặc [Label encoding.](https://www.geeksforgeeks.org/machine-learning/ml-label-encoding-of-datasets-in-python/)
* Áp dụng các phép biến đổi toán học như [Căn bậc hai logarit](https://www.geeksforgeeks.org/dsa/square-root-number-using-log/) để hiệu chỉnh độ lệch hoặc độ phi tuyến tính.
* [Tạo features mới](https://www.geeksforgeeks.org/machine-learning/feature-selection-techniques-in-machine-learning/) bằng cách lấy thông tin hữu ích từ các biến hiện có
* Tổng hợp hoặc nhóm dữ liệu dựa trên các biến hoặc điều kiện cụ thể.

### Bước 6: Trực quan hóa mối quan hệ của dữ liệu

[Trực quan hóa dữ liệu](https://www.geeksforgeeks.org/data-visualization/data-visualization-and-its-importance/) giúp chúng ta hiểu các model, xu hướng và mối quan hệ trong dataset mà có thể không rõ ràng chỉ bằng các con số.

* Biểu đồ thanh và biểu đồ hình tròn giúp phân tích phân bổ dữ liệu theo classification.
* Biểu đồ, biểu đồ hộp và biểu đồ mật độ hiển thị phân bố và phát hiện outliers trong dữ liệu số.
* Biểu đồ phân tán và thước đo tương quan giúp phân tích mối quan hệ giữa các biến.

### Bước 7: Xử lý Outliers

[Outliers](https://www.geeksforgeeks.org/machine-learning/machine-learning-outlier/) là các điểm dữ liệu khác biệt đáng kể so với các quan sát khác. Chúng có thể phát sinh do lỗi hoặc sự thay đổi thực sự trong dữ liệu.

* Sử dụng các phương pháp thống kê như [Phạm vi liên tứ phân vị (IQR)](https://www.geeksforgeeks.org/maths/interquartile-range/) hoặc [Điểm Z](https://www.geeksforgeeks.org/data-science/z-score-in-statistics/) để xác định các giá trị cực trị.
* Phân tích outliers cẩn thận trước khi thực hiện bất kỳ hành động nào.
* Sử dụng kiến ​​thức về miền để xác định xem chúng hợp lệ hay sai.
* Áp dụng các kỹ thuật như giới hạn hoặc chuyển đổi nếu cần thiết.
* Chỉ xóa outliers khi chúng rõ ràng không chính xác hoặc có hại cho việc phân tích.

### Bước 8: Truyền đạt kết quả và hiểu biết sâu sắc

Bước cuối cùng trong EDA là trình bày rõ ràng kết quả phân tích. Điều này giúp người khác hiểu được những hiểu biết sâu sắc được phát hiện và kết luận rút ra từ dữ liệu.

* Nêu mục tiêu và phạm vi phân tích.
* Cung cấp thông tin cơ bản hoặc bối cảnh để cách tiếp cận dễ hiểu.
* Sử dụng hình ảnh trực quan để hỗ trợ phát hiện và làm cho kết quả rõ ràng hơn.
* Làm nổi bật những thông tin chi tiết, mẫu hoặc điểm bất thường quan trọng được phát hiện trong dữ liệu.
* Đề cập đến những hạn chế hoặc thách thức gặp phải trong quá trình phân tích.
* Đề xuất các bước tiếp theo hoặc các lĩnh vực cần điều tra thêm.

Ứng dụng
-----------

* Phân tích thị trường và phân khúc khách hàng
* Đánh giá rủi ro trong tài chính và bảo hiểm
* Kiểm soát chất lượng trong sản xuất
* Phân tích dữ liệu chăm sóc sức khỏe và bệnh prediction
* Hệ thống khuyến nghị và tối ưu hóa sản phẩm

Câu đố được đề xuất
----------

Điều nào sau đây là NOT lợi ích chính của việc thực hiện Phân tích dữ liệu khám phá (EDA)?

- [ ] A. Xác định lỗi dữ liệu và outliers
    
- [ ] B. Lựa chọn features quan trọng để lập model
    
- [ ] C. Tự động xây dựng models dự đoán
    
- [ ] D. Tìm hiểu về phân bố dữ liệu và các mẫu

Loại EDA nào tập trung vào phân tích mối quan hệ giữa hai biến?

- [ ] A. Phân tích đơn biến
    
- [ ] B. Phân tích hai biến
    
- [ ] C. Phân tích đa biến
    
- [ ] D. Phân tích chuỗi thời gian

Khi xử lý dữ liệu bị thiếu trong EDA, phương pháp nào liên quan đến việc điền vào missing values giá trị trung bình hoặc trung vị?

- [ ] A. Xóa
    
- [ ] B. Imputation
    
- [ ] C. Normalization
    
- [ ] D. Phép biến đổi

Phương pháp nào thường được sử dụng để phát hiện outliers trong dữ liệu số?

- [ ] A. Phạm vi liên tứ phân vị (IQR)
    
- [ ] B. Bảng chéo
    
- [ ] C. One-hot Encoding
    
- [ ] D. Ma trận tương quan

Bạn phát hiện ra một cột số có độ lệch cao. Phép biến đổi nào thường được sử dụng để giảm độ lệch cho EDA hoặc model hóa?

- [ ] A. Bình phương các giá trị
    
- [ ] B. Lấy logarit của các giá trị
    
- [ ] C. Thay thế giá trị bằng NaN
    
- [ ] D. Chuyển thành chuỗi
