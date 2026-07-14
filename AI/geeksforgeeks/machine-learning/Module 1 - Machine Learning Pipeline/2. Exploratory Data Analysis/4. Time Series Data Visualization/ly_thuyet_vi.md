Dữ liệu chuỗi thời gian là dữ liệu được lập chỉ mục theo thứ tự thời gian, thường được thu thập theo định kỳ. Nó cho thấy mọi thứ thay đổi như thế nào ở những thời điểm khác nhau, như giá cổ phiếu hàng ngày hoặc nhiệt độ hàng giờ.

* Nó được sử dụng trong các ngành như tài chính, dược phẩm, truyền thông xã hội và nghiên cứu.
* Phân tích và trực quan hóa dữ liệu này giúp chúng ta tìm ra xu hướng, model và hành vi theo mùa.
* Những hiểu biết sâu sắc này hỗ trợ dự báo và hướng dẫn việc ra quyết định tốt hơn.
* Mục tiêu chính là nghiên cứu dữ liệu kịp thời để trích xuất các mẫu có ý nghĩa và predictions.

Các khái niệm trong phân tích chuỗi thời gian
--------------------------------

* ****Xu hướng:**** Hướng dữ liệu dài hạn (tăng, giảm hoặc ổn định).
* **** Tính thời vụ: **** Các mẫu lặp lại đều đặn.
* ****Đường trung bình động: **** Làm dịu các biến động ngắn hạn để làm nổi bật các xu hướng.
* ****Tiếng ồn:**** Các biến thể ngẫu nhiên không có hình mẫu rõ ràng.
* ****Khác biệt:**** Tính toán sự khác biệt giữa các giá trị tại một khoảng nhất định.
* ****Tính dừng:**** Chuỗi thời gian có các đặc tính thống kê (trung bình, variance, tự tương quan) không đổi theo thời gian.
* ****Thứ tự:**** Thứ tự sai phân đề cập đến số lần dữ liệu chuỗi thời gian cần được sai phân để đạt được tính dừng.
* ****Tự tương quan****[: Tự tương quan](https://www.geeksforgeeks.org/machine-learning/autocorrelation/) là một phương pháp thống kê được sử dụng trong phân tích chuỗi thời gian để định lượng mức độ tương tự giữa chuỗi thời gian và phiên bản bị trễ của chính nó.
* ****Lấy mẫu lại****: [Lấy mẫu lại](https://www.geeksforgeeks.org/python/how-to-resample-time-series-data-in-python/) là một kỹ thuật phân tích chuỗi thời gian được sử dụng để thay đổi tần suất quan sát dữ liệu.

### Các loại dữ liệu chuỗi thời gian

Dữ liệu chuỗi thời gian được xác định bằng cách lập chỉ mục dựa trên thời gian thay vì liên tục hoặc rời rạc. Nó có thể chứa cả giá trị liên tục và giá trị rời rạc tùy thuộc vào dataset.

1. ****Chuỗi thời gian liên tục****: Dữ liệu được ghi đều đặn với phạm vi giá trị liên tục như nhiệt độ, giá cổ phiếu, Dữ liệu cảm biến, v.v.
2. ****Chuỗi thời gian rời rạc****: Dữ liệu có các giá trị hoặc danh mục riêng biệt được ghi lại tại các thời điểm cụ thể như số lượng sự kiện, trạng thái classification, v.v. *****.****

### Phương pháp trực quan hóa

1. Sử dụng biểu đồ đường hoặc biểu đồ vùng để có dữ liệu liên tục nhằm làm nổi bật các xu hướng và biến động.
2. Sử dụng biểu đồ thanh hoặc biểu đồ cho dữ liệu rời rạc để hiển thị tần suất hoặc mức phân bổ giữa các danh mục.

Trực quan hóa chuỗi thời gian thực tế với Python
-----------------------------------------------

Hãy thực hiện từng bước này:

> Chúng ta sẽ sử dụng dataset gốc mà bạn có thể tải xuống từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20250122170223461909/stock_data.csv).

### Bước 1: Cài đặt và nhập thư viện

Chúng ta sẽ sử dụng các thư viện [Numpy](https://www.geeksforgeeks.org/python/numpy-tutorial/), [Pandas](https://www.geeksforgeeks.org/pandas/pandas-tutorial/), [Sinh ra ở biển](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) và [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/).

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt from statsmodels.graphics.tsaplots import plot_acf from statsmodels.tsa.stattools import adfuller
```

### Bước 2: Đang tải Dataset

Ở đây chúng ta sẽ tải dataset và sử dụng phân tích\_dates parameter để chuyển đổi cột Ngày sang định dạng DatetimeIndex.

```python
df = pd.read_csv("/content/stock_data.csv",
parse_dates=True,
index_col="Date")
df.head()
```

****Đầu ra:****

![time1](https://media.geeksforgeeks.org/wp-content/uploads/20250517131526591586/time1.webp "Click to enlarge")

### Bước 3: Làm sạch dữ liệu

Chúng ta sẽ loại bỏ các cột khỏi dataset không quan trọng đối với việc hiển thị của chúng ta.

```python
df.drop(columns='Unnamed: 0', inplace =True)
df.head()
```

****Đầu ra:****

![time2](https://media.geeksforgeeks.org/wp-content/uploads/20250517131616457361/time2.webp "Click to enlarge")

### Bước 4: Vẽ đồ thị giá cổ phiếu cao

Vì cột 'Cao' là loại dữ liệu liên tục nên chúng ta sẽ sử dụng biểu đồ đường để trực quan hóa nó.

* ****sns.lineplot(data=df, x=df.index, y='High', label='High Price', color='blue')****: Vẽ biểu đồ Giá cao theo thời gian bằng cách sử dụng chỉ số ngày giờ trên trục x.

```python
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y='High', label='High Price', color='blue')
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Share Highest Price Over Time')
plt.show()
```

****Đầu ra:****

![time3](https://media.geeksforgeeks.org/wp-content/uploads/20250517131703557061/time3.webp "Click to enlarge")

### Bước 5: Lấy mẫu lại dữ liệu

Để hiểu rõ hơn về xu hướng của dữ liệu, chúng ta sẽ sử dụng phương pháp lấy mẫu lại để cung cấp cái nhìn rõ ràng hơn về xu hướng và mẫu khi chúng ta xử lý dữ liệu hàng ngày.

* ****df\_resampled = df.resample('ME').mean(numeric\_only=True):**** Lấy mẫu lại dữ liệu theo tần suất hàng tháng và tính giá trị trung bình của tất cả các cột số cho mỗi tháng.

```python
df_resampled = df.resample('ME').mean(numeric_only=True)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_resampled, x=df_resampled.index, y='High', label='Month Wise Average High Price', color='blue')
plt.xlabel('Date (Monthly)')
plt.ylabel('High')
plt.title('Monthly Resampling Highest Price Over Time')
plt.show()
```

Df\_resampled \= df.resample('ME').mean(numeric\_only\=True)

​

Sns.set(style\="whitegrid")

​

Plt.figure(figsize\=(12, 6))

Sns.lineplot(data\=df\_resampled, x\=df\_resampled.index, y\='Cao', label\='Giá cao trung bình thông minh trong tháng', color\='blue')

​

Plt.xlabel('Ngày (Hàng tháng)')

Plt.ylabel('Cao')

Plt.title('Lấy mẫu lại hàng tháng Giá cao nhất theo thời gian')

​

Plt.show()

****Đầu ra:****

![time4](https://media.geeksforgeeks.org/wp-content/uploads/20250517131804520255/time4.webp "Click to enlarge")

### Bước 6: Phát hiện tính thời vụ bằng tự tương quan

Chúng ta sẽ phát hiện tính thời vụ bằng cách sử dụng biểu đồ hàm tự tương quan (ACF). Các đỉnh đều đặn trong biểu đồ ACF cho thấy sự hiện diện của tính thời vụ.

```python
if 'Date' not in df.columns:
print("'Date' is already the index or not present in the DataFrame.") else:
df.set_index('Date', inplace=True)
plt.figure(figsize=(12, 6)) plot_acf(df['High'], lags=40)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function (ACF) Plot')
plt.show()
```

Nếu 'Ngày' không có trong df.columns:

Print("'Date' đã là chỉ mục hoặc không có trong DataFrame.")

Khác:

Df.set\_index('Ngày', inplace\=True)

​

Plt.figure(figsize\=(12, 6))

Cốt truyện\_acf(df\['Cao'\], trễ\=40)

Plt.xlabel('Lag')

Plt.ylabel('Tự tương quan')

Plt.title('Biểu đồ hàm tự tương quan (ACF)')

Plt.show()

****Đầu ra:****

![acf_high](https://media.geeksforgeeks.org/wp-content/uploads/20250717163910301650/acf_high.webp "Click to enlarge")

### Bước 7: Tính ổn định của Testing với bài kiểm tra ADF

Chúng ta sẽ thực hiện [Kiểm tra ADF](https://www.geeksforgeeks.org/python/how-to-check-if-time-series-data-is-stationary-with-python/) để chính thức kiểm tra tính dừng.

```python
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['High'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])
```

Từ statsmodels.tsa.stattools nhập adfuller

​

Kết quả \= adfuller(df\['High'\])

Print('Thống kê ADF:', result\[0\])

Print('p-value:', result\[1\])

Print('Giá trị tới hạn:', result\[4\])

****Đầu ra:****

![time-6](https://media.geeksforgeeks.org/wp-content/uploads/20250517132016402380/time-6.webp "Click to enlarge")

* Dựa trên Thống kê ADF, chúng ta chấp nhận giả thuyết khống, chỉ ra rằng dữ liệu không cố định theo thử nghiệm Augmented Dickey-Fuller.
* Điều này gợi ý rằng có thể cần phải lấy vi phân hoặc các phép biến đổi khác để đạt được tính dừng trước khi áp dụng chuỗi thời gian models nhất định.

### Bước 8: Khác biệt để đạt được tính dừng

Sự khác biệt liên quan đến việc trừ quan sát trước đó khỏi quan sát hiện tại để loại bỏ xu hướng hoặc tính thời vụ.

```python
df['high_diff'] = df['High'].diff()
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_diff'], label='Differenced High', linestyle='--', color='green')
plt.legend()
plt.title('Original vs Differenced High')
plt.show()
```

Df\['high\_diff'\] \= df\['High'\].diff()

​

Plt.figure(figsize\=(12, 6))

Plt.plot(df\['High'\], label\='Cao ban đầu', color\='blue')

Plt.plot(df\['high\_diff'\], label\='Cao khác biệt', linestyle\='--', color\='green')

Plt.legend()

Plt.title('Bản gốc so với Mức cao khác biệt')

Plt.show()

****Đầu ra:****

![time7](https://media.geeksforgeeks.org/wp-content/uploads/20250517132110281933/time7.webp "Click to enlarge")

### Bước 9: Làm mịn dữ liệu bằng đường trung bình động

****df\['High'\].diff():**** giúp tính toán sự khác biệt giữa các giá trị liên tiếp trong cột Cao. Hoạt động sai phân này được sử dụng để chuyển đổi chuỗi thời gian thành chuỗi mới thể hiện sự thay đổi giữa các quan sát liên tiếp.

```python
window_size = 120 df['high_smoothed'] = df['High'].rolling(window=window_size).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_smoothed'], label=f'Moving Average (Window={window_size})', linestyle='--', color='orange')
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Original vs Moving Average')
plt.legend()
plt.show()
```

Cửa sổ\_size \= 120

Df\['high\_smoothed'\] \= df\['High'\].rolling(window\=window\_size).mean()

​

Plt.figure(figsize\=(12, 6))

​

Plt.plot(df\['High'\], label\='Cao ban đầu', color\='blue')

Plt.plot(df\['high\_smoothed'\], label\=f'Trung bình di chuyển (Window={window\_size})', linestyle\='--', color\='orange')

​

Plt.xlabel('Ngày')

Plt.ylabel('Cao')

Plt.title('Gốc so với Trung bình động')

Plt.legend()

Plt.show()

****Đầu ra:****

![time8](https://media.geeksforgeeks.org/wp-content/uploads/20250517133642785018/time8.webp "Click to enlarge")

Điều này tính toán mức trung bình di chuyển của cột Cao với kích thước cửa sổ là 120(Một phần tư), tạo ra một đường cong mượt mà hơn trong chuỗi ****high\_smoothed****. Cốt truyện so sánh các giá trị Cao ban đầu với phiên bản được làm mịn.

### Bước 10: Dữ liệu gốc và dữ liệu khác biệt

In dữ liệu gốc và dữ liệu khác biệt cạnh nhau, chúng ta nhận được:

```python
df_combined = pd.concat([df['High'], df['high_diff']], axis=1)
print(df_combined.head())
```

Df\_combined \= pd.concat(\[df\['High'\], df\['high\_diff'\]\], axis\=1)

​

Print(df\_combined.head())

****Đầu ra:****

![time9](https://media.geeksforgeeks.org/wp-content/uploads/20250517133748935004/time9.PNG "Click to enlarge")

Do đó cột high\_diff thể hiện sự khác biệt giữa các giá trị cao liên tiếp. Giá trị đầu tiên của high\_diff là NaN vì không có giá trị trước đó để tính chênh lệch.

Vì có giá trị NaN nên chúng ta sẽ loại bỏ giá trị đó để tiếp tục thử nghiệm:

```python
df.dropna(subset=['high_diff'], inplace=True)
df['high_diff'].head()
```

Df.dropna(subset\=\['high\_diff'\], inplace\=True)

Df\['high\_diff'\].head()

****Đầu ra:****

![time10](https://media.geeksforgeeks.org/wp-content/uploads/20250517133850976653/time10.PNG "Click to enlarge")

```python
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['high_diff'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:', result[4])
```

Từ statsmodels.tsa.stattools nhập adfuller

​

Kết quả \= adfuller(df\['high\_diff'\])

Print('Thống kê ADF:', result\[0\])

Print('p-value:', result\[1\])

Print('Giá trị tới hạn:', result\[4\])

****Đầu ra:****

![time11](https://media.geeksforgeeks.org/wp-content/uploads/20250517133951917532/time11.PNG "Click to enlarge")

Vì giá trị p nhỏ hơn 0,05 nên chúng ta bác bỏ giả thuyết không và kết luận rằng chuỗi này là chuỗi dừng.

> Bạn có thể tải xuống mã nguồn từ [Đây](https://media.geeksforgeeks.org/wp-content/uploads/20250517134209429098/Time_Series_Analysis.zip).

Câu đố được đề xuất
----------

Xu hướng thể hiện điều gì trong một chuỗi thời gian?

- [ ] A. Nhiễu ngẫu nhiên trong dữ liệu
    
- [ ] B. Định hướng dài hạn của dữ liệu
    
- [ ] C. Biến động ngắn hạn
    
- [ ] D. Tính thời vụ hàng tháng

Biểu đồ nào thường được sử dụng để phát hiện tính thời vụ bằng phương pháp tự tương quan?

- [ ] A. Biểu đồ
    
- [ ] B. Cốt truyện ACF
    
- [ ] C. Biểu đồ phân tán
    
- [ ] D. Sơ đồ thanh

Sự khác biệt làm gì trong phân tích chuỗi thời gian?

- [ ] A. Tăng tiếng ồn
    
- [ ] B. Chuyển đổi dữ liệu classification sang số
    
- [ ] C. Loại bỏ xu hướng/tính thời vụ bằng cách trừ đi các giá trị trước đó
    
- [ ] D. Chia dữ liệu thành bộ training và testing

Phương pháp Pandas nào được sử dụng để lấy mẫu lại dữ liệu chuỗi thời gian (ví dụ: hàng ngày đến hàng tháng)?

- [ ] A. .shift()
    
- [ ] B. .rolling()
    
- [ ] C. .resample()
    
* D
    
    .sort\_values()
