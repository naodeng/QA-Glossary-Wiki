#!/usr/bin/env python3
"""
QA Glossary Translation Script
Translates English QA glossary articles to Chinese using AI assistance.
"""

import os
import sys
import json
import time
import re
import urllib.parse
from pathlib import Path
from typing import List, Dict, Tuple

import requests

# Configuration
REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "state"
STATE_DIR.mkdir(exist_ok=True)
SECTIONS_DIR = REPO_ROOT / "Sections"
SECTIONS_ZH_DIR = REPO_ROOT / "Sections-zh"
TRANSLATION_PROMPT_PATH = Path.home() / "awsomeCode/AI-QA-Tools/Reference/translate-to-chinese-qa.md"
PROGRESS_FILE = STATE_DIR / "translation_progress.json"
LEGACY_PROGRESS_FILE = REPO_ROOT / "translation_progress.json"

# AI API Configuration (user will need to set these)
USE_AI_API = os.getenv("USE_AI_API", "false").lower() == "true"
AI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4")
USE_FREE_TRANSLATE = os.getenv("USE_FREE_TRANSLATE", "true").lower() == "true"
FREE_TRANSLATE_LINE_DELAY = float(os.getenv("FREE_TRANSLATE_LINE_DELAY", "0"))

# Terms that should stay in English in translated output.
NO_TRANSLATE_TERMS = [
    "API", "Appium", "Applitools", "BDD", "BrowserStack", "Bugzilla", "Chai.js",
    "Chrome", "CI/CD", "Cucumber", "Cypress", "DOM", "Edge", "Electron",
    "Firefox", "Gherkin", "GitHub", "GitLab", "GraphQL", "iOS", "Jasmine",
    "Java", "JavaScript", "Jest", "Jira", "JMeter", "JUnit", "KPI", "Mantis",
    "Node.js", "npm", "NUnit", "Percy", "Playwright", "Postman", "Puppeteer",
    "Python", "REST", "Ruby", "Selenium", "SPA", "SpecFlow", "SQL", "Swagger",
    "Trello", "TestCafe", "TestNG", "TypeScript", "URL", "WebDriver", "Xray",
]


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
        if LEGACY_PROGRESS_FILE.exists():
            with open(LEGACY_PROGRESS_FILE, 'r', encoding='utf-8') as f:
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

    def _translate_text_free_once(self, text: str) -> str:
        """Translate plain text via free no-key endpoint (single attempt)."""
        q = urllib.parse.quote(text)
        url = (
            "https://translate.googleapis.com/translate_a/single"
            f"?client=gtx&sl=en&tl=zh-CN&dt=t&q={q}"
        )
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return "".join(part[0] for part in data[0] if part and part[0])

    def _split_for_retry(self, text: str, max_chars: int = 320) -> List[str]:
        """Split text into smaller chunks, preserving line boundaries."""
        lines = text.splitlines(keepends=True)
        chunks: List[str] = []
        buf = ""
        for line in lines:
            if len(buf) + len(line) > max_chars and buf:
                chunks.append(buf)
                buf = line
            else:
                buf += line
        if buf:
            chunks.append(buf)
        return chunks

    def _translate_text_free(self, text: str) -> str:
        """Translate plain text with retries and chunk fallback."""
        if not text.strip():
            return text

        # Try direct translation with backoff first.
        last_err = None
        for attempt in range(3):
            try:
                return self._translate_text_free_once(text)
            except Exception as e:
                last_err = e
                time.sleep(0.5 * (attempt + 1))

        # Fallback: split into smaller chunks and translate piece by piece.
        chunks = self._split_for_retry(text)
        if len(chunks) <= 1:
            raise last_err if last_err else RuntimeError("free translation failed")

        translated_chunks: List[str] = []
        for chunk in chunks:
            chunk = chunk or ""
            if not chunk.strip():
                translated_chunks.append(chunk)
                continue

            ok = False
            chunk_err = None
            for attempt in range(3):
                try:
                    translated_chunks.append(self._translate_text_free_once(chunk))
                    ok = True
                    break
                except Exception as e:
                    chunk_err = e
                    time.sleep(0.4 * (attempt + 1))

            if not ok:
                # If still failing and chunk is long, split once more recursively.
                if len(chunk) > 120:
                    subparts = self._split_for_retry(chunk, max_chars=120)
                    if len(subparts) > 1:
                        translated_sub = [self._translate_text_free(sub) for sub in subparts]
                        translated_chunks.append("".join(translated_sub))
                        continue
                raise chunk_err if chunk_err else RuntimeError("chunk translation failed")

        return "".join(translated_chunks)

    def _protect_inline_markdown(self, text: str) -> tuple[str, Dict[str, str]]:
        """Protect inline markdown tokens from translation."""
        token_map: Dict[str, str] = {}

        def repl(pattern: str, source: str) -> str:
            def _inner(match):
                key = f"@@PROTECTED_{len(token_map)}@@"
                token_map[key] = match.group(0)
                return key
            return re.sub(pattern, _inner, source)

        protected = text
        # Inline code spans
        protected = repl(r"`[^`\n]+`", protected)
        # Markdown links and images
        protected = repl(r"!?\[[^\]]*\]\([^)]+\)", protected)
        # Raw URLs
        protected = repl(r"https?://\S+", protected)
        # Keep tool/product names unchanged.
        for term in sorted(NO_TRANSLATE_TERMS, key=len, reverse=True):
            pattern = rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])"
            protected = repl(pattern, protected)
        return protected, token_map

    def _restore_inline_markdown(self, text: str, token_map: Dict[str, str]) -> str:
        restored = text
        for key, value in token_map.items():
            restored = restored.replace(key, value)
        return restored

    def _translate_markdown_line_free(self, line: str) -> str:
        """Translate one markdown line while preserving syntax prefix and inline tokens."""
        if not line.strip():
            return line

        stripped = line.strip()
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            return line

        # Keep table separators and TOC bullets untouched.
        if re.fullmatch(r"\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*", line):
            return line
        if stripped.startswith("- [") and "](#" in stripped:
            return line

        # Preserve markdown structural prefix.
        m = re.match(r"^(\s*(?:>+\s+)?(?:#{1,6}\s+|[-*+]\s+|\d+\.\s+)?)(.*?)(\s*)$", line)
        if not m:
            return line
        prefix, body, suffix = m.groups()
        if not body.strip():
            return line

        protected, token_map = self._protect_inline_markdown(body)
        translated = self._translate_text_free(protected)
        restored = self._restore_inline_markdown(translated, token_map)
        return f"{prefix}{restored}{suffix}"

    def translate_article_with_free_api(self, english_content: str) -> str:
        """Translate markdown while preserving fenced code blocks and inline markdown tokens."""
        # Split content into non-fence / fence chunks using a line scanner so
        # indented fences are preserved exactly.
        chunks: List[tuple[str, str]] = []
        buf: List[str] = []
        fence_buf: List[str] = []
        in_fence = False
        fence_char = ""
        fence_len = 0

        for line in english_content.splitlines(keepends=True):
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if m:
                marker = m.group(1)
                marker_char = marker[0]
                marker_len = len(marker)

                if not in_fence:
                    if buf:
                        chunks.append(("text", "".join(buf)))
                        buf = []
                    in_fence = True
                    fence_char = marker_char
                    fence_len = marker_len
                    fence_buf.append(line)
                    continue

                if marker_char == fence_char and marker_len >= fence_len:
                    fence_buf.append(line)
                    chunks.append(("fence", "".join(fence_buf)))
                    fence_buf = []
                    in_fence = False
                    fence_char = ""
                    fence_len = 0
                    continue

            if in_fence:
                fence_buf.append(line)
            else:
                buf.append(line)

        if in_fence and fence_buf:
            # Unclosed fence: keep as-is to avoid data loss.
            chunks.append(("fence", "".join(fence_buf)))
        if buf:
            chunks.append(("text", "".join(buf)))

        out_segments: List[str] = []
        for kind, seg in chunks:
            if kind == "fence":
                out_segments.append(seg)
                continue

            protected, token_map = self._protect_inline_markdown(seg)
            parts = re.split(r"(\n\s*\n+)", protected)
            translated_parts: List[str] = []
            for part in parts:
                if not part:
                    continue
                if re.fullmatch(r"\n\s*\n+", part):
                    translated_parts.append(part)
                    continue
                translated_parts.append(self._translate_text_free(part))
                if FREE_TRANSLATE_LINE_DELAY > 0:
                    time.sleep(FREE_TRANSLATE_LINE_DELAY)

            translated = "".join(translated_parts)
            out_segments.append(self._restore_inline_markdown(translated, token_map))

        return "".join(out_segments)
    
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

            elif mode == "free":
                print(f"🌐 Translating {relative_path} with no-key API...")
                chinese_content = self.translate_article_with_free_api(english_content)
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(chinese_content)
                print(f"✓ Translated {relative_path}")
                self.progress["translated"].append(str(relative_path))
                self._save_progress()
                time.sleep(0.4)
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
    elif USE_FREE_TRANSLATE:
        mode = "free"
        print("\n🌐 Free translation mode enabled (no key)")
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
