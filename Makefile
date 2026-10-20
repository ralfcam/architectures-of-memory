# Multi-Series Editorial Monorepo Makefile
# Usage:
#   make audit BOOK=series/architectures-of-memory/book-01-vanishing-signal
#   make audit BOOK=series/parenthood-atlas
#   make five-rule BOOK=series/parenthood-atlas
#   make pdf BOOK=series/architectures-of-memory/book-01-vanishing-signal

PYTHON ?= python
BOOK ?= series/architectures-of-memory/book-01-vanishing-signal
PREFIX ?=
VOICE ?= Kore
CHAPTER ?=

PrefixArg = $(if $(strip $(PREFIX)),--prefix $(strip $(PREFIX)),)
ChapterArg = $(if $(strip $(CHAPTER)),--chapter $(strip $(CHAPTER)),)

.PHONY: merge merge-audiobook merge-both audit audit-gemini audit-all five-rule five-rule-online five-rule-all pdf sync-sources audiobook-dry-run audiobook-tts

merge:
	$(PYTHON) scripts/merge_book_chapters.py $(BOOK) $(PrefixArg)

merge-audiobook:
	$(PYTHON) scripts/merge_book_chapters.py $(BOOK) --audiobook $(PrefixArg)

merge-both: merge merge-audiobook

audit:
	$(PYTHON) scripts/audit_manuscript.py $(BOOK)

audit-gemini:
	$(PYTHON) scripts/audit_manuscript.py $(BOOK) --gemini

audit-all:
	$(PYTHON) scripts/audit_manuscript.py series/architectures-of-memory/book-01-vanishing-signal --strict
	$(PYTHON) scripts/audit_manuscript.py series/parenthood-atlas --strict

five-rule:
	$(PYTHON) scripts/five_rule_check.py $(BOOK) --summary-only

five-rule-online:
	$(PYTHON) scripts/five_rule_check.py $(BOOK) --online-retraction-check

five-rule-all:
	$(PYTHON) scripts/five_rule_check.py series/architectures-of-memory/book-01-vanishing-signal --summary-only
	$(PYTHON) scripts/five_rule_check.py series/architectures-of-memory/book-02-forget-gate --summary-only
	$(PYTHON) scripts/five_rule_check.py series/architectures-of-memory/book-03-weight-of-attention --summary-only
	$(PYTHON) scripts/five_rule_check.py series/architectures-of-memory/book-04-context-window --summary-only
	$(PYTHON) scripts/five_rule_check.py series/architectures-of-memory/book-05-architecture-of-forgetting --summary-only
	$(PYTHON) scripts/five_rule_check.py series/parenthood-atlas --summary-only

pdf:
	$(PYTHON) scripts/render_publishing_pdfs.py $(BOOK)

sync-sources:
	$(PYTHON) scripts/sync_okf_sources.py

audiobook-dry-run:
	$(PYTHON) scripts/generate_audiobook_tts.py $(BOOK) $(ChapterArg) --voice $(VOICE) --dry-run

audiobook-tts:
	$(PYTHON) scripts/generate_audiobook_tts.py $(BOOK) $(ChapterArg) --voice $(VOICE)
