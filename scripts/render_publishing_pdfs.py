#!/usr/bin/env python3
"""Universal Multi-Series Reader Edition PDF & HTML Publisher (fpdf2 + pypdf).

Compiles any book/series directory (`series/architectures-of-memory/book-*` or
`series/parenthood-atlas`) into a typeset Reader Edition PDF, standalone HTML,
and SHA-256 extraction verification report.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
from datetime import date
from pathlib import Path

from fpdf import FPDF, __version__ as FPDF_VERSION
from pypdf import PdfReader, __version__ as PYPDF_VERSION

from merge_book_chapters import iter_chapter_files, repo_root, resolve_book_path, strip_yaml_frontmatter


def resolve_serif_fonts() -> dict[str, Path]:
    """Locate Unicode TrueType serif fonts across Linux and Windows."""
    candidates = [
        {
            "": Path("/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"),
            "B": Path("/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"),
            "I": Path("/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"),
            "BI": Path("/usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf"),
        },
        {
            "": Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
            "B": Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"),
            "I": Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
            "BI": Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"),
        },
        {
            "": Path("C:/Windows/Fonts/georgia.ttf"),
            "B": Path("C:/Windows/Fonts/georgiab.ttf"),
            "I": Path("C:/Windows/Fonts/georgiai.ttf"),
            "BI": Path("C:/Windows/Fonts/georgiaz.ttf"),
        },
        {
            "": Path("C:/Windows/Fonts/times.ttf"),
            "B": Path("C:/Windows/Fonts/timesbd.ttf"),
            "I": Path("C:/Windows/Fonts/timesi.ttf"),
            "BI": Path("C:/Windows/Fonts/timesbi.ttf"),
        },
    ]
    for group in candidates:
        if all(p.is_file() for p in group.values()):
            return group
    raise RuntimeError("No suitable TrueType Serif font family found in /usr/share/fonts or C:/Windows/Fonts.")


def chapter_title(path: Path) -> str:
    text = strip_yaml_frontmatter(path.read_text(encoding="utf-8"))
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def clean_pdf_line(text: str) -> str:
    # Strip markdown formatting markers and normalize exotic math/symbols for clean serif rendering
    text = text.replace("\ufeff", "").replace("\u2192", "->").replace("\u2208", " in ").replace("\u209c", "_t")
    text = text.replace("\u1fe5", "r").replace("\u1fd6", "i")
    text = re.sub(r"\[\^([^\]]+)\]", r"[\1]", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    return text


def md_inline_html(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\[\^([^\]]+)\]", r"<sup>[\1]</sup>", text)
    return text


class ReaderEditionPDF(FPDF):
    def __init__(self, book_title: str, edition_label: str, fonts: dict[str, Path]) -> None:
        super().__init__(format="A4")
        self.book_title = book_title
        self.edition_label = edition_label
        self.current_chapter_header = book_title
        for style, fpath in fonts.items():
            self.add_font("BookSerif", style, str(fpath))
        self.set_margins(22, 22, 22)
        self.set_auto_page_break(True, margin=22)

    def header(self) -> None:
        if self.page_no() <= 1:
            return
        self.set_y(12)
        self.set_font("BookSerif", "I", 8.5)
        self.set_text_color(110, 110, 110)
        self.cell(0, 5, self.current_chapter_header[:85], align="R")
        self.ln(8)
        self.set_text_color(20, 20, 20)

    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("BookSerif", "", 8.5)
        self.set_text_color(110, 110, 110)
        self.cell(0, 5, f"{self.edition_label}  ·  Page {self.page_no()}", align="C")
        self.set_text_color(20, 20, 20)


def build_reader_pdf(
    book_title: str,
    edition_label: str,
    chapters: list[Path],
    fonts: dict[str, Path],
    toc_pages: dict[int, int] | None = None,
) -> tuple[ReaderEditionPDF, dict[int, int]]:
    pdf = ReaderEditionPDF(book_title=book_title, edition_label=edition_label, fonts=fonts)

    # Title & Contents Page
    pdf.add_page()
    pdf.set_font("BookSerif", "B", 20)
    pdf.multi_cell(0, 10, book_title)
    pdf.ln(2)
    pdf.set_font("BookSerif", "I", 11)
    pdf.multi_cell(0, 6, f"{edition_label} ({date.today().isoformat()})")
    pdf.ln(6)
    pdf.set_font("BookSerif", "B", 13)
    pdf.cell(0, 8, "Contents", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("BookSerif", "", 10)
    for idx, ch_path in enumerate(chapters, 1):
        pg = toc_pages.get(idx, 0) if toc_pages else 0
        pg_str = f"p. {pg}" if pg else "..."
        title = chapter_title(ch_path)
        pdf.multi_cell(0, 5.5, f"{idx:02d}. {title}  ({pg_str})", new_x="LMARGIN", new_y="NEXT")

    recorded_pages: dict[int, int] = {}
    for idx, ch_path in enumerate(chapters, 1):
        title = chapter_title(ch_path)
        pdf.current_chapter_header = f"{book_title} — {title}"
        pdf.add_page()
        recorded_pages[idx] = pdf.page_no()

        raw = strip_yaml_frontmatter(ch_path.read_text(encoding="utf-8"))
        for line in raw.splitlines():
            s = line.strip()
            if not s:
                pdf.ln(2.5)
                continue
            if s.startswith("# "):
                pdf.set_font("BookSerif", "B", 15)
                pdf.multi_cell(0, 8, clean_pdf_line(s[2:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(3)
            elif s.startswith("## "):
                pdf.ln(2)
                pdf.set_font("BookSerif", "B", 12)
                pdf.multi_cell(0, 6.5, clean_pdf_line(s[3:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(1.5)
            elif s.startswith("### "):
                pdf.ln(1.5)
                pdf.set_font("BookSerif", "BI", 10.5)
                pdf.multi_cell(0, 6, clean_pdf_line(s[4:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(1)
            elif s.startswith(">"):
                pdf.set_font("BookSerif", "I", 9.5)
                pdf.set_x(pdf.l_margin + 6)
                pdf.multi_cell(0, 5.2, clean_pdf_line(s.lstrip("> ").strip()), new_x="LMARGIN", new_y="NEXT")
            elif s == "---":
                pdf.ln(2)
            else:
                pdf.set_font("BookSerif", "", 10)
                pdf.multi_cell(0, 5.4, clean_pdf_line(s), new_x="LMARGIN", new_y="NEXT")

    return pdf, recorded_pages


def build_reader_html(book_title: str, edition_label: str, chapters: list[Path], chapter_pages: dict[int, int]) -> str:
    out: list[str] = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
        f"<title>{html.escape(book_title)} — {html.escape(edition_label)}</title>",
        "<style>",
        "body{font-family:Georgia,serif;max-width:760px;margin:2rem auto;padding:0 1rem;font-size:11.5pt;line-height:1.55;color:#181818}",
        "h1{font-size:19pt;margin-top:2.5rem;border-bottom:1px solid #ddd;padding-bottom:0.3rem}",
        "h2{font-size:14pt;margin-top:1.8rem} h3{font-size:12pt;font-style:italic}",
        "blockquote{border-left:3px solid #bbb;margin:1rem 0;padding:0.2rem 1rem;color:#444;font-style:italic}",
        "nav.toc{background:#f8f8f6;border:1px solid #e2e2dd;padding:1rem 1.5rem;border-radius:4px}",
        "</style></head><body>",
        f"<header><h1>{html.escape(book_title)}</h1><p><em>{html.escape(edition_label)} ({date.today().isoformat()})</em></p></header>",
        "<nav class='toc'><h2>Contents</h2><ol>",
    ]
    for idx, ch_path in enumerate(chapters, 1):
        t = chapter_title(ch_path)
        pg = chapter_pages.get(idx, 0)
        out.append(f"<li><a href='#chapter-{idx:02d}'>{html.escape(t)}</a> <small>(PDF p. {pg})</small></li>")
    out.append("</ol></nav>")

    for idx, ch_path in enumerate(chapters, 1):
        out.append(f"<section id='chapter-{idx:02d}'>")
        raw = strip_yaml_frontmatter(ch_path.read_text(encoding="utf-8"))
        for line in raw.splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith("# "):
                out.append(f"<h1>{md_inline_html(s[2:].strip())}</h1>")
            elif s.startswith("## "):
                out.append(f"<h2>{md_inline_html(s[3:].strip())}</h2>")
            elif s.startswith("### "):
                out.append(f"<h3>{md_inline_html(s[4:].strip())}</h3>")
            elif s.startswith(">"):
                out.append(f"<blockquote>{md_inline_html(s.lstrip('> ').strip())}</blockquote>")
            elif s.startswith("- "):
                out.append(f"<ul><li>{md_inline_html(s[2:].strip())}</li></ul>")
            elif s == "---":
                out.append("<hr>")
            else:
                out.append(f"<p>{md_inline_html(s)}</p>")
        out.append("</section>")

    out.append("</body></html>")
    return "\n".join(out)


def verify_and_report(
    book_title: str,
    edition_label: str,
    pdf_path: Path,
    html_path: Path,
    chapters: list[Path],
    chapter_pages: dict[int, int],
) -> str:
    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    blank_pages = [i + 1 for i, p in enumerate(reader.pages) if not (p.extract_text() or "").strip()]
    html_text = html_path.read_text(encoding="utf-8")
    html_missing = [
        idx for idx in range(1, len(chapters) + 1) if f"id='chapter-{idx:02d}'" not in html_text
    ]
    if blank_pages or html_missing:
        raise RuntimeError(f"Verification failed: blank_pages={blank_pages}, html_missing={html_missing}")

    digest = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    ch_lines = "\n".join(
        f"- PASS · PDF page {chapter_pages[idx]} · {chapter_title(p)}"
        for idx, p in enumerate(chapters, 1)
    )
    return (
        f"Reader Edition Extraction Verification — {book_title}\n"
        f"Status: PASS\n"
        f"Edition: {edition_label}\n"
        f"Renderer: fpdf2 {FPDF_VERSION} / pypdf {PYPDF_VERSION}\n"
        f"PDF: {pdf_path.name}\n"
        f"SHA-256: {digest}\n"
        f"Bytes: {pdf_path.stat().st_size:,}\n"
        f"Pages: {total_pages} ({total_pages - len(blank_pages)}/{total_pages} nonblank)\n"
        f"HTML anchors: {len(chapters) - len(html_missing)}/{len(chapters)}\n\n"
        f"Chapters:\n{ch_lines}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Reader Edition PDF + HTML for any book/series directory.")
    parser.add_argument(
        "book",
        nargs="?",
        default="series/parenthood-atlas",
        help="Book or series directory (default: series/parenthood-atlas)",
    )
    parser.add_argument("--edition", default="Reader Edition — Working Slice", help="Edition footer label")
    args = parser.parse_args()

    root = repo_root()
    book_path = resolve_book_path(root, Path(args.book))
    chapters_dir = book_path / "chapters"
    chapters = iter_chapter_files(chapters_dir)
    if not chapters:
        print(f"error: no chapters found in {chapters_dir}", file=sys.stderr)
        return 1

    pub_dir = (
        book_path / "preliminary" / "publishing"
        if (book_path / "preliminary" / "publishing").is_dir()
        else book_path / "publishing"
    )
    pub_dir.mkdir(parents=True, exist_ok=True)

    slug = book_path.name
    pdf_path = pub_dir / f"{slug}-reader-edition.pdf"
    html_path = pub_dir / f"{slug}-reader-edition.html"
    report_path = pub_dir / f"{slug}-extraction-report.txt"

    fonts = resolve_serif_fonts()
    book_title = slug.replace("-", " ").title()

    pass1_pdf, pass1_pages = build_reader_pdf(book_title, args.edition, chapters, fonts)
    final_pdf, final_pages = build_reader_pdf(book_title, args.edition, chapters, fonts, toc_pages=pass1_pages)
    final_pdf.output(str(pdf_path))

    html_path.write_text(
        build_reader_html(book_title, args.edition, chapters, final_pages),
        encoding="utf-8",
    )
    report = verify_and_report(book_title, args.edition, pdf_path, html_path, chapters, final_pages)
    report_path.write_text(report, encoding="utf-8")

    print(f"[pdf] Wrote {pdf_path.relative_to(root)} ({pdf_path.stat().st_size:,} bytes, {final_pdf.page_no()} pages)")
    print(f"[html] Wrote {html_path.relative_to(root)}")
    print(f"[verify] Wrote {report_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
