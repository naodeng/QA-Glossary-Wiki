#!/usr/bin/env python3
"""
Interactive Translation Helper
This script helps translate articles one by one using an AI assistant interactively.
"""

import os
import sys
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent
SECTIONS_DIR = REPO_ROOT / "Sections"
SECTIONS_ZH_DIR = REPO_ROOT / "Sections-zh"
TRANSLATION_PROMPT_PATH = Path.home() / "awsomeCode/AI-QA-Tools/Reference/translate-to-chinese-qa.md"

def load_translation_prompt():
    """Load the translation prompt."""
    with open(TRANSLATION_PROMPT_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def get_next_article_to_translate():
    """Get the next article that needs translation."""
    for letter_dir in sorted(SECTIONS_DIR.iterdir()):
        if not letter_dir.is_dir():
            continue
        
        for article_file in sorted(letter_dir.glob("*.md")):
            relative_path = article_file.relative_to(SECTIONS_DIR)
            zh_file = SECTIONS_ZH_DIR / relative_path
            
            # Check if already translated
            if not zh_file.exists():
                return article_file, relative_path
    
    return None, None

def display_article_for_translation(article_file, relative_path):
    """Display article content for translation."""
    with open(article_file, 'r', encoding='utf-8') as f:
        english_content = f.read()
    
    prompt = load_translation_prompt()
    
    print("=" * 80)
    print(f"NEXT ARTICLE TO TRANSLATE: {relative_path}")
    print("=" * 80)
    print()
    print("TRANSLATION PROMPT:")
    print("-" * 80)
    print(prompt)
    print()
    print("=" * 80)
    print("ENGLISH CONTENT:")
    print("=" * 80)
    print(english_content)
    print()
    print("=" * 80)
    print(f"When translated, save to: {SECTIONS_ZH_DIR / relative_path}")
    print("=" * 80)

def main():
    """Main entry point."""
    article_file, relative_path = get_next_article_to_translate()
    
    if article_file is None:
        print("✓ All articles have been translated!")
        return
    
    display_article_for_translation(article_file, relative_path)

if __name__ == "__main__":
    main()
