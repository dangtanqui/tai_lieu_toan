Phân tích dữ liệu khám phá nâng cao (EDA) giúp hiểu cấu trúc và đặc điểm của dataset trước khi áp dụng machine learning models. Nó liên quan đến việc phân tích dữ liệu để khám phá các mẫu, phát hiện sự bất thường và nghiên cứu mối quan hệ giữa các biến. Phân tích này cung cấp những hiểu biết sâu sắc giúp chuẩn bị dữ liệu cho việc lập model và phân tích sâu hơn.

* Đánh giá chất lượng dữ liệu bằng cách xác định missing values và sự không nhất quán
* Hỗ trợ lựa chọn các biến hữu ích để phát triển model
* Hỗ trợ đưa ra quyết định tốt hơn trong quá trình thiết kế data preprocessing và model

![advanced_eda](https://media.geeksforgeeks.org/wp-content/uploads/20260317165652014263/advanced_eda.webp "Click to enlarge")

Hiểu những điều cơ bản về thống kê mô tả
--------------------------------------------------

Thống kê mô tả cho chúng ta một bức tranh rõ ràng về sự phân bố, lan truyền và xu hướng trung tâm của dữ liệu. Những biện pháp này cho phép chúng ta tóm tắt dữ liệu theo những cách giúp phân tích và diễn giải dễ dàng hơn. Dưới đây là một số thống kê mô tả cần thiết được sử dụng trong EDA:

![mean_mod_median](https://media.geeksforgeeks.org/wp-content/uploads/20250501122658765639/mean_mod_median.webp "Click to enlarge")

### 1\. Nghĩa là

Giá trị trung bình là mức trung bình của các điểm dữ liệu, được tính bằng cách tính tổng tất cả các giá trị và chia cho tổng số quan sát.

* ****Được sử dụng tốt nhất:**** Giá trị trung bình rất hữu ích khi so sánh datasets với các mức phân bổ tương tự và không có giá trị cực trị, chẳng hạn như so sánh thu nhập trung bình giữa các khu vực hoặc phòng ban.
* ****Không phù hợp:****Giá trị trung bình rất nhạy cảm với outliers và dữ liệu bị lệch có giá trị cực cao hoặc thấp có thể làm sai lệch kết quả và khiến nó không thể hiện giá trị điển hình của dataset.

> ****Ví dụ:**** Nếu muốn hiểu doanh thu trung bình hàng tháng của một cửa hàng trong suốt một năm, chúng ta sẽ tính doanh thu trung bình để xem doanh thu điển hình được tạo ra mỗi tháng.

### 2\. Trung vị

Trung vị là giá trị ở giữa của dataset khi sắp xếp theo thứ tự tăng dần. Nó mạnh đối với outliers, nghĩa là các giá trị cực trị không ảnh hưởng đáng kể đến giá trị trung vị.

* ****Được sử dụng tốt nhất:**** Giá trị trung vị rất hữu ích cho datasets bị lệch hoặc những giá trị có outliers, vì nó thể hiện giá trị điển hình tốt hơn khi giá trị trung bình có thể gây hiểu nhầm.
* ****Không phù hợp:**** Giá trị trung bình có thể không lý tưởng cho datasets đối xứng khi cần giá trị trung bình chính xác vì nó chỉ đại diện cho giá trị ở giữa và bỏ qua độ lớn của các giá trị khác.

> ****Ví dụ:**** Trong dataset về thu nhập hộ gia đình, trong đó một số ít cá nhân có thu nhập rất cao, giá trị trung bình thể hiện thu nhập hộ gia đình điển hình tốt hơn so với giá trị trung bình.

### 3\. Cách thức

Chế độ này là giá trị hoặc danh mục thường xuyên nhất trong dataset.

* ****Được sử dụng tốt nhất:**** Chế độ này hữu ích cho dữ liệu classification hoặc rời rạc để xác định giá trị xuất hiện thường xuyên nhất, chẳng hạn như sản phẩm phổ biến nhất được bán trong cửa hàng.
* ****Không phù hợp:**** Chế độ này có thể không hữu ích đối với dữ liệu liên tục hoặc datasets không có giá trị lặp lại, chẳng hạn như các phép đo liên tục như chiều cao hoặc weight thường không có chế độ.

> ****Ví dụ:**** Một công ty có thể muốn biết sản phẩm nào được bán nhiều nhất trong chiến dịch khuyến mại. Bằng cách tính toán chế độ, họ có thể dễ dàng xác định sản phẩm được bán thường xuyên nhất.

### 4\. Độ lệch chuẩn

[Độ lệch chuẩn](https://www.geeksforgeeks.org/maths/standard-deviation-formula/) đo mức độ variance hoặc độ phân tán so với giá trị trung bình. Độ lệch chuẩn thấp có nghĩa là các điểm dữ liệu gần với giá trị trung bình, trong khi độ lệch chuẩn cao cho thấy mức độ phân tán của các điểm dữ liệu lớn hơn.

![frame_2997](https://media.geeksforgeeks.org/wp-content/uploads/20250412155606416787/frame_2997.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Độ lệch chuẩn rất hữu ích để hiểu mức độ phân tán của dữ liệu, chẳng hạn như trong phân tích lưu lượng truy cập trang web hàng ngày, độ lệch chuẩn cao cho thấy lưu lượng truy cập thay đổi rất nhiều theo từng ngày.
* ****Không phù hợp:**** Độ lệch chuẩn rất nhạy cảm với outliers và dữ liệu bị sai lệch, do đó, nó có thể không phải lúc nào cũng thể hiện chính xác độ variance của dataset.

> ****Ví dụ:**** Nếu một trang web thương mại điện tử gặp phải sự tăng đột biến về lưu lượng truy cập vào một số ngày nhất định, độ lệch chuẩn sẽ cho biết lưu lượng truy cập hàng ngày thay đổi bao nhiêu so với mức trung bình, giúp xác định xem lưu lượng truy cập của trang web là nhất quán hay biến đổi nhiều.

### 5\. Phạm vi liên tứ phân vị (IQR)

[IQR](https://www.geeksforgeeks.org/maths/interquartile-range/) là sự khác biệt giữa phân vị thứ 75 (Q3) và phân vị thứ 25 (Q1) của dữ liệu. Nó thể hiện sự phân tán của 50% dữ liệu ở giữa và rất hữu ích để xác định outliers.

* ****Được sử dụng tốt nhất:**** IQR giúp phát hiện outliers và hiểu mức độ lan truyền của 50% dữ liệu ở giữa, chẳng hạn như xác định những học sinh có thành tích tốt hơn hoặc kém hơn đáng kể so với hầu hết lớp khi phân tích điểm thi.
* ****Không phù hợp:**** IQR hữu ích cho tất cả các phân phối nhưng đặc biệt hữu ích khi có outliers, trong đó các thước đo như giá trị trung bình hoặc độ lệch chuẩn có thể phù hợp hơn.

> ****Ví dụ:**** Trong một lớp học sinh, nếu chúng ta muốn tập trung vào phạm vi điểm đại diện cho 50% học sinh ở giữa và loại trừ các giá trị cực đoan (chẳng hạn như một số học sinh đạt điểm cao hoặc thấp bất thường), chúng ta sẽ sử dụng IQR.

### 6\. Độ lệch

[Độ lệch](https://www.geeksforgeeks.org/data-science/skewness-measures-and-interpretation/) đo lường tính bất đối xứng của phân phối dữ liệu. Nó cho biết dữ liệu nghiêng về bên phải (độ lệch dương) hay bên trái (độ lệch âm). Nói một cách đơn giản, nó cho chúng ta biết liệu dữ liệu có ở bên này nhiều hơn bên kia hay không.

![customized_histogram](https://media.geeksforgeeks.org/wp-content/uploads/20260317165726003916/customized_histogram.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:****Độ lệch giúp xác định xem có cần chuyển đổi dữ liệu hay không khi phân phối có độ lệch cao để phù hợp với algorithms như linear regression.
* ****Không phù hợp:**** Đối với dữ liệu đối xứng. Nếu dữ liệu đã được phân phối bình thường thì không cần tính toán độ lệch vì nó sẽ gần bằng 0 và cung cấp rất ít thông tin bổ sung.

> ****Kịch bản ví dụ:**** Một nhà phân tích bán lẻ có thể sử dụng độ lệch để phân tích dữ liệu bán hàng hàng tháng cho một sản phẩm. Nếu dữ liệu bị sai lệch (ví dụ: doanh số bán hàng cao hơn trong thời gian nghỉ lễ), nhà phân tích có thể quyết định sử dụng phép chuyển đổi nhật ký để ổn định variance trước khi áp dụng machine learning models.

### 7\. Kurtosis

[Kurtosis](https://www.geeksforgeeks.org/maths/how-to-calculate-kurtosis-in-statistics/) đo lường độ đuôi của phân phối, cho biết dữ liệu có đuôi nặng hay nhẹ so với phân phối bình thường. Độ nhọn cao gợi ý outliers cực trị hơn, trong khi độ nhọn thấp biểu thị ít giá trị cực trị hơn.

* ****Sử dụng tốt nhất:**** Để xác định datasets có nhiều outliers hơn dự kiến. Độ nhọn cao có thể báo hiệu rằng chúng ta cần chú ý đến outliers hoặc dữ liệu có thể thiên về các giá trị cực đoan có thể ảnh hưởng đến hiệu suất của một số models nhất định.
* ****Không phù hợp****: Đối với dữ liệu bình thường, trong đó phần đuôi không được quan tâm đặc biệt. Nếu dataset đã hoạt động khá tốt với phân bố gần như bình thường thì độ nhọn có thể không mang lại giá trị bổ sung.

> ****Kịch bản ví dụ:**** Một nhà quản lý rủi ro phân tích lợi nhuận chứng khoán hàng ngày có thể tính toán độ nhọn để xác định khả năng xảy ra những ngày thua lỗ cực độ. Nếu độ nhọn cao, người quản lý có thể sử dụng các kỹ thuật để tính toán outliers đó, chẳng hạn như số liệu thống kê mạnh mẽ hoặc điều chỉnh rủi ro models để phản ánh sự biến động.

Trực quan hóa phân phối
-------------------------

Trực quan hóa là một bước quan trọng trong EDA, vì nó giúp xác định các mẫu, xu hướng và điểm bất thường trong dữ liệu. Việc chọn đúng loại hình ảnh trực quan là rất quan trọng để đạt được những hiểu biết sâu sắc có ý nghĩa.

### 1\. Batch đất

[Cốt truyện thanh](https://www.geeksforgeeks.org/pandas/bar-plot-in-matplotlib/) hiển thị tần suất hoặc tỷ lệ của các danh mục trong dữ liệu classification, giúp so sánh kích thước của các danh mục khác nhau.

![bar](https://media.geeksforgeeks.org/wp-content/uploads/20250819104312863917/bar.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Khi so sánh tần suất của các danh mục khác nhau, chẳng hạn như số lượng sản phẩm được bán trên nhiều danh mục khác nhau (ví dụ: đồ điện tử, quần áo hoặc đồ nội thất).
* ****Không phù hợp:**** Đối với dữ liệu liên tục hoặc khi các danh mục có quá nhiều giá trị riêng biệt, điều này có thể làm lộn xộn cốt truyện và làm giảm độ rõ ràng.

> ****Tình huống ví dụ:**** Bộ phận tiếp thị có thể sử dụng biểu đồ thanh để so sánh số lượng mua hàng của các loại sản phẩm khác nhau trong một tháng, giúp xác định dòng sản phẩm nào thành công nhất.

### 2\. Biểu đồ thanh xếp chồng

Biểu đồ thanh xếp chồng hiển thị thành phần của các danh mục, được chia thành các danh mục phụ. Nó giúp hiểu được tỷ lệ của từng danh mục phụ trong danh mục chính.

![stacked](https://media.geeksforgeeks.org/wp-content/uploads/20250819104424800656/stacked.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Để phân tích tỷ lệ các danh mục phụ trên các danh mục chính khác nhau, chẳng hạn như phân tích doanh số theo từng danh mục sản phẩm ở các quốc gia hoặc khu vực khác nhau.
* ****Không phù hợp:**** Đối với datasets có quá nhiều danh mục hoặc danh mục phụ vì biểu đồ có thể trở nên quá phức tạp để diễn giải rõ ràng.

> ****Tình huống ví dụ:**** Người quản lý bán hàng khu vực có thể sử dụng biểu đồ thanh xếp chồng để chia nhỏ doanh số bán sản phẩm theo khu vực, cho phép đưa ra quyết định chiến lược tốt hơn dựa trên hiệu suất khu vực của từng dòng sản phẩm.

### 3\. Biểu đồ

[Biểu đồ](https://www.geeksforgeeks.org/maths/histogram/) hiển thị phân phối dữ liệu liên tục bằng cách nhóm dữ liệu vào các thùng. Chiều cao của mỗi thanh biểu thị số lượng điểm dữ liệu trong mỗi thùng.

![customized_histogram](https://media.geeksforgeeks.org/wp-content/uploads/20250929174800996724/customized_histogram.webp "Click to enlarge")

* ****Sử dụng tốt nhất****: Để hiểu sự phân bổ tần suất của dữ liệu số, chẳng hạn như phân bổ mức lương, điểm thi hoặc độ tuổi của khách hàng.
* ****Không phù hợp****: Outliers hoặc sai lệch nặng có thể làm sai lệch việc giải thích dữ liệu, chẳng hạn như một số thu nhập cực cao làm lu mờ phần còn lại của thu nhập dataset.

> ****Tình huống ví dụ:**** Một trang web có thể sử dụng biểu đồ để phân tích sự phân bổ thời gian mà khách truy cập dành cho trang web, giúp xác định các xu hướng như thời gian người dùng thường ở lại trước khi rời đi.

### 4\. Batch hộp

[Ô hình hộp](https://www.geeksforgeeks.org/data-analysis/box-plot/) cung cấp bản tóm tắt bằng đồ họa về giá trị tối thiểu, tứ phân vị thứ nhất (phân vị thứ 25), phân vị trung vị (phân vị thứ 50), phân vị thứ ba (phân vị thứ 75) và các giá trị tối đa của dataset. Chúng cũng giúp xác định outliers tiềm năng.

![boxplot](https://media.geeksforgeeks.org/wp-content/uploads/20250819105344705834/boxplot.webp "Click to enlarge")

* ****Sử dụng tốt nhất:**** Để so sánh sự phân bổ giữa nhiều nhóm và để xác định outliers trong dataset. Nó đặc biệt hữu ích khi so sánh giá của các sản phẩm hoặc dịch vụ khác nhau ở các thị trường khác nhau.
* ****Không phù hợp:**** Đối với datasets nhỏ nơi phân phối có thể không rõ ràng hoặc khi dữ liệu thiếu biến thể.

> ****Tình huống ví dụ:**** Một nhà phân tích bất động sản có thể sử dụng biểu đồ hình hộp để hiển thị sự thay đổi về giá nhà theo khu vực, giúp xác định các thị trường có thể biến động nhiều hơn hoặc có tài sản có giá trị cao.

### 5\. Âm mưu vĩ cầm

[Âm mưu violin](https://www.geeksforgeeks.org/data-visualization/violin-plot-for-data-analysis/) kết hợp các khía cạnh của cả ô hộp và ô mật độ. Chúng hiển thị mức phân bổ dữ liệu và mật độ xác suất của nó, cho phép chúng ta so sánh mức phân bổ và mức độ lan truyền dữ liệu một cách kỹ lưỡng hơn.

![violinplot](https://media.geeksforgeeks.org/wp-content/uploads/20250819105644196681/violinplot.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Để so sánh sự phân bổ và mật độ giữa nhiều nhóm hoặc danh mục. Nó đặc biệt hữu ích khi chúng ta muốn hiểu sự phân bố và tập trung các giá trị giữa các nhóm khác nhau.
* ****Không phù hợp:**** Khi chỉ so sánh hai nhóm, vì nó có thể phức tạp không cần thiết so với các biểu đồ đơn giản hơn như biểu đồ hình hộp.

> ****Tình huống ví dụ:**** Một nhà phân tích chăm sóc sức khỏe có thể sử dụng biểu đồ violin để so sánh sự phân bổ chỉ số huyết áp ở các nhóm tuổi khác nhau, cho thấy cả mức độ lan truyền và mật độ của dữ liệu.

### 6\. Biểu đồ hình tròn

[Biểu đồ hình tròn](https://www.geeksforgeeks.org/maths/pie-charts/) hiển thị tỷ lệ của tổng thể, trong đó mỗi phân đoạn đại diện cho tỷ trọng của một danh mục trong tổng số. Chúng được sử dụng tốt nhất khi chúng ta muốn thể hiện những tỷ lệ đơn giản.

![123](https://media.geeksforgeeks.org/wp-content/uploads/20260317151457654718/123.webp "Click to enlarge")

* ****Sử dụng tốt nhất:**** Để hiển thị các tỷ lệ đơn giản trong datasets nhỏ như thị phần của các sản phẩm khác nhau hoặc phân bổ doanh số bán hàng trong một công ty.
* ****Không phù hợp:**** Dành cho datasets có quá nhiều danh mục vì biểu đồ hình tròn trở nên lộn xộn và khó đọc hơn. Nó cũng kém hiệu quả hơn khi cần so sánh chính xác.

> ****Tình huống ví dụ:**** Nhóm tiếp thị có thể sử dụng biểu đồ hình tròn để thể hiện tỷ trọng của từng danh mục sản phẩm trong tổng doanh số bán hàng, giúp các bên liên quan nhanh chóng hiểu được chi tiết.

### 7\. Bản đồ nhiệt tương quan

Bản đồ nhiệt được sử dụng để hiển thị mối tương quan giữa features số trong dataset. Mỗi ô biểu thị hệ số tương quan giữa hai biến, với cường độ màu thể hiện mức độ tương quan.

![heatmap](https://media.geeksforgeeks.org/wp-content/uploads/20250819112608903311/heatmap.webp "Click to enlarge")

* ****Sử dụng tốt nhất:**** Để kiểm tra tính đa cộng tuyến trong regression models và để xác định biến nào có tương quan cao với biến mục tiêu.
* ****Không phù hợp:**** Khi có quá nhiều biến số, vì bản đồ nhiệt có thể trở nên lộn xộn và khó diễn giải hơn. Trong những trường hợp như vậy, tốt hơn nên chọn một tập hợp con các biến.

> ****Tình huống ví dụ:**** Một nhà phân tích dữ liệu thực hiện khảo sát về mức độ hài lòng của khách hàng có thể sử dụng sơ đồ nhiệt tương quan để xem các số liệu về mức độ hài lòng khác nhau (chẳng hạn như chất lượng sản phẩm, dịch vụ khách hàng và thời gian giao hàng) tương quan như thế nào với mức độ hài lòng tổng thể.

### 8\. Biểu đồ phân tán

[Âm mưu phân tán](https://www.geeksforgeeks.org/maths/scatter-plot/) trực quan hóa mối quan hệ giữa hai biến liên tục bằng cách vẽ từng điểm dữ liệu dưới dạng một dấu chấm trên mặt phẳng hai chiều. Nó đặc biệt hữu ích để xác định xu hướng hoặc mối tương quan.

![scatterplot](https://media.geeksforgeeks.org/wp-content/uploads/20250819112940383108/scatterplot.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Để khám phá mối quan hệ tuyến tính giữa hai biến liên tục và phát hiện các xu hướng hoặc mẫu trong dữ liệu.
* ****Không phù hợp:**** Đối với các biến classification hoặc mối quan hệ phi tuyến tính mà không áp dụng các phép biến đổi (ví dụ: sử dụng thuật ngữ đa thức).

> ****Tình huống ví dụ:**** Một đại lý bất động sản có thể sử dụng biểu đồ phân tán để so sánh diện tích với giá, giúp hình dung những ngôi nhà lớn hơn có xu hướng được định giá cao hơn như thế nào.

Xử lý dữ liệu đa biến: Tương tác Feature
------------------------------------------------

Khi xử lý nhiều features, điều quan trọng là phải hiểu cách các biến khác nhau tương tác với nhau. Việc khám phá những tương tác này có thể phát hiện ra những mối quan hệ không rõ ràng khi xem xét từng biến số riêng lẻ.

### 1\. Lưới khía cạnh

Các lưới khía cạnh chia dữ liệu thành nhiều ô phụ dựa trên một feature cụ thể, cho phép chúng ta so sánh các tập hợp con khác nhau của dữ liệu.

![facetgrid](https://media.geeksforgeeks.org/wp-content/uploads/20250819113236721342/facetgrid.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Lưới khía cạnh rất hữu ích để so sánh các mối quan hệ khác nhau giữa các danh mục, Ví dụ: hiển thị các biến thể về doanh số bán hàng theo khu vực hoặc khoảng thời gian với các ô riêng biệt.
* ****Không phù hợp:**** Lưới thuộc tính có thể trở nên cồng kềnh khi xử lý một số lượng lớn danh mục vì lưới có thể trở nên quá lộn xộn và khó diễn giải.

> ****Ví dụ:**** Lưới khía cạnh có thể được sử dụng để phân tích doanh số bán sản phẩm khác nhau như thế nào giữa các mùa khác nhau. Mỗi khía cạnh có thể hiển thị một cốt truyện riêng cho từng mùa, cho phép chúng ta xem xu hướng theo mùa.

### 2\. Cặp ô

Biểu đồ cặp tạo ra một mạng lưới các biểu đồ phân tán cho mỗi cặp biến trong dataset, cho phép chúng ta hình dung mối quan hệ tiềm năng giữa chúng.

![pairplot](https://media.geeksforgeeks.org/wp-content/uploads/20250819112814812648/pairplot.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** Biểu đồ cặp rất phù hợp để kiểm tra mối quan hệ giữa một số biến liên tục. Chúng giúp xác định mối tương quan, xu hướng hoặc model có thể tồn tại giữa các features khác nhau.
* ****Không phù hợp:**** Biểu đồ cặp có thể trở nên quá tải khi làm việc với datasets lớn chứa nhiều biến, vì số lượng mối quan hệ cặp tăng theo cấp số nhân.

> ****Ví dụ:**** Có thể sử dụng biểu đồ cặp để khám phá mối liên hệ giữa các biến khác nhau như giá cả, độ tuổi của khách hàng và tần suất mua hàng trong dataset thương mại điện tử.

Xác định Outliers và các điểm bất thường
----------------------------------

Outliers là các điểm dữ liệu khác biệt đáng kể so với phần còn lại của dữ liệu và có thể làm sai lệch các phân tích thống kê. Xác định những điểm bất thường này là một phần quan trọng của EDA.

### 1\. Điểm Z

[Điểm Z](https://www.geeksforgeeks.org/data-science/z-score-in-statistics/) đo lường mức độ lệch chuẩn của một điểm dữ liệu so với giá trị trung bình, giúp chúng ta xác định outliers trong dữ liệu được phân phối thông thường.

* ****Được sử dụng tốt nhất:**** Điểm Z hữu ích nhất khi xử lý dữ liệu được phân phối bình thường, vì chúng giúp định lượng khoảng cách giữa mỗi điểm so với giá trị trung bình. Điểm Z trên 3 hoặc dưới -3 thường biểu thị outlier.
* ****Không phù hợp:**** Điểm Z ít hữu ích hơn khi dữ liệu không được phân phối bình thường vì chúng dựa vào giả định rằng dữ liệu tuân theo đường cong hình chuông.

> ****Ví dụ:**** Một công ty có thể sử dụng điểm Z để xác định những ngày bán hàng bất thường chênh lệch đáng kể so với mức trung bình, chẳng hạn như doanh số bán hàng tăng đột biến do một chương trình khuyến mãi đặc biệt.

### 2\. Rừng cách ly và LOF (Yếu tố Outlier cục bộ)

Các machine learning algorithms này xác định outliers bằng cách phân tích khoảng cách của các điểm dữ liệu với các điểm khác. Chúng hoạt động tốt với dữ liệu nhiều chiều.

* ****Được sử dụng tốt nhất:**** Rừng cách ly và LOF đặc biệt hữu ích khi làm việc với datasets lớn và phức tạp. Những algorithms này có thể tự động phát hiện outliers trong không gian nhiều chiều, chẳng hạn như phát hiện gian lận trong các giao dịch tài chính.
* ****Không phù hợp:**** Các phương pháp này có thể không hoạt động tốt trên datasets hoặc datasets nhỏ hơn với các phân phối đơn giản, trong đó các phương pháp thống kê truyền thống như điểm Z hoặc biểu đồ hộp có thể đủ.

> ****Ví dụ:**** Một nền tảng thương mại điện tử có thể sử dụng Rừng cách ly để phát hiện các giao dịch gian lận, gắn cờ những giao dịch đi chệch khỏi model mua hàng thông thường.

Feature Engineering (Biến đổi và tương tác)
------------------------------------------------------

Feature engineering là quá trình chuyển đổi hoặc kết hợp dữ liệu thô thành features có ý nghĩa nhằm cải thiện hiệu suất của machine learning models. Mục đích là nâng cao khả năng hiểu các mẫu của model và tạo ra predictions chính xác hơn.

### 1\. Chuyển đổi nhật ký

Chuyển đổi nhật ký giúp chuẩn hóa dữ liệu bị lệch, đặc biệt khi phân phối có độ lệch dương lớn. Nó làm giảm ảnh hưởng của outliers cực đoan bằng cách nén các giá trị lớn.

* ****Được sử dụng tốt nhất:**** Chuyển đổi nhật ký đặc biệt hữu ích cho dữ liệu có độ lệch dương lớn hoặc tăng trưởng theo cấp số nhân, chẳng hạn như dữ liệu về thu nhập hoặc dân số. Ví dụ: áp dụng phép chuyển đổi nhật ký cho dữ liệu thu nhập có thể làm cho việc phân phối đối xứng hơn và giảm ảnh hưởng của các giá trị thu nhập cực đoan.
* ****Không phù hợp:**** Nó không hiệu quả đối với dữ liệu đã tuân theo phân phối chuẩn hoặc không có độ lệch lớn. Đối với những dữ liệu như vậy, việc áp dụng chuyển đổi nhật ký có thể làm sai lệch dữ liệu một cách không cần thiết.

> ****Ví dụ:**** Nếu chúng ta có dataset về thu nhập hộ gia đình, chúng ta có thể áp dụng phép chuyển đổi log để làm cho sự phân bổ cân đối hơn, vì thu nhập thường bị sai lệch nhiều với một số outliers có thu nhập cực cao.

### 2\. Đa thức Features

Features đa thức tạo features mới bằng cách kết hợp các features hiện có thông qua các thuật ngữ đa thức, chẳng hạn như hình vuông hoặc hình khối. Điều này cho phép models tuyến tính nắm bắt được các mối quan hệ phi tuyến tính.

* ****Được sử dụng tốt nhất:**** Đa thức features rất hữu ích khi có mối quan hệ phi tuyến tính giữa features và biến mục tiêu. Ví dụ: nếu chúng ta đang lập model giá nhà, việc thêm features đa thức như số hạng bình phương hoặc bậc ba của thước vuông có thể giúp nắm bắt các mối quan hệ phi tuyến tính.
* ****Không phù hợp:**** Khi mối quan hệ giữa features và mục tiêu vốn đã tuyến tính. Features đa thức có thể dẫn đến overfitting trong những trường hợp như vậy, đặc biệt nếu bậc của đa thức quá cao.

> ****Ví dụ:**** Nếu chúng ta dự đoán giá nhà và có mối quan hệ phi tuyến tính giữa diện tích của một ngôi nhà và giá của nó, thì việc thêm đa thức features (ví dụ: bình phương của một ngôi nhà) có thể giúp nắm bắt được sự phức tạp đó.

### 3\. Tương tác Features

Tương tác features được tạo bằng cách kết hợp hai hoặc nhiều features để nắm bắt được hiệu ứng kết hợp mà chúng có thể có đối với biến mục tiêu. Những features này có giá trị khi chúng ta tin rằng tác động của một feature phụ thuộc vào giá trị của một feature khác.

* ****Sử dụng tốt nhất:**** Tương tác features đặc biệt hữu ích khi chúng ta nghi ngờ rằng hai features cùng nhau có tác động chung lên biến mục tiêu. Ví dụ: việc kết hợp tuổi tác và thu nhập có thể cho thấy tác động tương tác lên khả năng mua các mặt hàng xa xỉ.
* ****Không phù hợp:**** Việc lạm dụng tương tác features có thể dẫn đến overfitting, đặc biệt nếu chúng ta thêm quá nhiều kết hợp mà không có lý do chính đáng. Điều quan trọng là chỉ thêm những tương tác có tác động có ý nghĩa và có thể hiểu được.

> ****Ví dụ:**** Một nhà bán lẻ có thể tạo tương tác feature giữa độ tuổi và thu nhập với model khả năng mua đồ điện tử cao cấp. Người tiêu dùng trẻ hơn có thu nhập cao có thể hành xử khác với người tiêu dùng lớn tuổi có thu nhập tương tự và thuật ngữ tương tác sẽ thể hiện mối quan hệ mang nhiều sắc thái này.

Giảm kích thước
---------------

Kỹ thuật giảm kích thước rất cần thiết khi làm việc với dữ liệu nhiều chiều, vì chúng giúp đơn giản hóa dữ liệu trong khi vẫn bảo toàn các mẫu và cấu trúc quan trọng nhất. Việc giảm số lượng features giúp trực quan hóa dữ liệu dễ dàng hơn, loại bỏ nhiễu và nâng cao hiệu quả của machine learning algorithms.

### 1\. Principal Component Analysis (PCA)

[PCA](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/) là một kỹ thuật tuyến tính giúp giảm tính chiều của dữ liệu bằng cách chuyển đổi features ban đầu thành một tập hợp features không tương quan nhỏ hơn được gọi là các thành phần chính. Các thành phần này thu được variance tối đa trong dữ liệu.

![bfsbfhs8](https://media.geeksforgeeks.org/wp-content/uploads/20260317145000712683/bfsbfhs8.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** PCA rất hữu ích để giảm số lượng features trong dataset trong khi vẫn giữ được hầu hết các biến thể, chẳng hạn như tóm tắt các biến tài chính tương quan như lợi nhuận chứng khoán thành ít thành phần chính hơn chiếm phần lớn variance.
* ****Không phù hợp:**** PCA không hiệu quả đối với datasets trong đó features có liên quan phi tuyến tính vì nó chỉ nắm bắt các mối quan hệ tuyến tính. Ngoài ra, sẽ không lý tưởng nếu dữ liệu chứa các biến classification không thể dễ dàng biểu diễn trong một không gian liên tục.

> ****Ví dụ:**** Trong dataset có số lượng lớn features thể hiện hành vi của khách hàng trong nền tảng thương mại điện tử, PCA có thể giúp giảm kích thước và tạo features mới (các thành phần chính) nắm bắt các mẫu chính trong hành vi của khách hàng.

### 2\. T-SNE (Nhúng hàng xóm ngẫu nhiên phân phối t)

[T-SNE](https://www.geeksforgeeks.org/machine-learning/ml-t-distributed-stochastic-neighbor-embedding-t-sne-algorithm/) là một kỹ thuật giảm kích thước phi tuyến tính được sử dụng để trực quan hóa dữ liệu chiều cao theo hai hoặc ba chiều bằng cách duy trì sự tương đồng theo cặp giữa các điểm dữ liệu trong không gian chiều thấp hơn.

![t-SNE](https://media.geeksforgeeks.org/wp-content/uploads/20250518141350348130/t-SNE.webp "Click to enlarge")

* ****Được sử dụng tốt nhất****: t-SNE rất hữu ích để hiển thị dữ liệu nhiều chiều như kết quả clustering hoặc datasets phức tạp, giúp hiển thị các mẫu hoặc cụm khó nhìn thấy ở các chiều cao hơn.
* ****Không phù hợp****: t-SNE có chi phí tính toán cao và có thể gặp khó khăn với datasets rất lớn. Nó cũng không duy trì các mối quan hệ toàn cầu, do đó, nó có thể làm sai lệch khoảng cách giữa các điểm dữ liệu, khiến nó không phù hợp với các nhiệm vụ yêu cầu mối quan hệ chính xác.

> ****Ví dụ:**** Trong dataset chứa features như độ tuổi, thu nhập và lịch sử mua hàng của khách hàng, t-SNE có thể được sử dụng để trực quan hóa cách phân cụm khách hàng dựa trên hành vi mua hàng trong biểu đồ hai chiều, giúp chúng ta xác định các phân khúc khách hàng.

### 3\. UMAP (Xấp xỉ và phép chiếu đa dạng đồng nhất)

[UMAP](https://www.geeksforgeeks.org/machine-learning/umap-uniform-manifold-approximation-and-projection/) là một kỹ thuật giảm kích thước phi tuyến tính tương tự như t-SNE, nhưng nó nhanh hơn và bảo toàn cả cấu trúc dữ liệu cục bộ và toàn cầu. Nó hoạt động bằng cách xây dựng biểu đồ dữ liệu và nhúng nó vào không gian có chiều thấp hơn trong khi vẫn giữ được cấu trúc ban đầu nhiều nhất có thể.

![UMAP](https://media.geeksforgeeks.org/wp-content/uploads/20240703185120/UMAP.webp "Click to enlarge")

* ****Được sử dụng tốt nhất:**** UMAP rất hữu ích để trực quan hóa dữ liệu nhiều chiều, đặc biệt là datasets lớn, vì nó bảo tồn cả cấu trúc cục bộ và tổng thể, khiến nó phù hợp với clustering, classification, anomaly detection và các ứng dụng như phân tích bộ gen hoặc hình ảnh feature.
* ****Không phù hợp:**** Giống như t-SNE, UMAP có thể làm sai lệch khoảng cách chính xác của điểm dữ liệu, do đó, nó không phù hợp với các tác vụ yêu cầu số liệu khoảng cách chính xác. Nó cũng yêu cầu điều chỉnh hyperparameters cẩn thận để có được kết quả tối ưu.

> ****Ví dụ:**** Một nhà khoa học dữ liệu có thể sử dụng UMAP để trực quan hóa features về tương tác của khách hàng với cửa hàng trực tuyến, giảm dữ liệu nhiều chiều thành hai hoặc ba chiều để khám phá các xu hướng hoặc cụm có thể chỉ ra các chiến lược tiếp thị tiềm năng.

Câu đố được đề xuất
----------

Thước đo nào về xu hướng trung tâm ít bị ảnh hưởng nhất bởi các giá trị cực trị hoặc outliers?

- [ ] A. Nghĩa
    
- [ ] B. Trung vị
    
- [ ] C. Chế độ
    
- [ ] D. Độ lệch chuẩn

Khi nào Phạm vi liên tứ phân vị (IQR) được ưu tiên hơn độ lệch chuẩn?

- [ ] A. Khi dữ liệu được phân phối bình thường
    
- [ ] B. Khi so sánh nhiều datasets đối xứng
    
- [ ] C. Khi chúng ta muốn phát hiện outliers và tập trung vào 50% ở giữa
    
- [ ] D. Để tính giá trị trung bình

Kịch bản nào cho thấy sự cần thiết phải chuyển đổi nhật ký?

- [ ] A. Dữ liệu có phân bố chuẩn
    
- [ ] B. Dữ liệu có độ lệch dương cao
    
- [ ] C. Dữ liệu có độ lệch chuẩn thấp
    
- [ ] D. Dữ liệu không có outliers

Hình dung nào là tốt nhất để so sánh sự phân bố và mật độ giữa nhiều nhóm?

- [ ] A. Sơ đồ hộp
    
- [ ] B. Âm mưu đàn vĩ cầm
    
- [ ] C. Biểu đồ hình tròn
    
- [ ] D. Batch đất

Mục đích chính của bản đồ nhiệt tương quan là gì?

- [ ] A. Xác định tần số classification
    
- [ ] B. Phát hiện outliers trong dữ liệu số
    
- [ ] C. Thể hiện mối quan hệ giữa các biến số
    
- [ ] D. Hiển thị xu hướng theo chuỗi thời gian

Kỹ thuật nào phù hợp nhất để phát hiện outliers trong datasets chiều cao?

- [ ] A. Z-điểm
    
- [ ] B. Sơ đồ hộp
    
- [ ] C. Rừng cách ly
    
- [ ] D. Nghĩa

Đa thức features hữu ích nhất khi:

- [ ] A. Tất cả features đều có mối quan hệ tuyến tính
    
- [ ] B. Tồn tại mối quan hệ phi tuyến tính giữa features và mục tiêu
    
- [ ] C. Dataset chỉ có các biến classification
    
- [ ] D. Outliers thống trị dataset

Principal Component Analysis (PCA) chủ yếu được sử dụng cho:

- [ ] A. Giảm kích thước trong khi vẫn giữ được variance tối đa
    
- [ ] B. Trực quan hóa datasets nhỏ
    
- [ ] C. Phát hiện outliers
    
- [ ] D. Tạo features classification

Câu nào về t-SNE là đúng?

- [ ] A. Nó bảo tồn cấu trúc toàn cầu một cách hoàn hảo
    
- [ ] B. Nó nhanh đối với datasets rất lớn
    
- [ ] C. Tốt nhất để hiển thị các cụm có chiều cao
    
- [ ] D. Nó chỉ hoạt động với dữ liệu classification

Mục đích chính của việc tạo tương tác features trong dataset là gì?

- [ ] A. Để giảm số lượng features trong dataset
    
- [ ] B. Để nắm bắt được tác động kết hợp của hai hoặc nhiều features lên biến mục tiêu
    
- [ ] C. Để xác định và loại bỏ outliers khỏi dataset
    
- [ ] D. Để chuyển đổi dữ liệu bị lệch thành phân bố chuẩn
