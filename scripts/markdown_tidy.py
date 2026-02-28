#!/usr/bin/env python3
"""Simple Markdown tidier for wiki files.

- Collapse consecutive blank lines to one.
- Trim trailing whitespace.
- Remove leading spaces before list markers ("- ", "* ", "1. ").
- Ensure a blank line before any heading (except at file start).
"""
import os
import re

wiki_root = "/Users/nao.deng/Desktop/AwsomeCode/naodeng.com.cn/src/content/wiki"

for root, dirs, files in os.walk(wiki_root):
    for f in files:
        if not f.lower().endswith(".md"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        new_lines = []
        prev_blank = False
        for idx, line in enumerate(lines):
            # trim trailing spaces
            line = line.rstrip()
            # remove unnecessary leading spaces before list marker
            m = re.match(r"^(\s+)([-*+] |\d+\. )", line)
            if m:
                line = line[m.end(1):]
            # insert blank before headings if previous not blank and not first line
            if idx>0 and re.match(r"^#{1,6} ", line) and not prev_blank:
                new_lines.append("")
                prev_blank = True
            if line == "":
                if not prev_blank:
                    new_lines.append("")
                    prev_blank = True
                # else skip duplicate blank
            else:
                new_lines.append(line)
                prev_blank = False
        out = "\n".join(new_lines).strip() + "\n"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"tidied {path}")
