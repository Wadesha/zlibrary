#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_site.py — 把 books/<slug>/ 渲染成纯静态阅读站点（零运行时依赖）

产出
----
site/index.html                  总索引（搜索 + 语言/管线筛选）
site/books/<slug>/index.html     单本阅读页
site/assets/style.css            阅读样式

特点
----
- 纯静态 HTML/CSS/JS，双击 index.html 即可读，也可直接 GitHub Pages 发布
- markdown → HTML 用内置轻量渲染器，不依赖第三方库
- 中文/英文均支持

运行：python scripts/build_site.py
"""

import os
import re
import json
import html

import config


# ── 轻量 Markdown → HTML 渲染器 ──────────────────────────────────────────
def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < n:
        line = lines[i]
        # 代码块 ```
        if line.strip().startswith("```"):
            close_list()
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1  # 跳过结束 ```
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue

        # 标题
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list()
            # 页面分隔符：## --- Page 3 --- 等
            htxt = m.group(2).strip()
            pm = re.match(r"^-+\s*Page\s+(\d+)\s*-+$", htxt, re.IGNORECASE)
            if pm:
                out.append(f'<hr class="page"><span class="page-n">— Page {pm.group(1)} —</span>')
                i += 1
                continue
            lv = len(m.group(1))
            out.append(f"<h{lv}>{inline(htxt)}</h{lv}>")
            i += 1
            continue

        # 分隔线
        if re.match(r"^---+\s*$", line) or re.match(r"^\*{3,}\s*$", line):
            close_list()
            out.append("<hr>")
            i += 1
            continue

        # 引用
        if line.startswith(">"):
            close_list()
            out.append("<blockquote>" + inline(line[1:].strip()) + "</blockquote>")
            i += 1
            continue

        # 列表
        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + inline(m.group(1)) + "</li>")
            i += 1
            continue

        # 空行
        if not line.strip():
            close_list()
            i += 1
            continue

        # 普通段落
        close_list()
        out.append("<p>" + inline(line) + "</p>")
        i += 1

    close_list()
    return "\n".join(out)


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


# ── 页面模板 ────────────────────────────────────────────────────────────
PAGE_HEAD = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
"""

def render_index(manifest):
    books = manifest["books"]
    items = []
    for b in sorted(books, key=lambda x: x["title"].lower()):
        rel = f"books/{b['slug']}/index.html"
        badge = "中" if b["language"] == "zh" else "EN"
        items.append(
            f'<li class="book" data-title="{html.escape(b["title"].lower())}" '
            f'data-lang="{b["language"]}" data-pipe="{b["pipeline"]}">'
            f'<a href="{rel}">{html.escape(b["title"])}</a>'
            f'<span class="meta">[{badge}] {b["pipeline"]} · {b["chars"]:,} 字</span></li>'
        )
    list_html = "\n".join(items)

    body = f"""<header>
  <h1>Z-Library 阅读站</h1>
  <p class="sub">{manifest["count"]} 本书 · 由扫描/文本 PDF 提取整理</p>
  <div class="toolbar">
    <input id="q" type="search" placeholder="搜索书名…" oninput="filter()">
    <button onclick="setLang('all')" class="lf all active">全部</button>
    <button onclick="setLang('zh')" class="lf zh">中文</button>
    <button onclick="setLang('en')" class="lf en">English</button>
  </div>
</header>
<main>
  <ul class="booklist" id="list">
{list_html}
  </ul>
  <p id="empty" class="empty" style="display:none">没有匹配的书。</p>
</main>
<footer>由 build_site.py 生成 · 纯静态 · 可一键发布到 GitHub Pages</footer>
<script>
var cur='all';
function setLang(l){{cur=l;document.querySelectorAll('.lf').forEach(b=>b.classList.remove('active'));document.querySelector('.lf.'+l).classList.add('active');filter();}}
function filter(){{var q=document.getElementById('q').value.trim().toLowerCase();var n=0;
document.querySelectorAll('.book').forEach(li=>{{var t=li.dataset.title,ok=true;
if(cur!=='all'&&li.dataset.lang!==cur)ok=false;
if(q&&t.indexOf(q)<0)ok=false;
li.style.display=ok?'':'none';if(ok)n++;}});
document.getElementById('empty').style.display=n?'none':'block';}}
</script>
"""
    return PAGE_HEAD.format(lang="zh", title="Z-Library 阅读站",
                            css="assets/style.css") + body + "</body></html>"


def render_book(meta, content_html):
    lang = "zh" if meta["language"] == "zh" else "en"
    badge = "中文" if meta["language"] == "zh" else "English"
    back = "../../index.html"
    body = f"""<header class="bookhead">
  <p class="crumb"><a href="{back}">← 书架</a></p>
  <h1>{html.escape(meta["title"])}</h1>
  <p class="meta">[{badge}] 来源：{meta["pipeline"]} · {meta["chars"]:,} 字 · 校对：{'是' if meta.get('has_fixed') else '否'}</p>
</header>
<main class="reading">
{content_html}
</main>
<footer><a href="{back}">← 返回书架</a></footer>
"""
    return PAGE_HEAD.format(lang=lang, title=html.escape(meta["title"]),
                            css="../../assets/style.css") + body + "</body></html>"


CSS = """* { box-sizing: border-box; }
body { margin:0; font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
  color:#1f2328; background:#fafafa; line-height:1.7; }
header { padding:24px 20px 8px; max-width:860px; margin:0 auto; }
header h1 { margin:0 0 4px; font-size:24px; }
.sub { color:#666; margin:0 0 12px; font-size:14px; }
.toolbar { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
#q { flex:1; min-width:180px; padding:8px 12px; border:1px solid #ccc; border-radius:8px; font-size:14px; }
.lf { padding:6px 12px; border:1px solid #ccc; background:#fff; border-radius:8px; cursor:pointer; font-size:13px; }
.lf.active { background:#1f2328; color:#fff; border-color:#1f2328; }
main { max-width:860px; margin:0 auto; padding:8px 20px 60px; }
ul.booklist { list-style:none; padding:0; margin:16px 0; }
li.book { padding:10px 12px; border-bottom:1px solid #eee; display:flex; justify-content:space-between; gap:12px; align-items:baseline; flex-wrap:wrap; }
li.book a { font-size:16px; color:#0969da; text-decoration:none; }
li.book a:hover { text-decoration:underline; }
li.book .meta { color:#888; font-size:12px; white-space:nowrap; }
.empty { color:#888; text-align:center; padding:30px; }
.reading { font-size:17px; }
.reading h1,.reading h2,.reading h3 { margin-top:1.6em; line-height:1.3; }
.reading p { margin:.8em 0; }
.reading blockquote { border-left:3px solid #ddd; margin:1em 0; padding:.2em 1em; color:#555; }
.reading pre { background:#f0f0f0; padding:12px; border-radius:8px; overflow:auto; }
.reading code { background:#f0f0f0; padding:1px 5px; border-radius:4px; font-size:.9em; }
hr.page { border:none; border-top:1px dashed #ddd; margin:2em 0 1em; }
.page-n { display:block; text-align:center; color:#bbb; font-size:12px; margin-top:-1.4em; }
.bookhead { border-bottom:1px solid #eee; }
.bookhead .meta { color:#888; font-size:13px; }
.crumb { margin:0; font-size:13px; }
.crumb a { color:#666; text-decoration:none; }
footer { max-width:860px; margin:0 auto; padding:24px 20px; color:#aaa; font-size:12px; text-align:center; }
"""


def main():
    config.ensure_dirs()
    with open(config.BOOKS_MANIFEST, "r", encoding="utf-8") as fh:
        manifest = json.load(fh)

    # 样式
    with open(os.path.join(config.SITE_ASSETS_DIR, "style.css"), "w", encoding="utf-8") as fh:
        fh.write(CSS)

    # 索引页
    with open(os.path.join(config.SITE_DIR, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(render_index(manifest))

    # 每本书
    ok = 0
    keep_slugs = set()
    for b in manifest["books"]:
        slug = b["slug"]
        keep_slugs.add(slug)
        content_path = os.path.join(config.BOOKS_DIR, slug, "content.md")
        if not os.path.exists(content_path):
            continue
        with open(content_path, "r", encoding="utf-8", errors="ignore") as fh:
            md = fh.read()
        out_dir = os.path.join(config.SITE_BOOKS_DIR, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(render_book(b, md_to_html(md)))
        ok += 1

    # 清理 site/books 下的失效页面
    import shutil
    for d in os.listdir(config.SITE_BOOKS_DIR):
        if d not in keep_slugs:
            shutil.rmtree(os.path.join(config.SITE_BOOKS_DIR, d))

    print(f"站点生成完成：索引 1 页 + 阅读页 {ok} 页", flush=True)
    print(f"输出目录：{config.SITE_DIR}", flush=True)


if __name__ == "__main__":
    main()
