#!/usr/bin/env python3
"""Delegates to root scripts/five_rule_check.py."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT_SCRIPT = Path(__file__).resolve().parents[3] / "scripts" / "five_rule_check.py"
if __name__ == "__main__":
    sys.argv[0] = str(ROOT_SCRIPT)
    runpy.run_path(str(ROOT_SCRIPT), run_name="__main__")
