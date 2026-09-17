#!/usr/bin/env python3
"""Mechanical five-rule checks. Does not flip status: stable. Rule 3 still needs a human."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "What We Know",
    "How Confident We Are",
    "Evidence and Causal Assessment",
    "Effect Size and Persistence",
    "Bias, Heterogeneity, and Confounding",
    "What Remains Uncertain",
    "What This Does Not Mean",
    "What Action Is Reasonably Justified",
    "Sources",
]

GRADE_WORDS = ("high", "moderate", "low", "very-low", "very low")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1], parts[2]


def yaml_confidence(fm: str) -> str:
    m = re.search(r"^confidence:\s*(.+)$", fm, re.M)
    return (m.group(1).strip().strip('"') if m else "").lower()


def yaml_status(fm: str) -> str:
    m = re.search(r"^status:\s*(\S+)", fm, re.M)
    return m.group(1) if m else ""


def source_ids_and_urls(fm: str) -> list[tuple[str, str]]:
    ids = re.findall(r"^\s+- id: (\S+)", fm, re.M)
    urls = re.findall(r"^\s+resource: (\S+)", fm, re.M)
    out = []
    for i, sid in enumerate(ids):
        url = urls[i] if i < len(urls) else ""
        out.append((sid, url))
    return out


def in_body_grade_tokens(body: str) -> set[str]:
    tokens = set()
    for line in body.splitlines():
        if not re.search(r"\*\*Grade\*\*|\*\*grade\*\*", line, re.I):
            continue
        low = line.lower()
        if "very low" in low or "very-low" in low:
            tokens.add("very-low")
        for word in ("high", "moderate", "low"):
            if re.search(rf"\b{word}\b", low):
                tokens.add(word)
    return tokens


def yaml_grade_tokens(conf: str) -> set[str]:
    tokens = set()
    c = conf.replace("_", "-")
    if "very-low" in c or "very low" in c:
        tokens.add("very-low")
    for word in ("high", "moderate", "low"):
        if re.search(rf"\b{word}\b", c) or f"-{word}" in c or c.startswith(word):
            tokens.add(word)
    return tokens


def check_card(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    sources = source_ids_and_urls(fm)
    missing_sections = [s for s in REQUIRED_SECTIONS if f"## {s}" not in body]
    yaml_tok = yaml_grade_tokens(yaml_confidence(fm))
    body_tok = in_body_grade_tokens(body)
    rule4 = bool(yaml_tok) and yaml_tok == body_tok
    wtdm = "## What This Does Not Mean" in body
    wtdm_text = ""
    if wtdm:
        chunk = body.split("## What This Does Not Mean", 1)[1]
        wtdm_text = chunk.split("## ", 1)[0].strip()
    return {
        "path": str(path),
        "status": yaml_status(fm),
        "confidence": yaml_confidence(fm),
        "source_count": len(sources),
        "sources": sources,
        "rule1_urls_present": all(u.startswith("http") for _, u in sources) and bool(sources),
        "rule3_second_source_id": len(sources) >= 2,
        "rule4_yaml_matches_body_tokens": rule4,
        "rule4_yaml_tokens": sorted(yaml_tok),
        "rule4_body_tokens": sorted(body_tok),
        "rule5_wtdm_nonempty": wtdm and len(wtdm_text) > 40,
        "missing_sections": missing_sections,
    }


def format_report(r: dict) -> str:
    lines = [
        f"Card: `{r['path']}`",
        f"YAML status: `{r['status']}` (script never flips this)",
        f"YAML confidence: `{r['confidence']}`",
        "",
        f"- Rule 1 (mechanical): source URLs present = **{'pass' if r['rule1_urls_present'] else 'fail'}** ({r['source_count']} IDs).",
        "- Rule 2 (retraction/EoC): **not checked here** — resolve each DOI on Crossref (`update-to`) and PubMed publication types.",
        f"- Rule 3 (replication): second source ID on card = **{'present' if r['rule3_second_source_id'] else 'absent'}**. A second ID is not by itself independent conceptual replication; a human must classify it.",
        f"- Rule 4 (YAML = in-body grade tokens): **{'pass' if r['rule4_yaml_matches_body_tokens'] else 'fail'}** "
        f"(yaml {r['rule4_yaml_tokens']} vs body {r['rule4_body_tokens']}).",
        f"- Rule 5 (WTDM nonempty): **{'pass' if r['rule5_wtdm_nonempty'] else 'fail'}**.",
    ]
    if r["missing_sections"]:
        lines.append(f"- Missing sections: {', '.join(r['missing_sections'])}")
    lines.append("")
    lines.append("Do not set `status: stable` from this script.")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 scripts/five_rule_check.py evidence-cards/<card>.md [...]", file=sys.stderr)
        return 2
    rc = 0
    for arg in argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"FAIL missing file: {path}", file=sys.stderr)
            rc = 1
            continue
        report = check_card(path)
        print(format_report(report))
        if not report["rule1_urls_present"] or not report["rule4_yaml_matches_body_tokens"] or not report["rule5_wtdm_nonempty"]:
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
