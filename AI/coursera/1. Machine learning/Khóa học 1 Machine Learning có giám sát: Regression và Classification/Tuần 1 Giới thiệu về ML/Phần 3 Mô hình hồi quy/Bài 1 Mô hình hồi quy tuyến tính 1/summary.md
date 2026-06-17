## Linear Regression
- Model **đầu tiên** của khóa — fit **đường thẳng** vào data
- Thuật toán ML **phổ biến nhất** thế giới
- Nhiều khái niệm ở đây áp dụng cho model sau

## Bài toán: Dự đoán giá nhà (Portland)
- **x** = diện tích (sq ft) · **y** = giá ($)
- Ví dụ: nhà 1250 sq ft → fit đường thẳng → dự đoán ~**$220,000**

## Supervised + Regression
- **Train** từ data có đáp án đúng (size + price)
- Nhà khách hàng **không** có trong training set (chưa bán)
- Output là **số** → regression (khác classification: nhãn rời rạc)

## Regression vs Classification (nhắc lại)
| | Regression | Classification |
|---|------------|----------------|
| Output | Số (vô hạn) | Nhãn (hữu hạn) |
| Ví dụ | Giá nhà | Mèo / chó, bệnh / không bệnh |

## Ký hiệu chuẩn
| Ký hiệu | Ý nghĩa |
|---------|---------|
| **x** | Input / feature (diện tích) |
| **y** | Output / target (giá) |
| **m** | Số mẫu training (vd: 47) |
| **(x⁽ⁱ⁾, y⁽ⁱ⁾)** | Mẫu thứ i (hàng thứ i trong bảng) |
| **Training set** | Tập data dùng để train model |

**Lưu ý:** x⁽ⁱ⁾ không phải lũy thừa — chỉ là chỉ số mẫu thứ i.
