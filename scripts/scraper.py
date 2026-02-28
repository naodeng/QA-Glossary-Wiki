#!/usr/bin/env python3
"""
QA Glossary Wiki Scraper
Scrapes articles from https://ray.run/wiki and organizes them alphabetically
"""

import logging
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import os
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

try:
    from progress_tracker import ProgressTracker
except ModuleNotFoundError:
    class ProgressTracker:  # type: ignore[override]
        """Fallback tracker when progress_tracker.py is unavailable."""

        def is_done(self, slug, stage):
            return False

        def mark_done(self, slug, stage):
            return None

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "state"
STATE_DIR.mkdir(exist_ok=True)

# Error logger — writes to state/sync_error.log
_error_logger = logging.getLogger("scraper")
if not _error_logger.handlers:
    _handler = logging.FileHandler(
        STATE_DIR / "sync_error.log", encoding="utf-8"
    )
    _handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(levelname)s] [scraper] %(message)s",
                          datefmt="%Y-%m-%dT%H:%M:%SZ")
    )
    _error_logger.addHandler(_handler)
    _error_logger.setLevel(logging.ERROR)

BASE_URL = "https://ray.run/wiki"
OUTPUT_DIR = REPO_ROOT / "Sections"
SKIP_TAGS = {
    "script",
    "style",
    "noscript",
    "svg",
    "button",
    "form",
    "input",
    "textarea",
    "select",
    "option",
}
WRAPPER_TAGS = {"div", "section", "article", "main", "li", "dl", "dt", "dd", "figure"}
TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"

def get_article_links():
    """Extract all article links from the wiki index page"""
    print(f"Fetching index page: {BASE_URL}")
    response = requests.get(BASE_URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all links to wiki articles
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and href != '/wiki':
            full_url = urljoin(BASE_URL, href)
            title = link.get_text(strip=True)
            links.append({
                'url': full_url,
                'title': title,
                'slug': href.split('/')[-1]
            })
    
    # Remove duplicates
    seen = set()
    unique_links = []
    for link in links:
        if link['url'] not in seen:
            seen.add(link['url'])
            unique_links.append(link)
    
    print(f"Found {len(unique_links)} unique articles")
    return unique_links

def get_remote_slugs() -> set:
    """Return a set of unique slugs from the wiki index page.
    
    Reuses get_article_links() logic to fetch and deduplicate all article slugs.
    Raises an exception with a descriptive message on network failure.
    """
    try:
        articles = get_article_links()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch remote article list: {e}") from e

    slugs = {article['slug'] for article in articles}
    print(f"Discovered {len(slugs)} unique article slugs")
    return slugs


def fetch_missing(slugs: list, tracker: ProgressTracker) -> tuple:
    """Fetch and save articles for the given slugs, skipping already-completed ones.

    Args:
        slugs: List of article slugs to process.
        tracker: ProgressTracker instance used to skip and record completed slugs.

    Returns:
        (success_count, fail_count) tuple.
    """
    success_count = 0
    fail_count = 0

    for idx, slug in enumerate(slugs, 1):
        if tracker.is_done(slug, "en_sync"):
            print(f"[{idx}/{len(slugs)}] Skipping (already done): {slug}")
            continue

        print(f"[{idx}/{len(slugs)}] Fetching: {slug}")
        url = f"{BASE_URL}/{slug}"
        # Use slug as fallback title (hyphens → spaces, title-cased)
        title = slug.replace("-", " ").title()

        try:
            markdown = scrape_article(url, title, slug)
            if markdown is None:
                raise RuntimeError(f"scrape_article returned None for slug '{slug}'")

            save_article(markdown, title, slug)
            tracker.mark_done(slug, "en_sync")
            success_count += 1
        except Exception as exc:
            fail_count += 1
            _error_logger.error("Failed to fetch '%s': %s", slug, exc)
            print(f"  [ERROR] {slug}: {exc}")

        # Polite delay between requests (skip after the last item)
        if idx < len(slugs):
            time.sleep(1)

    print(f"\nfetch_missing complete — success: {success_count}, failed: {fail_count}")
    return success_count, fail_count


def get_first_letter(title):
    """Get the first letter of the title for folder organization"""
    # Remove special characters and get first alphanumeric character
    clean_title = re.sub(r'^[^a-zA-Z0-9]+', '', title)
    if clean_title:
        return clean_title[0].upper()
    return 'Other'

def scrape_article(url, title, slug):
    """Scrape a single article and convert to markdown"""
    print(f"Scraping: {title}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to find the main content area
        # This may need adjustment based on the actual HTML structure
        content = soup.find('article') or soup.find('main') or soup.find('div', class_=re.compile(r'content|article|post'))
        
        if not content:
            # Fallback: get the body
            content = soup.find('body')
        
        # Convert HTML to markdown-like format
        markdown = convert_to_markdown(content, title, slug)
        
        return markdown
        
    except Exception as e:
        print(f"Error scraping {title}: {e}")
        return None

def _collapse_ws(text: str) -> str:
    """Normalize whitespace while keeping intentional line breaks."""
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text


def _get_slug_from_href(href: str) -> str | None:
    """Extract wiki slug from '/wiki/<slug>' and '/glossary/<slug>' style paths."""
    if not href:
        return None
    href = href.strip()
    if href.startswith("http://") or href.startswith("https://"):
        return None

    clean = href.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    match = re.match(r"^/(?:wiki|glossary)/([^/]+)$", clean)
    if not match:
        return None
    return match.group(1)


def _slug_to_relative_md(slug: str) -> str:
    first = get_first_letter(slug.replace("-", " "))
    return f"../{first}/{slug}.md"


def normalize_href(href: str) -> str:
    """Normalize link target to absolute web URL or local relative markdown path."""
    if not href:
        return ""
    href = href.strip()
    if href.startswith("#"):
        return href
    if href.startswith("//"):
        return f"https:{href}"
    if href.startswith("http://") or href.startswith("https://"):
        return href

    slug = _get_slug_from_href(href)
    if slug:
        return _slug_to_relative_md(slug)

    if href.startswith("/"):
        return urljoin("https://ray.run", href)
    return href


def _render_inline(node) -> str:
    """Render inline HTML node to markdown."""
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    if node.name in SKIP_TAGS:
        return ""
    if node.get("aria-hidden") == "true" or node.has_attr("hidden"):
        return ""

    name = node.name.lower()
    if name == "br":
        return "  \n"

    if name == "a":
        href = normalize_href(node.get("href", ""))
        text = _collapse_ws("".join(_render_inline(c) for c in node.children)).strip()
        if not text:
            text = href
        if href:
            return f"[{text}]({href})"
        return text

    if name in {"strong", "b"}:
        text = _collapse_ws("".join(_render_inline(c) for c in node.children)).strip()
        return f"**{text}**" if text else ""

    if name in {"em", "i"}:
        text = _collapse_ws("".join(_render_inline(c) for c in node.children)).strip()
        return f"*{text}*" if text else ""

    if name == "code":
        if node.parent and node.parent.name and node.parent.name.lower() == "pre":
            return ""
        text = _collapse_ws(node.get_text(" ", strip=True))
        return f"`{text}`" if text else ""

    if name == "img":
        src = normalize_href(node.get("src", ""))
        alt = _collapse_ws(node.get("alt", "")).strip()
        return f"![{alt}]({src})" if src else ""

    return "".join(_render_inline(c) for c in node.children)


def _render_list(tag: Tag, depth: int = 0) -> list[str]:
    """Render ul/ol recursively with stable indentation."""
    lines: list[str] = []
    ordered = tag.name.lower() == "ol"
    index = 1
    for li in tag.find_all("li", recursive=False):
        nested_tags: list[Tag] = []
        for nested in li.find_all(["ul", "ol"]):
            nearest_li = nested.find_parent("li")
            if nearest_li is not li:
                continue
            parent_list = nested.find_parent(["ul", "ol"])
            if parent_list and parent_list.find_parent("li") is li:
                # Skip deeper nested lists here; outer recursive call will include them.
                continue
            nested_tags.append(nested)

        item_lines: list[str] = []
        extra_lines: list[str] = []
        for child in li.children:
            if isinstance(child, NavigableString):
                txt = _collapse_ws(str(child)).strip()
                if txt:
                    item_lines.append(txt)
                continue
            if not isinstance(child, Tag):
                continue

            name = child.name.lower()
            if name in {"ul", "ol"}:
                nested_tags.append(child)
                continue

            if name == "details":
                summary = child.find("summary")
                if summary:
                    summary_text = _collapse_ws(
                        "".join(_render_inline(c) for c in summary.children)
                    ).strip()
                    if summary_text:
                        item_lines.append(summary_text)

                for grand in child.children:
                    if isinstance(grand, Tag) and grand.name and grand.name.lower() == "summary":
                        continue
                    if isinstance(grand, Tag):
                        extra_lines.extend(_render_blocks(grand, ""))
                    else:
                        txt = _collapse_ws(str(grand)).strip()
                        if txt:
                            extra_lines.append(txt)
                continue

            if name in {"p", "div", "section", "article", "figure"}:
                txt = _collapse_ws("".join(_render_inline(c) for c in child.children)).strip()
                if txt:
                    item_lines.append(txt)
                continue

            if name == "pre":
                code_tag = child.find("code")
                lang = ""
                code_text = child.get_text("\n", strip=False).strip("\n")
                if code_tag:
                    classes = " ".join(code_tag.get("class", []))
                    lang_match = re.search(r"language-([a-zA-Z0-9_+-]+)", classes)
                    if lang_match:
                        lang = lang_match.group(1)
                    code_text = code_tag.get_text("\n", strip=False).strip("\n")
                extra_lines.append(f"```{lang}\n{code_text.rstrip()}\n```")
                continue

            txt = _collapse_ws(_render_inline(child)).strip()
            if txt:
                item_lines.append(txt)

        if item_lines:
            normalized_lines: list[str] = []
            for seg in item_lines:
                if normalized_lines and seg.lstrip().startswith(":"):
                    normalized_lines[-1] = f"{normalized_lines[-1]} {seg.lstrip()}"
                else:
                    normalized_lines.append(seg)
            item_lines = normalized_lines

            first_line = item_lines[0]
            q_idx = first_line.find("?")
            if 0 < q_idx < 140 and q_idx < len(first_line) - 1:
                question = first_line[: q_idx + 1].strip()
                answer = first_line[q_idx + 1 :].strip()
                if question and answer:
                    item_lines = [question, answer] + item_lines[1:]

            prefix = f"{index}. " if ordered else "- "
            lines.append(f"{'  ' * depth}{prefix}{item_lines[0]}")
            for extra in item_lines[1:]:
                lines.append(f"{'  ' * depth}  {extra}")
            for extra in extra_lines:
                if extra and extra.strip():
                    for sub in str(extra).splitlines():
                        lines.append(f"{'  ' * depth}  {sub}")

        for nested in nested_tags:
            lines.extend(_render_list(nested, depth + 1))

        if ordered:
            index += 1
    return lines


def _render_table(table: Tag) -> list[str]:
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        row = [_collapse_ws("".join(_render_inline(c) for c in cell.children)).strip()
               for cell in cells]
        if any(row):
            rows.append(row)
    if not rows:
        return []

    col_count = max(len(r) for r in rows)
    padded = [r + [""] * (col_count - len(r)) for r in rows]
    header = padded[0]
    separator = ["---"] * col_count
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in padded[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def _render_blocks(root: Tag, title: str) -> list[str]:
    lines: list[str] = []

    for child in root.children:
        if isinstance(child, NavigableString):
            text = _collapse_ws(str(child)).strip()
            if text:
                lines.append(text)
            continue

        if not isinstance(child, Tag):
            continue
        if child.name in SKIP_TAGS:
            continue
        if child.get("aria-hidden") == "true" or child.has_attr("hidden"):
            continue

        name = child.name.lower()

        if name in WRAPPER_TAGS:
            lines.extend(_render_blocks(child, title))
            continue

        cls = " ".join(child.get("class", []))
        if re.search(r"(sidebar|breadcrumb|share|social|cookie|consent|menu|nav)", cls, re.I):
            continue

        child_id = child.get("id", "")
        if child_id and re.search(r"(sidebar|breadcrumb|share|social|cookie|consent|menu|nav)",
                                  child_id, re.I):
            continue

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            text = _collapse_ws("".join(_render_inline(c) for c in child.children)).strip()
            if not text:
                continue
            if name == "h1" and text == title:
                continue
            lines.append(f"{'#' * int(name[1])} {text}")
            continue

        if name == "p":
            text = _collapse_ws("".join(_render_inline(c) for c in child.children)).strip()
            if text:
                lines.append(text)
            continue

        if name in {"ul", "ol"}:
            list_lines = _render_list(child)
            if list_lines:
                lines.extend(list_lines)
            continue

        if name == "details":
            summary = child.find("summary")
            summary_text = ""
            if summary:
                summary_text = _collapse_ws(
                    "".join(_render_inline(c) for c in summary.children)
                ).strip()
            if summary_text:
                lines.append(f"- {summary_text}")

            body_parts: list[str] = []
            for grand in child.children:
                if isinstance(grand, Tag) and grand.name and grand.name.lower() == "summary":
                    continue
                if isinstance(grand, Tag):
                    body_parts.extend(_render_blocks(grand, title))
                else:
                    text = _collapse_ws(str(grand)).strip()
                    if text:
                        body_parts.append(text)

            for body in body_parts:
                if body:
                    lines.append(body)
            continue

        if name == "pre":
            code_tag = child.find("code")
            lang = ""
            code_text = child.get_text("\n", strip=False).strip("\n")
            if code_tag:
                classes = " ".join(code_tag.get("class", []))
                lang_match = re.search(r"language-([a-zA-Z0-9_+-]+)", classes)
                if lang_match:
                    lang = lang_match.group(1)
                code_text = code_tag.get_text("\n", strip=False).strip("\n")
            lines.append(f"```{lang}\n{code_text.rstrip()}\n```")
            continue

        if name == "blockquote":
            quote_lines = _render_blocks(child, title)
            if not quote_lines:
                text = _collapse_ws("".join(_render_inline(c) for c in child.children)).strip()
                if text:
                    quote_lines = [text]
            lines.extend([f"> {line}" for line in quote_lines if line.strip()])
            continue

        if name == "table":
            table_lines = _render_table(child)
            if table_lines:
                lines.extend(table_lines)
            continue

        if name == "hr":
            lines.append("---")
            continue

        # Generic fallback for unhandled tags that may still carry visible content.
        text = _collapse_ws("".join(_render_inline(c) for c in child.children)).strip()
        if text:
            lines.append(text)

    return lines


def _is_list_line(line: str) -> bool:
    return bool(re.match(r"^\s*(?:- |\d+\. )", line))


def _is_table_line(line: str) -> bool:
    return line.startswith("| ")


def _is_quote_line(line: str) -> bool:
    return line.startswith("> ")


def _is_continuation_line(line: str) -> bool:
    return line.startswith("  ") and not _is_list_line(line) and not _is_table_line(line)


def _is_heading_line(line: str) -> bool:
    return bool(re.match(r"^#{1,6}\s+", line))


def _is_fence_line(line: str) -> bool:
    return bool(re.match(r"^\s*(```|~~~)", line))


def _clean_and_group_lines(lines: list[str]) -> list[str]:
    """Remove UI noise and keep Q&A answer paragraphs inside their list item."""
    cleaned: list[str] = []
    in_fence = False
    qa_continuation = False
    last_heading_level = 1
    seen_heading = False
    in_questions_section = False

    for raw in lines:
        for part in raw.splitlines():
            line = part.rstrip()

            if _is_fence_line(line):
                in_fence = not in_fence
                cleaned.append(line)
                qa_continuation = False
                continue

            if in_fence:
                # Preserve code block content exactly, including blank lines/indentation.
                cleaned.append(line)
                continue

            stripped = line.strip()
            if not stripped:
                continue

            # Remove obvious non-content UI artifacts from page chrome.
            if stripped in {"Thank you!", "Was this helpful?", "$/$", "$", "/$"}:
                continue

            if _is_heading_line(line) or line == "---":
                qa_continuation = False
                if _is_heading_line(line):
                    m = re.match(r"^(#{1,6})\s+(.*)$", line)
                    if m:
                        raw_level = len(m.group(1))
                        heading_text = m.group(2).strip()
                        adjusted_level = raw_level
                        if seen_heading and raw_level > last_heading_level + 1:
                            adjusted_level = last_heading_level + 1
                            line = re.sub(r"^#{1,6}", "#" * adjusted_level, line, count=1)

                        # Standardize hierarchy under "Questions about ...":
                        #   ## Questions...
                        #   ### Category
                        #   #### Question?
                        if heading_text.lower().startswith("questions about"):
                            adjusted_level = 2
                            in_questions_section = True
                            line = f"{'#' * adjusted_level} {heading_text}"
                        elif in_questions_section and adjusted_level >= 3:
                            adjusted_level = 4 if heading_text.endswith("?") else 3
                            line = f"{'#' * adjusted_level} {heading_text}"

                        last_heading_level = adjusted_level
                        seen_heading = True
                cleaned.append(line)
                continue

            if _is_list_line(line):
                list_text = re.sub(r"^\s*(?:- |\d+\. )", "", line).strip()
                # FAQ-style top-level question lines are headings, not list bullets.
                if line.startswith("- ") and list_text.endswith("?"):
                    question_level = 4 if in_questions_section else min(last_heading_level + 1, 6)
                    cleaned.append(f"{'#' * question_level} {list_text}")
                    last_heading_level = question_level
                    qa_continuation = True
                    continue

                cleaned.append(line)
                qa_continuation = line.strip().endswith("?")
                continue

            if _is_continuation_line(line):
                cleaned.append(line)
                continue

            if _is_table_line(line) or _is_quote_line(line):
                qa_continuation = False
                cleaned.append(line)
                continue

            if qa_continuation:
                cleaned.append(stripped)
            else:
                cleaned.append(stripped)

    return cleaned


def _join_markdown_lines(lines: list[str]) -> str:
    out: list[str] = []
    in_fence = False
    for raw in lines:
        line = raw.rstrip()
        if not in_fence and not line:
            continue
        if not out:
            out.append(line)
            if _is_fence_line(line):
                in_fence = not in_fence
            continue

        if _is_fence_line(line):
            if not in_fence and out and out[-1] != "":
                out.append("")
            out.append(line)
            in_fence = not in_fence
            continue

        if in_fence:
            out.append(line)
            continue

        prev = out[-1]
        keep_compact = (
            (_is_list_line(prev) and _is_list_line(line)) or
            (_is_list_line(prev) and _is_continuation_line(line)) or
            (_is_continuation_line(prev) and _is_continuation_line(line)) or
            (_is_table_line(prev) and _is_table_line(line)) or
            (_is_quote_line(prev) and _is_quote_line(line))
        )

        if keep_compact:
            out.append(line)
        else:
            out.append("")
            out.append(line)
    return "\n".join(out)


def convert_to_markdown(content, title, _slug):
    """Convert HTML content to markdown format."""
    if not content:
        return f"# {title}\n\nContent not available.\n"

    markdown_lines = [f"# {title}"]
    body_lines = _render_blocks(content, title)

    for line in body_lines:
        if not line or not line.strip():
            continue
        if _is_list_line(line) or _is_quote_line(line) or _is_table_line(line) or _is_continuation_line(line):
            markdown_lines.append(line.rstrip())
        else:
            clean = _collapse_ws(line).strip()
            if clean:
                markdown_lines.append(clean)

    markdown_lines = _clean_and_group_lines(markdown_lines)
    markdown = _join_markdown_lines(markdown_lines)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def _slugify_heading(text: str) -> str:
    """GitHub-style heading slug for markdown anchor links."""
    text = text.strip().lower()
    text = re.sub(r"`", "", text)
    text = re.sub(r"[\[\]\(\)\.:;!?,/\"'“”‘’]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text


def add_toc(markdown: str) -> str:
    """Insert or replace a TOC block based on h2-h4 headings."""
    lines = markdown.splitlines()

    # Remove existing TOC block if present.
    start = end = None
    for i, line in enumerate(lines):
        if line.strip() == TOC_START:
            start = i
        if line.strip() == TOC_END and start is not None:
            end = i
            break
    if start is not None and end is not None and end >= start:
        del lines[start:end + 1]

    toc_lines = []
    seen = {}
    for line in lines:
        m = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        slug = _slugify_heading(title)
        if not slug:
            continue
        dup = seen.get(slug, 0)
        seen[slug] = dup + 1
        if dup:
            slug = f"{slug}-{dup}"
        indent = "  " * (level - 2)
        toc_lines.append(f"{indent}- [{title}](#{slug})")

    if not toc_lines:
        return "\n".join(lines).strip() + "\n"

    toc_block = [TOC_START, *toc_lines, TOC_END, ""]

    # Insert after first h1 section.
    insert_at = 0
    if lines and lines[0].startswith("# "):
        insert_at = 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
    new_lines = lines[:insert_at] + [""] + toc_block + lines[insert_at:]
    return "\n".join(new_lines).strip() + "\n"

def save_article(markdown, title, slug):
    """Save article to appropriate folder based on first letter"""
    first_letter = get_first_letter(title)
    folder_path = OUTPUT_DIR / first_letter
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Create filename from slug
    filename = f"{slug}.md"
    file_path = folder_path / filename
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(add_toc(markdown))
    
    print(f"Saved: {file_path}")

def main():
    """Main scraping function"""
    print("Starting QA Glossary Wiki Scraper")
    print("=" * 50)
    
    # Get all article links
    articles = get_article_links()
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Scrape each article
    total = len(articles)
    for idx, article in enumerate(articles, 1):
        print(f"\n[{idx}/{total}] Processing: {article['title']}")
        
        markdown = scrape_article(article['url'], article['title'], article['slug'])
        
        if markdown:
            save_article(markdown, article['title'], article['slug'])
        
        # Be polite - add delay between requests
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("Scraping completed!")
    print(f"Articles saved to: {OUTPUT_DIR.absolute()}")

if __name__ == "__main__":
    main()
