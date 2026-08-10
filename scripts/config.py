#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config.py — 项目路径与共享常量

Z-Library-Web 是 GitHub 就绪的项目根目录。所有脚本都从这里读取路径，
避免在多个脚本里硬编码绝对路径。

目录约定
--------
Z-Library/                 (WPS 云盘原始书库，含 487 个源 PDF)
└── Z-Library-Web/         (本项目)
    ├── scripts/          代码（ocr_pipeline.py / collect_books.py / build_site.py / config.py）
    ├── data/             progress.json（OCR 进度）、books.json（书目清单）
    ├── books/            每本书一个子目录：<slug>/content.md + meta.json
    ├── site/             生成的静态站点（index.html + books/<slug>/index.html）
    ├── assets/           站点共用静态资源（style.css 等）
    └── docs/             README.md / ARCHITECTURE.md
"""

import os

# ── 根路径 ───────────────────────────────────────────────────────────────
# Z-Library-Web/ 自身（scripts/config.py 的上两级）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Z-Library-Web/ 的父目录 = 原始书库根（含源 PDF）
LIB_ROOT = os.path.dirname(PROJECT_ROOT)

# 防御：PROJECT_ROOT 必须含 scripts/ 子目录，否则路径解析异常
if not os.path.isdir(os.path.join(PROJECT_ROOT, "scripts")):
    raise RuntimeError(f"PROJECT_ROOT 解析异常: {PROJECT_ROOT}")

# ── 子目录 ───────────────────────────────────────────────────────────────
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
BOOKS_DIR = os.path.join(PROJECT_ROOT, "books")
SITE_DIR = os.path.join(PROJECT_ROOT, "site")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

SITE_BOOKS_DIR = os.path.join(SITE_DIR, "books")
SITE_ASSETS_DIR = os.path.join(SITE_DIR, "assets")

# ── 关键文件 ─────────────────────────────────────────────────────────────
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")   # OCR 进度（原 .scan_ocr_progress.json）
BOOKS_MANIFEST = os.path.join(DATA_DIR, "books.json")      # 书目清单（collect_books.py 生成）

# ── 提取结果的来源（归集时扫描这些位置）─────────────────────────────────
# 每个条目：(路径, 管线名, 优先级)  优先级越大越优
SOURCE_LOCATIONS = [
    (os.path.join(PROJECT_ROOT, "ocr_out"),         "ocr_rerun",    40),  # 本次高精度重扫（最高优先级）
    (os.path.join(LIB_ROOT, "_translated"),        "translated",   30),  # 译本（中文）
    (os.path.join(LIB_ROOT, "_native_output"),     "native",       20),  # 干净结构化提取
    (os.path.join(LIB_ROOT, "_converted", "markdown"), "ocr_md",    15),  # OCR→md（含 _fixed）
    (os.path.join(LIB_ROOT, "_hy3_output"),         "hy3",          10),  # 早期实验输出
    (LIB_ROOT,                                       "root_ocr",     5),   # 根目录 [OCR]*_fixed.txt / [OCR]*.txt
]

# ── slug 归一化时剥离的前缀/后缀片段 ──────────────────────────────────────
STRIP_PREFIXES = ["[MD]", "[OCR]", "[译]", "pre_", "pre", "[", "]"]
STRIP_SUFFIXES = ["(Z-Library)", "_fixed", "_16x9", "Z_Library", "Z Library"]


def normalize_title(raw_name: str) -> str:
    """从文件名推导出规范书名（去掉管线前缀、来源标记、扩展名）。"""
    name = raw_name
    # 去扩展名
    for ext in (".md", ".txt", ".pdf"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    # 去前缀
    for p in STRIP_PREFIXES:
        if name.startswith(p):
            name = name[len(p):].strip()
    # 去 (Z-Library) / Z_Library 等来源标记
    import re
    name = re.sub(r"\(Z-Library\)", "", name, flags=re.IGNORECASE)
    name = re.sub(r"Z_Library", "", name, flags=re.IGNORECASE)
    name = re.sub(r"_\d+bit", "", name)
    # 去尾部 _fixed / _16x9
    name = re.sub(r"_fixed$", "", name)
    name = re.sub(r"_16x9$", "", name)
    name = name.strip().strip("_- ").strip()
    return name


def slugify(title: str) -> str:
    """把书名转成可用于目录/URL 的 slug。"""
    import re, unicodedata
    # 保留中文、字母、数字，其余变空格
    s = title.lower()
    s = re.sub(r"[^\w\s一-鿿-]", " ", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = s.strip("-")
    # 限制长度，避免 Windows 路径过长
    return s[:80].strip("-")


def ensure_dirs():
    for d in (SCRIPTS_DIR, DATA_DIR, BOOKS_DIR, SITE_DIR,
              ASSETS_DIR, DOCS_DIR, SITE_BOOKS_DIR, SITE_ASSETS_DIR):
        os.makedirs(d, exist_ok=True)


if __name__ == "__main__":
    ensure_dirs()
    print("LIB_ROOT     :", LIB_ROOT)
    print("PROJECT_ROOT :", PROJECT_ROOT)
    print("BOOKS_DIR    :", BOOKS_DIR)
    print("normalize   :", normalize_title("[OCR]Quantum Physics (赵凯华) (Z-Library).md"))
    print("slug        :", slugify(normalize_title("[OCR]Quantum Physics (赵凯华) (Z-Library).md")))
