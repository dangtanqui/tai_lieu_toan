#!/usr/bin/env python3
"""Apply A3-style template to all ly_thuyet.tex in nhom_5."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COURSES = [
    {
        "dir": "X1_xac_suat",
        "header": "XÁC SUẤT 1",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Xác suất",
        "subtitle": "Giáo án lý thuyết --- Biến cố, BNN, phân phối, CLT",
        "modau_title": "Tại sao học xác suất?",
        "modau": r"""Xác suất trả lời câu hỏi: \emph{trong điều kiện không chắc chắn, ta đo mức độ tin cậy thế nào?} Từ tung đồng lật, kiểm tra y tế, đến mô hình học máy (phân loại, hồi quy xác suất), cùng một ngôn ngữ toán: không gian mẫu, biến cố, $P(\cdot)$, kỳ vọng.

\begin{itemize}
  \item \textbf{Thống kê} (X2, X3) dùng xác suất để suy luận từ \emph{mẫu} về \emph{tổng thể}.
  \item \textbf{Độ đo} (X4) làm nền chứng minh cho luật số lớn, CLT.
  \item \textbf{Quá trình ngẫu nhiên} (X8) mô tả hiện tượng thay đổi theo thời gian.
\end{itemize}""",
        "dongco_hints": {
            "Biến cố và xác suất": "Ta cần cách đếm và đo ``độ chắc chắn'' của kết quả thí nghiệm một cách nhất quán, không mâu thuẫn.",
            "Biến ngẫu nhiên": "Nhiều đại lượng quan sát được (điểm thi, chiều cao, số lỗi) --- ta gom chúng thành một hàm ngẫu nhiên $X$ và mô tả bằng phân phối.",
            "Kỳ vọng, phương sai, moment": "Phân phối cho biết \emph{tất cả} khả năng; kỳ vọng và phương sai tóm tắt ``trung tâm'' và ``độ lan'' bằng hai số.",
            "Vectơ ngẫu nhiên": "Khi nhiều BNN cùng xuất hiện (chiều cao và cân nặng), ta cần mô tả \emph{đồng thời} và mối phụ thuộc.",
            "Các bất đẳng thức và định lý giới hạn": "Với mẫu lớn, trung bình mẫu ổn định quanh kỳ vọng --- đây là cơ sở của thống kê và xấp xỉ chuẩn.",
        },
    },
    {
        "dir": "X2_thong_ke_toan",
        "header": "THỐNG KÊ TOÁN",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Thống kê toán",
        "subtitle": "Giáo án lý thuyết --- Mẫu, ước lượng, khoảng tin cậy, kiểm định",
        "modau_title": "Tại sao học thống kê toán?",
        "modau": r"""Thống kê toán dùng dữ liệu mẫu để \emph{suy luận} về tham số tổng thể chưa biết: trung bình thật, tỷ lệ thật, có khác không so với giả thuyết $H_0$?

\begin{itemize}
  \item \textbf{Ước lượng điểm} cho ``giá trị tốt nhất'' (MLE, moment).
  \item \textbf{Khoảng tin cậy} cho ``độ không chắc chắn''.
  \item \textbf{Kiểm định} cho quyết định có bằng chứng đủ mạnh hay chưa.
\end{itemize}""",
        "dongco_hints": {
            "Mẫu và thống kê mô tả": "Trước khi suy luận, ta tóm tắt dữ liệu bằng các thống kê mẫu và hiểu phân phối của chúng.",
            "Ước lượng điểm": "Từ một mẫu, ta cần quy tắc chọn giá trị ``đoán'' cho $\theta$.",
            "Ước lượng khoảng": "Điểm ước lượng chưa đủ --- ta cần khoảng bao quanh $\theta$ với xác suất đã cho.",
            "Kiểm định giả thuyết": "Bài toán quyết định: có từ chối $H_0$ được không khi chỉ có mẫu?",
        },
    },
    {
        "dir": "X3_thong_ke_ung_dung",
        "header": "THỐNG KÊ ỨNG DỤNG",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Thống kê ứng dụng",
        "subtitle": "Giáo án lý thuyết --- Mô tả, tương quan, hồi quy, ANOVA",
        "modau_title": "Tại sao học thống kê ứng dụng?",
        "modau": r"""Đây là lớp ``làm thống kê với dữ liệu thật'': mô tả, vẽ biểu đồ, đo mối quan hệ, dự báo $Y$ từ $X$, so sánh nhiều nhóm (ANOVA). Nền toán nằm ở X1--X2; ở đây ta nhấn \emph{diễn giải} và \emph{mô hình}.""",
        "dongco_hints": {
            "Thống kê mô tả": "Trước khi mô hình hóa, phải hiểu dữ liệu: trung tâm, phân tán, hình dạng, ngoại lai.",
            "Tương quan và hồi quy": "Câu hỏi: $X$ và $Y$ có đi cùng nhau không? Nếu biết $X$, dự đoán $Y$ ra sao?",
            "Phân tích phương sai (ANOVA)": "So sánh trung bình của \emph{nhiều nhóm} --- ví dụ ba phương pháp giảng dạy.",
        },
    },
    {
        "dir": "X4_xac_suat_va_do_do",
        "header": "XÁC SUẤT VÀ ĐỘ ĐO",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Xác suất và độ đo",
        "subtitle": "Giáo án lý thuyết --- Không gian xác suất, hội tụ, kỳ vọng có điều kiện",
        "modau_title": "Tại sao học xác suất đo lường?",
        "modau": r"""X1 cho trực giác; X4 xây nền \emph{chặt}: $\sigma$-đại số, các kiểu hội tụ ($P$, a.s., phân phối), hàm đặc trưng, kỳ vọng có điều kiện --- cần cho chứng minh luật số lớn và môn quá trình ngẫu nhiên.""",
        "dongco_hints": {
            "Không gian xác suất": "Ta cần khung toán cho phép xử lý vô hạn biến cố và tính xác suất nhất quán.",
            "Các loại hội tụ": "Dãy BNN và dãy phân phối ``tiến tới đâu'' --- cần phân biệt hội tụ theo phân phối, theo xác suất, hầu chắc.",
            "Hàm đặc trưng": "Công cụ gọn để chứng minh và nhận dạng phân phối qua đạo hàm tại $0$.",
            "Kỳ vọng có điều kiện": "Mô tả ``giá trị trung bình của $X$ khi đã biết thông tin $\mathcal{G}$'' --- nền của martingale.",
            "Luật số lớn và CLT (góc nhìn độ đo)": "Chứng minh và điều kiện áp dụng các định lý giới hạn ở mức đo lường.",
        },
    },
    {
        "dir": "X5_xac_suat_thong_ke_nang_cao",
        "header": "XSTK NÂNG CAO",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Xác suất thống kê nâng cao",
        "subtitle": "Giáo án lý thuyết --- Ước lượng, kiểm định, thống kê tiệm cận",
        "modau_title": "Mở đầu",
        "modau": r"""Mở rộng X2: tính chất ước lượng (hiệu quả Cramér--Rao), kiểm định likelihood ratio, delta method và phân phối tiệm cận --- nền cho nghiên cứu và học sau đại học.""",
        "dongco_hints": {
            "Lý thuyết ước lượng nâng cao": "Khi nào ước lượng ``tốt nhất'' và sai số có cận trên không?",
            "Kiểm định nâng cao": "So sánh các quy tắc kiểm định: Neyman--Pearson, LRT, Wald.",
            "Thống kê tiệm cận": "Khi $n$ lớn, phân phối của ước lượng xấp xỉ chuẩn --- cơ sở khoảng tin và kiểm định xấp xỉ.",
        },
    },
    {
        "dir": "X6_thong_ke_da_bien",
        "header": "THỐNG KÊ ĐA BIẾN",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Thống kê đa biến",
        "subtitle": "Giáo án lý thuyết --- PCA, nhân tố, phân biệt, phân cụm",
        "modau_title": "Mở đầu",
        "modau": r"""Dữ liệu thường có nhiều biến cùng lúc. Thống kê đa biến tìm cấu trúc ẩn (thành phần chính, nhân tố), phân nhóm (cụm), hoặc phân loại (phân biệt).""",
        "dongco_hints": {
            "Phân phối chuẩn nhiều chiều": "Nền xác suất cho vectơ ngẫu nhiên và ma trận hiệp phương sai.",
            "Phân tích thành phần chính (PCA)": "Giảm chiều nhưng giữ tối đa phương sai --- trực quan hóa và tiền xử lý.",
            "Phân tích nhân tố (Factor Analysis)": "Mô hình hóa biến quan sát bằng ít nhân tố tiềm ẩn.",
            "Phân tích phân biệt và phân cụm": "Hai hướng: có nhãn (phân loại) vs không nhãn (gom cụm).",
        },
    },
    {
        "dir": "X7_thong_ke_bayes",
        "header": "THỐNG KÊ BAYES",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Thống kê Bayes",
        "subtitle": "Giáo án lý thuyết --- Hậu nghiệm, MCMC, so sánh mô hình",
        "modau_title": "Mở đầu",
        "modau": r"""Thống kê cổ điển coi $\theta$ cố định; thống kê Bayes coi $\theta$ ngẫu nhiên với phân phối tiên nghiệm, cập nhật bằng dữ liệu thành \emph{hậu nghiệm}.""",
        "dongco_hints": {
            "Nguyên lý Bayes": "Công thức $p(\theta|data) \propto p(data|\theta)p(\theta)$ là trục của toàn bộ môn.",
            "Họ phân phối liên hợp": "Chọn prior--likelihood sao cho hậu nghiệm thuộc cùng họ --- tính được đóng.",
            "Phương pháp MCMC": "Khi hậu nghiệm không tính được, lấy mẫu xấp xỉ bằng chuỗi Markov.",
            "So sánh mô hình Bayes": "Bayes factor, DIC, WAIC --- chọn mô hình có dự đoán tốt hơn.",
        },
    },
    {
        "dir": "X8_qua_trinh_ngau_nhien",
        "header": "QUÁ TRÌNH NGẪU NHIÊN",
        "bookline": "NHÓM 5 --- XÁC SUẤT VÀ THỐNG KÊ",
        "title": "Quá trình ngẫu nhiên",
        "subtitle": "Giáo án lý thuyết --- Markov, Poisson, martingale, Brown",
        "modau_title": "Mở đầu",
        "modau": r"""Quá trình ngẫu nhiên mô tả hệ thống \emph{thay đổi theo thời gian}: hàng đợi, giá tài sản, mạng sinh học. Khác BNN tĩnh: ta quan tâm quỹ đạo $\{X_t\}_{t \ge 0}$.""",
        "dongco_hints": {
            "Tổng quan": "Định nghĩa quá trình, phân phối hữu hạn chiều, tính Markov và độc lập gia tăng.",
            "Xích Markov": "Tương lai chỉ phụ thuộc hiện tại --- mô hình hóa nhiều hệ rời rạc.",
            "Quá trình Poisson": "Đếm sự kiện rare trong thời gian liên tục.",
            "Martingale": "``Trò chơi công bằng'': kỳ vọng tương lai bằng giá trị hiện tại.",
            "Chuyển động Brown (Wiener process)": "Giới hạn của bước ngẫu nhiên nhỏ --- nền của tài chính và phương trình vi phân ngẫu nhiên.",
        },
    },
]

SECTION_RE = re.compile(r"\\section\{([^}]+)\}")
SUBSECTION_RE = re.compile(r"\\subsection\{([^}]+)\}")


def clean_body(body: str) -> str:
    body = re.sub(r"\\begin\{dongco\}.*?\\end\{dongco\}\s*", "", body, flags=re.DOTALL)
    body = re.sub(r"\\begin\{tongket\}.*?\\end\{tongket\}\s*", "", body, flags=re.DOTALL)
    return body.strip()


def extract_body(text: str) -> str:
    m = re.search(r"\\section\{", text)
    if not m:
        raise ValueError("No \\section found")
    end = text.rfind("\\end{document}")
    return clean_body(text[m.start() : end])


def extract_main_body(text: str, modau_title: str) -> str:
    """Body after mở đầu section (for re-running template)."""
    if "\\input{../_template/preamble.tex}" not in text:
        return extract_body(text)
    anchor = f"\\section{{{modau_title}}}"
    pos = text.find(anchor)
    if pos < 0:
        return extract_body(text)
    rest = text[pos:]
    m = re.search(r"\\newpage\s*\n\s*(\\section\{)", rest)
    if m:
        body = rest[m.start(1) :]
    else:
        # fallback: first section after modau dongco
        m2 = re.search(r"\\end\{dongco\}\s*\n+\s*(\\section\{)", rest)
        body = rest[m2.start(1) :] if m2 else rest
    body = body[: body.rfind("\\end{document}")].strip()
    return clean_body(body)


def split_sections(body: str):
    """Return list of (level, title, content) where level is 'section' or 'subsection'."""
    parts = []
    pattern = re.compile(r"(\\section\{|\\subsection\{)")
    matches = list(pattern.finditer(body))
    if not matches:
        return [("section", "", body)]
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[start:end].strip()
        if chunk.startswith("\\section{"):
            title = SECTION_RE.match(chunk).group(1)
            content = chunk[chunk.index("}") + 1 :].strip()
            parts.append(("section", title, content))
        else:
            title = SUBSECTION_RE.match(chunk).group(1)
            content = chunk[chunk.index("}") + 1 :].strip()
            parts.append(("subsection", title, content))
    return parts


def dongco_block(title: str, hint: str) -> str:
    return (
        f"\\begin{{dongco}}[title={{Động cơ --- {title}}}]\n"
        f"{hint}\n"
        f"\\end{{dongco}}\n\n"
    )


def tongket_block(title: str) -> str:
    return (
        f"\\begin{{tongket}}[title={{Tổng kết: {title}}}]\n"
        f"\\begin{{enumerate}}\n"
        f"  \\item Nắm lại các \\textbf{{định nghĩa}} và \\textbf{{công thức}} cốt lõi trong mục ``{title}''.\n"
        f"  \\item Tự làm lại ít nhất một ví dụ (nếu có) hoặc áp dụng công thức vào một tình huống số.\n"
        f"  \\item Ghi chú điều kiện áp dụng (giả thiết độc lập, phân phối chuẩn, $n$ đủ lớn, v.v.).\n"
        f"\\end{{enumerate}}\n"
        f"\\end{{tongket}}\n\n"
    )


def wrap_body(body: str, hints: dict) -> str:
    parts = split_sections(body)
    out = []
    i = 0
    while i < len(parts):
        level, title, content = parts[i]
        if level != "section":
            i += 1
            continue
        hint = hints.get(
            title, f"Phần này trình bày các khái niệm và kết quả về ``{title}''."
        )
        out.append(f"\\section{{{title}}}\n\n")
        out.append(dongco_block(title, hint))
        if content:
            out.append(content)
            if not content.endswith("\n"):
                out.append("\n")
            out.append("\n")
        j = i + 1
        while j < len(parts) and parts[j][0] == "subsection":
            _, sub_title, sub_content = parts[j]
            out.append(f"\\subsection{{{sub_title}}}\n\n")
            if sub_content:
                out.append(sub_content)
                if not sub_content.endswith("\n"):
                    out.append("\n")
                out.append("\n")
            j += 1
        out.append(tongket_block(title))
        i = j
    return "".join(out)


def build_file(course: dict, body: str) -> str:
    hints = course.get("dongco_hints", {})
    wrapped = wrap_body(body, hints)
    return f"""\\documentclass[12pt,a4paper]{{article}}

% --- Metadata (per course) ---
\\def\\courseshortheader{{{course["header"]}}}
\\def\\coverbookline{{{course["bookline"]}}}
\\def\\covermaintitle{{{course["title"]}}}
\\def\\coversubtitle{{{course["subtitle"]}}}

\\input{{../_template/preamble.tex}}

\\begin{{document}}

\\input{{../_template/trang_bia.tex}}
\\newpage
\\tableofcontents
\\newpage

\\input{{../_template/loi_noi_dau.tex}}

\\section{{{course["modau_title"]}}}

\\begin{{dongco}}[title={{Động cơ --- {course["modau_title"]}}}]
{course["modau"]}
\\end{{dongco}}

\\newpage

{wrapped}

\\end{{document}}
"""


def main():
    for course in COURSES:
        path = ROOT / course["dir"] / "ly_thuyet.tex"
        old = path.read_text(encoding="utf-8")
        body = extract_main_body(old, course["modau_title"])
        new = build_file(course, body)
        path.write_text(new, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
