#!/usr/bin/env python3
"""Generate ly_thuyet.tex: full Ch.1 text + template boxes + figures + code."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = Path(__file__).resolve().parent
NB_CANDIDATES = [
    Path("/home/dtqui/.cursor/projects/home-dtqui-Desktop-personal-tai-lieu-toan/agent-tools/3eac57d0-c25e-4eaa-8766-ba8b15028fe0.txt"),
    ROOT / "01_the_machine_learning_landscape.ipynb",
]

# (unique substring in body, image file, caption)
FIGURE_ANCHORS = [
    ("kỹ thuật lập trình truyền thống:", "p33_b2.png", "Hình 1-1. Cách tiếp cận truyền thống"),
    ("kỹ thuật Machine Learning sẽ tự động tìm hiểu", "p34_b0.png", "Hình 1-2. Cách tiếp cận Machine Learning"),
    ("Dành cho U", "p34_b2.png", "Hình 1-3. Tự động thích ứng với sự thay đổi"),
    ("Machine Learning có thể giúp con người học hỏi", "p35_b1.png", "Hình 1-4. ML giúp con người học"),
    ("được gọi là nhãn", "p38_b4.png", "Hình 1-5. Training set có nhãn (spam)"),
    ("được gọi là regression", "p39_b1.png", "Hình 1-6. Bài toán regression"),
    ("dữ liệu training không được gắn nhãn", "p40_b0.png", "Hình 1-7. Training set không nhãn"),
    ("phát hiện các nhóm khách truy cập tương tự", "p41_b1.png", "Hình 1-8. Clustering"),
    ("trực quan hóa t-SNE", "p41_b4.png", "Hình 1-9. Trực quan hóa t-SNE"),
    ("phát hiện sự bất thường", "p42_b4.png", "Hình 1-10. Phát hiện bất thường"),
    ("học bán giám sát", "p43_b4.png", "Hình 1-11. Học bán giám sát"),
    ("Reinforcement Learning là một con thú rất khác", "p44_b2.png", "Hình 1-12. Reinforcement Learning"),
    ("nhanh chóng khi nó đến.", "p46_b1.png", "Hình 1-13. Online learning"),
    ("được gọi là học ngoài lõi", "p47_b0.png", "Hình 1-14. Out-of-core learning"),
    ("phân loại là một hình tam giác", "p48_b2.png", "Hình 1-15. Instance-based learning"),
    ("được gọi là model-based learning.", "p48_b6.png", "Hình 1-16. Model-based learning"),
    ("Bảng 1-1 cho thấy", "p49_b9.png", "Hình 1-17. GDP vs mức hài lòng"),
    ("Trước khi có thể sử dụng model", "p50_b3.png", "Hình 1-18. Một vài model tuyến tính"),
    ("Bây giờ model khớp với dữ liệu training", "fig1_18_fitted_model.png", "Hình 1-18. Model sau training"),
    ("Michele Banko và Eric Brill", "fig1_20_data_effectiveness.png", "Hình 1-20. Hiệu quả phi lý của dữ liệu"),
    ("một vài quốc gia đã bị mất tích", "fig1_21_nonrepresentative.png", "Hình 1-21. Training set không đại diện"),
    ("\\subsection{Tính năng không liên quan}", "fig1_22_correlation.png", "Hình 1-22. Features không liên quan (ví dụ)"),
    ("overfitting", "fig1_23_overfitting.png", "Hình 1-23. Overfitting"),
    ("regularization", "fig1_24_regularization.png", "Hình 1-24. Regularization"),
    ("được gọi là xác thực giữ lại", "fig1_25_validation.png", "Hình 1-25. Train / validation / test"),
]

TABLE = r"""
\begin{center}
\captionof{table}{Bảng 1-1. GDP bình quân đầu người và mức hài lòng (trích)}
\begin{tabular}{lrr}
\toprule
Quốc gia & GDP bình quân (USD) & Hài lòng \\
\midrule
Hungary & 12\,240 & 4{,}9 \\
Hàn Quốc & 27\,195 & 5{,}8 \\
Pháp & 37\,675 & 6{,}5 \\
Úc & 50\,962 & 7{,}3 \\
Hoa Kỳ & 55\,805 & 7{,}2 \\
\bottomrule
\end{tabular}
\end{center}
"""


def fig_tex(fname: str, cap: str, width: str = "0.75") -> str:
    # Non-floating: figures live inside breakable tcolorbox
    return (
        f"\n\\begin{{center}}\n"
        f"\\homlimg[{width}]{{{fname}}}\n"
        f"\\captionof{{figure}}{{{cap}}}\n"
        f"\\end{{center}}\n"
    )


def clean_code_for_latex(src: str) -> str:
    src = src.replace("\u2265", ">=")
    src = re.sub(r"^%matplotlib inline\n", "", src, flags=re.M)
    return src


def load_notebook_code():
    for path in NB_CANDIDATES:
        if not path.exists():
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        cells = []
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = "".join(cell.get("source", []))
            if not src.strip():
                continue
            if any(x in src for x in ("PROJECT_ROOT_DIR", "def save_fig", "np.random.seed", "CHAPTER_ID")):
                continue
            cells.append(clean_code_for_latex(src.rstrip()))
        return cells[:8]
    return [
        "import matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport sklearn.linear_model",
        "oecd_bli = pd.read_csv(\"oecd_bli_2015.csv\", thousands=',')\ngdp_per_capita = pd.read_csv(\"gdp_per_capita.csv\", thousands=',', delimiter='\\t', encoding='latin1', na_values=\"n/a\")",
        "country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)\nX = np.c_[country_stats[\"GDP per capita\"]]\ny = np.c_[country_stats[\"Life satisfaction\"]]",
        "country_stats.plot(kind='scatter', x=\"GDP per capita\", y='Life satisfaction')\nplt.show()",
        "model = sklearn.linear_model.LinearRegression()\nmodel.fit(X, y)",
        "X_new = [[22587]]\nprint(model.predict(X_new))  # ~5.96",
    ]


def clean(t: str) -> str:
    t = re.sub(r"% --- page \d+ ---\n", "", t)
    t = re.sub(r"% [^\n]+\n", "", t)
    t = t.replace("\u200b", "")
    t = re.sub(r"10⁻⁵", r"$10^{-5}$", t)
    t = t.replace("× 10–5", r"$\times 10^{-5}$")
    t = t.replace("θ", r"$\theta$")
    t = t.replace("theta_0", r"$\theta_0$")
    t = t.replace("theta_1", r"$\theta_1$")
    return t


def load_body() -> str:
    p1 = (ROOT / "vi_latex/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron-1/content.tex").read_text(encoding="utf-8")
    p2 = (ROOT / "vi_latex/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron-2/content.tex").read_text(encoding="utf-8")
    ch1_p1 = clean(p1[p1.index("\\subsection{Chương 1 Phong cảnh Machine Learning}") :])
    ch1_p2 = clean(p2[: p2.index("\\subsection{Chương 2")])
    ch1_p1 = ch1_p1.replace(
        "\\subsection{Chương 1 Phong cảnh Machine Learning}",
        "\\section{Chương 1: Phong cảnh Machine Learning}",
        1,
    )
    ch1_p1 = re.sub(r"\\subsubsection\{", r"\\subsection{", ch1_p1)
    ch1_p2 = re.sub(r"\\subsubsection\{", r"\\subsection{", ch1_p2)
    ch1_p2 = ch1_p2.replace("\\subsection{Mục lục}", "\\subsection{Dữ liệu training không mang tính đại diện}")
    ch1_p2 = ch1_p2.replace(
        "\\subsection{Những thách thức chính của Machine Learning}",
        "\\section{Những thách thức chính của Machine Learning}",
        1,
    )
    ch1_p2 = ch1_p2.replace(
        "Kiểm tra và xác nhận\n\nCách duy nhất",
        "\\section{Kiểm tra và xác nhận}\n\nCách duy nhất",
        1,
    )
    ch1_p2 = re.sub(r"\\paragraph\{", r"\\subsection{", ch1_p2)
    ch1_p2 = re.sub(r"\\subparagraph\{", r"\\subsubsection{", ch1_p2)
    return ch1_p1 + "\n\n" + ch1_p2


def inject_figures(text: str) -> str:
    used = set()
    for anchor, fname, cap in FIGURE_ANCHORS:
        if anchor not in text or fname in used:
            continue
        idx = text.index(anchor)
        # insert after the paragraph containing anchor
        end = text.find("\n\n", idx)
        if end == -1:
            end = len(text)
        else:
            end += 2
        text = text[:end] + fig_tex(fname, cap) + text[end:]
        used.add(fname)
    return text


def fix_table(text: str) -> str:
    pat = (
        r"Quốc gia GDP bình quân đầu người \(USD\) Sự hài lòng về cuộc sống\n\n"
        r"Hungary 12\.240 4,9\n\nHàn Quốc 27\.195 5,8\n\nPháp 37\.675 6,5\n\n"
        r"Úc 50\.962 7,3\n\nHoa Kỳ 55\.805 7,2\n"
    )
    return re.sub(pat, lambda m: TABLE + "\n", text, count=1)


def fix_equation(text: str) -> str:
    text = text.replace(
        "Phương trình 1-1. Model tuyến tính đơn giản",
        "\\begin{congthuc}[title={Phương trình 1-1}]\nModel life\\_satisfaction tuyến tính đơn giản:",
    )
    marker = "\\begin{congthuc}[title={Phương trình 1-1}]"
    if marker in text:
        start = text.index(marker)
        # Close congthuc right after the equation line (before following prose)
        rest = text[start + len(marker) :]
        m = re.search(r"life\\_satisfaction = .*GDP\\_per\\_capita\n", rest)
        if m:
            eq_end = start + len(marker) + m.end()
            eq_block = (
                marker + "\n"
                "\\begin{equation}\\label{eq:life-gdp}\n"
                "  \\mathrm{life\\_satisfaction} = \\theta_0 + \\theta_1 \\times \\mathrm{GDP\\_per\\_capita}\n"
                "\\end{equation}\n\\end{congthuc}\n\n"
            )
            text = text[:start] + eq_block + text[eq_end:]
    text = text.replace("theta\\_0", r"$\theta_0$")
    text = text.replace("theta\\_1", r"$\theta_1$")
    text = text.replace("theta (theta)", r"$\theta$")
    text = text.replace("$\\theta$1", r"$\theta_1$")
    return text


def inject_code(text, code_cells):
    block = (
        "\\begin{vidu}[title={Ví dụ code 1-1 --- GDP vs life satisfaction}]\n"
        "Notebook gốc: \\url{https://github.com/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb}\n\n"
        "\\begin{lstlisting}[language=Python]\n"
        + "\n\n".join(code_cells)
        + "\n\\end{lstlisting}\n\n"
        "Thay Linear Regression bằng k-NN (chỉ đổi model):\n"
        "\\begin{lstlisting}[language=Python]\n"
        "import sklearn.neighbors\n"
        "model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)\n"
        "model.fit(X, y)\n"
        "print(model.predict(X_new))  # ~5.77\n"
        "\\end{lstlisting}\n\\end{vidu}\n\n"
    )
    anchor = "Ví dụ 1-1 hiển thị code Python"
    if anchor in text:
        return text.replace(anchor, block + anchor, 1)
    anchor2 = "Ví dụ 1-1\n"
    if anchor2 in text:
        return text.replace(anchor2, block, 1)
    return text


def choose_box_env(title: str, level: str) -> str:
    """Pick tcolorbox environment from heading title."""
    t = title.lower()
    if level == "section":
        if "thách thức" in t:
            return "luuy"
        if "kiểm tra" in t or "xác nhận" in t:
            return "phuongphap"
        if "bài tập" in t:
            return "vidu"
        return "dongco"
    # subsection / subsubsection
    if "machine learning là gì" in t or "định lý" in t:
        return "dinhly" if "định lý" in t else "dinhnghia"
    if "tại sao" in t:
        return "dongco"
    if "ứng dụng" in t:
        return "ungdung"
    if "ví dụ" in t or "bài tập" in t:
        return "vidu"
    if any(
        k in t
        for k in (
            "thách thức",
            "không đủ",
            "không mang tính",
            "kém chất",
            "không liên quan",
            "quá mức",
            "thiếu dữ liệu",
            "bước lùi",
            "không khớp",
            "hiệu quả phi lý",
            "lấy mẫu",
        )
    ):
        return "luuy"
    if any(k in t for k in ("siêu tham số", "điều chỉnh", "xác thực", "cross-validation")):
        return "phuongphap"
    if any(k in t for k in ("supervised", "unsupervised", "reinforcement", "batch", "online", "instance", "model-based", "loại hệ thống")):
        return "ynghia"
    return "ynghia"


def wrap_block(env: str, title: str, content: str) -> str:
    if not content.strip():
        return ""
    safe = title.replace("{", "\\{").replace("}", "\\}")
    return f"\\begin{{{env}}}[title={{{safe}}}]\n{content.strip()}\n\\end{{{env}}}\n"


SKIP_WRAP_PREFIXES = (
    "\\begin{vidu}",
    "\\begin{congthuc}",
    "\\begin{tongket}",
    "\\begin{dongco}",
    "\\begin{ynghia}",
    "\\begin{dinhnghia}",
    "\\begin{luuy}",
    "\\begin{phuongphap}",
    "\\begin{ungdung}",
)


def should_skip_wrap(chunk: str) -> bool:
    s = chunk.strip()
    return any(s.startswith(p) for p in SKIP_WRAP_PREFIXES)


def split_paragraphs_safe(text: str):
    """Split on blank lines without breaking \\begin/\\end environments."""
    parts = re.split(r"\n\n+", text.strip())
    merged = []
    buf = []
    depth = 0
    for p in parts:
        if not p.strip():
            continue
        opens = len(re.findall(r"\\begin\{", p))
        closes = len(re.findall(r"\\end\{", p))
        buf.append(p)
        depth += opens - closes
        if depth <= 0:
            merged.append("\n\n".join(buf))
            buf = []
            depth = 0
    if buf:
        merged.append("\n\n".join(buf))
    return merged


def parse_heading_block(part: str):
    m = re.match(r"\\(sub)?paragraph\{([^}]+)\}\s*\n?", part)
    if m:
        return m.group(2), part[m.end() :].strip()
    return None, part.strip()


def wrap_subsection_content(parent_title: str, level: str, content: str):
    """Split subsection into many small color boxes."""
    result = []
    if not content.strip():
        return result

    blocks = re.split(r"(?=\\(?:sub)?paragraph\{)", content)
    for block in blocks:
        if not block.strip():
            continue
        head_title, body = parse_heading_block(block)
        if not body:
            continue
        title_base = head_title or parent_title
        box_level = "subparagraph" if head_title else level
        env = choose_box_env(title_base, box_level)
        chunks = split_paragraphs_safe(body)
        for j, chunk in enumerate(chunks):
            if should_skip_wrap(chunk):
                result.append(chunk)
                continue
            if len(chunks) == 1:
                title = title_base
            elif head_title:
                title = title_base if j == 0 else f"{title_base} ({j + 1})"
            else:
                title = f"{parent_title} ({j + 1})"
            result.append(wrap_block(env, title, chunk))
    return result


def wrap_all_in_boxes(text: str) -> str:
    """Wrap content in many small tcolorboxes (per paragraph / subheading)."""
    sections = re.split(r"(?=\\section\*?\{)", text)
    out = []
    for sec in sections:
        if not sec.strip():
            continue
        m = re.match(r"(\\section\*?\{([^}]+)\})\s*\n?", sec)
        if not m:
            for chunk in split_paragraphs_safe(sec):
                if should_skip_wrap(chunk):
                    out.append(chunk)
                else:
                    out.append(wrap_block("ynghia", "Nội dung", chunk))
            continue
        heading, title = m.group(1), m.group(2)
        rest = sec[m.end() :]
        out.append(heading + "\n\n")
        sub_parts = re.split(r"(?=\\subsection\{)", rest)
        intro = sub_parts[0].strip()
        if intro:
            out.extend(wrap_subsection_content(title, "section", intro))
        for sub in sub_parts[1:]:
            sm = re.match(r"(\\subsection\{([^}]+)\})\s*\n?", sub)
            if not sm:
                out.append(sub)
                continue
            sub_heading, sub_title = sm.group(1), sm.group(2)
            sub_rest = sub[sm.end() :].strip()
            out.append(sub_heading + "\n\n")
            if sub_rest:
                out.extend(wrap_subsection_content(sub_title, "subsection", sub_rest))
    return "\n\n".join(out)


def add_template_boxes(text: str) -> str:
    # Remove PDF artifact line only; color boxes applied by wrap_all_in_boxes()
    text = re.sub(
        r"Indexer: Judith McConville.*Illustrator: Rebecca Demarest\n\n",
        "",
        text,
    )
    return text


def header() -> str:
    return r"""\documentclass[12pt,a4paper]{article}

\def\courseshortheader{HANDS-ON ML}
\def\coverbookline{Hands-On Machine Learning}
\def\covermaintitle{Phong cảnh Machine Learning}
\def\coversubtitle{Giáo án lý thuyết --- Chương 1 (Aurélien Géron, 2nd ed.)}

\input{../../../../../toan_dai_hoc/nhom_5_xac_suat_thong_ke/_template/preamble.tex}

\usepackage{listings}
\usepackage{float}
\usepackage{caption}

\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true,
  frame=single,
  backgroundcolor=\color{gray!8},
  columns=fullflexible,
  keepspaces=true,
}

\graphicspath{{figures/}}
\newcommand{\homlimg}[2][0.82]{\begin{center}\includegraphics[width=#1\linewidth]{#2}\end{center}}

\begin{document}

\input{../../../../../toan_dai_hoc/nhom_5_xac_suat_thong_ke/_template/trang_bia.tex}
\newpage
\tableofcontents
\newpage

\section*{Lời nói đầu}
\addcontentsline{toc}{section}{Lời nói đầu}

\begin{ynghia}[title={Lời nói đầu}]
Tài liệu theo template \texttt{toan\_dai\_hoc/nhom\_5\_xac\_suat\_thong\_ke}, tổng hợp \textbf{đầy đủ Chương 1} từ bản dịch PDF, kèm \textbf{hình minh họa} và \textbf{code Ví dụ 1-1} từ \href{https://github.com/ageron/handson-ml2}{handson-ml2}.
\end{ynghia}

\newpage

"""


def main():
    body = load_body()
    body = fix_table(body)
    body = fix_equation(body)
    body = inject_figures(body)
    body = inject_code(body, load_notebook_code())
    body = add_template_boxes(body)
    body = wrap_all_in_boxes(body)
    out = OUT_DIR / "ly_thuyet.tex"
    out.write_text(header() + body + "\n\\end{document}\n", encoding="utf-8")
    print(f"Wrote {out} ({len(body.splitlines())} body lines)")


if __name__ == "__main__":
    main()
