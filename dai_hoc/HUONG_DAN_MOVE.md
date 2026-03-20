# Hướng dẫn chuyển file từ nam_* sang nhom_*

## Cách chạy

Mở terminal trong thư mục `dai_hoc` và chạy:

```bash
bash move_to_nhom.sh
```

Hoặc:

```bash
python3 move_to_nhom.py
```

## Script làm gì

- Di chuyển tất cả file `ly_thuyet.tex` từ các folder `nam_1`, `nam_2`, `nam_3`, `nam_4` sang các folder tương ứng trong `nhom_*`
- Môn trùng đích (ví dụ: Toán cao cấp 1, Đại số tuyến tính nâng cao → cùng `dai_so_tuyen_tinh`) được đặt tên khác: `ly_thuyet.tex`, `ly_thuyet_nang_cao.tex`, `ly_thuyet_nang_cao_2.tex`

## Sau khi chạy

- Xóa các folder rỗng trong `nam_*` nếu muốn (hoặc giữ lại để tham khảo)
- Xóa file `move_to_nhom.py` và `move_to_nhom.sh` nếu không cần nữa
