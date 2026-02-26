#!/usr/bin/env python3
"""
QA Glossary Wiki Scraper
Scrapes articles from https://ray.run/wiki and organizes them alphabetically
"""

import logging
import requests
from bs4 import BeautifulSoup
import os
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from progress_tracker import ProgressTracker

# Error logger — writes to sync_error.log in the project root
_error_logger = logging.getLogger("scraper")
if not _error_logger.handlers:
    _handler = logging.FileHandler(
        Path(__file__).parent / "sync_error.log", encoding="utf-8"
    )
    _handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(levelname)s] [scraper] %(message)s",
                          datefmt="%Y-%m-%dT%H:%M:%SZ")
    )
    _error_logger.addHandler(_handler)
    _error_logger.setLevel(logging.ERROR)

BASE_URL = "https://ray.run/wiki"
OUTPUT_DIR = Path("Sections")

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
        markdown = convert_to_markdown(content, title)
        
        return markdown
        
    except Exception as e:
        print(f"Error scraping {title}: {e}")
        return None

def convert_to_markdown(content, title):
    """Convert HTML content to markdown format"""
    if not content:
        return f"# {title}\n\nContent not available.\n"
    
    markdown_lines = [f"# {title}\n"]
    
    # Process content elements
    for element in content.descendants:
        if element.name == 'h1':
            text = element.get_text(strip=True)
            if text and text != title:  # Avoid duplicate title
                markdown_lines.append(f"\n# {text}\n")
        elif element.name == 'h2':
            markdown_lines.append(f"\n## {element.get_text(strip=True)}\n")
        elif element.name == 'h3':
            markdown_lines.append(f"\n### {element.get_text(strip=True)}\n")
        elif element.name == 'h4':
            markdown_lines.append(f"\n#### {element.get_text(strip=True)}\n")
        elif element.name == 'h5':
            markdown_lines.append(f"\n##### {element.get_text(strip=True)}\n")
        elif element.name == 'h6':
            markdown_lines.append(f"\n###### {element.get_text(strip=True)}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append(f"\n{text}\n")
        elif element.name == 'ul':
            for li in element.find_all('li', recursive=False):
                markdown_lines.append(f"- {li.get_text(strip=True)}\n")
        elif element.name == 'ol':
            for idx, li in enumerate(element.find_all('li', recursive=False), 1):
                markdown_lines.append(f"{idx}. {li.get_text(strip=True)}\n")
        elif element.name == 'code':
            markdown_lines.append(f"`{element.get_text(strip=True)}`")
        elif element.name == 'pre':
            code_text = element.get_text(strip=True)
            markdown_lines.append(f"\n```\n{code_text}\n```\n")
        elif element.name == 'blockquote':
            text = element.get_text(strip=True)
            markdown_lines.append(f"\n> {text}\n")
        elif element.name == 'a':
            text = element.get_text(strip=True)
            href = element.get('href', '')
            if text and href:
                markdown_lines.append(f"[{text}]({href})")
        elif element.name == 'strong' or element.name == 'b':
            markdown_lines.append(f"**{element.get_text(strip=True)}**")
        elif element.name == 'em' or element.name == 'i':
            markdown_lines.append(f"*{element.get_text(strip=True)}*")
    
    # Clean up the markdown
    markdown = ''.join(markdown_lines)
    # Remove excessive newlines
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown.strip() + '\n'

def save_article(markdown, title, slug):
    """Save article to appropriate folder based on first letter"""
    first_letter = get_first_letter(title)
    folder_path = OUTPUT_DIR / first_letter
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Create filename from slug
    filename = f"{slug}.md"
    file_path = folder_path / filename
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
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
