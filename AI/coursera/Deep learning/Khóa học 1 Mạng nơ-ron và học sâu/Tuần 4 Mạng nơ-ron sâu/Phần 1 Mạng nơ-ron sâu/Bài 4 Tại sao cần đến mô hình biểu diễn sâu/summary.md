# Bài 4 — Tại sao cần mô hình biểu diễn sâu

## Trực giác 1: Biểu diễn phân cấp (hierarchical)

### Nhận diện khuôn mặt

| Lớp | Học gì |
|-----|--------|
| Sớm | **Cạnh** (edge detector) — vùng nhỏ |
| Giữa | **Bộ phận** mặt (mắt, mũi) — ghép cạnh |
| Sâu | **Khuôn mặt** hoàn chỉnh |

### Nhận dạng giọng nói

- Lớp sớm: đặc trưng sóng âm thấp (cao độ, hướng tăng/giảm)
- Lớp giữa: **phoneme** (âm vị) — đơn vị âm thanh cơ bản
- Lớp sâu: từ → cụm từ → câu

**Ý chính:** từ hàm **đơn giản** → ghép thành hàm **phức tạp** (compositional representation)

## Trực giác 2: Lý thuyết mạch (circuit theory)

- Hàm XOR parity \(x_1 \oplus x_2 \oplus \cdots \oplus x_n\):
  - Mạng **sâu** (độ sâu \(\sim \log n\)): ít node
  - Mạng **nông** (1 hidden layer): cần \(\sim 2^n\) hidden units — **tăng theo cấp số nhân**

→ Một số hàm **dễ tính bằng mạng sâu**, rất khó với mạng nông

## Thực tế khi làm việc

- **Deep learning** cũng là branding — nhưng mạng sâu thực sự hiệu quả
- Đừng cố quá nhiều lớp ẩn ngay từ đầu
- Quy trình: logistic regression → 1–2 hidden layers → tinh chỉnh độ sâu như siêu tham số
- Một số bài toán cần hàng chục lớp

## Liên hệ não bộ

- Có tương đồng lỏng lẻo (cạnh → khuôn mặt), nhưng analogy **có thể nguy hiểm** — xem Bài 8
