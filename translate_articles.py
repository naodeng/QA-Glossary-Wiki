#!/usr/bin/env python3
"""
QA Glossary Translation Script
Translates English QA glossary articles to Chinese using AI assistance.
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import List, Dict, Tuple

# Configuration
REPO_ROOT = Path(__file__).parent
SECTIONS_DIR = REPO_ROOT / "Sections"
SECTIONS_ZH_DIR = REPO_ROOT / "Sections-zh"
TRANSLATION_PROMPT_PATH = Path.home() / "awsomeCode/AI-QA-Tools/Reference/translate-to-chinese-qa.md"
PROGRESS_FILE = REPO_ROOT / "translation_progress.json"

# AI API Configuration (user will need to set these)
USE_AI_API = os.getenv("USE_AI_API", "false").lower() == "true"
AI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4")


class TranslationManager:
    """Manages the translation process for QA glossary articles."""
    
    def __init__(self):
        self.translation_prompt = self._load_translation_prompt()
        self.progress = self._load_progress()
        
    def _load_translation_prompt(self) -> str:
        """Load the translation prompt template."""
        if not TRANSLATION_PROMPT_PATH.exists():
            print(f"Error: Translation prompt not found at {TRANSLATION_PROMPT_PATH}")
            sys.exit(1)
        
        with open(TRANSLATION_PROMPT_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _load_progress(self) -> Dict:
        """Load translation progress from file."""
        if PROGRESS_FILE.exists():
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"translated": [], "failed": [], "skipped": []}
    
    def _save_progress(self):
        """Save translation progress to file."""
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)
    
    def get_all_articles(self) -> List[Tuple[str, Path]]:
        """Get list of all English articles to translate."""
        articles = []
        
        for letter_dir in sorted(SECTIONS_DIR.iterdir()):
            if not letter_dir.is_dir():
                continue
            
            for article_file in sorted(letter_dir.glob("*.md")):
                relative_path = article_file.relative_to(SECTIONS_DIR)
                articles.append((str(relative_path), article_file))
        
        return articles
    
    def create_directory_structure(self):
        """Create Chinese translation directory structure."""
        print("Creating directory structure...")
        SECTIONS_ZH_DIR.mkdir(exist_ok=True)
        
        for letter_dir in SECTIONS_DIR.iterdir():
            if letter_dir.is_dir():
                zh_letter_dir = SECTIONS_ZH_DIR / letter_dir.name
                zh_letter_dir.mkdir(exist_ok=True)
        
        print(f"✓ Created {SECTIONS_ZH_DIR}")
    
    def translate_article_with_ai(self, english_content: str) -> str:
        """Translate article using AI API."""
        if not USE_AI_API or not AI_API_KEY:
            raise Exception("AI API not configured")
        
        try:
            import openai
            openai.api_key = AI_API_KEY
            
            # Combine prompt and content
            full_prompt = f"{self.translation_prompt}\n\n{english_content}"
            
            response = openai.ChatCompletion.create(
                model=AI_MODEL,
                messages=[
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.3,
                max_tokens=16000
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            raise Exception(f"AI translation failed: {str(e)}")
    
    def prepare_manual_translation(self, relative_path: str, english_content: str) -> str:
        """Prepare article for manual translation."""
        separator = "=" * 80
        return f"""
{separator}
FILE: {relative_path}
{separator}

TRANSLATION PROMPT:
{self.translation_prompt}

{separator}
ENGLISH CONTENT TO TRANSLATE:
{separator}

{english_content}

{separator}
PASTE CHINESE TRANSLATION BELOW:
{separator}

"""
    
    def translate_article(self, relative_path: str, source_file: Path, 
                         mode: str = "manual") -> bool:
        """Translate a single article."""
        
        # Check if already translated
        if str(relative_path) in self.progress["translated"]:
            print(f"⊘ Skipping {relative_path} (already translated)")
            return True
        
        # Read English content
        with open(source_file, 'r', encoding='utf-8') as f:
            english_content = f.read()
        
        # Determine output path
        output_file = SECTIONS_ZH_DIR / relative_path
        
        try:
            if mode == "ai" and USE_AI_API:
                print(f"🤖 Translating {relative_path} with AI...")
                chinese_content = self.translate_article_with_ai(english_content)
                
                # Save translation
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(chinese_content)
                
                print(f"✓ Translated {relative_path}")
                self.progress["translated"].append(str(relative_path))
                self._save_progress()
                
                # Rate limiting
                time.sleep(2)
                return True
            
            elif mode == "manual":
                # Prepare for manual translation
                manual_content = self.prepare_manual_translation(
                    relative_path, english_content
                )
                
                # Save to a temporary file for manual processing
                temp_file = REPO_ROOT / f"manual_translation_{relative_path.replace('/', '_')}.txt"
                with open(temp_file, 'w', encoding='utf-8') as f:
                    f.write(manual_content)
                
                print(f"📝 Prepared {relative_path} for manual translation: {temp_file}")
                self.progress["skipped"].append(str(relative_path))
                self._save_progress()
                return True
            
            else:
                print(f"⚠ Skipping {relative_path} (no translation method available)")
                self.progress["skipped"].append(str(relative_path))
                self._save_progress()
                return False
        
        except Exception as e:
            print(f"✗ Failed to translate {relative_path}: {str(e)}")
            self.progress["failed"].append({
                "file": str(relative_path),
                "error": str(e)
            })
            self._save_progress()
            return False
    
    def translate_all(self, mode: str = "manual", limit: int = None):
        """Translate all articles."""
        articles = self.get_all_articles()
        total = len(articles)
        
        if limit:
            articles = articles[:limit]
            print(f"Limiting to first {limit} articles for testing")
        
        print(f"\nFound {total} articles to translate")
        print(f"Mode: {mode}")
        print(f"Already translated: {len(self.progress['translated'])}")
        print(f"Failed: {len(self.progress['failed'])}")
        print("-" * 80)
        
        success_count = 0
        for i, (relative_path, source_file) in enumerate(articles, 1):
            print(f"\n[{i}/{len(articles)}] Processing {relative_path}...")
            
            if self.translate_article(relative_path, source_file, mode):
                success_count += 1
        
        print("\n" + "=" * 80)
        print("TRANSLATION SUMMARY")
        print("=" * 80)
        print(f"Total articles: {total}")
        print(f"Processed: {len(articles)}")
        print(f"Successfully translated: {len(self.progress['translated'])}")
        print(f"Failed: {len(self.progress['failed'])}")
        print(f"Skipped: {len(self.progress['skipped'])}")
        print("=" * 80)
        
        if self.progress['failed']:
            print("\nFailed translations:")
            for item in self.progress['failed']:
                print(f"  - {item['file']}: {item['error']}")
    
    def verify_translations(self):
        """Verify that translations maintain markdown structure."""
        print("\nVerifying translations...")
        issues = []
        
        for relative_path in self.progress["translated"]:
            zh_file = SECTIONS_ZH_DIR / relative_path
            
            if not zh_file.exists():
                issues.append(f"Missing file: {relative_path}")
                continue
            
            with open(zh_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic checks
            if len(content) < 100:
                issues.append(f"Suspiciously short: {relative_path}")
            
            # Check for code blocks (should be preserved)
            en_file = SECTIONS_DIR / relative_path
            with open(en_file, 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            en_code_blocks = en_content.count("```")
            zh_code_blocks = content.count("```")
            
            if en_code_blocks != zh_code_blocks:
                issues.append(f"Code block mismatch in {relative_path}: EN={en_code_blocks}, ZH={zh_code_blocks}")
        
        if issues:
            print("\n⚠ Issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✓ All translations verified successfully")


def main():
    """Main entry point."""
    print("QA Glossary Translation Tool")
    print("=" * 80)
    
    manager = TranslationManager()
    
    # Create directory structure
    manager.create_directory_structure()
    
    # Determine mode
    if USE_AI_API and AI_API_KEY:
        mode = "ai"
        print("\n🤖 AI API mode enabled")
    else:
        mode = "manual"
        print("\n📝 Manual translation mode")
        print("To use AI API, set environment variables:")
        print("  export USE_AI_API=true")
        print("  export OPENAI_API_KEY=your-key-here")
        print("  export AI_MODEL=gpt-4  # optional")
    
    # Check for command line arguments
    limit = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            limit = 5
            print("\n🧪 Test mode: translating first 5 articles only")
        elif sys.argv[1] == "--verify":
            manager.verify_translations()
            return
        elif sys.argv[1] == "--help":
            print("""
Usage:
  python translate_articles.py           # Translate all articles
  python translate_articles.py --test    # Translate first 5 articles (testing)
  python translate_articles.py --verify  # Verify existing translations
  python translate_articles.py --help    # Show this help
            """)
            return
    
    # Run translation
    manager.translate_all(mode=mode, limit=limit)
    
    # Verify if in AI mode
    if mode == "ai":
        manager.verify_translations()


if __name__ == "__main__":
    main()
