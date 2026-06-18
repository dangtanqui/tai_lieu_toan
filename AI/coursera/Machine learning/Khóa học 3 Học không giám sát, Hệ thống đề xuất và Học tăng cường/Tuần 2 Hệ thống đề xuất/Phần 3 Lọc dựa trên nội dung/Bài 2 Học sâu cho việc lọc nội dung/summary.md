## Kiến trúc: hai mạng neural network

- **User network**: \(x_u\) → vài lớp Dense → \(v_u\) (32 số)
- **Movie network**: \(x_m\) → vài lớp Dense → \(v_m\) (32 số)
- Dự đoán: \(\hat{y} = v_u \cdot v_m\)
- Hai mạng có thể khác số lớp ẩn, nhưng **lớp output cùng kích thước**

## Sơ đồ kết hợp

- Vẽ chung một diagram: phần trên = user network, phần dưới = movie network → dot product
- Nhãn nhị phân: \(\hat{y} = \sigma(v_u \cdot v_m)\)

## Cost function và huấn luyện

\[J = \sum_{(i,j): r(i,j)=1} \left(v_u^{(j)} \cdot v_m^{(i)} - y^{(i,j)}\right)^2 + \text{regularization}\]

- **Một** cost function huấn luyện **cả hai** mạng — không tách riêng
- Tối ưu bằng gradient descent / Adam

## Tìm item tương tự & lưu ý thực tế

- So khoảng cách \(v_m^{(k)}\) và \(v_m^{(i)}\) — tương tự collaborative filtering
- Có thể **pre-compute** phim tương tự qua đêm
- **Feature engineering** rất quan trọng trong triển khai thương mại
- Hạn chế: tốn kém tính toán với catalog lớn → bài sau giải quyết
