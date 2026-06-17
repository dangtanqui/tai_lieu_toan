# Bài 5 — Chu trình hoàn chỉnh dự án ML

## Các giai đoạn

1. **Scoping**: xác định bài toán (vd. voice search — nói thay vì gõ)
2. **Data collection**: thu audio + transcript
3. **Train model**: huấn luyện, error analysis, bias/variance
4. **Lặp**: quay lại thu thêm data (toàn bộ hoặc loại cụ thể — vd. audio trong xe)
5. **Deploy**: đưa vào production khi đủ tốt
6. **Monitor & maintain**: theo dõi, cập nhật model

## Deploy pattern

- Model trên **inference server**
- App mobile gọi API → gửi audio → server trả transcript
- Cần software engineering: scale, độ tin cậy, chi phí compute

## Monitoring

- Log input x và prediction ŷ (nếu privacy/consent cho phép)
- Phát hiện **data drift**: tên celebrity/politician mới → model tệ hơn → retrain
- Data từ production (nếu được phép) giúp cải thiện liên tục

## MLOps

- **MLOps** (Machine Learning Operations): quy trình xây dựng, deploy, duy trì hệ thống ML
- Tối ưu inference, logging, monitoring, model update
- Train model là phần quan trọng; deploy quy mô lớn cần thêm nhiều bước
