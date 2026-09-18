#!/usr/bin/env python3
"""Render publishing markdown to HTML and PDF (fpdf2 + DejaVu)."""

from __future__ import annotations

import html
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from fpdf import FPDF
from fpdf.fonts import FontFace
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
FONT_B = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
FONT_I = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf")
FONT_BI = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf")
PUBLISHING = ROOT / "preliminary/publishing"
EDITION = "Reader Edition 0.1 — Private circulation"
EDITION_DATE = "2026-09-18"
FEEDBACK_DEADLINE = "2026-10-16"
SOURCE_COMMIT = "9f3b151b9c6fdfc1204f4070d09386e76e1b4168"
READER_PDF = PUBLISHING / "parenthood-atlas-reader-edition-01.pdf"
READER_HTML = PUBLISHING / "parenthood-atlas-reader-edition-01.html"
READER_REPORT = PUBLISHING / "reader-edition-01--extraction-report.txt"
READER_NOTE = PUBLISHING / "reader-edition-01--reader-note.md"
EVIDENCE_NOTE = PUBLISHING / "reader-edition-01--evidence-and-uncertainty.md"
FEEDBACK_GUIDE = PUBLISHING / "reader-edition-01--feedback-guide.md"
CHAPTER_FILES = (
    "01-before-the-child-is-born.md",
    "02-first-environment.md",
    "03-the-great-transition.md",
    "04-regulatory-relationship.md",
    "05-becoming-a-mind.md",
    "06-the-mind-in-motion.md",
    "07-the-birth-of-language.md",
    "08-the-expanding-world.md",
    "09-the-emotional-revolution.md",
    "10-boundaries-behavior.md",
    "11-the-developing-executive.md",
    "12-play-imagination.md",
    "13-the-ecology-of-development.md",
    "14-what-actually-works.md",
    "15-three-years.md",
)


def md_inline_html(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def md_to_html(md: str, title: str) -> str:
    lines = md.splitlines()
    out: list[str] = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
        f"<title>{html.escape(title)}</title>",
        "<style>body{font-family:Georgia,serif;max-width:720px;margin:1.2cm auto;font-size:11pt;line-height:1.35}",
        "h1{font-size:18pt} table{border-collapse:collapse} td,th{border:1px solid #ccc;padding:4px 6px}</style></head><body>",
    ]
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            out.append(f"<h1>{md_inline_html(line[2:])}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{md_inline_html(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{md_inline_html(line[4:])}</h3>")
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-:| ]+\|$", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-:| ]+\|$", lines[i]):
                    cells = [md_inline_html(c.strip()) for c in lines[i].strip("|").split("|")]
                    rows.append(cells)
                i += 1
            out.append("<table>")
            for n, cells in enumerate(rows):
                tag = "th" if n == 0 else "td"
                out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
            out.append("</table>")
            continue
        elif line.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].startswith("- "):
                out.append(f"<li>{md_inline_html(lines[i][2:])}</li>")
                i += 1
            out.append("</ul>")
            continue
        elif re.match(r"^\d+\. ", line):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                item = re.sub(r"^\d+\. ", "", lines[i])
                out.append(f"<li>{md_inline_html(item)}</li>")
                i += 1
            out.append("</ol>")
            continue
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.strip():
            out.append(f"<p>{md_inline_html(line)}</p>")
        i += 1
    out.append("</body></html>")
    return "\n".join(out)


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return text


def is_table_separator(line: str) -> bool:
    return bool(re.fullmatch(r"\|[-:| ]+\|", line))


def table_cells(line: str) -> list[str]:
    return [strip_md(cell.strip()) for cell in line.strip("|").split("|")]


class BriefPDF(FPDF):
    def __init__(self) -> None:
        super().__init__(format="letter")
        self.set_creation_date(datetime(2000, 1, 1, tzinfo=timezone.utc))
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("DejaVu", "", str(FONT))
        self.add_font("DejaVu", "B", str(FONT_B))

    def heading(self, text: str, size: int) -> None:
        self.set_font("DejaVu", "B", size)
        self.multi_cell(0, size * 0.45, strip_md(text))
        self.ln(2)

    def body(self, text: str, size: int = 10.5) -> None:
        self.set_font("DejaVu", "", size)
        self.multi_cell(0, 5.1, strip_md(text))
        self.ln(1.2)

    def table_row(self, cells: list[str], *, header: bool = False) -> None:
        self.set_font("DejaVu", "B" if header else "", 9.5)
        self.multi_cell(0, 4.7, " · ".join(cells))
        self.ln(0.8)


def md_to_pdf(md: str, pdf_path: Path) -> None:
    pdf = BriefPDF()
    pdf.add_page()
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            pdf.heading(line[2:], 16)
        elif line.startswith("## "):
            pdf.ln(2)
            pdf.heading(line[3:], 12)
        elif line.startswith("### "):
            pdf.heading(line[4:], 11)
        elif line.startswith("|"):
            if i + 1 >= len(lines) or not is_table_separator(lines[i + 1]):
                raise ValueError(f"Unsupported Markdown table at line {i + 1}: missing separator")
            rows = [table_cells(line)]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                if not is_table_separator(lines[i]):
                    rows.append(table_cells(lines[i]))
                i += 1
            pdf.table_row(rows[0], header=True)
            for row in rows[1:]:
                pdf.table_row(row)
            pdf.ln(1)
            continue
        elif line.startswith("- "):
            pdf.body("• " + line[2:], 10.5)
        elif line.strip() == "---":
            pdf.ln(2)
        elif line.strip():
            pdf.body(line, 10.5)
        i += 1
    pdf.output(str(pdf_path))


def write_pair(md_path: Path, title: str, pdf_path: Path | None = None) -> None:
    md = md_path.read_text(encoding="utf-8")
    html_path = (pdf_path or md_path).with_suffix(".html")
    html_path.write_text(md_to_html(md, title), encoding="utf-8")
    target = pdf_path or md_path.with_suffix(".pdf")
    md_to_pdf(md, target)
    print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size} bytes)")


def chapter_paths() -> list[Path]:
    expected = [ROOT / "chapters" / name for name in CHAPTER_FILES]
    missing = [path.relative_to(ROOT) for path in expected if not path.is_file()]
    actual = set((ROOT / "chapters").glob("[0-9][0-9]-*.md"))
    unexpected = sorted(path.relative_to(ROOT) for path in actual - set(expected))
    if missing or unexpected:
        parts = []
        if missing:
            parts.append("missing: " + ", ".join(map(str, missing)))
        if unexpected:
            parts.append("unexpected: " + ", ".join(map(str, unexpected)))
        raise FileNotFoundError("Reader Edition chapter set mismatch — " + "; ".join(parts))
    return expected


def chapter_title(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    if not first.startswith("# Chapter "):
        raise ValueError(f"{path.relative_to(ROOT)} has no Chapter heading on line 1")
    return strip_md(first[2:])


def reader_plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("**", "").replace("__", "").replace("*", "").replace("`", "")


def reader_inline_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "")
    return re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"__\1__", text)


def html_fragment(md: str) -> str:
    document = md_to_html(md, "fragment")
    return document.split("<body>", 1)[1].rsplit("</body>", 1)[0].strip()


class ReaderPDF(FPDF):
    def __init__(self) -> None:
        super().__init__(format="letter")
        self.set_creation_date(datetime(2000, 1, 1, tzinfo=timezone.utc))
        self.set_auto_page_break(auto=True, margin=18)
        self.set_title("Parenthood: The Atlas — Reader Edition 0.1")
        self.set_subject("Private working manuscript for reader feedback")
        self.set_author("Parenthood: The Atlas")
        self.add_font("DejaVu", "", str(FONT))
        self.add_font("DejaVu", "B", str(FONT_B))
        self.add_font("DejaVu", "I", str(FONT_I))
        self.add_font("DejaVu", "BI", str(FONT_BI))

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("DejaVu", "", 7)
        self.set_text_color(90)
        self.cell(
            0,
            4,
            f"{EDITION}  ·  {self.page_no()} / {{nb}}",
            align="C",
        )
        self.set_text_color(0)

    def centered_title(self, text: str, size: int, y: float) -> None:
        self.set_y(y)
        self.set_font("DejaVu", "B", size)
        self.multi_cell(0, size * 0.48, reader_plain(text), align="C")

    def heading(self, text: str, size: int) -> None:
        if self.will_page_break(24):
            self.add_page()
        self.set_font("DejaVu", "B", size)
        self.multi_cell(0, size * 0.46, reader_plain(text), align="L")
        self.ln(1.5)

    def body(self, text: str, size: float = 10.2, *, align: str = "J") -> None:
        self.set_font("DejaVu", "", size)
        self.multi_cell(
            0,
            4.9,
            reader_inline_md(text),
            align=align,
            markdown=True,
        )
        self.ln(1.1)

    def rule(self) -> None:
        self.ln(1)
        self.set_draw_color(150)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def markdown_table(self, rows: list[list[str]]) -> None:
        if not rows or len(rows) == 1:
            raise ValueError("Markdown table must contain a heading and at least one data row")
        columns = len(rows[0])
        if any(len(row) != columns for row in rows):
            raise ValueError("Markdown table rows have inconsistent column counts")
        widths: tuple[float, ...] | None
        if columns == 2:
            widths = (1, 3)
        elif columns == 3:
            widths = (1.2, 1.5, 2.3)
        else:
            widths = None
        self.set_font("DejaVu", "", 8.2)
        with self.table(
            [[reader_inline_md(cell) for cell in row] for row in rows],
            col_widths=widths,
            headings_style=FontFace(
                family="DejaVu",
                emphasis="B",
                size_pt=8.2,
                fill_color=235,
            ),
            line_height=4.1,
            markdown=True,
            padding=1.2,
            text_align="LEFT",
            v_align="TOP",
        ):
            pass
        self.ln(2)


def render_reader_markdown(pdf: ReaderPDF, md: str) -> None:
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            pdf.heading(line[2:], 17)
        elif line.startswith("## "):
            pdf.heading(line[3:], 12.5)
        elif line.startswith("### "):
            pdf.heading(line[4:], 11)
        elif line.startswith("|"):
            if i + 1 >= len(lines) or not is_table_separator(lines[i + 1]):
                raise ValueError(f"Unsupported Markdown table at line {i + 1}: missing separator")
            rows = [table_cells(line)]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                if not is_table_separator(lines[i]):
                    rows.append(table_cells(lines[i]))
                i += 1
            pdf.markdown_table(rows)
            continue
        elif line.startswith("- "):
            pdf.body("• " + line[2:], 9.8, align="L")
        elif re.match(r"^\d+\. ", line):
            pdf.body(line, 9.8, align="L")
        elif line.strip() == "---":
            pdf.rule()
        elif line.strip():
            pdf.body(line)
        i += 1


def colophon_markdown(total_pages: int) -> str:
    return f"""# Colophon

**Edition:** {EDITION}

**Frozen:** {EDITION_DATE}

**Canonical source commit:** `{SOURCE_COMMIT}`

**Included manuscript:** fifteen curated chapters in the explicit order recorded by `reader-edition-01--manifest.md`

**Feedback deadline:** {FEEDBACK_DEADLINE}

**Extent:** {total_pages} US Letter pages

Generated reproducibly with `fpdf2 2.8.8`; verified by extraction with `pypdf 6.19.0`.

This is a working manuscript for private feedback. It is not a knowledge-base release, public preprint, clinical guide, or finished publishing master. Reader response may motivate an editorial issue; factual changes still require the evidence-card workflow.
"""


def build_reader_pdf(
    chapters: list[Path],
    toc_pages: dict[int, int] | None = None,
    *,
    total_pages: int = 0,
) -> tuple[ReaderPDF, dict[int, int]]:
    pdf = ReaderPDF()

    pdf.add_page()
    pdf.centered_title("Parenthood: The Atlas", 24, 105)

    pdf.add_page()
    pdf.centered_title("Parenthood: The Atlas", 25, 74)
    pdf.centered_title("Reader Edition 0.1", 16, 100)
    pdf.set_y(124)
    pdf.set_font("DejaVu", "", 11)
    pdf.multi_cell(
        0,
        6,
        "Private circulation\nWorking manuscript for reader feedback\n"
        f"{EDITION_DATE}",
        align="C",
    )
    pdf.set_y(215)
    pdf.set_font("DejaVu", "I", 9)
    pdf.multi_cell(
        0,
        5,
        "Not medical, clinical, legal, or individualized parenting guidance.",
        align="C",
    )

    pdf.add_page()
    render_reader_markdown(pdf, READER_NOTE.read_text(encoding="utf-8"))

    pdf.add_page()
    pdf.heading("Contents", 17)
    for number, path in enumerate(chapters, 1):
        title = chapter_title(path)
        page = toc_pages[number] if toc_pages else 999
        label = f"{title} "
        dots = "." * max(3, 82 - len(label))
        pdf.body(f"{label}{dots} {page}", 9.3, align="L")

    chapter_pages: dict[int, int] = {}
    for number, path in enumerate(chapters, 1):
        pdf.add_page()
        chapter_pages[number] = pdf.page_no()
        pdf.start_section(chapter_title(path), level=0)
        render_reader_markdown(pdf, path.read_text(encoding="utf-8"))

    pdf.add_page()
    render_reader_markdown(pdf, EVIDENCE_NOTE.read_text(encoding="utf-8"))

    pdf.add_page()
    render_reader_markdown(pdf, FEEDBACK_GUIDE.read_text(encoding="utf-8"))

    pdf.add_page()
    render_reader_markdown(pdf, colophon_markdown(total_pages or pdf.page_no()))
    return pdf, chapter_pages


def build_reader_html(chapters: list[Path], chapter_pages: dict[int, int], total_pages: int) -> str:
    toc = "\n".join(
        f"<li><a href='#chapter-{number:02d}'>{md_inline_html(chapter_title(path))}</a>"
        f"<span>PDF page {chapter_pages[number]}</span></li>"
        for number, path in enumerate(chapters, 1)
    )
    chapter_html = "\n".join(
        f"<section class='chapter' id='chapter-{number:02d}'>"
        f"{html_fragment(path.read_text(encoding='utf-8'))}</section>"
        for number, path in enumerate(chapters, 1)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Parenthood: The Atlas — Reader Edition 0.1</title>
<style>
@page {{ size: Letter; margin: 20mm 19mm 22mm; }}
body {{ color:#181818; font-family:Georgia,serif; font-size:11pt; line-height:1.42; margin:0 auto; max-width:760px; }}
h1 {{ font-size:21pt; line-height:1.15; margin-top:0; }} h2 {{ font-size:14pt; margin-top:1.6em; }}
h3 {{ font-size:12pt; }} p, li {{ orphans:3; widows:3; }}
table {{ border-collapse:collapse; font-size:9pt; width:100%; }} th,td {{ border:1px solid #aaa; padding:5px; vertical-align:top; }}
th {{ background:#eee; }} code {{ font-size:9pt; }}
.page {{ break-after:page; min-height:220mm; display:flex; flex-direction:column; justify-content:center; text-align:center; }}
.matter, .chapter {{ break-before:page; }} .chapter h1 {{ break-after:avoid; }}
.toc {{ break-before:page; break-after:page; }} .toc ol {{ list-style:none; padding:0; }}
.toc li {{ display:flex; justify-content:space-between; gap:2em; padding:.18em 0; }}
.edition-footer {{ border-top:1px solid #bbb; color:#666; font-size:8pt; margin-top:4em; padding-top:.6em; text-align:center; }}
@media print {{ a {{ color:inherit; text-decoration:none; }} }}
</style>
</head>
<body>
<section class="page"><h1>Parenthood: The Atlas</h1></section>
<section class="page"><h1>Parenthood: The Atlas</h1><h2>Reader Edition 0.1</h2>
<p>Private circulation<br>Working manuscript for reader feedback<br>{EDITION_DATE}</p>
<p><em>Not medical, clinical, legal, or individualized parenting guidance.</em></p></section>
<section class="matter">{html_fragment(READER_NOTE.read_text(encoding="utf-8"))}</section>
<nav class="toc"><h1>Contents</h1><ol>{toc}</ol></nav>
{chapter_html}
<section class="matter">{html_fragment(EVIDENCE_NOTE.read_text(encoding="utf-8"))}</section>
<section class="matter">{html_fragment(FEEDBACK_GUIDE.read_text(encoding="utf-8"))}</section>
<section class="matter">{html_fragment(colophon_markdown(total_pages))}</section>
<div class="edition-footer">{EDITION}</div>
</body>
</html>
"""


def expected_fragments(md: str) -> list[str]:
    fragments: list[str] = []
    for line in md.splitlines():
        if not line.strip() or line.strip() == "---" or is_table_separator(line):
            continue
        if line.startswith("|"):
            fragments.extend(reader_plain(cell.strip()) for cell in line.strip("|").split("|"))
            continue
        text = re.sub(r"^(?:#{1,3} |- |\d+\. )", "", line)
        fragments.append(reader_plain(text))
    return [re.sub(r"\s+", " ", fragment).strip() for fragment in fragments if fragment.strip()]


def verify_reader_pdf(
    chapters: list[Path],
    chapter_pages: dict[int, int],
) -> str:
    reader = PdfReader(READER_PDF)
    total_pages = len(reader.pages)
    page_texts = [page.extract_text() or "" for page in reader.pages]
    normalized_pages = [re.sub(r"\s+", " ", text).strip() for text in page_texts]
    blank_pages = [number for number, text in enumerate(normalized_pages, 1) if len(text) < 8]
    footer_failures = [
        number
        for number, text in enumerate(normalized_pages, 1)
        if EDITION not in text or f"{number} / {total_pages}" not in text
    ]
    chapter_failures = [
        number
        for number, path in enumerate(chapters, 1)
        if chapter_title(path) not in normalized_pages[chapter_pages[number] - 1]
    ]

    footer_pattern = re.compile(
        rf"{re.escape(EDITION)}\s+·\s+\d+\s+/\s+{total_pages}"
    )
    content_text = " ".join(
        footer_pattern.sub("", text) for text in normalized_pages
    )
    sources = [
        READER_NOTE,
        *chapters,
        EVIDENCE_NOTE,
        FEEDBACK_GUIDE,
    ]
    fragments = [
        fragment
        for source in sources
        for fragment in expected_fragments(source.read_text(encoding="utf-8"))
    ]
    missing_fragments = [fragment for fragment in fragments if fragment not in content_text]
    html_text = READER_HTML.read_text(encoding="utf-8")
    html_failures = [
        number
        for number, path in enumerate(chapters, 1)
        if f"id='chapter-{number:02d}'" not in html_text or chapter_title(path) not in html_text
    ]
    if (
        READER_PDF.stat().st_size == 0
        or blank_pages
        or footer_failures
        or chapter_failures
        or missing_fragments
        or html_failures
    ):
        raise RuntimeError(
            "Reader Edition verification failed: "
            f"blank={blank_pages}, footer={footer_failures}, chapters={chapter_failures}, "
            f"missing_content={len(missing_fragments)}, html={html_failures}"
        )

    digest = hashlib.sha256(READER_PDF.read_bytes()).hexdigest()
    chapter_lines = "\n".join(
        f"- PASS · PDF page {chapter_pages[number]} · {chapter_title(path)}"
        for number, path in enumerate(chapters, 1)
    )
    return f"""Reader Edition 0.1 extraction verification
Status: PASS
Edition: {EDITION}
Source commit: {SOURCE_COMMIT}
PDF: {READER_PDF.name}
SHA-256: {digest}
Bytes: {READER_PDF.stat().st_size}
Pages: {total_pages}
Nonblank pages: {total_pages}/{total_pages}
Edition footer and page number: {total_pages}/{total_pages}
Source content fragments: {len(fragments)}/{len(fragments)}
HTML chapter anchors and titles: 15/15
TOC/chapter-start pagination stable across both render passes: PASS

Chapter-title extraction
{chapter_lines}

Mechanical scope
- Confirms nonempty output, page text, footer numbering, ordered chapter starts, source fragments, and HTML anchors.
- Physical trim, binding, widows/orphans, and perceived readability require the two-copy proof-print checklist.
"""


def write_reader_edition() -> None:
    chapters = chapter_paths()
    first_pdf, first_pages = build_reader_pdf(chapters)
    first_total = first_pdf.page_no()
    final_pdf, final_pages = build_reader_pdf(
        chapters,
        first_pages,
        total_pages=first_total,
    )
    if first_pages != final_pages or first_total != final_pdf.page_no():
        raise RuntimeError("TOC pagination changed between render passes")
    final_pdf.output(READER_PDF)
    READER_HTML.write_text(
        build_reader_html(chapters, final_pages, final_pdf.page_no()),
        encoding="utf-8",
    )
    READER_REPORT.write_text(
        verify_reader_pdf(chapters, final_pages),
        encoding="utf-8",
    )
    print(
        f"wrote {READER_PDF.relative_to(ROOT)} "
        f"({READER_PDF.stat().st_size} bytes, {final_pdf.page_no()} pages)"
    )
    print(f"wrote {READER_HTML.relative_to(ROOT)}")
    print(f"wrote {READER_REPORT.relative_to(ROOT)}")


def main() -> int:
    write_pair(
        ROOT / "preliminary/publishing/evidence-brief-01--narrow-lab-stables.md",
        "Evidence Brief #1",
    )
    cover = (ROOT / "preliminary/publishing/ch01-preprint.md").read_text(encoding="utf-8")
    chapter = (ROOT / "chapters/01-before-the-child-is-born.md").read_text(encoding="utf-8")
    combined = ROOT / "preliminary/publishing/ch01-preprint-combined.md"
    combined.write_text(cover.rstrip() + "\n\n---\n\n" + chapter, encoding="utf-8")
    write_pair(
        combined,
        "Before the Child Is Born — Chapter 1 preprint",
        ROOT / "preliminary/publishing/ch01-preprint.pdf",
    )
    combined.unlink()
    write_reader_edition()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
