# Bài 1 — Vòng lặp phát triển ML

## Iterative loop

1. Chọn kiến trúc (model, data, hyperparameter)
2. Implement và train — lần đầu hầu như chưa đủ tốt
3. Chạy **diagnostic**: bias/variance, error analysis
4. Quyết định: mạng lớn hơn, Lambda, thêm/bớt data/feature…
5. Lặp đến khi đạt hiệu suất mong muốn

## Ví dụ: spam classifier

- **Text classification**: email → spam (1) / không spam (0)
- Feature: top 10.000 từ → xᵢ = 0/1 (hoặc đếm tần suất)
- Model: logistic regression hoặc neural network

## Ý tưởng cải thiện (cần ưu tiên)

- Thu thêm data (honeypot email giả để thu spam)
- Feature từ email routing (header, đường đi qua server)
- Feature tinh vi hơn từ nội dung (stemming, từ đồng nghĩa)
- Phát hiện lỗi chính tả cố ý (watches, medicine…)

## Diagnostic hướng dẫn ưu tiên

- High bias → honeypot nhiều tháng có thể vô ích
- High variance → thêm data hiệu quả
- Error analysis (bài sau) giúp chọn hướng hứa hẹn nhất — có thể nhanh gấp ~10 lần
