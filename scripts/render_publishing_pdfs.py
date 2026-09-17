#!/usr/bin/env python3
"""Render publishing markdown to HTML and PDF (fpdf2 + DejaVu)."""

from __future__ import annotations

import html
import re
from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
FONT = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
FONT_B = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")


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


class BriefPDF(FPDF):
    def __init__(self) -> None:
        super().__init__(format="letter")
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


def md_to_pdf(md: str, pdf_path: Path) -> None:
    pdf = BriefPDF()
    pdf.add_page()
    for line in md.splitlines():
        if line.startswith("# "):
            pdf.heading(line[2:], 16)
        elif line.startswith("## "):
            pdf.ln(2)
            pdf.heading(line[3:], 12)
        elif line.startswith("### "):
            pdf.heading(line[4:], 11)
        elif line.startswith("|"):
            continue
        elif line.startswith("- "):
            pdf.body("• " + line[2:], 10.5)
        elif line.strip() == "---":
            pdf.ln(2)
        elif line.strip():
            pdf.body(line, 10.5)
    pdf.output(str(pdf_path))


def write_pair(md_path: Path, title: str, pdf_path: Path | None = None) -> None:
    md = md_path.read_text(encoding="utf-8")
    html_path = (pdf_path or md_path).with_suffix(".html")
    html_path.write_text(md_to_html(md, title), encoding="utf-8")
    target = pdf_path or md_path.with_suffix(".pdf")
    md_to_pdf(md, target)
    print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size} bytes)")


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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
