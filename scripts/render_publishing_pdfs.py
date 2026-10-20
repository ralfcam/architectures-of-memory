#!/usr/bin/env python3
"""Universal Multi-Series Commercial & Patronage Publisher (fpdf2 + pypdf + EPUB 3).

Supports:
- `--format a4` (default): Patreon / Private Circulation Reader Edition PDF + standalone HTML
- `--format kdp-6x9`: Amazon KDP Print-on-Demand 6"x9" (152.4 x 228.6 mm) trade paperback interior PDF
  with mirrored inside-gutter (20mm) and outside (15mm) margins
- `--epub`: Amazon KDP / Apple Books compliant EPUB 3 (.epub) reflowable eBook archive
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
import uuid
import zipfile
from datetime import date
from pathlib import Path

from fpdf import FPDF, __version__ as FPDF_VERSION
from pypdf import PdfReader, __version__ as PYPDF_VERSION

from merge_book_chapters import iter_chapter_files, repo_root, resolve_book_path, strip_yaml_frontmatter

KDP_6X9_MM = (152.4, 228.6)


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


class BookEditionPDF(FPDF):
    def __init__(
        self,
        book_title: str,
        edition_label: str,
        fonts: dict[str, Path],
        page_format: str = "a4",
    ) -> None:
        fmt = KDP_6X9_MM if page_format == "kdp-6x9" else "A4"
        super().__init__(format=fmt)
        self.book_title = book_title
        self.edition_label = edition_label
        self.page_format = page_format
        self.current_chapter_header = book_title
        for style, fpath in fonts.items():
            self.add_font("BookSerif", style, str(fpath))
        if page_format == "kdp-6x9":
            self.set_margins(20, 18, 15)
            self.set_auto_page_break(True, margin=18)
        else:
            self.set_margins(22, 22, 22)
            self.set_auto_page_break(True, margin=22)

    def header(self) -> None:
        # Apply mirrored inside/outside gutter margins on KDP 6x9 pages
        if self.page_format == "kdp-6x9":
            if self.page_no() % 2 == 1:  # Recto (odd page): inside gutter on left (20mm), outside on right (15mm)
                self.set_left_margin(20)
                self.set_right_margin(15)
            else:  # Verso (even page): outside on left (15mm), inside gutter on right (20mm)
                self.set_left_margin(15)
                self.set_right_margin(20)
        if self.page_no() <= 1:
            return
        self.set_y(10 if self.page_format == "kdp-6x9" else 12)
        self.set_font("BookSerif", "I", 8.0 if self.page_format == "kdp-6x9" else 8.5)
        self.set_text_color(110, 110, 110)
        align = "R" if self.page_no() % 2 == 1 else "L"
        self.cell(0, 5, self.current_chapter_header[:70], align=align)
        self.ln(7)
        self.set_text_color(20, 20, 20)

    def footer(self) -> None:
        self.set_y(-14 if self.page_format == "kdp-6x9" else -15)
        self.set_font("BookSerif", "", 8.0 if self.page_format == "kdp-6x9" else 8.5)
        self.set_text_color(110, 110, 110)
        if self.page_format == "kdp-6x9":
            self.cell(0, 5, f"{self.page_no()}", align="C")
        else:
            self.cell(0, 5, f"{self.edition_label}  ·  Page {self.page_no()}", align="C")
        self.set_text_color(20, 20, 20)


def build_book_pdf(
    book_title: str,
    edition_label: str,
    chapters: list[Path],
    fonts: dict[str, Path],
    page_format: str = "a4",
    toc_pages: dict[int, int] | None = None,
) -> tuple[BookEditionPDF, dict[int, int]]:
    pdf = BookEditionPDF(
        book_title=book_title,
        edition_label=edition_label,
        fonts=fonts,
        page_format=page_format,
    )
    body_pt = 9.5 if page_format == "kdp-6x9" else 10.0
    line_h = 4.9 if page_format == "kdp-6x9" else 5.4

    # Title & Contents Page
    pdf.add_page()
    pdf.set_font("BookSerif", "B", 18 if page_format == "kdp-6x9" else 20)
    pdf.multi_cell(0, 9, book_title)
    pdf.ln(2)
    pdf.set_font("BookSerif", "I", 10 if page_format == "kdp-6x9" else 11)
    pdf.multi_cell(0, 6, f"Realized Press · {edition_label} ({date.today().isoformat()})")
    pdf.ln(5)
    pdf.set_font("BookSerif", "B", 12 if page_format == "kdp-6x9" else 13)
    pdf.cell(0, 7, "Contents", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("BookSerif", "", 9.2 if page_format == "kdp-6x9" else 10)
    for idx, ch_path in enumerate(chapters, 1):
        pg = toc_pages.get(idx, 0) if toc_pages else 0
        pg_str = f"p. {pg}" if pg else "..."
        title = chapter_title(ch_path)
        pdf.multi_cell(0, 5.0, f"{idx:02d}. {title}  ({pg_str})", new_x="LMARGIN", new_y="NEXT")

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
                pdf.ln(2.2)
                continue
            if s.startswith("# "):
                pdf.set_font("BookSerif", "B", 14 if page_format == "kdp-6x9" else 15)
                pdf.multi_cell(0, 7.5, clean_pdf_line(s[2:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(2.5)
            elif s.startswith("## "):
                pdf.ln(1.8)
                pdf.set_font("BookSerif", "B", 11.2 if page_format == "kdp-6x9" else 12)
                pdf.multi_cell(0, 6.0, clean_pdf_line(s[3:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(1.2)
            elif s.startswith("### "):
                pdf.ln(1.2)
                pdf.set_font("BookSerif", "BI", 10.0 if page_format == "kdp-6x9" else 10.5)
                pdf.multi_cell(0, 5.5, clean_pdf_line(s[4:].strip()), new_x="LMARGIN", new_y="NEXT")
                pdf.ln(1)
            elif s.startswith(">"):
                pdf.set_font("BookSerif", "I", body_pt - 0.5)
                pdf.set_x(pdf.l_margin + 5)
                pdf.multi_cell(0, line_h - 0.3, clean_pdf_line(s.lstrip("> ").strip()), new_x="LMARGIN", new_y="NEXT")
            elif s == "---":
                pdf.ln(2)
            else:
                pdf.set_font("BookSerif", "", body_pt)
                pdf.multi_cell(0, line_h, clean_pdf_line(s), new_x="LMARGIN", new_y="NEXT")

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
        f"<header><h1>{html.escape(book_title)}</h1><p><em>Realized Press · {html.escape(edition_label)} ({date.today().isoformat()})</em></p></header>",
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


def build_kdp_epub(book_title: str, author: str, chapters: list[Path], epub_path: Path) -> None:
    """Compile a valid, KDP-ready EPUB 3 archive using Python's built-in zipfile module."""
    book_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"realized-press.{epub_path.stem}"))
    today = date.today().isoformat()

    container_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
        "  <rootfiles>\n"
        '    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n'
        "  </rootfiles>\n"
        "</container>\n"
    )
    style_css = (
        "body { font-family: Georgia, serif; line-height: 1.55; margin: 5%; color: #111; }\n"
        "h1 { font-size: 1.5em; margin-top: 1.5em; margin-bottom: 0.6em; page-break-before: always; }\n"
        "h2 { font-size: 1.2em; margin-top: 1.2em; }\n"
        "h3 { font-size: 1.05em; font-style: italic; }\n"
        "blockquote { border-left: 2px solid #888; padding-left: 1em; font-style: italic; margin: 1em 0; }\n"
    )

    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="style.css" media-type="text/css"/>',
    ]
    spine_items = ['<itemref idref="nav"/>']
    nav_links = []
    chapter_xhtmls: list[tuple[str, str]] = []

    for idx, ch_path in enumerate(chapters, 1):
        fname = f"chapter-{idx:02d}.xhtml"
        cid = f"ch{idx:02d}"
        title = chapter_title(ch_path)
        manifest_items.append(f'<item id="{cid}" href="{fname}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="{cid}"/>')
        nav_links.append(f'<li><a href="{fname}">{html.escape(title)}</a></li>')

        body_lines: list[str] = []
        raw = strip_yaml_frontmatter(ch_path.read_text(encoding="utf-8"))
        for line in raw.splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith("# "):
                body_lines.append(f"<h1>{md_inline_html(s[2:].strip())}</h1>")
            elif s.startswith("## "):
                body_lines.append(f"<h2>{md_inline_html(s[3:].strip())}</h2>")
            elif s.startswith("### "):
                body_lines.append(f"<h3>{md_inline_html(s[4:].strip())}</h3>")
            elif s.startswith(">"):
                body_lines.append(f"<blockquote><p>{md_inline_html(s.lstrip('> ').strip())}</p></blockquote>")
            elif s.startswith("- "):
                body_lines.append(f"<ul><li>{md_inline_html(s[2:].strip())}</li></ul>")
            elif s == "---":
                body_lines.append("<hr/>")
            else:
                body_lines.append(f"<p>{md_inline_html(s)}</p>")

        xhtml = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n'
            f"<head><meta charset=\"utf-8\"/><title>{html.escape(title)}</title>"
            '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
            "<body>\n" + "\n".join(body_lines) + "\n</body></html>\n"
        )
        chapter_xhtmls.append((fname, xhtml))

    nav_xhtml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n'
        f"<head><meta charset=\"utf-8\"/><title>{html.escape(book_title)}</title>"
        '<link rel="stylesheet" type="text/css" href="style.css"/></head>\n'
        "<body>\n"
        f"<h1>{html.escape(book_title)}</h1>\n"
        f"<p><em>{html.escape(author)} · Realized Press ({today})</em></p>\n"
        '<nav epub:type="toc" id="toc"><h2>Contents</h2><ol>\n'
        + "\n".join(nav_links)
        + "\n</ol></nav></body></html>\n"
    )

    content_opf = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id">\n'
        '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        f'    <dc:identifier id="pub-id">urn:uuid:{book_uuid}</dc:identifier>\n'
        f"    <dc:title>{html.escape(book_title)}</dc:title>\n"
        f"    <dc:creator>{html.escape(author)}</dc:creator>\n"
        "    <dc:publisher>Realized Press</dc:publisher>\n"
        "    <dc:language>en</dc:language>\n"
        f'    <meta property="dcterms:modified">{today}T00:00:00Z</meta>\n'
        "  </metadata>\n"
        "  <manifest>\n    "
        + "\n    ".join(manifest_items)
        + "\n  </manifest>\n"
        "  <spine>\n    "
        + "\n    ".join(spine_items)
        + "\n  </spine>\n"
        "</package>\n"
    )

    with zipfile.ZipFile(epub_path, "w") as zf:
        # EPUB spec requires uncompressed 'mimetype' as the very first entry
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/style.css", style_css, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/content.opf", content_opf, compress_type=zipfile.ZIP_DEFLATED)
        for fname, content in chapter_xhtmls:
            zf.writestr(f"OEBPS/{fname}", content, compress_type=zipfile.ZIP_DEFLATED)


def verify_and_report(
    book_title: str,
    edition_label: str,
    pdf_path: Path,
    html_path: Path | None,
    chapters: list[Path],
    chapter_pages: dict[int, int],
) -> str:
    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    blank_pages = [i + 1 for i, p in enumerate(reader.pages) if not (p.extract_text() or "").strip()]
    html_missing: list[int] = []
    if html_path and html_path.is_file():
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
        f"Publishing Extraction Verification — {book_title}\n"
        f"Status: PASS\n"
        f"Edition: {edition_label}\n"
        f"Renderer: fpdf2 {FPDF_VERSION} / pypdf {PYPDF_VERSION}\n"
        f"PDF: {pdf_path.name}\n"
        f"SHA-256: {digest}\n"
        f"Bytes: {pdf_path.stat().st_size:,}\n"
        f"Pages: {total_pages} ({total_pages - len(blank_pages)}/{total_pages} nonblank)\n\n"
        f"Chapters:\n{ch_lines}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Patreon Reader Edition (A4) or Amazon KDP (6x9 PDF + EPUB 3).")
    parser.add_argument(
        "book",
        nargs="?",
        default="series/parenthood-atlas",
        help="Book or series directory (default: series/parenthood-atlas)",
    )
    parser.add_argument(
        "--format",
        choices=("a4", "kdp-6x9"),
        default="a4",
        help="Page trim format: 'a4' (Reader Edition) or 'kdp-6x9' (Amazon KDP 6x9 in paperback interior)",
    )
    parser.add_argument("--epub", action="store_true", help="Also generate KDP-ready EPUB 3 (.epub) eBook package")
    parser.add_argument("--author", default="Jose Campos", help="Author metadata for EPUB/PDF")
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
        if (book_path / "preliminary" / "publishing").is_dir() and args.format == "a4"
        else book_path / "publishing"
    )
    pub_dir.mkdir(parents=True, exist_ok=True)

    slug = book_path.name
    suffix = "kdp-6x9" if args.format == "kdp-6x9" else "reader-edition"
    pdf_path = pub_dir / f"{slug}-{suffix}.pdf"
    html_path = pub_dir / f"{slug}-reader-edition.html" if args.format == "a4" else None
    report_path = pub_dir / f"{slug}-{suffix}-extraction-report.txt"

    fonts = resolve_serif_fonts()
    book_title = slug.replace("-", " ").title()

    pass1_pdf, pass1_pages = build_book_pdf(book_title, args.edition, chapters, fonts, page_format=args.format)
    final_pdf, final_pages = build_book_pdf(
        book_title, args.edition, chapters, fonts, page_format=args.format, toc_pages=pass1_pages
    )
    final_pdf.output(str(pdf_path))

    if html_path:
        html_path.write_text(
            build_reader_html(book_title, args.edition, chapters, final_pages),
            encoding="utf-8",
        )
    report = verify_and_report(book_title, args.edition, pdf_path, html_path, chapters, final_pages)
    report_path.write_text(report, encoding="utf-8")

    print(f"[pdf:{args.format}] Wrote {pdf_path.relative_to(root)} ({pdf_path.stat().st_size:,} bytes, {final_pdf.page_no()} pages)")
    if html_path:
        print(f"[html] Wrote {html_path.relative_to(root)}")
    print(f"[verify] Wrote {report_path.relative_to(root)}")

    if args.epub:
        epub_path = pub_dir / f"{slug}-kdp.epub"
        build_kdp_epub(book_title, args.author, chapters, epub_path)
        print(f"[epub] Wrote {epub_path.relative_to(root)} ({epub_path.stat().st_size:,} bytes)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
