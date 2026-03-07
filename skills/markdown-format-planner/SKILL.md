---
name: markdown-format-planner
description: Standardize and plan Markdown document structure and formatting. Use when users ask to reformat, tidy, normalize, restructure, outline, or improve readability of Markdown files, including heading hierarchy, list consistency, spacing, tables, code fences, links, and section planning.
---

# Markdown Format Planner

Follow this workflow to reformat and restructure Markdown files without changing intended meaning.

## 1. Inspect the source quickly

- Identify the file type and scope: short note, article, guide, changelog, or documentation page.
- Detect existing style signals: heading depth, bullet style, code fence language tags, table usage, and link format.
- Preserve semantic content, factual statements, and technical identifiers exactly unless the user asks for rewrites.

## 2. Normalize formatting

Apply these rules consistently:

- Keep one `#` top-level title per file.
- Increase heading depth one level at a time (`##` -> `###`), avoid skipping levels.
- Use one bullet style per list (`-` preferred) and keep indentation consistent.
- Keep one blank line around headings, lists, tables, and fenced code blocks.
- Always use fenced code blocks with a language tag when inferable.
- Normalize links to `[text](url)` and remove malformed Markdown syntax.
- Align table pipes and ensure header separator rows are valid.
- Remove trailing spaces and repeated blank lines.

## 3. Plan structure before rewriting

Before final output, choose a structure pattern from [references/structure-patterns.md](references/structure-patterns.md).

- For guides: use `Overview -> Prerequisites -> Steps -> Validation -> Troubleshooting`.
- For reference docs: use `Summary -> Definitions -> Examples -> Notes`.
- For changelogs/updates: use date/version grouped entries with concise bullets.

If the input is unstructured, create a clear section outline first, then place original content into the new structure.

## 4. Produce output

- Return clean Markdown that is ready to save.
- Keep tone and language consistent with the original document unless user asks otherwise.
- If content is missing for required sections, add a short placeholder like `TODO:` rather than inventing facts.

## 5. Run a quality check

Validate all of the following before finishing:

- Heading hierarchy is valid and sequential.
- Lists, code blocks, and tables render correctly.
- Internal anchors and links still point to valid targets.
- No accidental content loss.

## Reusable resources

- Use [references/format-checklist.md](references/format-checklist.md) for final QA checks.
- Use [assets/templates/standard-doc-template.md](assets/templates/standard-doc-template.md) when the user requests a fresh structure template.
