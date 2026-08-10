#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_books.py — 把分散在多管线、多目录的提取结果，按书归集到 books/<slug>/

背景
----
书库经过多个处理管线，产物散落在：
    _translated/        译本（中文），干净结构化
    _native_output/     原生文本提取（确定性结构化）
    _converted/markdown OCR → Markdown（含 _fixed 校对版）
    _hy3_output/        早期实验输出
    根目录 [OCR]*.txt   当前 OCR 流水线输出（含 _fixed 校对版）

本脚本：
    1. 扫描上述位置的所有 .md / .txt
    2. 用 normalize_title + slugify 把同一本书归并为同一 slug
    3. 按管线优先级 + _fixed 加权挑选“最佳版本”
    4. 写入 books/<slug>/content.md （正文）与 meta.json （书目信息）
    5. 生成 data/books.json 总清单

运行：python scripts/collect_books.py
"""

import os
import re
import json
import glob
import shutil

import config


def prose_of(text: str) -> int:
    """剔除 # 标题行与空白行后的正文字数（识别纯目录/大纲 stub 用）。"""
    return sum(
        len(ln) for ln in text.split("\n")
        if ln.strip() and not ln.lstrip().startswith("#")
    )


def is_book_file(raw_name):
    """过滤掉非书籍文件（内部笔记/流程/大纲/习题/单章等）。"""
    return not config.is_excluded(raw_name)


def list_source_files():
    """返回 [(path, pipeline, priority), ...]，priority 越大越优。"""
    out = []
    for path, pipeline, priority in config.SOURCE_LOCATIONS:
        if not os.path.isdir(path):
            continue
        patterns = ["*.md", "*.txt"]
        if pipeline == "root_ocr":
            # 只取 [OCR] 前缀，避免把脚本/日志算进来
            for f in os.listdir(path):
                if f.startswith("[OCR]") and (f.endswith(".txt") or f.endswith(".md")):
                    if is_book_file(f):
                        out.append((os.path.join(path, f), pipeline, priority))
        else:
            for pat in patterns:
                for f in glob.glob(os.path.join(path, pat)):
                    if is_book_file(os.path.basename(f)):
                        out.append((f, pipeline, priority))
    return out


def score(path, pipeline, base_priority):
    """综合评分：管线优先级 + _fixed 加权。"""
    s = base_priority
    name = os.path.basename(path)
    if "_fixed" in name:
        s += 10
    return s


def detect_lang(text):
    """语言判断委托给 config（取文档中部采样，避免扉页英文版权块干扰）。"""
    return config.detect_lang(text)


def strip_yaml_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def find_source_pdf(title, slug):
    """在书库根目录找同名源 PDF（大小写不敏感）。"""
    for ext in ("*.pdf", "*.PDF"):
        for f in glob.glob(os.path.join(config.LIB_ROOT, ext)):
            b = os.path.basename(f)
            base = re.sub(r"\.(pdf|PDF)$", "", b, flags=re.IGNORECASE)
            if base.lower() == title.lower() or config.slugify(base) == slug:
                return b
    return None


def main():
    config.ensure_dirs()
    files = list_source_files()
    print(f"扫描到源文件：{len(files)}", flush=True)

    # 1) 按 slug 分组，选每 slug 最佳版本
    groups = {}
    for path, pipeline, priority in files:
        raw = os.path.basename(path)
        title = config.normalize_title(raw)
        if not title:
            continue
        slug = config.slugify(title)
        if not slug:
            continue
        groups.setdefault(slug, []).append((path, pipeline, priority, title))

    best_per_slug = {}
    for slug, items in groups.items():
        best = max(items, key=lambda it: score(it[0], it[1], it[2]))
        best_per_slug[slug] = best

    # 2) 跨 slug 去重（同一本书的不同文件名变体合并，保留字数更多者）
    records = {}          # dedup_key -> (slug, item, content, clen)
    merged = []           # (被并标题, 保留slug)
    for slug, item in best_per_slug.items():
        path, pipeline, priority, title = item
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            raw_text = fh.read()
        # 去 YAML frontmatter / OCR 头
        raw_text = strip_yaml_frontmatter(raw_text)
        if pipeline in ("ocr_md", "root_ocr"):
            raw_text = "\n".join(
                ln for ln in raw_text.split("\n")
                if not re.match(r"^#\s*OCR:", ln)
                and not re.match(r"^#\s*Pages:", ln)
            )
        content = config.clean_content(raw_text)
        clen = len(content)
        # 散文字数（剔除 # 标题行与空白行后的正文），用于识别纯目录/大纲 stub
        prose = sum(
            len(ln) for ln in content.split("\n")
            if ln.strip() and not ln.lstrip().startswith("#")
        )
        key = config.dedup_key(title) or slug
        if key in records:
            prev = records[key]
            if clen > prev[3]:
                merged.append((title, slug))
                records[key] = (slug, item, content, clen)
            else:
                merged.append((title, prev[0]))
        else:
            records[key] = (slug, item, content, clen)

    # 3) 写入 books/<slug>/，跳过空书
    manifest = []
    skipped_empty = 0
    for key, (slug, item, content, clen) in records.items():
        if clen < config.MIN_CHARS or prose_of(content) < config.MIN_PROSE_CHARS:
            skipped_empty += 1
            continue
        _, pipeline, _, title = item
        book_dir = os.path.join(config.BOOKS_DIR, slug)
        os.makedirs(book_dir, exist_ok=True)
        with open(os.path.join(book_dir, "content.md"), "w", encoding="utf-8") as fh:
            fh.write(content)
        lang = detect_lang(content)
        src_pdf = find_source_pdf(title, slug)
        meta = {
            "slug": slug,
            "title": title,
            "language": lang,
            "pipeline": pipeline,
            "source_file": os.path.basename(item[0]),
            "source_pdf": src_pdf,
            "chars": clen,
            "has_fixed": "_fixed" in os.path.basename(item[0]),
        }
        with open(os.path.join(book_dir, "meta.json"), "w", encoding="utf-8") as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=2)
        manifest.append(meta)

    # 写总清单
    with open(config.BOOKS_MANIFEST, "w", encoding="utf-8") as fh:
        json.dump({"count": len(manifest), "books": manifest}, fh,
                  ensure_ascii=False, indent=2)

    # 清理上次遗留的失效书目目录
    keep = {m["slug"] for m in manifest}
    for d in os.listdir(config.BOOKS_DIR):
        dp = os.path.join(config.BOOKS_DIR, d)
        if os.path.isdir(dp) and d not in keep:
            shutil.rmtree(dp)

    # 统计
    by_lang, by_pipe = {}, {}
    for m in manifest:
        by_lang[m["language"]] = by_lang.get(m["language"], 0) + 1
        by_pipe[m["pipeline"]] = by_pipe.get(m["pipeline"], 0) + 1
    print("归集完成。", flush=True)
    print("  书目总数：", len(manifest), flush=True)
    print("  去重合并：", len(merged), " 对", flush=True)
    for t, kept in merged:
        print(f"    - 合并：{t}  →  保留 {kept}", flush=True)
    print("  跳过空书（< %d 字）：" % config.MIN_CHARS, skipped_empty, flush=True)
    print("  语言分布：", by_lang, flush=True)
    print("  管线分布：", by_pipe, flush=True)


if __name__ == "__main__":
    main()
