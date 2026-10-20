---
name: audiobook-tts
description: >-
  Compiles TTS-ready chapter transcripts and synthesizes audiobook audio files using
  Gemini Audio / TTS. Use when the user asks to generate audiobook audio, estimate
  audiobook duration, or run text-to-speech on book chapters.
---

# Audiobook TTS Pipeline

## Steps

1. **Merge Audiobook Transcript:**
   ```powershell
   python scripts/merge_book_chapters.py book-01-vanishing-signal --audiobook --prefix vanishing-signal
   ```
2. **Dry-Run & Duration Estimate (No API Call):**
   Inspect word counts, TTS chunks, and estimated speaking duration per chapter:
   ```powershell
   python scripts/generate_audiobook_tts.py book-01-vanishing-signal --dry-run
   ```
3. **Synthesize Chapter Audio (Requires `GEMINI_API_KEY`):**
   Synthesize `.wav` files for a specific chapter or the full book into `book-0X-*/audiobook/`:
   ```powershell
   python scripts/generate_audiobook_tts.py book-01-vanishing-signal --chapter 01 --voice Kore
   ```
