# 项目架构（ARCHITECTURE）

## 1. 背景与目标

`Z-Library/` 是一个 PDF 书库（487 本，多为物理/经济/历史类）。这些 PDF 来源混杂：

- **文字版**：内嵌文本层，可直接用 PyMuPDF 提取
- **扫描版**：纯图片，需 Tesseract OCR + LLM 校对

历史上跑过多套实验性脚本，产物散落在 `_converted/`、`_native_output/`、`_translated/`、
`_hy3_output/` 及根目录 `[OCR]*` 中，命名与质量不一。本项目的目标：

1. 把所有提取结果**按书归集**、去重、挑最佳版本
2. 生成**纯静态阅读站**，方便逐本阅读
3. 把代码整理成**清晰、可上传 GitHub** 的形态，并把"重新逐字扫描"封装为可手动触发的流水线

---

## 2. 目录与职责

| 目录/文件 | 职责 |
|-----------|------|
| `scripts/config.py` | 统一路径、slug 归一化、来源位置表 `SOURCE_LOCATIONS`（含优先级） |
| `scripts/collect_books.py` | 扫描所有来源 → 按 slug 分组 → 选最佳 → 写 `books/<slug>/` → 生成 `data/books.json` |
| `scripts/build_site.py` | 读 `books/` + `meta.json` → 渲染 `site/index.html` 与 `site/books/<slug>/index.html`（内置轻量 Markdown→HTML） |
| `scripts/ocr_pipeline.py` | 高精度重扫流水线（扫描版判定 → Tesseract → LLM 校对），输出 `ocr_out/` |
| `data/progress.json` | OCR 进度（断点续传），源自原始 `.scan_ocr_progress.json` |
| `data/books.json` | 书目总清单：`count` + 每本书 `meta` |
| `books/<slug>/content.md` | 该书最佳提取正文 |
| `books/<slug>/meta.json` | 书目元信息 |
| `site/` | 生成的静态站（可直接打开 / GitHub Pages） |
| `ocr_out/` | 本次重扫结果（优先级最高，覆盖旧版） |

源 PDF 只在 `Z-Library/`（上级目录），不进入本仓库。

---

## 3. 提取来源与优先级

`collect_books.py` 按以下优先级选"最佳版本"（数值越大越优先）：

| 优先级 | 来源 | 说明 |
|--------|------|------|
| 40 | `ocr_out/` | 本次高精度重扫（最新、最准） |
| 30 | `_translated/` | 中文译本（已结构化） |
| 20 | `_native_output/` | 原生文本确定性结构化提取 |
| 15 | `_converted/markdown/` | OCR→Markdown（含 `_fixed` 校对版） |
| 10 | `_hy3_output/` | 早期实验输出 |
| 5 | 根目录 `[OCR]*` | 最早的 OCR 文本 |

同一本书若多个管线都有产出，取优先级最高者；同管线内 `_fixed` 版加权 +10。

---

## 4. 关键实现要点

### 4.1 扫描版判定（`is_scanned`）
- **均匀采样**：在 PDF 前/中/后均匀取 `SAMPLE_PAGES=16` 页（避免封面/目录误导）
- **阈值**：平均每页字符数 `< 200` 判为扫描版（文字版通常远高于此）
- 早期版本因"只采前 8 页 + 阈值 80"导致文字版被误判扫描版，已修正

### 4.2 高精度重扫（`ocr_pipeline.py`）
- DPI=300（早期 200）
- 灰度 + 自动对比度预处理（`PIL.ImageOps.autocontrast`），提升小字/低对比度准确率
- 语言包 `eng+chi_sim`（中文 PDF 必须装 chi_sim，否则全乱码）
- LLM 逐段校对（`mimo-v2.5`，低 temperature），修正 OCR 典型错字但保留公式结构
- 每 5 页 / 每 20 段写检查点，崩溃可续传

### 4.3 slug 归一化
- 去前缀：`[MD]` `[OCR]` `[译]` `pre_`
- 去来源标记：`(Z-Library)` `Z_Library`
- 去后缀：`_fixed` `_16x9`
- 非字母数字（含中文）统一变 `-`，限长 80（兼容 Windows 长路径）

### 4.4 Markdown→HTML
内置轻量渲染器，覆盖标题/段落/引用/列表/代码块/分隔线/粗斜体/行内代码，
并把 `--- Page N ---` 渲染为页面分隔符。不依赖第三方库，保证站点零构建依赖。

---

## 5. 重新触发"逐字扫描"的步骤

1. 确认 `C:\Program Files\Tesseract-OCR\tesseract.exe` 与
   `C:\Users\wade\AppData\Local\tessdata\chi_sim.traineddata` 就位
2. 用装有 `requests/fitz/pytesseract/PIL` 的 Python 运行：
   ```bash
   python scripts/ocr_pipeline.py > ocr_run.log 2>&1 &
   ```
3. 重扫完成后重新归集与建站：
   ```bash
   python scripts/collect_books.py
   python scripts/build_site.py
   ```
`ocr_out/` 优先级最高，新结果会自动覆盖 `books/` 里的旧版本。

---

## 6. 历史遗留（不在本仓库清理范围内）

根目录及 `_*` 目录里的其他实验脚本（如 `test_*.py`、`*_v2.py`、`batch_convert_*.py` 等）
为早期探索产物，未纳入 `scripts/`，不影响本流水线的运行与发布。
