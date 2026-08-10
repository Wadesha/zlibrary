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

import config


# 非书籍的内部/笔记文件，归集时跳过
SKIP_RE = re.compile(
    r"^(process[-_]?log|candidates|clean[-_]?candidates|wave\d+[-_]plan|sync[-_]?test|"
    r"批次完成报告|todo|readme|notes?)",
    re.IGNORECASE,
)


def is_book_file(raw_name):
    """过滤掉明显的非书籍文件（以下划线开头的内部笔记等）。"""
    name = raw_name
    for ext in (".md", ".txt"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    if name.startswith("_"):
        return False
    if SKIP_RE.match(name):
        return False
    return True


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
    """粗略判断语言：CJK 占比高 → zh，否则 en。"""
    cjk = len(re.findall(r"[一-鿿]", text))
    total = max(1, len(text))
    return "zh" if cjk / total > 0.15 else "en"


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

    # 按 slug 分组
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

    print(f"去重后书目：{len(groups)}", flush=True)

    manifest = []
    for slug, items in sorted(groups.items()):
        # 选最佳版本
        best = max(items, key=lambda it: score(it[0], it[1], it[2]))
        best_path, best_pipeline, _, best_title = best

        with open(best_path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()

        # 清理：去掉 YAML frontmatter（OCR md 顶部噪声）
        content = strip_yaml_frontmatter(content)
        # OCR 产物去掉顶部 "# OCR:" / "# Pages:" 噪声行
        if best_pipeline in ("ocr_md", "root_ocr"):
            content = "\n".join(
                ln for ln in content.split("\n")
                if not re.match(r"^#\s*OCR:", ln)
                and not re.match(r"^#\s*Pages:", ln)
            )

        lang = detect_lang(content)
        src_pdf = find_source_pdf(best_title, slug)

        book_dir = os.path.join(config.BOOKS_DIR, slug)
        os.makedirs(book_dir, exist_ok=True)
        with open(os.path.join(book_dir, "content.md"), "w", encoding="utf-8") as fh:
            fh.write(content)

        meta = {
            "slug": slug,
            "title": best_title,
            "language": lang,
            "pipeline": best_pipeline,
            "source_file": os.path.basename(best_path),
            "source_pdf": src_pdf,
            "chars": len(content),
            "has_fixed": "_fixed" in os.path.basename(best_path),
        }
        with open(os.path.join(book_dir, "meta.json"), "w", encoding="utf-8") as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=2)

        manifest.append(meta)

    # 写总清单
    with open(config.BOOKS_MANIFEST, "w", encoding="utf-8") as fh:
        json.dump({
            "count": len(manifest),
            "books": manifest,
        }, fh, ensure_ascii=False, indent=2)

    # 清理上次遗留的失效书目目录
    keep = {m["slug"] for m in manifest}
    for d in os.listdir(config.BOOKS_DIR):
        dp = os.path.join(config.BOOKS_DIR, d)
        if os.path.isdir(dp) and d not in keep:
            import shutil
            shutil.rmtree(dp)

    # 统计
    by_lang = {}
    by_pipe = {}
    for m in manifest:
        by_lang[m["language"]] = by_lang.get(m["language"], 0) + 1
        by_pipe[m["pipeline"]] = by_pipe.get(m["pipeline"], 0) + 1
    print("归集完成。", flush=True)
    print("  书目总数：", len(manifest), flush=True)
    print("  语言分布：", by_lang, flush=True)
    print("  管线分布：", by_pipe, flush=True)


if __name__ == "__main__":
    main()
