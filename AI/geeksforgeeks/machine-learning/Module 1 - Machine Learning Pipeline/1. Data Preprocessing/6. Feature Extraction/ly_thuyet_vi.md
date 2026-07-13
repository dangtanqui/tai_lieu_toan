Feature extraction chuyển đổi dữ liệu thô thành features có cấu trúc và có ý nghĩa mà machine learning models có thể dễ dàng diễn giải. Nó tổ chức dữ liệu phức tạp thành các biến rõ ràng và hữu ích để có thể hiểu được các mẫu và mối quan hệ trong dữ liệu dễ dàng hơn. Bước này chuẩn bị dữ liệu ở dạng hỗ trợ phân tích hiệu quả và prediction.

* Chuyển đổi dữ liệu thô và phi cấu trúc thành features hữu ích
* Thể hiện các đặc điểm quan trọng của dataset thông qua các biến rõ ràng
* Giúp machine learning models tìm hiểu các mẫu và mối quan hệ trong dữ liệu bằng cách cung cấp đầu vào có ý nghĩa

![features_11.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260317170406396582/features_11.webp)

![key_techniques_for_feature_extraction.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260317161430705434/key_techniques_for_feature_extraction.webp)

![advantages_of_feature_extraction.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260317161430199700/advantages_of_feature_extraction.webp)

![challenges_in_feature_extraction.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260317161430452259/challenges_in_feature_extraction.webp)

Tầm quan trọng của Feature Extraction
--------------------------------

* Giảm tính toán bằng cách đơn giản hóa dữ liệu thô phức tạp.
* Cải thiện hiệu suất model bằng cách sử dụng features có liên quan.
* Cung cấp thông tin chi tiết tốt hơn bằng cách loại bỏ tiếng ồn.
* Giúp ngăn chặn overfitting bằng cách giảm độ phức tạp của feature.

Các kỹ thuật chính cho Feature Extraction
-------------------------------------

### 1\. Phương pháp thống kê

Các phương pháp thống kê được sử dụng trong feature extraction để tóm tắt và giải thích các mẫu dữ liệu. Các thuộc tính dữ liệu phổ biến bao gồm:

![stat](https://media.geeksforgeeks.org/wp-content/uploads/20250527152834205375/stat.png "Click to enlarge")

* [****Nghĩa là****](https://www.geeksforgeeks.org/maths/what-is-mean/)****:**** Giá trị trung bình của dataset.
* [****Trung vị****](https://www.geeksforgeeks.org/maths/median/)****:**** Giá trị ở giữa khi được sắp xếp theo thứ tự tăng dần.
* [****Độ lệch chuẩn****](https://www.geeksforgeeks.org/maths/standard-deviation-formula/)****:**** Thước đo mức độ lan truyền hoặc phân tán của mẫu.
* [****Tương quan và hiệp phương sai****](https://www.geeksforgeeks.org/data-analysis/mathematics-covariance-and-correlation/)****:**** Đo lường mối quan hệ tuyến tính giữa hai hoặc nhiều yếu tố.

Bạn có thể sử dụng các phương pháp thống kê này để thể hiện xu hướng trung tâm, mức độ lan truyền và các mối liên kết trong một bộ sưu tập.

### 2\. Giảm kích thước

[Giảm kích thước](https://www.geeksforgeeks.org/machine-learning/dimensionality-reduction/) giảm số lượng features mà không làm mất thông tin quan trọng. Một số phương pháp phổ biến là:

![dim1.png](https://media.geeksforgeeks.org/wp-content/uploads/20250527152833905404/dim1.png)

* [****Principal Component Analysis****:](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/) Nó biến đổi features ban đầu thành các thành phần trực giao mới để thu được variance tối đa trong dữ liệu.
* [****Phân tích phân biệt tuyến tính (LDA):****](https://www.geeksforgeeks.org/machine-learning/ml-linear-discriminant-analysis/) Nó tìm thấy sự kết hợp tốt nhất của features để phân tách các lớp khác nhau, tối đa hóa khả năng phân tách lớp để có classification tốt hơn.
* [****t-Nhúng hàng xóm ngẫu nhiên phân tán (t-SNE)****](https://www.geeksforgeeks.org/machine-learning/ml-t-distributed-stochastic-neighbor-embedding-t-sne-algorithm/): Một kỹ thuật giảm dữ liệu chiều cao thành hai hoặc ba chiều lý tưởng để hiển thị datasets phức tạp.

### 3\. Feature Extraction cho dữ liệu văn bản

Trong Natural Language Processing (NLP), chúng ta thường chuyển đổi văn bản thô sang định dạng mà machine learning models có thể hiểu được.

1. [****Túi Từ (BoW)****](https://www.geeksforgeeks.org/nlp/bag-of-words-bow-model-in-nlp/)****:**** Trình bày tài liệu bằng cách đếm tần số từ, bỏ qua thứ tự từ, hữu ích cho văn bản cơ bản classification.
2. [****Tần số nghịch đảo của thuật ngữ (TF-IDF)****](https://www.geeksforgeeks.org/machine-learning/understanding-tf-idf-term-frequency-inverse-document-frequency/): Điều chỉnh tầm quan trọng của từ dựa trên tần suất trong một tài liệu cụ thể so với tất cả các tài liệu, làm nổi bật các thuật ngữ duy nhất.

### ****4\. Phương pháp xử lý tín hiệu****

Nó được sử dụng để phân tích dữ liệu chuỗi thời gian, âm thanh và cảm biến:

![origsig](https://media.geeksforgeeks.org/wp-content/uploads/20250527152833040108/origsig.png "Click to enlarge")

1. [****Biến đổi Fourier:****](https://www.geeksforgeeks.org/maths/fourier-transform/) Nó chuyển đổi tín hiệu từ miền thời gian sang miền tần số để phân tích các thành phần tần số của nó.
2. [****Biến đổi Wavelet:****](https://www.geeksforgeeks.org/data-science/wavelet-transforms/) Nó phân tích các tín hiệu thay đổi theo thời gian, cung cấp cả thông tin về thời gian và tần số cho các tín hiệu không cố định.

### ****5\. Khai thác dữ liệu hình ảnh****

Kỹ thuật trích xuất features từ hình ảnh:

![cnnhog](https://media.geeksforgeeks.org/wp-content/uploads/20250527153014413670/cnnhog.jpg "Click to enlarge")

1. [****Biểu đồ của các gradient định hướng (HOG):****](https://www.geeksforgeeks.org/machine-learning/hog-feature-visualization-in-python-using-skimage/) Kỹ thuật này tìm ra sự phân bố gradient cường độ hoặc hướng cạnh trong một hình ảnh. Nó được sử dụng trong các nhiệm vụ phát hiện và nhận dạng đối tượng.
2. [****Neural Networks chuyển đổi (CNN) Features:****](https://www.geeksforgeeks.org/machine-learning/introduction-convolution-neural-network/) Họ học features phân cấp từ hình ảnh thông qua các lớp tích chập, lý tưởng cho classification và các nhiệm vụ phát hiện.

Chọn phương pháp phù hợp
-------------------------

Việc chọn phương pháp feature extraction thích hợp tùy thuộc vào loại dữ liệu và vấn đề cụ thể mà chúng ta đang giải quyết. Nó đòi hỏi phải xem xét cẩn thận và thường là chuyên môn về miền.

* ****Mất thông tin:**** Feature extraction có thể đơn giản hóa dữ liệu quá nhiều, có khả năng làm mất thông tin quan trọng trong quá trình này.
* ****Độ phức tạp tính toán:**** Một số phương pháp, đặc biệt đối với datasets lớn có thể tốn kém về mặt tính toán và có thể yêu cầu tài nguyên đáng kể.

****Feature Selection so với Feature Extraction****
------------------------------------------------

Vì Feature Selection và Feature Extraction có liên quan nhưng không giống nhau, chúng ta hãy nhanh chóng xem những điểm khác biệt chính giữa chúng để hiểu rõ hơn:

Diện mạo

Feature Selection

Feature Extraction

Sự định nghĩa

Chọn một tập hợp con features có liên quan từ tập hợp ban đầu

Chuyển đổi features ban đầu thành bộ features mới

Mục đích

Giảm kích thước

Chuyển đổi dữ liệu thành dạng trình bày dễ quản lý hơn hoặc mang tính thông tin hơn

Quá trình

Lọc, phương thức bao bọc, phương thức nhúng

Xử lý tín hiệu, kỹ thuật thống kê, biến đổi algorithms

Đầu ra

Tập hợp con của features đã chọn

Bộ features biến đổi mới

Chi phí tính toán

Chi phí thấp hơn

Có thể cao hơn, đặc biệt đối với các phép biến đổi phức tạp

Khả năng giải thích

Giữ lại khả năng diễn giải của features gốc

Có thể mất khả năng diễn giải tùy thuộc vào sự chuyển đổi

Công cụ và thư viện cho Feature Extraction
------------------------------------------

Có một số công cụ và thư viện có sẵn cho feature extraction trên các miền khác nhau. Chúng ta hãy xem một số cái phổ biến:

* [****Scikit-learn****](https://www.geeksforgeeks.org/machine-learning/what-is-python-scikit-library/)****:**** Nó cung cấp các công cụ cho các tác vụ machine learning khác nhau bao gồm PCA, ICA và các phương pháp tiền xử lý cho feature extraction.
* [****OpenCV****](https://www.geeksforgeeks.org/computer-vision/opencv-overview/)****:**** Một thư viện computer vision phổ biến với các chức năng dành cho hình ảnh feature extraction như SIFT, SURF và ORB.
* [****TensorFlow****](https://www.geeksforgeeks.org/python/introduction-to-tensorflow/) ****/**** [****Keras****](https://www.geeksforgeeks.org/deep-learning/what-is-keras/)****:**** Các thư viện deep learning này trong Python cung cấp APIs để xây dựng và training neural networks có thể được sử dụng cho feature extraction từ hình ảnh, văn bản và các loại dữ liệu khác.
* [****PyTorch****](https://www.geeksforgeeks.org/deep-learning/getting-started-with-pytorch/)****:**** Thư viện deep learning cho phép thiết kế neural network tùy chỉnh cho feature extraction và các tác vụ khác.
* [****NLTK (Bộ công cụ ngôn ngữ tự nhiên)****](https://www.geeksforgeeks.org/python/nltk-nlp/)****:**** Một thư viện NLP phổ biến cung cấp các phương thức feature extraction như túi từ, TF-IDF và nhúng từ cho dữ liệu văn bản.

Ứng dụng
------------

* ****Computer Vision và Xử lý hình ảnh:**** Được sử dụng trong các phương tiện tự hành để phát hiện biển báo đường và người đi bộ bằng cách trích xuất features trực quan chính để điều hướng an toàn.
* ****Natural Language Processing (NLP):**** Hỗ trợ lọc thư rác qua email bằng cách trích xuất features văn bản để classification chính xác thư là thư rác hoặc hợp pháp.
* ****Kỹ thuật y sinh:**** Trích xuất features từ tín hiệu EEG hoặc MRI giúp chẩn đoán rối loạn thần kinh hoặc phát hiện sớm các dấu hiệu của bệnh.
* ****Giám sát thiết bị và công nghiệp:**** Bảo trì dự đoán sử dụng dữ liệu cảm biến features để thấy trước các lỗi máy, giảm thời gian ngừng hoạt động và chi phí sửa chữa.
* ****Phát hiện tài chính và gian lận:**** Phân tích các mẫu giao dịch để xác định các hoạt động gian lận và ngăn ngừa tổn thất tài chính.

Thuận lợi
----------

* ****Đơn giản hóa dữ liệu:**** Giảm dữ liệu phức tạp thành dạng có thể quản lý được để phân tích và trực quan hóa dễ dàng hơn.
* ****Tăng hiệu suất Model:**** Loại bỏ dữ liệu không liên quan, giúp algorithms nhanh hơn và chính xác hơn.
* ****Làm nổi bật các mẫu chính:**** Lọc tiếng ồn để tập trung vào features quan trọng để có thông tin chi tiết nhanh hơn.
* ****Cải thiện tính tổng quát hóa:**** Giúp models hoạt động tốt hơn trên dữ liệu mới, chưa được xem bằng cách nhấn mạnh features mang tính thông tin.
* ****Tăng tốc Training và Prediction:**** Ít features hơn có nghĩa là model training và predictions thời gian thực nhanh hơn.

Thử thách
----------

* ****Quản lý dữ liệu chiều cao:**** Việc trích xuất features có liên quan từ datasets lớn và phức tạp có thể khó khăn.
* ****Rủi ro của Overfitting hoặc Underfitting:**** Quá nhiều hoặc quá ít features có thể ảnh hưởng đến model accuracy và tính tổng quát.
* ****Chi phí tính toán:**** Các phương pháp phức tạp có thể yêu cầu nhiều tài nguyên, hạn chế sử dụng với dữ liệu lớn hoặc thời gian thực.
* ****Features dư thừa hoặc không liên quan:**** features chồng chéo hoặc ồn ào có thể gây nhầm lẫn cho models và giảm hiệu quả.

Câu đố được đề xuất
----------

Sự khác biệt chính giữa feature selection và feature extraction là gì

- [ ] A. Feature selection chọn features phù hợp, feature extraction tạo features kết hợp mới
    
- [ ] B. Feature selection tạo features mới, feature extraction chọn những cái hiện có
    
- [ ] C. Feature extraction loại bỏ features không liên quan, feature selection thêm features mới
    
- [ ] D. Cả hai đều giống nhau

Mục đích chính của Phân tích phân biệt tuyến tính (LDA) là gì

- [ ] A. Tìm tổ hợp tuyến tính của features để phân tách các lớp tốt nhất
    
- [ ] B. Giảm kích thước dataset để lưu trữ
    
- [ ] C. Chỉ hiển thị các mẫu clustering
    
- [ ] D. Dự đoán giá trị số

Feature Extraction là gì?

- [ ] A. Xóa tất cả features khỏi dataset
    
- [ ] B. Tạo features có ý nghĩa từ dữ liệu thô
    
- [ ] C. Lưu trữ dữ liệu trong cơ sở dữ liệu
    
- [ ] D. Tăng số lượng dataset features

Kỹ thuật nào thể hiện một tài liệu bằng cách sử dụng tần số từ?

- [ ] A. TF-IDF
    
- [ ] B. Túi Từ
    
- [ ] C. PCA
    
- [ ] D. Biến đổi Fourier

Loại dữ liệu nào Biến đổi Fourier chủ yếu được sử dụng trong feature extraction?

- [ ] A. Dữ liệu hình ảnh
    
- [ ] B. Dữ liệu văn bản
    
- [ ] C. Dữ liệu chuỗi thời gian hoặc tín hiệu
    
- [ ] D. Dữ liệu dạng bảng
