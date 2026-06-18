## K-means — ý tưởng trực quan

- Dữ liệu: m ví dụ **không nhãn** (ví dụ 30 điểm)
- Chọn K cụm (ví dụ K = 2) → đoán ban đầu vị trí **tâm cụm** (centroid)

## Hai bước lặp lại

1. **Gán điểm** — mỗi điểm gán vào centroid **gần nhất**
2. **Di chuyển centroid** — đặt centroid tại **trung bình** (mean) các điểm trong cụm

```
Lặp: Gán → Di chuyển → Gán → Di chuyển → ... cho đến hội tụ
```

## Hội tụ

- Khi không còn điểm nào đổi cụm và centroid không dịch chuyển → **đã hội tụ**
- Ví dụ 2 cụm: điểm phía trên vs phía dưới được tách khá tốt

## Thuật ngữ

- **Cluster centroid** — tâm cụm (μ₁, μ₂, ...)
- Khởi tạo ban đầu thường **ngẫu nhiên** và chưa tối ưu
