## Unsupervised Learning là gì?
- Loại ML phổ biến thứ hai (sau supervised)
- Dữ liệu **không có nhãn y** → không có "đáp án đúng"
- Nhiệm vụ: tìm **cấu trúc / pattern** thú vị trong data
- Thuật toán **tự khám phá**, không bị "giám sát" bằng nhãn

## Supervised vs Unsupervised
| | Supervised | Unsupervised |
|---|------------|--------------|
| Nhãn | Có (benign/malignant...) | Không |
| Mục tiêu | Dự đoán y cho x mới | Tìm pattern / nhóm trong data |

## Clustering (phân cụm)
- Thuật toán unsupervised phổ biến nhất
- Gom data không nhãn thành các **cluster** (nhóm)

## Ví dụ ứng dụng

**Google News**
- Hàng trăm nghìn bài/ngày → gom bài liên quan (cùng từ khóa: panda, twin, zoo...)
- Không ai gán nhãn thủ công — algorithm tự tìm cluster mỗi ngày

**DNA / Gen**
- Mỗi cột = 1 người, mỗi hàng = 1 gene
- Clustering nhóm người theo đặc điểm di truyền (type 1, 2, 3...)

**Market segmentation (phân khúc khách hàng)**
- Gom khách hàng thành nhóm để phục vụ hiệu quả hơn
- Ví dụ DeepLearning.AI: học kỹ năng / phát triển sự nghiệp / cập nhật AI trong ngành

## Tóm tắt
> Clustering = unsupervised learning: **data không nhãn → tự gom nhóm**
