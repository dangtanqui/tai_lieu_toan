## Vấn đề quy mô

- Catalog: hàng nghìn đến **hàng chục triệu** item
- Chạy neural network cho mọi item mỗi lần user vào → **không khả thi**

## Hai bước: Retrieval + Ranking

### 1. Retrieval (thu hẹp ứng viên)
- Nhanh, bao phủ rộng — chấp nhận nhiều item user không thích
- Ví dụ:
  - 10 phim gần nhất user xem → 10 phim tương tự mỗi phim (pre-computed)
  - Top 10 phim trong 3 thể loại user hay xem
  - Top 20 phim tại quốc gia user
- Kết quả: ~100–1000 ứng viên; loại trùng, loại đã xem/mua

### 2. Ranking (xếp hạng chi tiết)
- Chạy mô hình trên danh sách thu hẹp → chọn top đề xuất
- Tối ưu: pre-compute \(v_m\) cho mọi phim → chỉ inference **user network** một lần → dot product với \(v_m\) của ứng viên

## Trade-off

- Retrieval nhiều item hơn → chất lượng tốt hơn nhưng chậm hơn
- Thử nghiệm offline: so sánh xác suất \(P(y=1)\) hoặc điểm dự đoán khi retrieve 100 vs 500 vs 1000 item

## Kết quả

- Hệ thống **nhanh** (retrieval) + **chính xác** (ranking) trên catalog cực lớn
