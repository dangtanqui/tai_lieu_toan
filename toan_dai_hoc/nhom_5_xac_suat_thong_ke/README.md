# Nhóm 5: Xác suất và thống kê

Giáo án `ly_thuyet.tex` trong từng môn dùng **cùng template** với giáo án Đại số tuyến tính (`nhom_1_dai_so_logic/A3_dai_so_tuyen_tinh/ly_thuyet.tex`): trang bìa, watermark, header/footer, các ô `dongco`, `dinhnghia`, `vidu`, `tongket`, v.v.

| Folder | ID | Môn |
|--------|-----|-----|
| X1_xac_suat | X1 | Xác suất |
| X2_thong_ke_toan | X2 | Thống kê toán |
| X3_thong_ke_ung_dung | X3 | Thống kê ứng dụng |
| X4_xac_suat_va_do_do | X4 | Xác suất và độ đo |
| X5_xac_suat_thong_ke_nang_cao | X5 | Xác suất thống kê nâng cao |
| X6_thong_ke_da_bien | X6 | Thống kê đa biến |
| X7_thong_ke_bayes | X7 | Thống kê Bayes |
| X8_qua_trinh_ngau_nhien | X8 | Quá trình ngẫu nhiên |

## Template dùng chung

- `_template/preamble.tex` — gói, header, 12 loại `tcolorbox`
- `_template/trang_bia.tex` — trang bìa (macro `\coverbookline`, `\covermaintitle`, `\coversubtitle`)
- `_template/loi_noi_dau.tex` — lời nói đầu nhóm 5
- `_template/apply_template.py` — tái áp dụng template sau khi sửa nội dung (giữ phần thân, bọc lại Động cơ / Tổng kết)

Mỗi `ly_thuyet.tex` khai báo metadata rồi `\input{../_template/...}`.

## Biên dịch PDF

```bash
cd X1_xac_suat   # hoặc X2_..., X3_...
pdflatex -interaction=nonstopmode ly_thuyet.tex
pdflatex -interaction=nonstopmode ly_thuyet.tex   # lần 2 cho mục lục
```

## Hướng phát triển tiếp (giống A3)

Nội dung hiện tại vẫn là **khung lý thuyết** (định nghĩa + công thức). Các bước tiếp theo khi biên soạn sâu:

1. Thêm ô **Ví dụ** có lời giải từng bước cho mỗi mục lớn.
2. Thêm **Ý nghĩa \& Trực giác** / **Ứng dụng** (y tế, ML, tài chính).
3. Mở rộng X1 tương đương độ dày A3 nếu cần một cuốn “xác suất đầy đủ”.
