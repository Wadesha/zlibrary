#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_fix_titles.py — 清理标题行的 Z-Library 源平台标签

OCR 导出时很多书名行被追加了 " Z Library" / "Z-Library" / "(Z Library)" 等源平台标签。
本脚本只处理**第一行（标题行）**，移除行尾的 Z-Library 标签，零内容损失。
对正文无影响，幂等。

用法（仓库根）：
  python scripts/ocr_fix_titles.py
"""
import os
import re
import io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")

LABEL_RE = re.compile(r"\s*[(（]?\s*Z[\-\s]?Library\s*[)）]?\s*$", re.IGNORECASE)


def main():
    changed = 0
    for slug in sorted(os.listdir(BOOKS)):
        p = os.path.join(BOOKS, slug, "content.md")
        if not os.path.isfile(p):
            continue
        lines = io.open(p, encoding="utf-8").read().split("\n")
        if not lines:
            continue
        new_title = LABEL_RE.sub("", lines[0]).strip()
        if new_title != lines[0]:
            lines[0] = new_title
            io.open(p, "w", encoding="utf-8").write("\n".join(lines))
            changed += 1
    print("DONE: %d titles cleaned (Z-Library label removed)" % changed)


if __name__ == "__main__":
    main()
