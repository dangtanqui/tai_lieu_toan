# Hướng dẫn dịch *Machine Learning* (Tom Mitchell) sang tiếng Việt (LaTeX)

Tool: `translate_pdf_vi.py` — trích xuất PDF → dịch → xuất LaTeX có thể chỉnh sửa → biên dịch lại PDF.

## Yêu cầu

- Python 3.8+ (repo dùng `.venv` Python 3.8)
- [MiKTeX](https://miktex.org/) (hoặc TeX Live) với **XeLaTeX**
- Kết nối internet (khi dịch qua Google Translate)

## Cài đặt (chạy một lần)

**Luôn dùng venv của repo** — máy thường không có lệnh `python`, và `python3` hệ thống thiếu `fitz` (PyMuPDF):

```bash
cd "/home/dtqui/Desktop/personal/tai_lieu_toan"
source .venv/bin/activate

pip install -r "AI/tai_lieu/Machine Learning Tom Mitchell/requirements-translate.txt"
```

Kiểm tra:

```bash
python3 -c "import fitz; from deep_translator import GoogleTranslator; print('OK')"
xelatex --version
```

Mọi lệnh bên dưới giả định đã `source .venv/bin/activate` và:

```bash
cd "AI/tai_lieu/Machine Learning Tom Mitchell"
```

Không activate venv thì gọi trực tiếp:

```bash
../../../.venv/bin/python3 translate_pdf_vi.py --part N ...
```

## Cấu trúc thư mục

| Thư mục / file | Vai trò |
|----------------|---------|
| `MachineLearningTomMitchell.pdf` | PDF tiếng Anh gốc (**421 trang**; `--part 1` đọc file này nếu chưa tách) |
| `ilovepdf_split/MachineLearningTomMitchell-{N}.pdf` | PDF đã cắt part (khuyến nghị khi dịch cả sách) |
| `vi/MachineLearningTomMitchell.pdf` hoặc `vi/...-{N}.pdf` | PDF Google dịch (tham khảo, không bắt buộc) |
| `translate_pdf_vi.py` | Script chính |
| `.translate_cache_vi.json` | Cache bản dịch (tái sử dụng khi chạy lại) |
| `vi_latex/MachineLearningTomMitchell-{N}/` | Output chỉnh sửa được |
| `vi_latex/.../blocks.json` | **Nguồn chính để sửa tay** |
| `vi_latex/.../content.tex`, `main.tex` | LaTeX sinh tự động từ `blocks.json` |
| `vi_latex/.../figures/` | Ảnh trích từ PDF (chỉ khi **không** dùng `--no-images`) |
| `vi_latex/MachineLearningTomMitchell-{N}.pdf` | PDF tiếng Việt sau compile |

**Part** = số thứ tự file trong `ilovepdf_split/` (1, 2, 3, …). Mỗi part xử lý độc lập.

## Đọc song song (khuyến nghị: bỏ hình trong bản dịch)

Nếu bạn mở **PDF gốc tiếng Anh** và **PDF dịch** cạnh nhau, không cần nhúng hình vào bản Việt. Thêm `--no-images` để:

- Bỏ qua trích ảnh ra `figures/` (extract nhanh hơn, ít dung lượng)
- Không chèn `\includegraphics` vào `content.tex` / PDF dịch
- Compile LaTeX nhẹ hơn

Căn nội dung theo comment `% --- page N ---` trong `content.tex`, hoặc theo tiêu đề section.

```bash
python3 translate_pdf_vi.py --part N --all --no-images
```

Đã extract có `figures/` từ trước? Chỉ cần export lại:

```bash
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Một file hay tách nhiều part?

| Cách | Khi nào dùng |
|------|----------------|
| **1 file** (`--part 1`, PDF gốc 421 trang) | Thử nghiệm hoặc máy đủ kiên nhẫn chờ dịch lâu |
| **Tách 8–10 part** (~40–70 trang/part) | **Khuyến nghị** — resume khi lỗi mạng, `blocks.json` nhỏ hơn, compile nhanh hơn |

Tách bằng [ilovepdf.com/split_pdf](https://www.ilovepdf.com/split_pdf), đặt tên `MachineLearningTomMitchell-1.pdf`, `-2.pdf`, … vào `ilovepdf_split/`.

## Quy trình chuẩn (mỗi part)

Thay `N` bằng số part (1, 2, 3, …):

```bash
# Lần đầu: extract + dịch + xuất + compile
python3 translate_pdf_vi.py --part N --all --no-images
```

Hoặc từng bước:

```bash
python3 translate_pdf_vi.py --part N --extract --no-images
python3 translate_pdf_vi.py --part N --translate
python3 translate_pdf_vi.py --part N --export-latex --no-images
python3 translate_pdf_vi.py --part N --compile
```

### Thử vài trang trước (khuyến nghị)

`--extract` luôn trích **cả part**; `--page-range` chỉ áp dụng cho `--translate` và `--fix-existing`:

```bash
python3 translate_pdf_vi.py --part N --extract --no-images
python3 translate_pdf_vi.py --part N --translate --page-range 1-5
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

### Dịch cả part theo từng đoạn trang

```bash
python3 translate_pdf_vi.py --part N --translate --page-range 1-35
python3 translate_pdf_vi.py --part N --translate --page-range 36-70
# cache + blocks.json giữ tiến độ giữa các lần chạy
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Sau khi cập nhật script / sửa thuật ngữ

Khi đã có `blocks.json` và muốn áp dụng logic mới (gộp đoạn văn, lọc header trang, `POST_FIXES`, …):

```bash
# Bước 1: gộp đoạn + polish (nhanh, không gọi Google)
python3 translate_pdf_vi.py --part N --fix-existing --no-retranslate-headings

# Bước 2: dịch lại (đoạn đã gộp + heading + paragraph)
python3 translate_pdf_vi.py --part N --translate --force

# Bước 3: xuất PDF
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

Hoặc gộp luôn dịch lại heading trong `--fix-existing` (chậm hơn, gọi Google):

```bash
python3 translate_pdf_vi.py --part N --fix-existing
python3 translate_pdf_vi.py --part N --translate --force
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Chỉnh sửa tay và build lại

**Sửa file:** `vi_latex/MachineLearningTomMitchell-{N}/blocks.json`

Tìm block theo `id` (ví dụ `p12_b2`), chỉnh field `"vi"`:

```json
{
  "id": "p12_b2",
  "en": "Inductive learning algorithms...",
  "vi": "..."
}
```

**Không nên** sửa `content.tex` làm nguồn chính — file bị ghi đè mỗi lần `--export-latex`.

```bash
python3 translate_pdf_vi.py --part N --fix-existing --no-retranslate-headings
python3 translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Các tùy chọn CLI

| Lệnh | Mô tả |
|------|--------|
| `--part N` | Chọn part (mặc định `1`) |
| `--all` | `extract` + `translate` + `export-latex` + `compile` |
| `--extract` | Trích block từ PDF → `blocks.json` (+ `figures/` nếu không `--no-images`) |
| `--translate` | Dịch field `vi` trong `blocks.json` |
| `--export-latex` | Sinh `main.tex`, `content.tex` |
| `--compile` | Chạy `xelatex` → `main.pdf` |
| `--page-range 12-20` | Chỉ `--translate` / `--fix-existing` trang 12–20 |
| `--force` | Dịch lại dù block đã có `vi` |
| `--fix-existing` | Gộp đoạn, reclassify, polish, (tuỳ chọn) dịch lại heading |
| `--no-retranslate-headings` | Với `--fix-existing`: bỏ bước dịch heading online |
| `--no-vi-ref` | Bỏ PDF Google trong `vi/`, chỉ dùng translator |
| `--no-toc` | Xuất `main.tex` không có `\tableofcontents` |
| `--no-images` | Không trích/nhúng hình — dùng khi đọc song song PDF gốc |
| `--allow-en-fallback` | Xuất tiếng Anh nếu thiếu `vi` (không khuyến nghị) |

## Pipeline

```
PDF EN (gốc hoặc ilovepdf_split)  ──┐
                                     ├── extract ──► blocks.json [+ figures/]
PDF VI Google (vi/)               ───┘                    │
                                                          ▼
                                                   translate (vi)
                                                          │
                                                          ▼
                                              export-latex ──► main.tex
                                                          │
                                                          ▼
                                                   xelatex ──► PDF
```

(`figures/` và `\includegraphics` chỉ khi không dùng `--no-images`.)

## Thuật ngữ và chất lượng dịch

- Giữ **tiếng Anh** các thuật ngữ ML phổ biến: `feature`, `model`, `training set`, `decision tree`, `gradient descent`, …
- Một số cụm được chuẩn hóa trong `POST_FIXES`, ví dụ:
  - `hypothesis space` → không gian giả thuyết
  - `training example` (không dịch thành “ví dụ training”)
  - `function` → hàm, `gradient` / `descent` giữ cụm `gradient descent`
  - `AirTemp` → Nhiệt độ không khí, `Warm` → Ấm, `Sky` → Bầu trời
- Sửa thêm: chỉnh `PROTECT_TERMS`, `POST_FIXES`, `HEADING_PROTECT_TERMS` trong `translate_pdf_vi.py`
- **Heading** (mục `3.1`, `3.2.1`, …) dịch riêng; header lặp đầu trang (`CHAPTER 3 … 59`, `74 MACHINE LEARNING`) bị lọc, không xuất ra PDF
- **Bullet** (`•`) xuất dạng `itemize`; đoạn văn bị tách dòng / nối bằng `-` được gộp trước khi dịch

## PDF output nhiều trang hơn PDF gốc?

Bình thường. Ví dụ part 2 gốc **70 trang** có thể ra PDF LaTeX **~110–120 trang** do:

- Tiếng Việt thường dài hơn tiếng Anh
- Ảnh + khoảng cách section (nếu không dùng `--no-images`)
- Không map 1:1 “trang PDF output” với “trang PDF gốc”

Nếu thấy **nội dung tiếng Anh** trong bản dịch: thường do `vi` vẫn còn từ tiếng Anh (heading chưa dịch, thuật ngữ được protect) — chạy `--fix-existing` rồi `--translate --force`, không phải do thiếu trang extract.

## Xử lý sự cố

| Triệu chứng | Cách xử lý |
|-------------|------------|
| `command not found: python` | Dùng `python3` hoặc `source .venv/bin/activate` |
| `No module named 'fitz'` | `pip install -r requirements-translate.txt` **trong venv** |
| `FileNotFoundError` ilovepdf_split | Đặt `MachineLearningTomMitchell.pdf` ở thư mục gốc (`--part 1`), hoặc tạo `ilovepdf_split/` |
| PDF / LaTeX thiếu tiếng Việt | Chạy `--translate` (hoặc `--all`); không dùng `--allow-en-fallback` |
| Heading vẫn tiếng Anh | `--fix-existing` (hoặc `--translate --force` — heading dùng `translate_heading`) |
| `--fix-existing` chạy rất lâu | Dùng `--no-retranslate-headings`; dịch heading sau bằng `--translate --force` |
| Dịch chậm / rate limit Google | `--page-range` chia nhỏ; tách PDF thành nhiều part |
| `xelatex` không tìm thấy | Cài MiKTeX/TeX Live |
| Muốn dịch lại một đoạn | `--translate --page-range X-Y --force` |
| Muốn dịch lại từ đầu | Xóa `.translate_cache_vi.json` (tuỳ chọn), rồi `--translate --force` |

## Ví dụ nhanh: part 2 (đã tách trong `ilovepdf_split/`)

```bash
source ../../../.venv/bin/activate
cd "AI/tai_lieu/Machine Learning Tom Mitchell"

python3 translate_pdf_vi.py --part 2 --fix-existing --no-retranslate-headings
python3 translate_pdf_vi.py --part 2 --translate --force
python3 translate_pdf_vi.py --part 2 --export-latex --compile --no-images
```

Output: `vi_latex/MachineLearningTomMitchell-2.pdf`

## Tham khảo

- Cùng pipeline: `AI/tai_lieu/An Introduction to Statistical Learning/HUONG_DAN_DICH_PDF.md`
- Tool notebook: `AI/coursera/Machine learning/Machine-Learning-Specialization-Coursera/translate_notebooks_vi.py`
