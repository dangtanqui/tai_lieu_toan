Vòng đời Machine Learning là một quy trình có cấu trúc được sử dụng để phát triển, training, triển khai và duy trì machine learning models một cách hiệu quả. Nó bao gồm nhiều giai đoạn như thu thập dữ liệu, tiền xử lý, model training, đánh giá và giám sát để đảm bảo predictions chính xác và đáng tin cậy.

* Cung cấp quy trình làm việc có hệ thống để xây dựng ML models có thể mở rộng và đáng tin cậy
* Giúp liên tục cải thiện hiệu suất model thông qua giám sát và training lại

![machine_learning_lifecycle](https://media.geeksforgeeks.org/wp-content/uploads/20251108151323674165/machine_learning_lifecycle.webp "Click to enlarge")

Bước 1: Định nghĩa vấn đề
-----------------

Bước đầu tiên là xác định rõ vấn đề cần giải quyết. Một vấn đề được xác định rõ ràng sẽ cung cấp nền tảng để xác định mục tiêu của dự án, kết quả mong đợi và loại giải pháp cần thiết.

* Đảm bảo sự liên kết giữa nhu cầu kinh doanh và giải pháp kỹ thuật
* Xác định mục tiêu, phạm vi và tiêu chí thành công của dự án
* Đảm bảo sự rõ ràng trong kết quả mong muốn

Bước 2: Thu thập dữ liệu
--------------

Giai đoạn [Thu thập dữ liệu](https://www.geeksforgeeks.org/data-analysis/methods-of-data-collection/) bao gồm việc thu thập datasets một cách có hệ thống có thể được sử dụng làm dữ liệu thô để training model. Chất lượng và sự đa dạng của dữ liệu ảnh hưởng trực tiếp đến hiệu suất của model.

Dưới đây là một số features cơ bản về Thu thập dữ liệu:

* ****Mức độ liên quan:**** Thu thập dữ liệu phải phù hợp với vấn đề đã xác định và bao gồm features cần thiết.
* ****Chất lượng:**** Đảm bảo chất lượng dữ liệu bằng cách xem xét các yếu tố như accuracy và việc sử dụng có đạo đức.
* ****Số lượng:**** Thu thập đủ khối lượng dữ liệu để training một model mạnh mẽ.
* ****Tính đa dạng:**** Bao gồm datasets đa dạng để nắm bắt được nhiều tình huống và kiểu mẫu.

Bước 3: Data Cleaning và tiền xử lý
------------------------------

Dữ liệu thô thường lộn xộn và không có cấu trúc và nếu chúng ta sử dụng dữ liệu này trực tiếp để training thì có thể dẫn đến accuracy kém. Chúng ta cần thực hiện [Data cleaning và tiền xử lý](https://www.geeksforgeeks.org/data-analysis/data-cleaning-introduction/), thường liên quan đến:

* ****Data Cleaning:**** Giải quyết các vấn đề như missing values, outliers và sự không nhất quán trong dữ liệu.
* ****Data Preprocessing:**** Chuẩn hóa các định dạng, giá trị tỷ lệ và mã hóa các biến classification để đảm bảo tính nhất quán.
* ****Chất lượng dữ liệu:**** Đảm bảo rằng dữ liệu được tổ chức tốt và chuẩn bị cho việc phân tích có ý nghĩa.

Bước 4: Phân tích dữ liệu thăm dò (EDA)
------------------------------

Để tìm các mẫu và đặc điểm ẩn trong dữ liệu, [Phân tích dữ liệu thăm dò (EDA)](https://www.geeksforgeeks.org/data-analysis/what-is-exploratory-data-analysis/) được sử dụng để khám phá thông tin chi tiết và hiểu cấu trúc của dataset. Trong các mẫu EDA, các xu hướng và thông tin chi tiết được cung cấp mà có thể không nhìn thấy được bằng mắt thường. Cái nhìn sâu sắc có giá trị này có thể được sử dụng để đưa ra quyết định sáng suốt.

Dưới đây là features cơ bản của Phân tích dữ liệu khám phá:

* ****Khám phá:**** Sử dụng các công cụ thống kê và trực quan để khám phá các mẫu trong dữ liệu.
* ****Các model và xu hướng:**** Xác định các model, xu hướng cơ bản và những thách thức tiềm ẩn trong dataset.
* ****Thông tin chi tiết:**** Có được thông tin chi tiết có giá trị để đưa ra quyết định sáng suốt trong các giai đoạn sau.
* ****Ra quyết định:**** Sử dụng EDA để lựa chọn feature engineering và model.

Bước 5: Feature Engineering và lựa chọn
-----------------------------------------

[Feature engineering và lựa chọn](https://www.geeksforgeeks.org/machine-learning/what-is-feature-engineering/) là một quá trình biến đổi bao gồm việc chỉ chọn features có liên quan để nâng cao hiệu quả của model và prediction trong khi giảm độ phức tạp.

Dưới đây là features cơ bản của Feature Engineering và Lựa chọn:

* ****Feature Engineering:**** Tạo features mới hoặc chuyển đổi những cái hiện có để nắm bắt các mẫu và mối quan hệ tốt hơn.
* ****Feature Selection:**** Xác định tập hợp con features có tác động đáng kể nhất đến hiệu suất của model.
* ****Chuyên môn về miền:**** Sử dụng kiến thức về miền để thiết kế features nhằm đóng góp một cách có ý nghĩa cho dự đoán[.](https://www.geeksforgeeks.org/physics/power/)
* ****Tối ưu hóa:**** Bộ cân bằng features cho accuracy đồng thời giảm thiểu độ phức tạp tính toán.

Bước 6: Lựa chọn Model
--------------

Để có một machine learning model tốt, việc lựa chọn model là một phần rất quan trọng vì chúng ta cần tìm model phù hợp với vấn đề đã xác định, bản chất của dữ liệu, độ phức tạp của vấn đề và kết quả mong muốn.

Dưới đây là features cơ bản của Lựa chọn Model:

* ****Độ phức tạp:**** Hãy xem xét mức độ phức tạp của vấn đề và bản chất của dữ liệu khi chọn model.
* ****Các yếu tố quyết định:**** Đánh giá các yếu tố như hiệu suất, khả năng diễn giải và khả năng mở rộng khi chọn model.
* ****Thử nghiệm:**** Thử nghiệm với các models khác nhau để tìm ra giải pháp phù hợp nhất cho vấn đề.

Bước 7: Model Training
----------------------

Với model đã chọn, vòng đời machine learning sẽ chuyển sang quy trình model training. Quá trình này bao gồm việc hiển thị model với dữ liệu lịch sử cho phép nó tìm hiểu các mẫu, mối quan hệ và sự phụ thuộc trong dataset.

Dưới đây là features cơ bản của Model Training:

* ****Quy trình lặp lại:**** Training model lặp đi lặp lại, điều chỉnh parameters để giảm thiểu lỗi và nâng cao accuracy.
* ****Tối ưu hóa:**** Tinh chỉnh model để tối ưu hóa khả năng dự đoán của nó.
* ****Validation:**** Training model một cách nghiêm ngặt để đảm bảo accuracy có dữ liệu mới chưa được nhìn thấy.

Bước 8: Đánh giá và điều chỉnh Model
-----------------------------------

[Đánh giá Model](https://www.geeksforgeeks.org/machine-learning/machine-learning-model-evaluation/) liên quan đến testing nghiêm ngặt đối với validation hoặc thử nghiệm datasets để kiểm tra accuracy của model trên dữ liệu mới chưa thấy. Nó cung cấp cái nhìn sâu sắc về điểm mạnh và điểm yếu của model. Nếu model không đạt được mức hiệu suất mong muốn, chúng ta có thể cần điều chỉnh lại model và điều chỉnh hyperparameters của nó để nâng cao accuracy dự đoán.

Dưới đây là features cơ bản của Đánh giá và điều chỉnh Model:

* ****Số liệu đánh giá:**** Sử dụng các số liệu như điểm accuracy, precision, recall và F1 để đánh giá hiệu suất của model.
* ****Điểm mạnh và điểm yếu:**** Xác định điểm mạnh và điểm yếu của model thông qua testing nghiêm ngặt.
* ****Cải tiến lặp lại:**** Bắt đầu điều chỉnh model để điều chỉnh hyperparameters và nâng cao accuracy dự đoán.
* ****Độ mạnh mẽ của Model:**** Điều chỉnh lặp đi lặp lại để đạt được mức độ mạnh mẽ và độ tin cậy mong muốn của model.

Bước 9: Triển khai Model
---------------

Bây giờ model đã sẵn sàng để triển khai ứng dụng trong thế giới thực. Nó liên quan đến việc tích hợp model dự đoán với các hệ thống hiện có cho phép doanh nghiệp sử dụng hệ thống này để đưa ra quyết định sáng suốt.

Dưới đây là features cơ bản của Triển khai Model:

* Tích hợp với các hệ thống hiện có
* Cho phép ra quyết định bằng predictions
* Đảm bảo khả năng mở rộng triển khai và bảo mật
* Cung cấp APIs hoặc pipeline để sử dụng cho sản xuất

Bước 10: Giám sát và bảo trì Model
-----------------------------------------

Sau khi triển khai models phải được giám sát để đảm bảo chúng hoạt động tốt theo thời gian. Việc theo dõi thường xuyên giúp phát hiện tình trạng trôi dạt dữ liệu, accuracy bị rớt hoặc thay đổi mẫu và có thể cần phải training lại để giữ cho model luôn đáng tin cậy khi sử dụng trong thế giới thực.

Dưới đây là features cơ bản của Giám sát và bảo trì Model:

* Theo dõi hiệu suất model theo thời gian
* Phát hiện trôi dạt dữ liệu hoặc trôi dạt khái niệm
* Cập nhật và training lại model khi accuracy giảm
* Duy trì nhật ký và cảnh báo cho các vấn đề theo thời gian thực

Câu đố được đề xuất
-----------------------------------------

Vòng đời Machine Learning là gì?

- [ ] A. Một quy trình chỉ được sử dụng để triển khai machine learning models
    
- [ ] B. Khung để xây dựng, triển khai và duy trì ML models
    
- [ ] C. Phương pháp chỉ dùng để thu thập dữ liệu
    
- [ ] D. Một kỹ thuật chỉ được sử dụng cho model training

Tại sao Data Cleaning và Tiền xử lý lại cần thiết?

- [ ] A. Để triển khai model nhanh hơn
    
- [ ] B. Để giảm kích thước dataset
    
- [ ] C. Vì dữ liệu thô có thể lộn xộn và dẫn đến accuracy kém
    
- [ ] D. Để tạo machine learning algorithms mới

Mục đích của Phân tích dữ liệu thăm dò (EDA) là gì?

- [ ] A. Để khám phá các model, xu hướng và hiểu biết sâu sắc về dữ liệu
    
- [ ] B. Để xóa tất cả features khỏi dataset
    
- [ ] C. Để tạo datasets mới
    
- [ ] D. Để triển khai model vào sản xuất

Tại sao Đánh giá Model được thực hiện?

- [ ] A. Để xóa features khỏi model
    
- [ ] B. Để thay thế dataset bằng dữ liệu mới
    
- [ ] C. Để giảm kích thước dataset
    
- [ ] D. Để kiểm tra accuracy của model trên dữ liệu chưa xem

Mục đích của việc Giám sát và Bảo trì Model là gì?

- [ ] A. Để tạo datasets mới
    
- [ ] B. Để đảm bảo model hoạt động tốt theo thời gian
    
- [ ] C. Để loại bỏ các pipeline triển khai
    
- [ ] D. Ngừng training lại models