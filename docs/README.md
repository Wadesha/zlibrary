🌐 在线阅读（GitHub Pages）：https://wadesha.github.io/zlibrary/

# Z-Library 阅读站

把 Z-Library 书库里的 PDF（扫描版 + 文字版）提取、整理成**纯静态阅读网站**，
可双击打开，也可一键发布到 GitHub Pages。

- 当前收录：**420 本**（中文 171 / 英文 249）
- 零运行时依赖：只有 HTML + CSS + 原生 JS
- 文本版 PDF 直接提取，扫描版 PDF 用 Tesseract + LLM 校对识别

---

## 目录结构

```
Z-Library/                        ← 原始书库（含 487 个源 PDF，不进本仓库）
└── Z-Library-Web/                ← 本项目（GitHub 就绪）
    ├── scripts/
    │   ├── config.py            路径/常量/工具
    │   ├── collect_books.py     把分散的提取结果按书归集到 books/
    │   ├── build_site.py        把 books/ 渲染成 site/ 静态站
    │   └── ocr_pipeline.py      高精度扫描版重扫流水线（可选，手动触发）
    ├── data/
    │   ├── progress.json        OCR 进度（断点续传）
    │   └── books.json           书目总清单（collect_books 生成）
    ├── books/                   每本书一个子目录：<slug>/content.md + meta.json
    ├── site/                    生成的静态站（index.html + books/<slug>/index.html）
    ├── ocr_out/                 本次重扫结果（ocr_pipeline 输出，gitignore）
    ├── docs/
    │   ├── README.md            本文件
    │   └── ARCHITECTURE.md      架构与管线说明
    └── .gitignore
```

> 源 PDF 留在 `Z-Library/` 上级目录，不进 `Z-Library-Web/`（体积大、不适合 Git）。

---

## 快速开始（本地阅读）

```bash
# 1) 生成静态站（需要能跑 Python 的环境，含 PyMuPDF 即可）
python scripts/build_site.py

# 2) 直接打开
start site/index.html        # Windows
# 或在文件管理器双击 site/index.html
```

`site/index.html` 支持：书名搜索、中文/英文筛选、点击进入单本阅读页。

---

## 工作流

```
源 PDF (Z-Library/)
   │
   ├─ 文字版 ──► 直接文本提取（_native_output / _translated）
   │
   └─ 扫描版 ──► Tesseract OCR ──► LLM 校对 ──► [OCR]*_fixed.txt
                                   （ocr_pipeline.py，可选重扫）
   │
   ▼
collect_books.py  ──►  books/<slug>/{content.md, meta.json}  ──►  data/books.json
   │
   ▼
build_site.py  ──►  site/{index.html, books/<slug>/index.html}
```

### 1. 整理已有提取结果（已做过）

`collect_books.py` 会扫描 `_native_output`、`_translated`、`_converted/markdown`、
`_hy3_output`、根目录 `[OCR]*` 以及 `ocr_out/`，按书名 slug 去重，挑选最佳版本，
写入 `books/<slug>/`。

```bash
python scripts/collect_books.py
```

### 2. 重新高精度扫描（按需手动触发）

仅对**扫描版 PDF** 重新识别（"逐字扫描"），输出到 `ocr_out/`。
该目录在 `collect_books` 里优先级最高，重扫后会自动覆盖旧版本。

```bash
# 后台运行（推荐，耗时较长）
python scripts/ocr_pipeline.py > ocr_run.log 2>&1 &
```

识别设定：DPI=300 + 灰度/自动对比度预处理 + `eng+chi_sim` 中英混合语言包 + LLM 逐段校对。
进度存 `data/progress.json`，崩溃后直接重跑即可续传。

> 注意：OCR 流水线依赖 `requests` / `fitz` / `pytesseract` / `PIL`，
> 请使用装有这些包的 Python（本机为 `C:\Users\wade\AppData\Local\Programs\Python\Python312`）。
> 而 `collect_books.py` 与 `build_site.py` 仅用标准库，任意 Python 3 均可。

### 3. 重新生成站点

```bash
python scripts/build_site.py
```

---

## 发布到 GitHub Pages

站点已就绪：`index.html`（仓库根）会自动跳转到 `site/index.html`，裸地址 `https://wadesha.github.io/zlibrary/` 即可访问。

1. 把整个 `Z-Library-Web/` 推到 GitHub（含 `site/` 与根 `index.html`）
2. 仓库 Settings → Pages → Source 选 **main** 分支、**`/ (root)`** 目录 → Save
3. 初次部署约 1–2 分钟，之后每次 push 自动更新
4. 若要改站点内容：本地改 `books/` 后重跑 `python scripts/build_site.py`，再 push

---

## 命名规范

| 位置 | 约定 |
|------|------|
| `books/<slug>/` | slug = 书名小写、非字母数字变 `-`、限长 80 |
| 提取产物 | `[MD]<名>.md`（原生）/ `[OCR]<名>.txt`（OCR）/ `[译]<名>.md`（译本） |
| 校对版 | 同名加 `_fixed` 后缀 |
| 元信息 | 每本书 `meta.json`：`title/language/pipeline/source_pdf/chars/has_fixed` |
