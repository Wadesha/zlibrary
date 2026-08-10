#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_fix_test.py — 小批量试跑 hy3 OCR 文本纠错（不重扫 PDF，只跑 LLM 校对）

- 独立脚本：仅用标准库 urllib 调用 hy3，避免依赖 requests/fitz/pytesseract
- 从 books/<slug>/content.md 读取已构建正文，逐段送 hy3 纠错
- 每块上限 LLM_CHUNK 字符；每本最多处理 MAX_CHUNKS 块（试跑控时长）
- 输出到 test_out/<slug>.md，并打印首块前后对比 + 耗时

用法：
python scripts/ocr_fix_test.py
"""
import os
import sys
import time
import json
import urllib.request
import urllib.error

import config

LLM_API_URL = 'https://token-plan-cn.xiaomimimo.com/v1/chat/completions'
LLM_API_KEY = 'tp-c3m8y92r0nj7msaxho4lmxzw6i17ernmpqs8kkt0jn8cd1xs'
LLM_MODEL = 'hy3'
LLM_CHUNK = 8000
LLM_DELAY = 1
MAX_CHUNKS = 4          # 试跑：每本最多处理 4 块 ≈ 32k 字符
REQUEST_TIMEOUT = 120

# 如需代理（与 git 同网段），取消下一行注释
# PROXY = 'http://127.0.0.1:7897'
PROXY = None

SYSTEM_MSG = (
    "You are a careful scientific text editor. The text below is OCR output and "
    "may contain recognition errors. Fix obvious OCR errors: wrong characters "
    "(e.g. '0-4?L' -> '0-471'), broken words, stray symbols, and confusion between "
    "similar glyphs. Keep equations, numbers, citations, and the original structure "
    "(paragraphs, headings, blank lines) intact. Return ONLY the corrected text, "
    "no commentary, no markdown code fences."
)

# 试跑目标：混合中英文 OCR 书，尺寸适中
TEST_SLUGS = [
    "quantum-physics-john-gribbin",
    "给孩子讲量子力学-李淼-1",
    "国外建筑设计-绘画精品书架-徒手绘画及速写",
]


def chunk_text(text, size):
    chunks, pos = [], 0
    while pos < len(text):
        end = pos + size
        if end < len(text):
            nl = text.rfind("\n", pos, end)
            if nl > pos:
                end = nl + 1
        chunks.append(text[pos:end])
        pos = end
    return chunks


def call_hy3(chunk, attempt=1):
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_MSG},
            {"role": "user", "content": chunk},
        ],
        "temperature": 0.1,
        "max_tokens": 4096,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        LLM_API_URL, data=data, method="POST",
        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
        },
    )
    handlers = []
    if PROXY:
        handlers.append(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    opener = urllib.request.build_opener(*handlers)
    try:
        with opener.open(req, timeout=REQUEST_TIMEOUT) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"]
    except Exception as e:
        if attempt < 3:
            time.sleep(3)
            return call_hy3(chunk, attempt + 1)
        raise


def main():
    config.ensure_dirs()
    out_dir = os.path.join(config.PROJECT_ROOT, "test_out")
    os.makedirs(out_dir, exist_ok=True)

    for slug in TEST_SLUGS:
        src = os.path.join(config.BOOKS_DIR, slug, "content.md")
        if not os.path.exists(src):
            print(f"[SKIP] 缺少 {src}")
            continue
        text = open(src, "r", encoding="utf-8").read()
        chunks = chunk_text(text, LLM_CHUNK)[:MAX_CHUNKS]
        print(f"\n=== {slug} | 总字符 {len(text):,} | 处理 {len(chunks)} 块 ===", flush=True)
        t0 = time.time()
        fixed_parts = []
        for i, ch in enumerate(chunks):
            try:
                fixed = call_hy3(ch)
            except Exception as e:
                print(f"  块 {i} 失败: {e}，保留原文", flush=True)
                fixed = ch
            fixed_parts.append(fixed)
            print(f"  块 {i+1}/{len(chunks)} 完成 ({time.time()-t0:.1f}s)", flush=True)
            time.sleep(LLM_DELAY)
        out_path = os.path.join(out_dir, slug + ".md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(fixed_parts))
        print(f"  用时 {time.time()-t0:.1f}s -> {out_path}", flush=True)

        # 首块前后对比
        before = chunks[0]
        after = fixed_parts[0]
        print("  --- 原文首 400 字 ---")
        print("  " + before[:400].replace("\n", "\n  "))
        print("  --- 纠错后首 400 字 ---")
        print("  " + after[:400].replace("\n", "\n  "))

    print("\n=== 试跑结束 ===", flush=True)


if __name__ == "__main__":
    main()
