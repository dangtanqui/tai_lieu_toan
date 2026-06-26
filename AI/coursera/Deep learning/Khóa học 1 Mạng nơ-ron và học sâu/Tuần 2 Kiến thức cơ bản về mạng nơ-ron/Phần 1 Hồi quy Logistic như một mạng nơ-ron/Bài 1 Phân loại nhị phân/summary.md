## Phân loại nhị phân

- Tuần 2 giới thiệu **lập trình mạng nơ-ron**: **vector hóa**, **forward propagation**, **backward propagation**
- Dùng **hồi quy logistic** làm ví dụ đơn giản trước khi sang mạng nơ-ron đầy đủ

## Bài toán ví dụ

- Input: ảnh → output **y ∈ {0, 1}** (mèo / không mèo)
- Ảnh RGB 64×64 lưu 3 ma trận → **unroll** thành vector **x** kích thước \(n_x = 64 \times 64 \times 3 = 12{,}288\)

## Ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| \((x^{(i)}, y^{(i)})\) | Một mẫu huấn luyện |
| **m** | Số mẫu train (hoặc \(m_{\text{test}}\) cho test) |
| **n** / \(n_x\) | Số chiều feature |
| **X** | Ma trận \(n_x \times m\) — mỗi **cột** là một mẫu |
| **Y** | Ma trận \(1 \times m\) — nhãn xếp theo cột |

## Quy ước quan trọng

- Trong khóa này: xếp mẫu theo **cột** (không phải hàng như một số khóa khác)
- `X.shape` → `(n_x, m)`; `Y.shape` → `(1, m)`
- Có **notation guide** trên website khóa học khi quên ký hiệu
