Feature selection là quá trình chỉ chọn features đầu vào hữu ích nhất cho machine learning model. Nó giúp cải thiện hiệu suất model, giảm tiếng ồn và giúp kết quả dễ hiểu hơn.

* Giúp loại bỏ features không liên quan và dư thừa
* Cải thiện accuracy và giảm overfitting
* Tăng tốc model training
* Làm cho models đơn giản và dễ hiểu hơn

![binary_number_system.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)

![1.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165146012474/1.webp)

![2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165145779522/2.webp)

![3.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)

### Cần Feature Selection

Các phương pháp Feature selection rất cần thiết trong khoa học dữ liệu và machine learning vì một số lý do chính:

* **** Cải thiện Accuracy****: Models học tốt hơn khi chỉ được training trên features quan trọng.
* ****Training nhanh hơn****: features ít hơn giúp giảm thời gian tính toán.
* ****Khả năng diễn giải tốt hơn****: Với ít đầu vào hơn, việc hiểu hành vi model trở nên dễ dàng hơn.
* ****Tránh Lời nguyền của chiều ****: Giảm độ phức tạp khi làm việc với dữ liệu nhiều chiều.

Các loại phương pháp Feature Selection
----------------------------------

Có nhiều loại algorithms khác nhau được sử dụng cho feature selection và được nhóm thành ba loại chính và mỗi loại có điểm mạnh và sự cân bằng riêng tùy thuộc vào trường hợp sử dụng.

### 1\. Phương pháp lọc

[Phương pháp lọc](https://www.geeksforgeeks.org/machine-learning/feature-selection-filter-methods/) đánh giá từng feature một cách độc lập đối với biến mục tiêu. Features được lựa chọn dựa trên các biện pháp thống kê cho thấy mức độ phù hợp của chúng với mục tiêu. Các phương pháp này thường được sử dụng trong giai đoạn tiền xử lý để loại bỏ features không liên quan hoặc dư thừa.

* Đừng chỉ dựa vào mối tương quan
* Sử dụng các kỹ thuật thống kê khác nhau tùy thuộc vào loại dữ liệu
* Cách tiếp cận feature selection nhanh và độc lập với model

![filter](https://media.geeksforgeeks.org/wp-content/uploads/20250830103247936857/filter.webp "Click to enlarge")

****Các kỹ thuật lọc phổ biến****

* [****Thu được thông tin****](https://www.geeksforgeeks.org/machine-learning/information-gain-and-mutual-information-for-machine-learning/)****:**** Đo mức giảm entropy khi sử dụng feature.
* [****Kiểm định chi bình phương****](https://www.geeksforgeeks.org/maths/chi-square-test/)****:**** Kiểm tra mối quan hệ giữa features classification.
* [****Điểm của Fisher:****](https://www.geeksforgeeks.org/r-language/fishers-f-test-in-r-programming/) Xếp hạng features dựa trên khả năng phân tách lớp.
* [****Hệ số tương quan Pearson****](https://www.geeksforgeeks.org/maths/pearson-correlation-coefficient/)****:**** Đo mối quan hệ tuyến tính giữa hai biến liên tục.
* [****Ngưỡng Variance****](https://www.geeksforgeeks.org/machine-learning/variance-threshold/)****:**** Loại bỏ features với variance rất thấp.
* [****Sự khác biệt tuyệt đối trung bình****](https://www.geeksforgeeks.org/maths/mean-absolute-deviation/)****:**** Tương tự như ngưỡng variance nhưng sử dụng sự khác biệt tuyệt đối.
* [****Tỷ lệ phân tán****](https://www.geeksforgeeks.org/maths/measures-of-dispersion/)****:**** Tỷ lệ trung bình số học và trung bình hình học; giá trị cao hơn cho thấy features hữu ích.

****Thuận lợi****

* ****Nhanh và hiệu quả****: Các phương pháp lọc không tốn kém về mặt tính toán, khiến chúng trở nên lý tưởng cho datasets lớn.
* ****Dễ triển khai****: Các phương pháp này thường được tích hợp sẵn trong các thư viện machine learning phổ biến, đòi hỏi nỗ lực mã hóa tối thiểu.
* ****Model Độc lập****: Các phương pháp lọc có thể được sử dụng với bất kỳ loại machine learning model nào, khiến chúng trở thành công cụ linh hoạt.

****Hạn chế****

* ****Tương tác hạn chế với model****: Vì chúng hoạt động độc lập nên các phương pháp lọc có thể bỏ lỡ các tương tác dữ liệu có thể quan trọng đối với prediction.
* ****Chọn số liệu phù hợp****: Việc chọn số liệu thích hợp cho dữ liệu và nhiệm vụ của chúng ta là điều quan trọng để đạt được hiệu suất tối ưu.

### 2\. Phương pháp bao bọc

[Phương pháp bao bọc](https://www.geeksforgeeks.org/machine-learning/wrapper-methods-feature-selection/) là các kỹ thuật feature selection đánh giá các kết hợp features khác nhau bằng cách đo lường tác động của chúng đối với hiệu suất của model. Họ sử dụng các chiến lược tìm kiếm để thêm hoặc xóa features và chọn tập hợp con tối ưu dựa trên tiêu chí dừng được xác định trước.

* Đánh giá các tập hợp con feature bằng machine learning model
* Sử dụng các chiến lược tìm kiếm tham lam hoặc không tham lam
* Đo lường mối quan hệ giữa các tập hợp con feature và biến mục tiêu
* Thêm hoặc xóa features dựa trên hiệu suất model
* Dừng khi hiệu suất giảm hoặc đạt đến số lượng features mong muốn

![wrapper](https://media.geeksforgeeks.org/wp-content/uploads/20250830104446954251/wrapper.webp "Click to enlarge")

****Kỹ thuật bao bọc thông thường****

* [**** Lựa chọn chuyển tiếp ****](https://www.geeksforgeeks.org/machine-learning/forward-feature-selection-in-machine-learning/)****:**** Bắt đầu không có features và thêm từng cái một dựa trên sự cải thiện.
* [****Loại bỏ ngược****](https://www.geeksforgeeks.org/machine-learning/ml-multiple-linear-regression-backward-elimination-technique/)****:**** Bắt đầu với tất cả features và loại bỏ những cái ít hữu ích nhất.
* [****Loại bỏ Feature đệ quy (RFE)****](https://www.geeksforgeeks.org/machine-learning/recursive-feature-elimination/)****:**** Loại bỏ từng bước features ít quan trọng nhất.

### Thuận lợi

* ****Tối ưu hóa dành riêng cho Model****: Các phương pháp trình bao bọc xem xét trực tiếp mức độ ảnh hưởng của features đến model, có khả năng dẫn đến hiệu suất tốt hơn so với các phương pháp lọc.
* ****Linh hoạt****: Các phương pháp này có thể được điều chỉnh cho phù hợp với nhiều loại model và chỉ số đánh giá khác nhau.

### Hạn chế

* ****Đắt về mặt tính toán****: Việc đánh giá các kết hợp feature khác nhau có thể tốn thời gian, đặc biệt là đối với datasets lớn.
* ****Rủi ro của overfitting****: Việc tinh chỉnh features cho một model cụ thể có thể dẫn đến một model được trang bị quá mức và hoạt động kém trên dữ liệu không nhìn thấy được.

### 3\. Phương pháp nhúng

[Phương pháp nhúng](https://www.geeksforgeeks.org/machine-learning/feature-selection-embedded-methods/) thực hiện feature selection trong quá trình model training. Chúng kết hợp các lợi ích của cả phương pháp lọc và trình bao bọc. Feature selection được tích hợp vào model training cho phép model chọn features phù hợp nhất dựa trên quy trình training một cách linh hoạt.

![embedded](https://media.geeksforgeeks.org/wp-content/uploads/20250830104521819821/embedded.webp "Click to enlarge")

****Các kỹ thuật nhúng phổ biến****

* [****L1 Regularization (Lasso)****](https://www.geeksforgeeks.org/machine-learning/what-is-lasso-regression/)****:**** Chỉ giữ lại features có hệ số khác 0.
* [****Decision Trees****](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/) và [****Rừng ngẫu nhiên****](https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/)****:**** Chọn features dựa trên mức giảm tạp chất.
* [****Gradient Boosting****](https://www.geeksforgeeks.org/machine-learning/ml-gradient-boosting/)****:**** Chọn features giúp giảm lỗi prediction nhiều nhất

****Thuận lợi****

* ****Hiệu quả và hiệu quả****: Các phương pháp nhúng có thể đạt được kết quả tốt mà không cần gánh nặng tính toán như một số phương pháp trình bao bọc.
* ****Tìm hiểu dành riêng cho Model****: Tương tự như các phương pháp bao bọc, các kỹ thuật này sử dụng quy trình học để xác định features có liên quan.

****Hạn chế****

* ****Khả năng diễn giải bị hạn chế****: Các phương pháp nhúng có thể khó diễn giải hơn so với các phương pháp lọc, khiến việc hiểu lý do features cụ thể được chọn trở nên khó khăn hơn.
* ****Không áp dụng phổ biến****: Không phải tất cả machine learning algorithms đều hỗ trợ các kỹ thuật feature selection được nhúng.

Chọn phương pháp Feature Selection phù hợp
------------------------------------------

Việc lựa chọn phương pháp feature selection phụ thuộc vào một số yếu tố:

* ****Kích thước Dataset****: Các phương pháp lọc thường nhanh hơn đối với datasets lớn trong khi các phương thức trình bao bọc có thể phù hợp với datasets nhỏ hơn.
* ****Loại Model****: Một số models như models dựa trên cây, có các khả năng feature selection tích hợp sẵn.
* ****Khả năng diễn giải****: Nếu hiểu được lý do căn bản đằng sau feature selection là rất quan trọng thì các phương pháp lọc có thể là lựa chọn tốt hơn.
* ****Tài nguyên tính toán:**** Các phương pháp trình bao bọc có thể tốn thời gian, vì vậy hãy xem xét khả năng tính toán sẵn có của chúng ta.

Với các phương pháp feature selection này, chúng ta có thể dễ dàng cải thiện hiệu suất của model và giảm chi phí tính toán của nó.

Câu đố được đề xuất
----------

Phương pháp nào sau đây là phương pháp lọc cho feature selection?

- [ ] A. Loại bỏ Feature đệ quy
    
- [ ] B. Kiểm định Chi-Square
    
- [ ] C. Random Forest
    
- [ ] D. Loại bỏ ngược

Tỷ lệ phân tán cao trong feature có ý nghĩa gì?

- [ ] A. Feature là hằng số
    
- [ ] B. Feature phù hợp hơn
    
- [ ] C. Feature có missing values
    
- [ ] D. Feature không liên quan

Trong các phương thức trình bao bọc, cách tiếp cận nào bắt đầu với tất cả features và loại bỏ phương thức ít hữu ích nhất trong mỗi bước

- [ ] A. Loại bỏ ngược
    
- [ ] B. Lựa chọn chuyển tiếp
    
- [ ] C. Điểm của Fisher
    
- [ ] D. L1 Regularization

Mối quan hệ giữa feature selection và lời nguyền của chiều là gì?

- [ ] A. Tăng tính chiều
    
- [ ] B. Không có tác dụng
    
- [ ] C. Giảm kích thước và độ phức tạp
    
- [ ] D. Chuyển đổi features

Hạn chế của phương pháp lọc là gì?

- [ ] A. Thực thi chậm
    
- [ ] B. Chi phí tính toán cao
    
- [ ] C. Yêu cầu training data
    
- [ ] D. Bỏ qua các tương tác feature
