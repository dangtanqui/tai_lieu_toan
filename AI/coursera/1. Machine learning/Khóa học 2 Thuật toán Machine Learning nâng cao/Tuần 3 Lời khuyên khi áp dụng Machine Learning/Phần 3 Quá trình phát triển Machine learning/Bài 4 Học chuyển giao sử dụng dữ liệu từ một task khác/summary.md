# Bài 4 — Transfer learning

## Khi nào dùng

- Ít dữ liệu có nhãn cho task target
- Có dataset lớn task **liên quan** (cùng loại input)

## Hai bước

1. **Supervised pre-training**: train NN lớn trên task lớn (vd. 1M ảnh, 1000 lớp)
2. **Fine-tuning**: copy các layer trước output; thay output layer mới (10 lớp cho chữ số 0–9); train tiếp

## Hai cách fine-tune

- **Option 1** (dataset rất nhỏ): giữ W¹…W⁴ cố định, chỉ train W⁵, b⁵
- **Option 2** (dataset lớn hơn chút): train toàn bộ, khởi tạo từ pre-trained

## Pre-trained model có sẵn

- ImageNet, BERT, GPT-3… — download miễn phí, thay output layer, fine-tune
- Cộng đồng ML chia sẻ model/parameter

## Tại sao hoạt động

- Layer sớm học feature chung: cạnh, góc, hình cơ bản → hữu ích cho nhiều task vision
- Chỉ cần học thêm phần task-specific

## Ràng buộc

- Input x pre-training và fine-tuning phải **cùng kiểu** (ảnh→ảnh, audio→audio, text→text)
- Không panacea — nhưng có thể fine-tune từ vài chục đến vài nghìn ảnh
