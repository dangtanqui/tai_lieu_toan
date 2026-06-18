# Bài 6 — Công bằng, thiên vị và đạo đức

## Vấn đề thực tế

- Công cụ tuyển dụng phân biệt giới tính
- Face recognition khớp người da tối với ảnh tội phạm nhiều hơn
- Phê duyệt vay ngân hàng thiên vị nhóm nhỏ
- Deepfake, bot nội dung giả, thuật toán khuếch đại ngôn từ độc hại
- ML cũng bị lạm dụng (spam, fraud)

## Nguyên tắc cá nhân

- Không xây hệ thống gây hại xã hội
- Từ chối dự án phi đạo đức dù có lợi nhuận

## Không có checklist 5 bước

- Đạo đức phức tạp — chỉ có hướng dẫn chung

## Gợi ý trước deploy

1. **Đội đa dạng** (giới, ethnicity, văn hoá…) brainstorm rủi ro, đặc biệt với nhóm dễ tổn thương
2. **Literature search**: tiêu chuẩn ngành (vd. tài chính — fairness trong phê duyệt vay)
3. **Audit** model theo các chiều bias đã xác định (giới, ethnicity…) trước production
4. **Mitigation plan**: rollback model cũ; monitor sau deploy; kế hoạch xử lý sự cố (như xe tự lái)

## Mức độ nghiêm trọng

- Roast coffee beans vs quyết định vay — hệ quả đạo đức rất khác nhau
- Cộng đồng ML cần phát hiện và sửa trước khi gây hại
