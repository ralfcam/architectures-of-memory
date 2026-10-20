#!/usr/bin/env python3
"""Academic & Bibliographic MCP Server (and CLI) for Architectures of Memory.

Provides 4 tools over MCP Stdio (JSON-RPC 2.0) or CLI (`--cli`):
- crossref_lookup: Verify DOIs, volume/issue/pages, errata, and fetch official BibTeX via Crossref.
- arxiv_search: Search arXiv preprints by ID or query, returning metadata, PDF URLs, and BibTeX.
- openalex_work: Query OpenAlex for citation counts, open-access PDFs, and retraction status (`is_retracted`).
- add_bibtex_entry: Append or update a verified BibTeX entry in `book-NN-*/research/sources.bib`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

USER_AGENT = "ArchitecturesOfMemory-AcademicMCP/1.0 (https://github.com/ralfcam/architectures-of-memory; mailto:research@architecturesofmemory.org)"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _http_get_json(url: str, timeout: int = 15) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _http_get_text(url: str, accept: str = "*/*", timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _fetch_doi_bibtex(doi: str) -> str:
    clean_doi = doi.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/").removeprefix("doi:")
    url = f"https://doi.org/{urllib.parse.quote(clean_doi, safe='/')}"
    try:
        bib = _http_get_text(url, accept="application/x-bibtex; charset=utf-8", timeout=10).strip()
        if bib.startswith("@"):
            return bib
    except Exception:
        pass
    return ""


def _synthesize_bibtex_from_crossref(item: dict[str, Any]) -> str:
    doi = item.get("DOI", "")
    authors_raw = item.get("author") or []
    authors = []
    for a in authors_raw:
        family = a.get("family", "")
        given = a.get("given", "")
        if family and given:
            authors.append(f"{family}, {given}")
        elif family:
            authors.append(family)
    first_family = re.sub(r"[^a-zA-Z0-9]", "", (authors_raw[0].get("family", "ref") if authors_raw else "ref")).lower()
    year = ""
    for date_field in ("published-print", "published-online", "issued", "created"):
        parts = (item.get(date_field) or {}).get("date-parts") or []
        if parts and parts[0]:
            year = str(parts[0][0])
            break
    key = f"{first_family}{year}" if year else first_family
    title_list = item.get("title") or []
    title = title_list[0] if title_list else ""
    container_list = item.get("container-title") or []
    journal = container_list[0] if container_list else ""
    volume = item.get("volume", "")
    issue = item.get("issue", "")
    page = item.get("page", "")
    publisher = item.get("publisher", "")
    entry_type = "book" if item.get("type") in ("book", "monograph") else "article"

    lines = [f"@{entry_type}{{{key},"]
    if authors:
        lines.append(f"  author = {{{' and '.join(authors)}}},")
    if title:
        lines.append(f"  title = {{{title}}},")
    if journal:
        lines.append(f"  journal = {{{journal}}},")
    if publisher and entry_type == "book":
        lines.append(f"  publisher = {{{publisher}}},")
    if year:
        lines.append(f"  year = {{{year}}},")
    if volume:
        lines.append(f"  volume = {{{volume}}},")
    if issue:
        lines.append(f"  number = {{{issue}}},")
    if page:
        lines.append(f"  pages = {{{page}}},")
    if doi:
        lines.append(f"  doi = {{{doi}}},")
    lines.append("}")
    return "\n".join(lines)


def _format_crossref_item(item: dict[str, Any], include_bibtex: bool = True) -> dict[str, Any]:
    doi = item.get("DOI", "")
    year = None
    for date_field in ("published-print", "published-online", "issued", "created"):
        parts = (item.get(date_field) or {}).get("date-parts") or []
        if parts and parts[0]:
            year = parts[0][0]
            break
    authors = [
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in (item.get("author") or [])
    ]
    updates = item.get("update-to") or []
    updated_by = item.get("updated-by") or []
    bib = (_fetch_doi_bibtex(doi) if (include_bibtex and doi) else "") or _synthesize_bibtex_from_crossref(item)
    return {
        "doi": doi,
        "url": f"https://doi.org/{doi}" if doi else item.get("URL"),
        "title": (item.get("title") or [""])[0],
        "authors": authors,
        "year": year,
        "journal": (item.get("container-title") or [""])[0],
        "volume": item.get("volume"),
        "issue": item.get("issue"),
        "pages": item.get("page"),
        "publisher": item.get("publisher"),
        "type": item.get("type"),
        "is_referenced_by_count": item.get("is-referenced-by-count"),
        "updates_or_errata": updates + updated_by,
        "bibtex": bib,
    }


def tool_crossref_lookup(args: dict[str, Any]) -> dict[str, Any]:
    doi = (args.get("doi") or "").strip()
    query = (args.get("query") or "").strip()
    limit = min(max(int(args.get("limit") or 5), 1), 10)

    if doi:
        clean_doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/").removeprefix("doi:")
        url = f"https://api.crossref.org/works/{urllib.parse.quote(clean_doi, safe='')}"
        data = _http_get_json(url)
        item = data.get("message") or {}
        return {"results": [_format_crossref_item(item, include_bibtex=True)]}

    if not query:
        raise ValueError("Provide either 'doi' or 'query'.")

    params = urllib.parse.urlencode({"query": query, "rows": limit})
    url = f"https://api.crossref.org/works?{params}"
    data = _http_get_json(url)
    items = (data.get("message") or {}).get("items") or []
    results = [_format_crossref_item(it, include_bibtex=(idx == 0)) for idx, it in enumerate(items)]
    return {"query": query, "count": len(results), "results": results}


def tool_arxiv_search(args: dict[str, Any]) -> dict[str, Any]:
    query = (args.get("query") or "").strip()
    arxiv_id = (args.get("arxiv_id") or "").strip()
    limit = min(max(int(args.get("limit") or 5), 1), 10)

    if arxiv_id:
        clean_id = arxiv_id.removeprefix("arXiv:").removeprefix("arxiv:")
        params = urllib.parse.urlencode({"id_list": clean_id, "max_results": 1})
    elif query:
        if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", query):
            params = urllib.parse.urlencode({"id_list": query, "max_results": 1})
        else:
            params = urllib.parse.urlencode({"search_query": f"all:{query}", "start": 0, "max_results": limit})
    else:
        raise ValueError("Provide either 'query' or 'arxiv_id'.")

    url = f"http://export.arxiv.org/api/query?{params}"
    xml_text = _http_get_text(url, accept="application/atom+xml")
    root = ET.fromstring(xml_text)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

    results = []
    for entry in root.findall("atom:entry", ns):
        id_url = (entry.findtext("atom:id", default="", namespaces=ns) or "").strip()
        aid = id_url.rsplit("/abs/", 1)[-1] if "/abs/" in id_url else id_url
        title = re.sub(r"\s+", " ", (entry.findtext("atom:title", default="", namespaces=ns) or "").strip())
        summary = re.sub(r"\s+", " ", (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip())
        published = (entry.findtext("atom:published", default="", namespaces=ns) or "")[:10]
        updated = (entry.findtext("atom:updated", default="", namespaces=ns) or "")[:10]
        authors = [
            (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
            for a in entry.findall("atom:author", ns)
        ]
        doi = (entry.findtext("arxiv:doi", default="", namespaces=ns) or "").strip()
        journal_ref = (entry.findtext("arxiv:journal_ref", default="", namespaces=ns) or "").strip()
        year = published[:4] if published else ""
        first_last = re.sub(r"[^a-zA-Z0-9]", "", (authors[0].split()[-1] if authors else "arxiv")).lower()
        bib_key = f"{first_last}{year}arxiv"
        bib_authors = " and ".join(authors)
        base_id = re.sub(r"v\d+$", "", aid)
        bib = (
            f"@article{{{bib_key},\n"
            f"  author = {{{bib_authors}}},\n"
            f"  title = {{{title}}},\n"
            f"  journal = {{arXiv preprint arXiv:{base_id}}},\n"
            f"  year = {{{year}}},\n"
            f"  eprint = {{{base_id}}},\n"
            f"  archivePrefix = {{arXiv}},\n"
            f"  url = {{https://arxiv.org/abs/{base_id}}}\n"
            f"}}"
        )
        results.append(
            {
                "arxiv_id": base_id,
                "title": title,
                "authors": authors,
                "published": published,
                "updated": updated,
                "doi": doi or None,
                "journal_ref": journal_ref or None,
                "abs_url": f"https://arxiv.org/abs/{base_id}",
                "pdf_url": f"https://arxiv.org/pdf/{base_id}.pdf",
                "summary": summary[:600] + ("..." if len(summary) > 600 else ""),
                "bibtex": bib,
            }
        )
    return {"count": len(results), "results": results}


def tool_openalex_work(args: dict[str, Any]) -> dict[str, Any]:
    doi = (args.get("doi") or "").strip()
    query = (args.get("query") or "").strip()
    limit = min(max(int(args.get("limit") or 5), 1), 10)

    def _format_oa(w: dict[str, Any]) -> dict[str, Any]:
        authorships = w.get("authorships") or []
        authors = [(a.get("author") or {}).get("display_name", "") for a in authorships]
        loc = w.get("primary_location") or {}
        source = loc.get("source") or {}
        biblio = w.get("biblio") or {}
        oa = w.get("open_access") or {}
        return {
            "openalex_id": w.get("id"),
            "doi": w.get("doi"),
            "title": w.get("display_name") or w.get("title"),
            "publication_year": w.get("publication_year"),
            "authors": authors,
            "venue": source.get("display_name"),
            "volume": biblio.get("volume"),
            "issue": biblio.get("issue"),
            "pages": f"{biblio.get('first_page', '')}-{biblio.get('last_page', '')}".strip("-"),
            "cited_by_count": w.get("cited_by_count"),
            "is_retracted": w.get("is_retracted", False),
            "is_oa": oa.get("is_oa", False),
            "oa_url": oa.get("oa_url"),
        }

    if doi:
        clean_doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/").removeprefix("doi:")
        url = f"https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(clean_doi, safe='/')}"
        w = _http_get_json(url)
        return {"results": [_format_oa(w)]}

    if not query:
        raise ValueError("Provide either 'doi' or 'query'.")

    params = urllib.parse.urlencode({"search": query, "per-page": limit})
    url = f"https://api.openalex.org/works?{params}"
    data = _http_get_json(url)
    items = data.get("results") or []
    return {"query": query, "count": len(items), "results": [_format_oa(w) for w in items]}


def tool_add_bibtex_entry(args: dict[str, Any]) -> dict[str, Any]:
    book = (args.get("book") or "").strip()
    bibtex = (args.get("bibtex") or "").strip()
    if not book or not bibtex:
        raise ValueError("Both 'book' and 'bibtex' are required.")

    m = re.match(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibtex)
    if not m:
        raise ValueError("Invalid BibTeX entry: could not parse citation key.")
    cite_key = m.group(1)

    bib_path = (repo_root() / book / "research" / "sources.bib").resolve()
    if not bib_path.parent.is_dir():
        raise ValueError(f"Directory does not exist: {bib_path.parent}")

    existing = bib_path.read_text(encoding="utf-8") if bib_path.is_file() else ""
    key_pattern = re.compile(
        rf"@\w+\s*\{{\s*{re.escape(cite_key)}\s*,.*?(?:\n\}}|\}}\s*$)",
        re.MULTILINE | re.DOTALL,
    )
    if key_pattern.search(existing):
        existing_match = key_pattern.search(existing)
        # If same key but different DOI/title, disambiguate key with suffix
        doi_m = re.search(r"DOI\s*=\s*\{([^}]+)\}", bibtex, re.IGNORECASE)
        new_doi = doi_m.group(1).lower() if doi_m else ""
        if existing_match and new_doi and new_doi not in existing_match.group(0).lower():
            suffix = re.sub(r"[^a-z0-9]", "", new_doi[-4:]) or "b"
            cite_key = f"{cite_key}_{suffix}"
            bibtex = re.sub(r"^(@\w+\s*\{\s*)[^,\s]+", rf"\1{cite_key}", bibtex, count=1)
            sep = "\n\n" if existing.strip() else ""
            updated = existing.rstrip() + sep + bibtex + "\n"
            action = "added"
        else:
            updated = key_pattern.sub(bibtex, existing, count=1)
            action = "updated"
    else:
        sep = "\n\n" if existing.strip() else ""
        updated = existing.rstrip() + sep + bibtex + "\n"
        action = "added"

    bib_path.write_text(updated, encoding="utf-8")
    return {"status": action, "citation_key": cite_key, "path": bib_path.as_posix()}


TOOLS_SCHEMA = [
    {
        "name": "crossref_lookup",
        "description": "Search Crossref or look up an exact DOI to verify publication year, journal, volume, issue, pagination, errata/updates, and retrieve official BibTeX.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "doi": {"type": "string", "description": "Exact DOI (e.g., '10.1162/neco.1997.9.8.1735')"},
                "query": {"type": "string", "description": "Bibliographic search string (title, author, year)"},
                "limit": {"type": "integer", "description": "Max results when searching by query (1-10, default 5)", "default": 5},
            },
        },
    },
    {
        "name": "arxiv_search",
        "description": "Search arXiv preprints by query or exact arXiv ID, returning authors, dates, abstract, PDF link, DOI/journal_ref, and BibTeX.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "arxiv_id": {"type": "string", "description": "Exact arXiv ID (e.g., '1409.0473' or '1706.03762')"},
                "query": {"type": "string", "description": "Search query for arXiv title/author/abstract"},
                "limit": {"type": "integer", "description": "Max results (1-10, default 5)", "default": 5},
            },
        },
    },
    {
        "name": "openalex_work",
        "description": "Look up academic works in OpenAlex by DOI or search query to check citation counts, retraction status (is_retracted), and open-access PDF URLs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "doi": {"type": "string", "description": "Exact DOI to look up in OpenAlex"},
                "query": {"type": "string", "description": "Search query for OpenAlex works"},
                "limit": {"type": "integer", "description": "Max results (1-10, default 5)", "default": 5},
            },
        },
    },
    {
        "name": "add_bibtex_entry",
        "description": "Add or update a verified BibTeX entry in a book's research/sources.bib file (deduplicated by citation key).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "book": {"type": "string", "description": "Book folder name (e.g. 'book-01-vanishing-signal' or 'book-02-forget-gate')"},
                "bibtex": {"type": "string", "description": "Complete BibTeX entry string starting with @article{..., @book{..., etc."},
            },
            "required": ["book", "bibtex"],
        },
    },
]

TOOL_HANDLERS = {
    "crossref_lookup": tool_crossref_lookup,
    "arxiv_search": tool_arxiv_search,
    "openalex_work": tool_openalex_work,
    "add_bibtex_entry": tool_add_bibtex_entry,
}


def run_stdio_server() -> None:
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method")
        msg_id = msg.get("id")

        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "academic-bib", "version": "1.0.0"},
                },
            }
            print(json.dumps(resp), flush=True)
        elif method == "notifications/initialized":
            continue
        elif method == "ping":
            print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {}}), flush=True)
        elif method == "tools/list":
            print(
                json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SCHEMA}}),
                flush=True,
            )
        elif method == "tools/call":
            params = msg.get("params") or {}
            tname = params.get("name")
            targs = params.get("arguments") or {}
            handler = TOOL_HANDLERS.get(tname)
            if not handler:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"Unknown tool: {tname}"},
                }
                print(json.dumps(err_resp), flush=True)
                continue
            try:
                out = handler(targs)
                res_resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(out, indent=2, ensure_ascii=False)}],
                        "isError": False,
                    },
                }
            except Exception as exc:
                res_resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [{"type": "text", "text": f"Error: {exc}"}],
                        "isError": True,
                    },
                }
            print(json.dumps(res_resp), flush=True)
        elif msg_id is not None:
            print(
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "error": {"code": -32601, "message": f"Method not found: {method}"},
                    }
                ),
                flush=True,
            )


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        parser = argparse.ArgumentParser(description="CLI interface for academic-bib MCP tools")
        parser.add_argument("--cli", action="store_true")
        parser.add_argument("tool", choices=list(TOOL_HANDLERS.keys()))
        parser.add_argument("--doi", default="")
        parser.add_argument("--arxiv-id", default="")
        parser.add_argument("--query", default="")
        parser.add_argument("--limit", type=int, default=5)
        parser.add_argument("--book", default="")
        parser.add_argument("--bibtex", default="")
        args = parser.parse_args()
        out = TOOL_HANDLERS[args.tool](
            {
                "doi": args.doi,
                "arxiv_id": args.arxiv_id,
                "query": args.query,
                "limit": args.limit,
                "book": args.book,
                "bibtex": args.bibtex,
            }
        )
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        run_stdio_server()


if __name__ == "__main__":
    main()
