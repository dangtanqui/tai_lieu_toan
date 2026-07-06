# Hướng dẫn dịch *Hands-On Machine Learning* (Aurélien Géron, 2nd ed.) sang tiếng Việt

Tool: `translate_pdf_vi.py` — trích xuất PDF → dịch → làm sạch → xuất LaTeX → biên dịch PDF.

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

Làm việc trong thư mục sách:

```bash
cd "AI/tai_lieu/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
```

## Lệnh chính — một dòng cho mỗi part

Thay `N` = 1, 2, 3, …

```bash
python3 translate_pdf_vi.py --part N --all
```

`--all` tự chạy đủ pipeline:

1. **extract** — trích text từ PDF (không trích hình)
2. **translate** — dịch sang tiếng Việt
3. **fix-existing** — gộp đoạn, loại code/footnote/caption/hình/meta, polish, reclassify heading
4. **export-latex** — sinh `main.tex` + `content.tex`
5. **compile** — XeLaTeX → PDF

Mặc định **không nhúng hình** (đọc song song PDF gốc tiếng Anh). Căn nội dung theo comment `% --- page N ---` trong `content.tex`.

Muốn có hình trong bản dịch:

```bash
python3 translate_pdf_vi.py --part N --all --with-images
```

## Chuẩn bị PDF

| File / thư mục | Vai trò |
|----------------|---------|
| `Hands-On_Machine_Learning_...-Aurelien-Geron.pdf` | PDF gốc (**851 trang**) — **không** dùng bản `-note.pdf` |
| `ilovepdf_split/Hands-On_Machine_Learning_...-{N}.pdf` | PDF đã cắt part (**khuyến nghị**) |
| `vi/...pdf` | PDF Google dịch (tham khảo, tùy chọn) |
| `translate_pdf_vi.py` | Script chính |
| `.translate_cache_vi.json` | Cache dịch (tự cập nhật khi dịch) |
| `vi_latex/Hands-On_Machine_Learning_...-{N}/` | Output |
| `vi_latex/.../blocks.json` | **Sửa tay tại đây** (field `"vi"`) — chỉ còn nội dung in PDF |
| `vi_latex/.../content.tex` | LaTeX sinh tự động — bị ghi đè khi export |
| `vi_latex/.../main.pdf` | PDF tiếng Việt sau compile |

Tên file part: `Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron-1.pdf`, `-2.pdf`, …

**Khuyến nghị tách PDF:** ~17 part × ~50 trang ([ilovepdf split](https://www.ilovepdf.com/split_pdf)) → đặt vào `ilovepdf_split/`. Có thể thử part 1 từ file gốc nếu chưa tách.

`blocks.json` **không chứa** code, footnote, chú thích hình, ảnh, header/footer PDF — các block đó bị lọc khi lưu.

## Sau khi sửa tay `blocks.json`

```bash
python3 translate_pdf_vi.py --part N --fix-existing --export-latex --compile
```

Hoặc ngắn hơn (chỉ fix + export + compile):

```bash
python3 translate_pdf_vi.py --part N --fix-existing --export-latex --compile --no-retranslate-headings
```

**Part 1** đã polish `content.tex` tay: chỉ compile, **không** `--export-latex`:

```bash
python3 translate_pdf_vi.py --part 1 --compile
```

## Các trường hợp khác

### Thử vài trang trước

```bash
python3 translate_pdf_vi.py --part 1 --extract --no-images
python3 translate_pdf_vi.py --part 1 --translate --page-range 1-5
python3 translate_pdf_vi.py --part 1 --fix-existing --export-latex --compile --no-images
```

### Dịch part theo đoạn (part dài, tránh mất tiến độ)

```bash
python3 translate_pdf_vi.py --part N --translate --page-range 1-25
python3 translate_pdf_vi.py --part N --translate --page-range 26-50
python3 translate_pdf_vi.py --part N --fix-existing --export-latex --compile
```

### Dịch lại toàn bộ (đã có `vi`)

```bash
python3 translate_pdf_vi.py --part N --translate --force
python3 translate_pdf_vi.py --part N --fix-existing --export-latex --compile
```

### Chỉ export lại LaTeX / PDF (đã có `blocks.json` dịch xong)

```bash
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Tùy chọn CLI

| Lệnh | Mô tả |
|------|--------|
| `--part N` | Part (mặc định `1`) |
| `--all` | Toàn bộ pipeline (mặc định không hình) |
| `--with-images` | Kèm `--all`: trích và nhúng hình |
| `--no-images` | Bỏ hình (dùng với từng bước riêng lẻ) |
| `--extract` / `--translate` / `--export-latex` / `--compile` | Từng bước |
| `--fix-existing` | Gộp đoạn, polish, reclassify, lọc block |
| `--page-range A-B` | Chỉ translate / fix-existing |
| `--force` | Dịch lại dù đã có `vi` |
| `--no-retranslate-headings` | Fix nhanh, không gọi Google cho heading |
| `--no-vi-ref` | Bỏ PDF trong `vi/` |
| `--no-toc` | Không sinh mục lục LaTeX |
| `--toc-depth N` | Độ sâu mục lục (1=section … 4=paragraph) |
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
| PDF thiếu tiếng Việt | Chạy lại `--all` hoặc `--translate` |
| Heading tiếng Anh | `--translate --force` hoặc `--fix-existing` (bỏ `--no-retranslate-headings`) |
| Còn code trong `blocks.json` | `--fix-existing` |
| Dịch quá chậm | Tách part nhỏ hơn; `--page-range` |

## Tham khảo

- `AI/tai_lieu/Machine Learning Tom Mitchell/HUONG_DAN_DICH_PDF.md`
- `AI/tai_lieu/An Introduction to Statistical Learning/HUONG_DAN_DICH_PDF.md`
