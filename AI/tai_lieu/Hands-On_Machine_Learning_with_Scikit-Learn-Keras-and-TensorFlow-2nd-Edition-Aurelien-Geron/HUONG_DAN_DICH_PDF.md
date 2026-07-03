# Hướng dẫn dịch *Hands-On Machine Learning* (Aurélien Géron, 2nd ed.) sang tiếng Việt

Tool: `translate_pdf_vi.py` — trích xuất PDF → dịch → xuất LaTeX chỉnh sửa được → biên dịch lại PDF.

## Yêu cầu

- Python 3.8+ (dùng `.venv` của repo)
- [MiKTeX](https://miktex.org/) hoặc TeX Live với **XeLaTeX**
- Kết nối internet (Google Translate)

## Cài đặt (một lần)

```bash
cd "/home/dtqui/Desktop/personal/tai_lieu_toan"
source .venv/bin/activate

pip install -r "AI/tai_lieu/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron/requirements-translate.txt"
```

Kiểm tra:

```bash
python3 -c "import fitz; from deep_translator import GoogleTranslator; print('OK')"
xelatex --version
```

Làm việc trong thư mục sách (tên dài — dùng tab-complete):

```bash
cd "AI/tai_lieu/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
```

Hoặc không `activate` venv:

```bash
../../../.venv/bin/python3 translate_pdf_vi.py --part N ...
```

## Cấu trúc thư mục

| File / thư mục | Vai trò |
|----------------|---------|
| `Hands-On_Machine_Learning_...-Aurelien-Geron.pdf` | PDF gốc (**851 trang**) — dùng file này, **không** dùng bản `-note.pdf` |
| `ilovepdf_split/Hands-On_Machine_Learning_...-{N}.pdf` | PDF đã cắt part (**khuyến nghị bắt buộc**) |
| `vi/...pdf` | PDF Google dịch (tham khảo, tùy chọn) |
| `translate_pdf_vi.py` | Script chính |
| `.translate_cache_vi.json` | Cache dịch |
| `vi_latex/Hands-On_Machine_Learning_...-{N}/` | Output |
| `vi_latex/.../blocks.json` | **Sửa tay tại đây** (field `"vi"`) |
| `vi_latex/.../figures/` | Ảnh trích từ PDF (chỉ khi **không** dùng `--no-images`) |

Tên file part phải khớp prefix: `Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron-1.pdf`, `-2.pdf`, …

## Đọc song song (khuyến nghị: bỏ hình trong bản dịch)

Nếu bạn mở **PDF gốc tiếng Anh** và **PDF dịch** cạnh nhau, không cần nhúng hình vào bản Việt. Thêm `--no-images` để:

- Bỏ qua trích ảnh ra `figures/` (extract nhanh hơn, ít dung lượng)
- Không chèn `\includegraphics` vào `content.tex` / PDF dịch
- Compile LaTeX nhẹ hơn

Căn nội dung theo comment `% --- page N ---` trong `content.tex`, hoặc theo tiêu đề section.

```bash
# Quy trình khuyến nghị
python3 translate_pdf_vi.py --part N --all --no-images
```

Đã extract có `figures/` từ trước? Chỉ cần export lại:

```bash
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Bắt buộc tách PDF?

**Rất khuyến nghị.** 851 trang một lần sẽ:

- Extract/`blocks.json` cực lớn
- Dịch nhiều ngày, dễ mất tiến độ khi mạng lỗi
- Compile XeLaTeX rất chậm / thiếu RAM

Tách **~17 part × ~50 trang** bằng [ilovepdf split](https://www.ilovepdf.com/split_pdf), đặt vào `ilovepdf_split/`.

Có thể thử **part 1** từ file gốc (chưa tách) với `--part 1` — script đọc PDF đầy đủ ở thư mục gốc nếu chưa có file trong `ilovepdf_split/`.

## Quy trình chuẩn (mỗi part)

Thay `N` = 1, 2, 3, …

```bash
python3 translate_pdf_vi.py --part N --all --no-images
```

Hoặc từng bước:

```bash
python3 translate_pdf_vi.py --part N --extract --no-images
python3 translate_pdf_vi.py --part N --translate
python3 translate_pdf_vi.py --part N --export-latex --no-images
python3 translate_pdf_vi.py --part N --compile
```

### Thử vài trang trước

```bash
python3 translate_pdf_vi.py --part 1 --extract --no-images
python3 translate_pdf_vi.py --part 1 --translate --page-range 1-5
python3 translate_pdf_vi.py --part 1 --export-latex --compile --no-images
```

### Dịch part theo đoạn trang

```bash
python3 translate_pdf_vi.py --part N --translate --page-range 1-25
python3 translate_pdf_vi.py --part N --translate --page-range 26-50
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Sau khi cập nhật script

```bash
python3 translate_pdf_vi.py --part N --fix-existing --no-retranslate-headings
python3 translate_pdf_vi.py --part N --translate --force
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Chỉnh sửa tay

Sửa `vi_latex/Hands-On_Machine_Learning_...-{N}/blocks.json`, rồi:

```bash
python3 translate_pdf_vi.py --part N --fix-existing --no-retranslate-headings
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

Không sửa `content.tex` làm nguồn chính — bị ghi đè khi `--export-latex`.

## Tùy chọn CLI

| Lệnh | Mô tả |
|------|--------|
| `--part N` | Part (mặc định `1`) |
| `--all` | extract + translate + export + compile |
| `--page-range A-B` | Chỉ translate / fix-existing |
| `--force` | Dịch lại dù đã có `vi` |
| `--fix-existing` | Gộp đoạn, polish, reclassify |
| `--no-retranslate-headings` | Fix nhanh, không gọi Google cho heading |
| `--no-vi-ref` | Bỏ PDF trong `vi/` |
| `--no-toc` | Không sinh mục lục LaTeX |
| `--no-images` | Không trích/nhúng hình — dùng khi đọc song song PDF gốc |
| `--allow-en-fallback` | Xuất tiếng Anh nếu thiếu `vi` (không khuyến nghị) |

## Thuật ngữ

Giữ tiếng Anh: `feature`, `model`, `epoch`, `batch`, `training set`, `scikit-learn`, `Keras`, `TensorFlow`, `gradient descent`, `CNN`, `RNN`, …

Chỉnh trong `translate_pdf_vi.py`: `PROTECT_TERMS`, `POST_FIXES`, `HEADING_PROTECT_TERMS`.

## Xử lý sự cố

| Triệu chứng | Cách xử lý |
|-------------|------------|
| `No module named 'fitz'` | `pip install -r requirements-translate.txt` trong venv |
| `command not found: python` | Dùng `python3` hoặc `source .venv/bin/activate` |
| `FileNotFoundError` | Kiểm tra tên file PDF / `ilovepdf_split/` |
| PDF thiếu tiếng Việt | Chạy `--translate` trước `--export-latex` |
| Heading tiếng Anh | `--translate --force` hoặc `--fix-existing` |
| `--fix-existing` lâu | Thêm `--no-retranslate-headings` |
| Dịch quá chậm | Tách part nhỏ hơn; `--page-range` |

## Ví dụ part 1 (chưa tách — thử nghiệm)

```bash
source ../../../.venv/bin/activate
cd "AI/tai_lieu/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"

python3 translate_pdf_vi.py --part 1 --extract --no-images
python3 translate_pdf_vi.py --part 1 --translate --page-range 1-10
python3 translate_pdf_vi.py --part 1 --export-latex --compile --no-images
```

## Tham khảo

- `AI/tai_lieu/Machine Learning Tom Mitchell/HUONG_DAN_DICH_PDF.md`
- `AI/tai_lieu/An Introduction to Statistical Learning/HUONG_DAN_DICH_PDF.md`
