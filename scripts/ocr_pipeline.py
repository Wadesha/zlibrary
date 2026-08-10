#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ocr_pipeline.py — 高精度扫描版 PDF 识别流水线（逐字级）

职责
----
1. 遍历书库根目录所有 PDF，用均匀采样判断是否为“扫描版”（图片型、无可提取文本）
2. 对扫描版用 Tesseract 逐页识别（eng+chi_sim），输出 ocr_out/[OCR]<书名>.txt
3. 用 LLM 对识别结果做逐段校对，输出 ocr_out/[OCR]<书名>_fixed.txt
4. 进度写入 data/progress.json，支持断点续传（崩溃后直接重跑即可）

高质量设定（对比早期版本）
-------------------------
- DPI=300（原 200）
- 灰度 + 自动对比度预处理，提升小字/低对比度页面准确率
- 中英文混合语言包 chi_sim+eng

输出位置
--------
PROJECT_ROOT/ocr_out/       本次重扫结果（collect_books.py 会优先采用）

运行
----
python scripts/ocr_pipeline.py
（建议后台运行：python scripts/ocr_pipeline.py > ocr_run.log 2>&1 &）
"""

import os
import sys
import time
import glob
import json
import io
import requests

import fitz  # PyMuPDF
import pytesseract
from PIL import Image, ImageOps

import config


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Users\wade\AppData\Local\tessdata'

LLM_API_URL = 'https://token-plan-cn.xiaomimimo.com/v1/chat/completions'
LLM_API_KEY = 'tp-c3m8y92r0nj7msaxho4lmxzw6i17ernmpqs8kkt0jn8cd1xs'
LLM_MODEL   = 'hy3'

DPI = 300
SAMPLE_PAGES = 16        # 扫描版判定时均匀采样的页数
SCANNED_THRESHOLD = 200  # 平均每页字符数低于此值视为扫描版
LLM_CHUNK = 8000
LLM_DELAY = 2

OCR_OUT = os.path.join(config.PROJECT_ROOT, "ocr_out")
os.makedirs(OCR_OUT, exist_ok=True)


# ── 进度（断点续传）─────────────────────────────────────────────────────
def load_progress():
    if os.path.exists(config.PROGRESS_FILE):
        with open(config.PROGRESS_FILE, "r", encoding="utf-8") as f:
            prog = json.load(f)
        for key in ["processed", "skipped_text", "failed"]:
            seen, cleaned = {}, []
            for item in prog.get(key, []):
                low = item.lower()
                if low not in seen:
                    seen[low] = item
                    cleaned.append(item)
            prog[key] = cleaned
        return prog
    return {"processed": [], "skipped_text": [], "failed": []}


def save_progress(prog):
    with open(config.PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(prog, f, ensure_ascii=False, indent=2)


def is_scanned(pdf_path):
    """均匀采样前/中/后页面，估算平均字符数；低于阈值即判定为扫描版。"""
    try:
        doc = fitz.open(pdf_path)
        total = len(doc)
        sample_n = min(SAMPLE_PAGES, total)
        indices = set()
        for i in range(sample_n):
            idx = int(i * total / sample_n)
            indices.add(min(idx, total - 1))
        chars = sum(len(doc[i].get_text().strip()) for i in indices)
        doc.close()
        avg = chars / len(indices) if indices else 0
        return avg < SCANNED_THRESHOLD, avg
    except Exception:
        return True, 0.0


def preprocess(pix):
    """像素图 → 灰度 + 自动对比度，提升 OCR 准确率。"""
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("L")
    img = ImageOps.autocontrast(img)
    return img


def ocr_pdf(pdf_path, out_path):
    """逐页 Tesseract 识别，带断点（每 5 页写检查点）。返回页数。"""
    doc = fitz.open(pdf_path)
    total = len(doc)
    ckpt = out_path + ".ckpt"
    start = 0
    if os.path.exists(ckpt):
        start = int(open(ckpt).read().strip() or 0)

    mode = "a" if start > 0 else "w"
    with open(out_path, mode, encoding="utf-8") as fout:
        if start == 0:
            fout.write(f"# OCR: {os.path.basename(pdf_path)}\n# Pages: {total}\n\n")
        mat = fitz.Matrix(DPI / 72, DPI / 72)
        for p in range(start, total):
            img = preprocess(doc[p].get_pixmap(matrix=mat))
            try:
                text = pytesseract.image_to_string(img, lang="eng+chi_sim")
            except Exception as e:
                text = f"[OCR ERROR p{p+1}: {e}]"
            fout.write(f"\n--- Page {p+1} ---\n{text}\n")
            fout.flush()
            if (p + 1) % 5 == 0:
                open(ckpt, "w").write(str(p + 1))
                print(f"    OCR: {p+1}/{total}", flush=True)
        open(ckpt, "w").write(str(total))
    doc.close()
    if os.path.exists(ckpt):
        os.remove(ckpt)
    return total


def llm_fix(txt_path, fixed_path):
    """LLM 逐段校对 OCR 结果，带断点。"""
    text = open(txt_path, "r", encoding="utf-8").read()
    chunks, pos = [], 0
    while pos < len(text):
        end = pos + LLM_CHUNK
        if end < len(text):
            nl = text.rfind("\n", pos, end)
            if nl > pos:
                end = nl + 1
        chunks.append(text[pos:end])
        pos = end

    ckpt = fixed_path + ".ckpt"
    start_chunk = int(open(ckpt).read().strip() or 0) if os.path.exists(ckpt) else 0
    mode = "a" if start_chunk > 0 else "w"
    headers = {"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"}
    system_msg = (
        "You are a scientific text editor. Fix OCR errors in the provided text. "
        "Fix obvious typos caused by OCR (e.g. \"0-4?L\"->\"0-471\", wrong characters). "
        "Keep equations, symbols, and structure intact. "
        "Return ONLY the corrected text, no comments."
    )
    total_chunks = len(chunks)
    with open(fixed_path, mode, encoding="utf-8") as fout:
        for i in range(start_chunk, total_chunks):
            payload = {
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": chunks[i]},
                ],
                "temperature": 0.1,
                "max_tokens": 4096,
            }
            try:
                r = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=120)
                r.raise_for_status()
                fixed_chunk = r.json()["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"    LLM chunk {i} error: {e}, using original", flush=True)
                fixed_chunk = chunks[i]
            fout.write(fixed_chunk)
            fout.flush()
            open(ckpt, "w").write(str(i + 1))
            if (i + 1) % 20 == 0 or i == total_chunks - 1:
                print(f"    LLM fix: {i+1}/{total_chunks}", flush=True)
            time.sleep(LLM_DELAY)
    if os.path.exists(ckpt):
        os.remove(ckpt)


def main():
    config.ensure_dirs()
    prog = load_progress()
    done_lower = {x.lower() for x in prog["processed"] + prog["skipped_text"]}

    pdf_files = sorted(
        glob.glob(os.path.join(config.LIB_ROOT, "*.pdf")) +
        glob.glob(os.path.join(config.LIB_ROOT, "*.PDF")),
        key=os.path.getsize,
    )
    print(f"Total PDFs: {len(pdf_files)}", flush=True)
    print(f"Already done: {len(done_lower)}", flush=True)

    for pdf_path in pdf_files:
        basename = os.path.basename(pdf_path)
        stem = os.path.splitext(basename)[0]
        ocr_txt = os.path.join(OCR_OUT, f"[OCR]{stem}.txt")
        fixed_txt = os.path.join(OCR_OUT, f"[OCR]{stem}_fixed.txt")

        if basename.lower() in done_lower:
            continue
        if os.path.exists(fixed_txt):
            prog["processed"].append(basename)
            save_progress(prog)
            continue
        if os.path.exists(ocr_txt) and os.path.getsize(ocr_txt) > 1000:
            print(f"\n[RESUME LLM FIX] {basename}", flush=True)
            llm_fix(ocr_txt, fixed_txt)
            prog["processed"].append(basename)
            save_progress(prog)
            print(f"  -> done: {os.path.basename(fixed_txt)}", flush=True)
            continue

        print(f"\n[CHECK] {basename}", flush=True)
        scanned, avg = is_scanned(pdf_path)
        size_mb = os.path.getsize(pdf_path) / 1024 / 1024
        print(f"  size={size_mb:.1f}MB  avg_chars={avg:.0f}  scanned={scanned}", flush=True)

        if not scanned:
            prog["skipped_text"].append(basename)
            save_progress(prog)
            print("  -> TEXT-TYPE, skipped", flush=True)
            continue

        print("  -> SCANNED, starting OCR...", flush=True)
        try:
            pages = ocr_pdf(pdf_path, ocr_txt)
            print(f"  OCR done: {pages} pages", flush=True)
        except Exception as e:
            print(f"  OCR FAILED: {e}", flush=True)
            prog["failed"].append(basename)
            save_progress(prog)
            continue

        print("  -> LLM fix...", flush=True)
        try:
            llm_fix(ocr_txt, fixed_txt)
            print("  LLM fix done", flush=True)
        except Exception as e:
            print(f"  LLM fix FAILED: {e}", flush=True)
            prog["failed"].append(basename + ":llm")
            save_progress(prog)
            continue

        prog["processed"].append(basename)
        save_progress(prog)
        print(f"  COMPLETE: [OCR]{stem}_fixed.txt", flush=True)

    print("\n=== ALL DONE ===", flush=True)


if __name__ == "__main__":
    main()
