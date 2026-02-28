#!/usr/bin/env python3
"""Backward-compatible entrypoint for scripts/scraper.py."""
from runpy import run_path
from pathlib import Path

if __name__ == "__main__":
    run_path(str(Path(__file__).resolve().parent / "scripts" / "scraper.py"), run_name="__main__")
