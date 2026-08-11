#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_fix_noise.py — OCR 噪声安全去噪（全量幂等）

对所有 books/<slug>/content.md 应用两层安全去噪：
  1. 删除分页标记行（形如 `--- Page N ---`）
  2. 中文书：对"纯英文碎片 # 行"（行首 # 后内容首字符为 ASCII 字母且整行不含 CJK）
     去掉 # 前缀、保留内容（不删行）。这类是 OCR 把图注 / 参考文献断裂行 / 化学式 /
     人名 / 乱码英文 当成了 # 标题的噪声；保留内容可避免误删正文（如化学成分列表）。
  3. 英文书：保留 # 前缀（当作标题层级，去前缀无实质改善且改动巨大）。

保护规则：
  - 绝不删除含中文的标题/正文；中文书的英文 # 行仅去前缀、内容完整保留。
  - 幂等：已清理/已手工规范的书重复运行无副作用。

用法（从仓库根目录）：
  python scripts/ocr_fix_noise.py
"""
import os
import re
import io
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
PAGE_RE = re.compile(r"^--- Page \d+ ---$")
HASH_RE = re.compile(r"^(#+)\s*(.*)$")


def is_english(text):
    return len(CJK.findall(text)) / max(1, len(text)) < 0.05


def clean_text(text):
    eng = is_english(text)
    lines = text.split("\n")
    out = []
    dropped_page = 0
    stripped_en = 0
    for ln in lines:
        if PAGE_RE.match(ln):
            dropped_page += 1
            continue
        m = HASH_RE.match(ln)
        if m and not eng:
            content = m.group(2)
            if content and content[0].isascii() and content[0].isalpha() and not CJK.search(content):
                out.append(content)  # strip '#', keep english fragment text (no content loss)
                stripped_en += 1
                continue
        out.append(ln)
    return "\n".join(out), dropped_page, stripped_en


def main():
    total_page = 0
    total_en = 0
    changed = 0
    for slug in sorted(os.listdir(BOOKS)):
        p = os.path.join(BOOKS, slug, "content.md")
        if not os.path.isfile(p):
            continue
        try:
            text = io.open(p, encoding="utf-8").read()
        except Exception as e:
            print(f"SKIP(decode) {slug}: {e}", file=sys.stderr)
            continue
        new, dp, de = clean_text(text)
        if new != text:
            io.open(p, "w", encoding="utf-8").write(new)
            total_page += dp
            total_en += de
            changed += 1
    print(f"DONE: {changed} books modified | page-markers dropped={total_page} | english-# prefixes stripped(zh)={total_en}")


if __name__ == "__main__":
    main()
