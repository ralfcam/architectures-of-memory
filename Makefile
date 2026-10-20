# Merge all chapters under a book-NN-* directory into one Markdown file.
# Requires GNU Make and Python 3 on PATH.
#
# Examples:
#   make merge BOOK=book-01-vanishing-signal PREFIX=vanishing-signal
#   make merge-audiobook BOOK=book-01-vanishing-signal PREFIX=vanishing-signal

.PHONY: merge merge-audiobook merge-help audit audiobook-dry-run audiobook-tts

BOOK ?=
PREFIX ?=
VOICE ?= Kore

_MERGE_EXTRA = $(if $(strip $(PREFIX)),--prefix $(PREFIX),)

merge-help:
	@echo Usage:
	@echo   make merge BOOK=book-01-vanishing-signal
	@echo   make merge BOOK=book-01-vanishing-signal PREFIX=vanishing-signal
	@echo   make merge-audiobook BOOK=book-01-vanishing-signal
	@echo   make audit BOOK=book-01-vanishing-signal
	@echo   make audiobook-dry-run BOOK=book-01-vanishing-signal
	@echo   make audiobook-tts BOOK=book-01-vanishing-signal VOICE=Kore

merge:
ifeq ($(strip $(BOOK)),)
	$(error Set BOOK, e.g. make merge BOOK=book-01-vanishing-signal)
endif
	python scripts/merge_book_chapters.py $(BOOK) $(_MERGE_EXTRA)

merge-audiobook:
ifeq ($(strip $(BOOK)),)
	$(error Set BOOK, e.g. make merge-audiobook BOOK=book-01-vanishing-signal)
endif
	python scripts/merge_book_chapters.py $(BOOK) --audiobook $(_MERGE_EXTRA)

audit:
ifeq ($(strip $(BOOK)),)
	$(error Set BOOK, e.g. make audit BOOK=book-01-vanishing-signal)
endif
	python scripts/audit_manuscript.py $(BOOK)

audiobook-dry-run:
ifeq ($(strip $(BOOK)),)
	$(error Set BOOK, e.g. make audiobook-dry-run BOOK=book-01-vanishing-signal)
endif
	python scripts/generate_audiobook_tts.py $(BOOK) --dry-run --voice $(VOICE)

audiobook-tts:
ifeq ($(strip $(BOOK)),)
	$(error Set BOOK, e.g. make audiobook-tts BOOK=book-01-vanishing-signal)
endif
	python scripts/generate_audiobook_tts.py $(BOOK) --voice $(VOICE)
