#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_local_fix.py — 不依赖外部 LLM 的本地 OCR 文本修复

问题背景
--------
OCR->Markdown 转换给几乎每一行都加了 `## ` / `### ` 前缀，导致整本书在网页上
被渲染成巨大的二级标题，完全不可读。此外还有常见 OCR 字符/断行噪声。

本脚本做三件事（纯启发式，零 API）：
1. 标题前缀归一：去掉伪 `#` 标题标记；把“看起来像真标题”的短行保留为 `#` 标题，
   其余正文行转为普通段落。
2. 断行修复：OCR 常在右边界硬断行，把明显是同一句的相邻短行合并。
3. 少量高精度字符修正（仅在不破坏正常文本的安全规则下）。

用法
----
python scripts/ocr_local_fix.py --dry          # 只打印前 2 本书的前后对比，不写盘
python scripts/ocr_local_fix.py               # 处理全部 OCR 书并写回 content.md
python scripts/ocr_local_fix.py --slug XXX    # 只处理指定 slug
"""
import os
import re
import sys
import json
import argparse

import config


# 真标题判定：去除 `#` 后，符合下列之一视为章节标题
# 注意：中文正文常被 OCR 切成短行，故“短中文行”绝不能当标题，必须带结构标记
HEADING_PATTERNS = [
    re.compile(r"^第[一二三四五六七八九十百千\d]+[讲章节回部卷篇]"),
    re.compile(r"^([一二三四五六七八九十]+)[\．、]"),         # 一、二、
    re.compile(r"^（[一二三四五六七八九十\d]+）"),            # （一）
    re.compile(r"^(序|前言|目录|后记|附录|参考文献|引子|结语|注释|致谢|自序)"),
    re.compile(r"^[Cc]hapter\s+\d+", re.IGNORECASE),
    re.compile(r"^[Pp]art\s+\d+", re.IGNORECASE),
    re.compile(r"^[Ll]esson\s+\d+", re.IGNORECASE),
    re.compile(r"^[Ss]ection\s+\d+", re.IGNORECASE),
    re.compile(r"^\d+[\.\、]\s*\S"),
    re.compile(r"^[A-Z][A-Za-z0-9 ,&.'-]{2,40}$"),   # 全大写/标题大小写短行
]

# 句末标点（用于判断断行是否应合并）
SENT_END = set("。！？!?；;…\u2026.”』」）)]}")

# 高精度字符修正（仅替换明确错误的模式，避免误伤正常文本）
CHAR_FIXES = [
    (re.compile(r"(?<=ISBN)\s*[:：]?\s*0[\-—]?4\?L"), "0-471"),  # 典型 OCR 错误
    (re.compile(r"\b0[\-—]4\?L\b"), "0-471"),
    (re.compile(r"(?<=\d)l(?=\d)"), "1"),            # 数字间的 l->1（保守）
]


def looks_heading(stripped: str) -> bool:
    s = stripped.strip()
    if not s:
        return False
    if len(s) > 60:
        return False
    for pat in HEADING_PATTERNS:
        if pat.match(s):
            return True
    return False


def fix_headings(text: str) -> str:
    lines = text.split("\n")
    out = []
    for ln in lines:
        # 统计并去掉左侧连续的 # 标记
        m = re.match(r"^(#{1,6})\s?(.*)$", ln)
        if not m:
            out.append(ln)
            continue
        # 剥掉嵌套的 # 标记（如 "### # Title" -> "Title"）
        body = re.sub(r"^#+\s*", "", m.group(2)).strip()
        if not body:
            out.append("")
            continue
        if looks_heading(body):
            out.append("# " + body)
        else:
            out.append(body)   # 正文：去掉伪标题标记，变普通段落
    return "\n".join(out)


def fix_cjk_spacing(text: str) -> str:
    """折叠 CJK 字符（含中文标点/全角符号）之间的空格。
    英文词之间的空格保留。这是中文 OCR 最常见的缺陷：每个字都被空格隔开。"""
    cjk = r"[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]"
    text = re.sub(rf"({cjk})\s+(?={cjk})", r"\1", text)
    # 去除中文标点外侧多余空格
    text = re.sub(rf"\s+(?=[\u3000-\u303f\uff00-\uffef])", "", text)
    text = re.sub(rf"(?<=[\u3000-\u303f\uff00-\uffef])\s+", "", text)
    # 数字与中文之间的空格（如 "1979 年" -> "1979年"、"吨 12" -> "吨12"）
    zh = r"[\u4e00-\u9fff]"
    text = re.sub(rf"(\d) ({zh})", r"\1\2", text)
    text = re.sub(rf"({zh}) (\d)", r"\1\2", text)
    # 小数点后的空格（"20. 9" -> "20.9"）
    text = re.sub(r"(?<=\.) (\d)", "", text)
    return text


def fix_chars(text: str) -> str:
    for rx, rep in CHAR_FIXES:
        text = rx.sub(rep, text)
    return text


def join_broken(text: str) -> str:
    """把明显是同一句、被 OCR 在右边界硬断开的相邻短行合并（补一个空格）。"""
    PAGE_RE = re.compile(r"^-+\s*Page\s+\d+\s*-+$", re.IGNORECASE)
    lines = text.split("\n")
    res = []
    i = 0
    n = len(lines)
    while i < n:
        cur = lines[i]
        cur_s = cur.strip()
        # 当前行非空、非标题、非页码、非列表、不以句末标点结尾，
        # 且下一行存在、非页码、偏短 -> 合并（补空格）
        if (cur_s and not cur.lstrip().startswith("#")
                and not PAGE_RE.match(cur_s)
                and not cur.lstrip().startswith(("-", "*", ">", "1.", "2.", "3."))
                and cur.rstrip()[-1:] not in SENT_END
                and i + 1 < n and lines[i + 1].strip()
                and not PAGE_RE.match(lines[i + 1].strip())
                and len(lines[i + 1].strip()) < 50):
            nxt = lines[i + 1].strip()
            merged = cur.rstrip() + " " + nxt
            res.append(merged)
            i += 2
            continue
        res.append(cur)
        i += 1
    return "\n".join(res)


def fix_page_markers(text: str) -> str:
    """确保 '--- Page N ---' 独立成行（前后空行），避免被并入正文段落。"""
    PAGE_RE = re.compile(r"---+\s*Page\s+\d+\s*-+", re.IGNORECASE)
    out = []
    for ln in text.split("\n"):
        m = PAGE_RE.search(ln)
        if m and ln.strip() != m.group(0).strip():
            # 行内嵌了页码标记，拆开
            pre, post = ln[:m.start()], ln[m.end():]
            if pre.strip():
                out.append(pre.strip())
            out.append(m.group(0).strip())
            if post.strip():
                out.append(post.strip())
        else:
            out.append(ln)
    return "\n".join(out)


def fix_book(text: str) -> str:
    text = fix_headings(text)
    text = fix_cjk_spacing(text)
    text = fix_chars(text)
    text = fix_page_markers(text)
    text = join_broken(text)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="只打印前后对比，不写盘")
    ap.add_argument("--slug", default=None, help="只处理指定 slug")
    args = ap.parse_args()

    config.ensure_dirs()
    manifest = json.load(open(config.BOOKS_MANIFEST, encoding="utf-8"))
    SKIP = {
        "清华出版社物理难题150例086890-01",
        "电动力学南京大学ch0-0",
        "给孩子讲量子力学-李淼-1",
        "温州乡土建筑-丁俊清-肖健雄著-ding-junqing-xiao-jianxiong-丁俊清-etc",
    }
    targets = [b for b in manifest["books"]
               if b["pipeline"] in ("ocr_md", "hy3")
               and (args.slug is not None or b["slug"] not in SKIP)
               and (args.slug is None or b["slug"] == args.slug)]

    print(f"待处理 OCR 书：{len(targets)}", flush=True)
    shown = 0
    for b in targets:
        slug = b["slug"]
        src = os.path.join(config.BOOKS_DIR, slug, "content.md")
        if not os.path.exists(src):
            continue
        text = open(src, "r", encoding="utf-8").read()
        fixed = fix_book(text)
        if args.dry:
            print(f"\n===== {slug} =====")
            print("--- BEFORE (前 600 字) ---")
            print(text[:600])
            print("--- AFTER  (前 600 字) ---")
            print(fixed[:600])
            shown += 1
            if shown >= 2:
                break
            continue
        with open(src, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  已修复：{slug} ({len(text):,} -> {len(fixed):,})", flush=True)

    if not args.dry:
        print("全部 OCR 书修复完成。", flush=True)


if __name__ == "__main__":
    main()
