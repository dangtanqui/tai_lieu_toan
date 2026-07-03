# Hướng dẫn dịch PDF ISL/ISLP sang tiếng Việt (LaTeX)

Tool: `translate_pdf_vi.py` — trích xuất PDF → dịch → xuất LaTeX có thể chỉnh sửa → biên dịch lại PDF.

## Yêu cầu

- Python 3.10+
- [MiKTeX](https://miktex.org/) (hoặc TeX Live) với **XeLaTeX**
- Kết nối internet (khi dịch qua Google Translate)

Cài dependency:

```bash
cd "AI/tai_lieu/An Introduction to Statistical Learning"
pip install -r requirements-translate.txt
```

## Cấu trúc thư mục

| Thư mục / file | Vai trò |
|----------------|---------|
| `ilovepdf_split/An Introduction to Statistical Learning-{N}.pdf` | PDF tiếng Anh gốc (đã cắt part) |
| `vi/An Introduction to Statistical Learning-{N}.pdf` | PDF Google dịch (tham khảo, không bắt buộc chính xác) |
| `translate_pdf_vi.py` | Script chính |
| `.translate_cache_vi.json` | Cache bản dịch (tái sử dụng khi chạy lại) |
| `vi_latex/An Introduction to Statistical Learning-{N}/` | Output chỉnh sửa được |
| `vi_latex/An Introduction to Statistical Learning-{N}/blocks.json` | **Nguồn chính để sửa tay** |
| `vi_latex/.../content.tex`, `main.tex` | LaTeX sinh tự động từ `blocks.json` |
| `vi_latex/.../figures/` | Ảnh trích từ PDF (chỉ khi **không** dùng `--no-images`) |
| `vi_latex/An Introduction to Statistical Learning-{N}.pdf` | PDF tiếng Việt sau compile |

**Part** = số thứ tự file sau khi cắt bằng ilovepdf (1–12). Mỗi part xử lý độc lập.

## Đọc song song (khuyến nghị: bỏ hình trong bản dịch)

Nếu bạn mở **PDF gốc tiếng Anh** và **PDF dịch** cạnh nhau, không cần nhúng hình vào bản Việt. Thêm `--no-images` để:

- Bỏ qua trích ảnh ra `figures/` (extract nhanh hơn, ít dung lượng)
- Không chèn `\includegraphics` vào `content.tex` / PDF dịch
- Compile LaTeX nhẹ hơn

Căn nội dung theo comment `% --- page N ---` trong `content.tex`, hoặc theo tiêu đề section.

```bash
python translate_pdf_vi.py --part N --all --no-images
```

Đã extract có `figures/` từ trước? Chỉ cần export lại:

```bash
python translate_pdf_vi.py --part N --export-latex --compile --no-images
```

## Quy trình nhanh (lần đầu)

```bash
cd "AI/tai_lieu/An Introduction to Statistical Learning"

# Part 1: extract + dịch + xuất LaTeX + compile PDF (~30–60 phút/part)
python translate_pdf_vi.py --part 1 --all --no-images
```

Lặp lại với `--part 2`, `--part 3`, … cho toàn bộ sách.

## Quy trình từng bước

```bash
# 1. Trích block từ PDF EN + PDF Google (nếu có)
python translate_pdf_vi.py --part 1 --extract --no-images

# 2. Dịch (ghi vào blocks.json, field "vi")
python translate_pdf_vi.py --part 1 --translate

# 3. Xuất LaTeX
python translate_pdf_vi.py --part 1 --export-latex --no-images

# 4. Biên dịch PDF (xelatex)
python translate_pdf_vi.py --part 1 --compile
```

## Chỉnh sửa tay và build lại

**Sửa file:** `vi_latex/An Introduction to Statistical Learning-1/blocks.json`

Tìm block theo `id` (ví dụ `p12_b2`), chỉnh field `"vi"`:

```json
{
  "id": "p12_b2",
  "en": "Statistical learning refers to...",
  "vi": "Statistical learning là một bộ công cụ..."
}
```

**Không nên** sửa `content.tex` làm nguồn chính — file này bị ghi đè mỗi lần `--export-latex`.

Sau khi sửa:

```bash
python translate_pdf_vi.py --part 1 --fix-existing
python translate_pdf_vi.py --part 1 --export-latex --compile --no-images
```

- `--fix-existing`: áp dụng lại sửa thuật ngữ tự động, phân loại block, lọc nhiễu biểu đồ (`o`/`Ồ`…).

## Các tùy chọn hữu ích

| Lệnh | Mô tả |
|------|--------|
| `--part N` | Chọn part (mặc định `1`) |
| `--all` | `extract` + `translate` + `export-latex` + `compile` |
| `--page-range 12-20` | Chỉ dịch/sửa trang 12–20 |
| `--force` | Dịch lại dù block đã có `vi` |
| `--no-vi-ref` | Bỏ PDF Google, chỉ dùng translator online |
| `--fix-existing` | Polish + reclassify + dọn nhiễu, không dịch lại |
| `--no-toc` | Xuất `main.tex` không có `\tableofcontents` |
| `--no-images` | Không trích/nhúng hình — dùng khi đọc song song PDF gốc |
| `--allow-en-fallback` | Xuất tiếng Anh nếu thiếu `vi` (không khuyến nghị) |

Ví dụ dịch thử vài trang:

```bash
python translate_pdf_vi.py --part 1 --translate --page-range 12-15
python translate_pdf_vi.py --part 1 --export-latex --no-images
```

## Pipeline bên trong

```
PDF EN (ilovepdf_split)  ──┐
                           ├── extract ──► blocks.json [+ figures/]
PDF VI Google (vi/)     ───┘                    │
                                                ▼
                                         translate (vi)
                                                │
                                                ▼
                                    export-latex ──► main.tex, content.tex
                                                │
                                                ▼
                                         xelatex ──► main.pdf
```

(`figures/` và `\includegraphics` chỉ khi không dùng `--no-images`.)

## Lưu ý khi đọc kết quả

1. **Phải chạy `--translate` xong** trước khi export — nếu không PDF/LaTeX sẽ thiếu tiếng Việt.
2. **Mục lục LaTeX** chỉ gồm heading thật (dạng `1 Tiêu đề`, `2.1 Tiêu đề`…). Dòng thường (tên tác giả, nhãn trục, mảnh công thức) không vào TOC; dùng `--no-toc` nếu vẫn thấy lộn xộn.
3. **Công thức** (`Pr(Y|X)`, `X_1`, `max_j`…) được chuẩn hóa khi `--fix-existing` và bọc `$...$` khi xuất LaTeX. Sửa tay trong `blocks.json` nếu còn sai.
4. **Điểm trên biểu đồ** (`o`, `Ồ`, `X1`…) là nhiễu trích từ hình — đã được lọc. Với `--no-images`, hình không xuất ra PDF dịch; xem hình trên PDF gốc khi đọc song song.
5. **Trang bìa** có thể lỗi font encoding từ PDF gốc — sửa tay trong `blocks.json` nếu cần.
6. Thuật ngữ ML giữ **tiếng Anh** (`statistical learning`, `feature`, `model`, …) kèm giải thích tiếng Việt — giống tool dịch notebook Coursera.

## Xử lý sự cố

| Triệu chứng | Cách xử lý |
|-------------|------------|
| PDF ra toàn tiếng Anh | Chạy `--translate` (hoặc `--all`), không dùng `--allow-en-fallback` |
| Hàng loạt chữ `Ồ` | `python translate_pdf_vi.py --part N --fix-existing` rồi `--export-latex` |
| `xelatex` không tìm thấy | Cài MiKTeX, thêm vào PATH, chạy `xelatex --version` |
| Dịch chậm / bị giới hạn | Bình thường (~1400 block/part); dùng `--page-range` chia nhỏ |
| Muốn dịch lại một đoạn | `--translate --page-range X-Y --force` |

## Tham khảo

- Tool notebook tương tự: `AI/coursera/Machine learning/Machine-Learning-Specialization-Coursera/translate_notebooks_vi.py`
- Sửa thuật ngữ: chỉnh `POST_FIXES` và `PROTECT_TERMS` trong `translate_pdf_vi.py`
