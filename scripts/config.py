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
import re
import html as _html

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

# 非书籍文件（内部笔记/流程/大纲/习题/单章/候选清单等）归集时跳过
EXCLUDE_RE = re.compile(
    r"(批次完成报告|完成报告|回顾总结|复习笔记|学习笔记|课堂笔记|读书笔记|"
    r"process[-_]?log|wave\d+[-_]plan|candidates|clean[-_]?candidates|"
    r"syllabus|course[_ ]and[_ ]exam[_ ]description|chapter[ _]\d|chap\d|"
    r"excerpt|大纲|习题答案|习题集|课件|幻灯片|handout|lecture|"
    r"第\d+次课|qc[-_]|todo|readme|notes?|"
    r"coverage[-_]?report|覆盖率报告|处理覆盖率|coverage)",
    re.IGNORECASE,
)

# 去重键构建时忽略的停用词（中英）
STOPWORDS = set(
    "the a an of and de la der die le les von und to in on for with "
    "的 了 与 和 及 等 著 译 编 第 版 卷 册 上 下 一 二 三 四 五 六 七 八 九 十".split()
)

# 最小正文字数：低于此值的书视为空书，不收录
MIN_CHARS = 200

# 最小“散文”字数（剔除 # 标题行后剩余的正文）：低于此值视为纯目录/大纲 stub，不收录
MIN_PROSE_CHARS = 400


def normalize_title(raw_name: str) -> str:
    """从文件名推导出规范书名（去掉管线前缀、来源标记、编号、ISBN、扩展名）。"""
    name = raw_name
    # 去扩展名
    for ext in (".md", ".txt", ".pdf"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    # 去方括号前缀
    for p in ("[MD]", "[OCR]", "[译]"):
        if name.startswith(p):
            name = name[len(p):].strip()
    # 去 (Z-Library) / Z_Library / Z Library 等来源标记
    name = re.sub(r"\(Z-Library\)", "", name, flags=re.IGNORECASE)
    name = re.sub(r"Z_Library", "", name, flags=re.IGNORECASE)
    name = re.sub(r"Z Library", "", name, flags=re.IGNORECASE)
    # 去尾部 _fixed / _16x9 / _ebooks_corner / _excerpt
    name = re.sub(r"_(fixed|16x9|ebooks_corner|excerpt)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r" ebooks corner$", "", name, flags=re.IGNORECASE)
    # 去前导编号（Z-Library 编号 / 课程号）：17_  2_  aa210a_  554625_
    name = re.sub(r"^[\w]*\d+[\w]*_", "", name)
    # 去前导 QC / 编号标记（QC 16  →  16  →  【16】）
    name = re.sub(r"^qc[\W_]*\d*[\W_]*", "", name, flags=re.IGNORECASE)
    name = re.sub(r"^[\W_]*\d+[\W_]*", "", name)
    # 去书名里夹杂的 ISBN（10/13 位连续数字，避免误删 4 位年份）
    name = re.sub(r"\d{10,13}", "", name)
    # 去其余括号/方括号，下划线转空格
    name = re.sub(r"[\[\]()]", " ", name)
    name = name.replace("_", " ")
    name = re.sub(r"\s+", " ", name).strip(" -")
    return name


def slugify(title: str) -> str:
    """把书名转成可用于目录/URL 的 slug。"""
    # 保留中文、字母、数字，其余变空格
    s = title.lower()
    s = re.sub(r"[^\w\s一-鿿-]", " ", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = s.strip("-")
    # 限制长度，避免 Windows 路径过长
    return s[:80].strip("-")


def is_excluded(raw_name: str) -> bool:
    """判断文件名是否对应非书籍文件。"""
    base = re.sub(r"\.(md|txt|pdf)$", "", raw_name, flags=re.IGNORECASE)
    return bool(EXCLUDE_RE.search(base))


def clean_content(text: str) -> str:
    """清洗正文：解码 HTML 实体（&#13; &amp;）、去回车/BOM、合并空行，
    并剔除集中在扉页的版权页/贡献者名单段落。"""
    text = _html.unescape(text)            # &#13; → \r ；&amp; → &
    text = text.replace("\r", "")
    text = text.replace("\ufeff", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    # 按空行分段，仅对“文档前 25%”的段落做版权页清洗，避免误伤正文引用
    paras = text.split("\n\n")
    total = len(text)
    boiler = re.compile(
        r"(ISBN|©|copyright|all rights reserved|specialsales|https?://|www\.|"
        r"@[\w.]+|printed in|first published|published by .*limited|"
        r"forest stewardship|邮编\d|来源文件|处理说明|本文件：|字符数（约）)",
        re.IGNORECASE,
    )
    out = []
    pos = 0
    for p in paras:
        start = pos
        pos += len(p) + 2
        if start < total * 0.25 and boiler.search(p):
            continue
        out.append(p)
    text = "\n\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def detect_lang(text: str) -> str:
    """判断语言：取文档中部采样，避免扉页英文版权块干扰判断。"""
    n = len(text)
    if n == 0:
        return "en"
    sample = text[int(n * 0.2):int(n * 0.8)]
    cjk = len(re.findall(r"[一-鿿]", sample))
    total = max(1, len(sample))
    return "zh" if cjk / total > 0.12 else "en"


def dedup_key(title: str) -> str:
    """生成去重键：取书名前几个有效词（忽略编号/停用词）。"""
    s = title.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff\s]", " ", s)
    toks = [t for t in s.split()
            if len(t) >= 3 and not t.isdigit() and t not in STOPWORDS]
    return " ".join(toks[:5])


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
