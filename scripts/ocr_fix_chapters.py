#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_fix_chapters.py — 把行内粘连的 "# 第X章/部分" 章首断开为独立标题行

OCR 常把章首标题粘连在前一段正文末尾（如 "……前述。# 第二章权力的文化网络在……整段"）。
本脚本：
  1. 找到行内（非行首）粘连的 "# 第X章/部分" 标记；
  2. 提取章名（到第一个"第X节" / 句末标点 / 20 字上限为止）；
  3. 把章名写成独立标题行 " # 第X章<章名> "，剩余正文完整移到下一行（零内容损失）。

保护：
  - 仅处理中文书（英文书跳过）；仅处理行内粘连的 # 章首，不动行首已有的规整标题。
  - 不删除任何正文，只是把粘连点断开。

用法（仓库根）：
  python scripts/ocr_fix_chapters.py            # 正式运行
  python scripts/ocr_fix_chapters.py --dry-run  # 只打印将要改动，不写文件
"""
import os
import re
import io
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "books")

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
PAT = re.compile(r"(?<=[^\n#])#\s*(第[一二三四五六七八九十百]+[章部分])([^#\n]*)")
NAME_END = re.compile(r"第[一二三四五六七八九十百]+节|[。！？]")


def is_english(text):
    return len(CJK.findall(text)) / max(1, len(text)) < 0.05


def process(text):
    # 预置：书里已有的行首 "# 第X章" 章号（目录区规整标题）不再重复断开
    seen = set(re.findall(r"^# (第[一二三四五六七八九十百]+[章部分])", text, re.M))
    NAME_END = re.compile(r"第[一二三四五六七八九十百]+节|[。！？]")

    def repl(m):
        ch = m.group(1)
        if ch in seen:
            return m.group(0)  # 该章号已有行首标题（目录已标），粘连点保留原样不导航
        seen.add(ch)
        rest = m.group(2)
        me = NAME_END.search(rest)
        if me:
            ne = me.start()
        elif len(rest) > 20:
            ne = 20
        else:
            ne = len(rest)
        name = rest[:ne].strip()
        body = rest[ne:]
        return "\n\n# %s%s\n\n%s" % (ch, name, body)

    return PAT.sub(repl, text)


def main():
    dry = "--dry-run" in sys.argv
    changed = 0
    broken = 0
    for slug in sorted(os.listdir(BOOKS)):
        p = os.path.join(BOOKS, slug, "content.md")
        if not os.path.isfile(p):
            continue
        text = io.open(p, encoding="utf-8").read()
        if is_english(text):
            continue
        if not PAT.search(text):
            continue
        new = process(text)
        if new == text:
            continue
        changed += 1
        if dry:
            # show chapter heads that will be broken out
            for m in PAT.finditer(text):
                ch = m.group(1)
                rest = m.group(2)
                me = NAME_END.search(rest)
                ne = me.start() if me else (20 if len(rest) > 20 else len(rest))
                print("[%s] #%s | name=<%s> | body_head=<%s>" % (
                    slug[:30], ch, rest[:ne].strip()[:30], rest[ne:][:25]))
        else:
            io.open(p, "w", encoding="utf-8").write(new)
    if dry:
        print("\nDRY-RUN: %d books would be modified" % changed)
    else:
        print("DONE: %d books modified" % changed)


if __name__ == "__main__":
    main()
