https://vungocthanh1984.blogspot.com

https://muonnha.com.vn/ban-nha-rieng-thu-duc
MjAyNi0wMy0yNFQwNzoyNjowNi43MTNa

30/4: https://drive.google.com/file/d/1KNxznCbI9AgRT-i0vXl1ypMYtqkyjKAA/edit

https://math.libretexts.org/Bookshelves

https://tutorial.math.lamar.edu/terms.aspx

https://www.youtube.com/watch?v=0l785AhLjFs&list=PLbM8_sG_bjwonfuK_04GtX-3U4DxlMb6M

https://www.mathvn.com/2010/09/giao-trinh-toan-cao-cap-a1-va-a2.html

https://toancaocap.net/giai-tich-2/ham-so-nhieu-bien/

https://chuyentoan.wordpress.com/

https://thuviendien.blogspot.com/

https://www.vms.org.vn/category/thong-tin-toan-hoc-1

https://diendantoanhoc.org/topic/125987-t%E1%BB%95ng-h%E1%BB%A3p-s%C3%A1ch-to%C3%A1n-cao-c%E1%BA%A5p-dai-cuong-d%C3%A0nh-cho-sinh-vi%C3%AAn-%C4%91h/

# Trên Windows

Lệnh terminal để sau này tự sinh PDF
Mở terminal tại thư mục chứa ly_thuyet.tex, rồi:

PowerShell (Windows):

Set-Location "d:\DangTanQui\Toan\tai_lieu_toan\cursor\toan_dai_hoc\nhom_1_dai_so_logic\A3_dai_so_tuyen_tinh"
pdflatex -interaction=nonstopmode ly_thuyet.tex

Chạy hai lần nếu bạn chỉnh nhiều \section/\subsection và muốn mục lục (\tableofcontents) cập nhật đúng:

pdflatex -interaction=nonstopmode ly_thuyet.tex; pdflatex -interaction=nonstopmode ly_thuyet.tex

Một lệnh gọn (nếu đã cd vào đúng thư mục):

pdflatex -interaction=nonstopmode ly_thuyet.tex

Nếu cài latexmk (MiKTeX thường có), tự gọi đủ số lần và dọn file phụ:

latexmk -pdf -interaction=nonstopmode ly_thuyet.tex

File PDF tạo ra cùng thư mục: ly_thuyet.pdf.

# Trên Ubuntu

## Cài gói LaTeX (một lần)

Cần `pdflatex` (và gói tiếng Việt `vntex` nếu dùng `\usepackage[vietnamese]{babel}`). Cách gọn:

```bash
sudo apt update
sudo apt install -y texlive-latex-extra texlive-lang-other texlive-fonts-recommended
```

Nếu thiếu font/gói, có thể cài bộ đầy đủ hơn (nặng, vài GB):

```bash
sudo apt install -y texlive-full
```

## Sinh PDF (mỗi lần chỉnh `ly_thuyet.tex`)

Mở terminal, `cd` vào thư mục chứa `ly_thuyet.tex` (đường dẫn trên máy bạn có thể khác, ví dụ):

```bash
cd ~/Desktop/personal/tai_lieu_toan/toan_dai_hoc/nhom_1_dai_so_logic/A3_dai_so_tuyen_tinh
pdflatex -interaction=nonstopmode ly_thuyet.tex
```

**Mục lục** (`\tableofcontents`) cập nhật đúng sau khi thêm/sửa `\section`/`\subsection`: chạy **hai lần** liên tiếp:

```bash
pdflatex -interaction=nonstopmode ly_thuyet.tex && pdflatex -interaction=nonstopmode ly_thuyet.tex
```

## Một lệnh gọn (đã `cd` đúng thư mục)

```bash
pdflatex -interaction=nonstopmode ly_thuyet.tex
```

## latexmk (tự chạy đủ số lần, tiện khi sửa nhiều)

```bash
sudo apt install -y latexmk
latexmk -pdf -interaction=nonstopmode ly_thuyet.tex
```

File PDF: `ly_thuyet.pdf` trong cùng thư mục với `ly_thuyet.tex`.
