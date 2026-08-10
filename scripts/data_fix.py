#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data_fix.py — 书目数据清洗（本地、无 API）

- 删除明确的非书条目（图表 / 测试册 / 单章残片）
- 修复被截断 / 损坏的书名
- 为每本书补 category（主题）与 author（作者，best-effort）
- 写回 data/books.json，并清理 site/books 下失效页面

运行：python scripts/data_fix.py
"""
import os
import json
import shutil

import config


# ── 明确的非书（删除）─────────────────────────────────────────────────────
JUNK_SLUGS = {
    "emf-spectrum-chart1",                                  # 一张 EMF 频谱图
    "ap-physics-c-mechanics-hybrid-sample-free-response-booklet",  # 测试小册子
    "qt04",                                                  # 某量子力学书的一章残片
}

# ── 损坏 / 截断标题 → 修复后的书名 ─────────────────────────────────────────
TITLE_FIXES = {
    "e": "Macroeconomics (7th Edition) — N. Gregory Mankiw",
    "edition": "Recursive Macroeconomic Theory (2nd Edition) — Ljungqvist & Sargent",
    "tsay": "Analysis of Financial Time Series — Ruey S. Tsay",
    "高清": "Principles of Economics: Microeconomics (5th ed., English) — Mankiw",
    "for": "Physics for Scientists and Engineers (9th Ed.) — Serway & Jewett (Solutions Manual)",
    "高级教程": "宏观经济学（高级教程）— 布兰查德、费希尔",
}


def main():
    config.ensure_dirs()
    manifest = json.load(open(config.BOOKS_MANIFEST, "r", encoding="utf-8"))
    books = manifest["books"]

    removed = []
    for b in books:
        if b["slug"] in JUNK_SLUGS:
            # 删除本地 books/<slug> 与 site/books/<slug>
            for base in (config.BOOKS_DIR, config.SITE_BOOKS_DIR):
                p = os.path.join(base, b["slug"])
                if os.path.isdir(p):
                    shutil.rmtree(p, ignore_errors=True)
            removed.append(b["slug"])

    kept = [b for b in books if b["slug"] not in JUNK_SLUGS]

    # 修复标题 + 补 category / author
    for b in kept:
        slug = b["slug"]
        if slug in TITLE_FIXES:
            b["title"] = TITLE_FIXES[slug]
        # 头 1500 字符用于分类
        cp = os.path.join(config.BOOKS_DIR, slug, "content.md")
        head = ""
        if os.path.exists(cp):
            head = open(cp, "r", encoding="utf-8", errors="ignore").read(1500)
        b["category"] = config.classify_category(b["title"], head)
        b["author"] = config.extract_author(b.get("source_file", ""), b["title"])
        b["chars"] = len(open(cp, "r", encoding="utf-8", errors="ignore").read()) if os.path.exists(cp) else b.get("chars", 0)

    manifest["books"] = kept
    manifest["count"] = len(kept)

    json.dump(manifest, open(config.BOOKS_MANIFEST, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(f"删除非书：{len(removed)} 本 -> {removed}")
    print(f"修复标题：{list(TITLE_FIXES.keys())}")
    # 分类统计
    from collections import Counter
    c = Counter(b["category"] for b in kept)
    print("分类分布：")
    for k, v in c.most_common():
        print(f"  {k}: {v}")
    print(f"剩余书目：{len(kept)} 本（原 {len(books)}）")
    no_author = sum(1 for b in kept if not b.get("author"))
    print(f"已提取作者：{len(kept) - no_author} / {len(kept)}（其余留空）")


if __name__ == "__main__":
    main()
