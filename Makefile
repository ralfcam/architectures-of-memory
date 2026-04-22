# Merge all chapters under a book-NN-* directory into one Markdown file.
# Requires GNU Make and Python 3 on PATH.
#
# Examples:
#   make merge BOOK=book-01-vanishing-signal PREFIX=vanishing-signal
#   make merge-audiobook BOOK=book-01-vanishing-signal PREFIX=vanishing-signal

.PHONY: merge merge-audiobook merge-help

BOOK ?=
PREFIX ?=

_MERGE_EXTRA = $(if $(strip $(PREFIX)),--prefix $(PREFIX),)

merge-help:
	@echo Usage:
	@echo   make merge BOOK=book-01-vanishing-signal
	@echo   make merge BOOK=book-01-vanishing-signal PREFIX=vanishing-signal
	@echo   make merge-audiobook BOOK=book-01-vanishing-signal

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
