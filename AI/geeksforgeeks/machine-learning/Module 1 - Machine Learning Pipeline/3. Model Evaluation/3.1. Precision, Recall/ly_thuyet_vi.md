Precision và recall là hai thước đo đánh giá được sử dụng để kiểm tra hiệu suất của Machine Learning Model. Precision là tỷ lệ classification của model trong tất cả các classification tích cực là tích cực. Recall cho chúng ta biết model có thể tìm thấy bao nhiêu mặt hàng tích cực thực tế. Precision và recall giúp giải quyết các vấn đề về classification.

****1\. Precision****
---------------------

Precision là tỷ lệ giữa Giá trị thực và tất cả Giá trị tích cực. Nó cho thấy có bao nhiêu câu predictions “có” do model tạo ra thực sự đúng. Nó giúp chúng ta giảm bớt những lần đoán sai “có” được gọi là kết quả dương tính giả (FP). Precision được tính như sau:

![precision](https://media.geeksforgeeks.org/wp-content/uploads/20250517113847930547/precision.png "Click to enlarge")

Hãy tưởng tượng bạn xây dựng một model để tìm các loài chim trong ảnh. Nó đánh dấu một số bức ảnh là "chim".

* Nếu những bức ảnh được đánh dấu đó thực sự có chim thì tốt (tích cực thực sự).
* Nhưng nếu một số không có chim thì model đã mắc lỗi (kết quả dương tính giả).

![precision_in_ml](https://media.geeksforgeeks.org/wp-content/uploads/20260423091756205630/precision_in_ml.webp "Click to enlarge")

### ****Công dụng của Precision****

* Precision giúp chúng ta hiểu mức accuracy của model “có” predictions. Nó đặc biệt hữu ích khi dữ liệu có nhiều loại kết quả hơn loại kia.
* Ví dụ: nếu hầu hết các email không phải là thư rác và chỉ một số ít là thư rác thì precision sẽ giúp chúng ta biết model tìm kiếm thư rác tốt đến mức nào mà không mắc quá nhiều lỗi. Trong dữ liệu không đồng đều như vậy, precision giúp đo lường mức accuracy của model trong việc chọn ra nhóm ít phổ biến hơn như thư rác hoặc gian lận.

### ****Ưu điểm của Precision cao****

Model có precision cao sẽ rất giỏi tránh sai lầm khi nói “có”. Điều này rất quan trọng trong những tình huống mà báo động sai là một vấn đề lớn. Ví dụ:

* Khi phát hiện email spam, sẽ tốt hơn nếu email thật không bị đánh dấu nhầm là thư rác.
* Chúng ta quan tâm đến việc nhận đúng các email quan trọng hơn là dừng mọi thư rác.

Vì vậy, trong những trường hợp này, model đưa ra ít câu trả lời "có" sai hơn sẽ hữu ích hơn.

### ****Hạn chế của Precision****

* Nếu chúng ta chỉ quan tâm đến precision thì model có thể bỏ sót một số trường hợp thực tế. Nó trở nên quá cẩn thận và có thể nói “không” ngay cả khi điều gì đó thực sự là “có”.
* Nếu model quá tập trung vào tính chính xác, nó có thể để nhiều email spam vào hộp thư đến của bạn vì nó sợ đánh dấu sai một email thực là thư rác.

****2\. Recall****
------------------

Recall cho chúng ta biết model tìm thấy tất cả các trường hợp “có” chính xác trong dữ liệu tốt đến mức nào. Nó kiểm tra xem model có thể xác định chính xác bao nhiêu trường hợp dương tính thực sự. Công thức tính recall là:

![Screenshot-2025-05-17-114003](https://media.geeksforgeeks.org/wp-content/uploads/20250517114040183598/Screenshot-2025-05-17-114003.png "Click to enlarge")

* ****Kết quả tích cực thực sự (TP)****: model đã nói chính xác là “có”.
* ****Phủ định sai (FN)****: model đã bỏ lỡ câu trả lời “có” thực sự và thay vào đó nói “không”.

Hãy tưởng tượng một chiếc máy tính model tìm kiếm các loài chim trong ảnh.

* Recall cho chúng ta biết model đã tìm thấy chính xác bao nhiêu con chim thật.
* Một model hoàn hảo sẽ tìm thấy tất cả các loài chim không có sai sót nào, nghĩa là không có kết quả âm tính giả.

![recall_in_ml](https://media.geeksforgeeks.org/wp-content/uploads/20260423091452364710/recall_in_ml.webp "Click to enlarge")

### ****Công dụng của Recall****

Bạn sử dụng recall khi việc tìm ra tất cả các trường hợp tích cực có thể xảy ra là rất quan trọng ngay cả khi một số trường hợp trong số đó hóa ra là sai. Ví dụ:

* Trong các xét nghiệm y tế, bạn muốn phát hiện mọi bệnh nhân có thể bị bệnh ngay cả khi điều đó có nghĩa là một số người khỏe mạnh bị gắn cờ sai.
* Khi phát hiện gian lận, tốt hơn hết bạn nên kiểm tra thêm một số giao dịch bình thường hơn là bỏ sót một vụ gian lận thực sự.

### ****Ưu điểm của Recall cao****

* Model có recall cao sẽ rất tốt trong việc không bỏ sót những trường hợp quan trọng.
* Nó xác định hầu hết các trường hợp “có” thực tế trong dữ liệu.
* Hữu ích khi thiếu một trường hợp thực tế nguy hiểm hoặc tốn kém.
* Ví dụ: Trong an ninh mạng, việc bỏ lỡ một cuộc tấn công còn tệ hơn việc gắn cờ sai hoạt động an toàn.

### ****Hạn chế của Recall****

* Tối ưu hóa model để thu được càng nhiều thông tin tích cực thực tế càng tốt
* Có thể nhầm kết quả âm bản label thành kết quả dương tính
* Dẫn đến số lượng kết quả dương tính giả cao hơn

Câu đố được đề xuất
----------

Precision đo lường những gì trong classification model?

- [ ] A. Số lượng dương tính thực tế được xác định chính xác
    
- [ ] B. Tỷ lệ số kết quả dương tính được dự đoán đúng trên tổng số kết quả dương tính được dự đoán chính xác
    
- [ ] C. Số lượng predictions được model classification không chính xác
    
- [ ] D. Tỷ lệ phần trăm của tất cả predictions được classification chính xác

Khi nào recall cao được ưa thích hơn precision cao?

- [ ] A. Khi âm tính giả có hại hơn
    
- [ ] B. Khi dương tính giả có hại hơn
    
- [ ] C. Khi model là overfitting
    
- [ ] D. Khi accuracy là mối quan tâm chính

Công thức nào sau đây __không__ được sử dụng để tính Precision?

- [ ] A. Giá trị tích cực thực sự (TP)
    
- [ ] B. Kết quả dương tính giả (FP)
    
- [ ] C. Âm tính giả (FN)
    
- [ ] D. Không có ý nào ở trên

Tình huống nào phù hợp nhất để sử dụng recall làm thước đo đánh giá chính?

- [ ] A. Khi dương tính giả có hại hơn âm tính giả
    
- [ ] B. Khi dataset được cân bằng hoàn hảo
    
- [ ] C. Khi thiếu một trường hợp dương tính là tốn kém hoặc nguy hiểm
    
- [ ] D. Khi model tạo ra rất ít predictions
