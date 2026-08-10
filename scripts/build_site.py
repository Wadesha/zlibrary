#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_site.py — 把 books/<slug>/ 渲染成纯静态阅读站点（零运行时依赖）

产出
----
site/index.html                  总索引（搜索 + 语言 / 主题筛选 + 排序）
site/books/<slug>/index.html     单本阅读页（章节目录 + 阅读控件）
site/assets/style.css            阅读样式（含夜间模式）
site/assets/search.js            全文检索索引（标题/作者/主题/正文片段/章节）
site/assets/app.js               索引页交互逻辑

特点
----
- 纯静态 HTML/CSS/JS，可直接 GitHub Pages 发布
- 内置轻量 Markdown → HTML 渲染器（不依赖第三方库）
- 中文 / 英文均支持；阅读页含可跳转目录与暗色模式
"""
import os
import re
import json
import html

import config


# ── 轻量 Markdown → HTML 渲染器（同时抽取章节目录）────────────────────────
def md_to_html(md: str):
    lines = md.split("\n")
    out = []
    toc = []
    i = 0
    n = len(lines)
    in_list = False
    sec = 0

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < n:
        line = lines[i]
        if line.strip().startswith("```"):
            close_list()
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_list()
            htxt = m.group(2).strip()
            pm = re.match(r"^-+\s*Page\s+(\d+)\s*-+$", htxt, re.IGNORECASE)
            if pm:
                out.append(f'<hr class="page"><span class="page-n">— Page {pm.group(1)} —</span>')
                i += 1
                continue
            lv = len(m.group(1))
            # 仅 h1–h3 进目录
            if lv <= 3:
                sec += 1
                anchor = f"sec-{sec}"
                out.append(f'<h{lv} id="{anchor}">{inline(htxt)}</h{lv}>')
                toc.append((lv, htxt, anchor))
            else:
                out.append(f"<h{lv}>{inline(htxt)}</h{lv}>")
            i += 1
            continue

        if re.match(r"^---+\s*$", line) or re.match(r"^\*{3,}\s*$", line):
            close_list()
            out.append("<hr>")
            i += 1
            continue

        if line.startswith(">"):
            close_list()
            out.append("<blockquote>" + inline(line[1:].strip()) + "</blockquote>")
            i += 1
            continue

        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>" + inline(m.group(1)) + "</li>")
            i += 1
            continue

        if not line.strip():
            close_list()
            i += 1
            continue

        close_list()
        out.append("<p>" + inline(line) + "</p>")
        i += 1

    close_list()
    return "\n".join(out), toc


def inline(text: str) -> str:
    if len(text) > 5000:
        return html.escape(text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


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

CSS = """* { box-sizing: border-box; }
:root {
  --bg:#fafafa; --fg:#1f2328; --muted:#6a737d; --line:#e6e6e6;
  --accent:#0969da; --card:#fff; --chip:#eef2f6; --chip-on:#1f2328;
  --reading-font:17px; --reading-w:760px;
}
body.dark { --bg:#0d1117; --fg:#c9d1d9; --muted:#8b949e; --line:#21262d;
  --accent:#58a6ff; --card:#161b22; --chip:#21262d; --chip-on:#c9d1d9; }
body { margin:0; font-family:-apple-system,"Segoe UI","Noto Sans CJK SC","Microsoft YaHei",sans-serif;
  background:var(--bg); color:var(--fg); line-height:1.7; transition:background .2s,color .2s; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }

/* ── 书架索引 ── */
header.top { padding:28px 20px 10px; max-width:1080px; margin:0 auto; }
header.top h1 { margin:0 0 4px; font-size:26px; }
.sub { color:var(--muted); margin:0 0 14px; font-size:14px; }
.toolbar { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
#q { flex:1; min-width:200px; padding:9px 12px; border:1px solid var(--line);
  background:var(--card); color:var(--fg); border-radius:8px; font-size:14px; }
.btn { padding:6px 12px; border:1px solid var(--line); background:var(--chip);
  color:var(--fg); border-radius:8px; cursor:pointer; font-size:13px; }
.btn.active { background:var(--chip-on); color:var(--bg); border-color:var(--chip-on); }
.chips { display:flex; gap:6px; flex-wrap:wrap; margin:12px 0 4px; }
.count { color:var(--muted); font-size:13px; margin:8px 0; }
main { max-width:1080px; margin:0 auto; padding:0 20px 60px; }
ul.booklist { list-style:none; padding:0; margin:8px 0; display:grid;
  grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:10px; }
li.book { background:var(--card); border:1px solid var(--line); border-radius:10px;
  padding:12px 14px; display:flex; flex-direction:column; gap:6px; }
li.book a.title { font-size:15.5px; font-weight:600; line-height:1.4; }
li.book .meta { color:var(--muted); font-size:12px; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
.tag { background:var(--chip); border-radius:6px; padding:1px 7px; font-size:11px; }
.tag.zh { color:#0a7d3b; } .tag.en { color:#b35900; }
.empty { color:var(--muted); text-align:center; padding:40px; }
footer { max-width:1080px; margin:0 auto; padding:24px 20px; color:var(--muted);
  font-size:12px; text-align:center; }

/* ── 阅读页 ── */
.layout { display:flex; max-width:1280px; margin:0 auto; }
nav.toc { width:230px; flex:0 0 230px; position:sticky; top:0; align-self:flex-start;
  height:100vh; overflow:auto; padding:20px 14px; border-right:1px solid var(--line); font-size:13px; }
nav.toc h4 { margin:0 0 8px; font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:.05em; }
nav.toc ol { list-style:none; margin:0; padding:0; }
nav.toc li { margin:2px 0; }
nav.toc a { color:var(--muted); display:block; padding:2px 6px; border-radius:5px; line-height:1.4; }
nav.toc a:hover { background:var(--chip); text-decoration:none; }
nav.toc li.lv3 a { padding-left:18px; font-size:12px; }
nav.toc .empty-toc { color:var(--muted); font-size:12px; }
.readcol { flex:1; min-width:0; }
.readwrap { max-width:var(--reading-w); margin:0 auto; padding:18px 22px 80px; }
.controls { position:sticky; top:0; z-index:5; display:flex; gap:8px; align-items:center;
  justify-content:flex-end; padding:8px 22px; background:var(--bg); border-bottom:1px solid var(--line); }
.controls .btn { font-size:12px; padding:4px 9px; }
.bookhead { border-bottom:1px solid var(--line); margin-bottom:10px; }
.bookhead .crumb { margin:0; font-size:13px; color:var(--muted); }
.bookhead h1 { margin:6px 0 4px; font-size:23px; line-height:1.3; }
.bookhead .meta { color:var(--muted); font-size:13px; display:flex; gap:10px; flex-wrap:wrap; }
.reading { font-size:var(--reading-font); }
.reading h1,.reading h2,.reading h3 { margin-top:1.5em; line-height:1.3; scroll-margin-top:60px; }
.reading p { margin:.8em 0; }
.reading blockquote { border-left:3px solid var(--line); margin:1em 0; padding:.2em 1em; color:var(--muted); }
.reading pre { background:var(--chip); padding:12px; border-radius:8px; overflow:auto; }
.reading code { background:var(--chip); padding:1px 5px; border-radius:4px; font-size:.9em; }
hr.page { border:none; border-top:1px dashed var(--line); margin:2em 0 1em; }
.page-n { display:block; text-align:center; color:var(--muted); font-size:12px; margin-top:-1.4em; }

@media (max-width:820px){
  nav.toc { display:none; }
  ul.booklist { grid-template-columns:1fr; }
}
"""

JS_APP = r"""
var CATS=[], LANG='all', Q='', SORT='title';
function setLang(l){ LANG=l; document.querySelectorAll('.lf').forEach(b=>b.classList.remove('active'));
  document.querySelector('.lf.'+l).classList.add('active'); apply(); }
function setCat(c){ CATS = (CATS.includes(c)) ? CATS.filter(x=>x!==c) : [c];
  document.querySelectorAll('.cat').forEach(b=>b.classList.toggle('active', CATS.includes(b.dataset.cat)));
  apply(); }
function setSort(s){ SORT=s; document.querySelectorAll('.sort').forEach(b=>b.classList.remove('active'));
  document.querySelector('.sort.'+s).classList.add('active'); apply(); }
function apply(){
  Q=document.getElementById('q').value.trim().toLowerCase();
  var rows=Array.prototype.slice.call(document.querySelectorAll('li.book'));
  var n=0;
  rows.forEach(li=>{
    var t=li.dataset.title, a=li.dataset.author||'', c=li.dataset.cat||'', l=li.dataset.lang;
    var idx=window.BOOK_INDEX ? window.BOOK_INDEX[li.dataset.slug] : null;
    var ok=true;
    if(LANG!=='all' && l!==LANG) ok=false;
    if(CATS.length && !CATS.includes(c)) ok=false;
    if(Q){
      var hay=(t+' '+a+' '+c).toLowerCase();
      if(idx){ hay += ' '+(idx.intro||'')+' '+(idx.headings||[]).join(' '); }
      if(hay.indexOf(Q)<0) ok=false;
    }
    li.style.display=ok?'':'none'; if(ok) n++;
  });
  document.getElementById('empty').style.display=n?'none':'block';
  document.getElementById('cnt').textContent=n+' / '+rows.length+' 本';
}
function sortRows(){
  var ul=document.getElementById('list');
  var rows=Array.prototype.slice.call(ul.querySelectorAll('li.book'));
  rows.sort((x,y)=>{
    if(SORT==='title') return x.dataset.title.localeCompare(y.dataset.title);
    if(SORT==='author') return (x.dataset.author||'~').localeCompare(y.dataset.author||'~');
    return 0;
  });
  rows.forEach(r=>ul.appendChild(r));
}
document.getElementById('q').addEventListener('input', apply);
document.addEventListener('DOMContentLoaded', function(){ sortRows(); apply(); });
"""

JS_BOOK = r"""
function toggleDark(){ var b=document.body; b.classList.toggle('dark');
  localStorage.setItem('zdark', b.classList.contains('dark')?'1':'0'); }
function setFont(d){ var s=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--reading-font'));
  s=Math.max(14,Math.min(24,s+d)); document.documentElement.style.setProperty('--reading-font',s+'px');
  localStorage.setItem('zfont',s); }
function setWidth(d){ var w=parseInt(getComputedStyle(document.documentElement).getPropertyValue('--reading-w'));
  w=Math.max(560,Math.min(960,w+d)); document.documentElement.style.setProperty('--reading-w',w+'px');
  localStorage.setItem('zw',w); }
(function(){ var d=localStorage.getItem('zdark'); if(d==='1') document.body.classList.add('dark');
  var f=localStorage.getItem('zfont'); if(f) document.documentElement.style.setProperty('--reading-font',f+'px');
  var w=localStorage.getItem('zw'); if(w) document.documentElement.style.setProperty('--reading-w',w+'px'); })();
"""


def render_index(manifest):
    books = manifest["books"]
    # 主题清单（用于筛选条）
    cats = sorted({b.get("category", "其他") for b in books})
    cat_chips = "".join(
        f'<button class="btn cat" data-cat="{html.escape(c)}" onclick="setCat(\'{html.escape(c)}\')">{html.escape(c)}</button>'
        for c in cats)
    items = []
    for b in sorted(books, key=lambda x: x["title"].lower()):
        rel = f"books/{b['slug']}/index.html"
        lang = b["language"]
        badge = "中" if lang == "zh" else "EN"
        author = b.get("author") or ""
        cat = b.get("category", "其他")
        meta_bits = [f'<span class="tag {lang}">{badge}</span>',
                     f'<span class="tag">{html.escape(cat)}</span>']
        if author:
            meta_bits.append(f'<span class="meta-author">{html.escape(author)}</span>')
        meta_bits.append(f'{b["chars"]:,} 字')
        items.append(
            f'<li class="book" data-title="{html.escape(b["title"].lower())}" '
            f'data-author="{html.escape(author.lower())}" data-cat="{html.escape(cat)}" '
            f'data-lang="{lang}" data-slug="{html.escape(b["slug"])}">'
            f'<a class="title" href="{rel}">{html.escape(b["title"])}</a>'
            f'<span class="meta">{" ".join(meta_bits)}</span></li>'
        )
    list_html = "\n".join(items)
    body = f"""<header class="top">
  <h1>Z-Library 阅读站</h1>
  <p class="sub">{manifest["count"]} 本书 · 由扫描 / 文本 PDF 提取整理 · 支持全文检索</p>
  <div class="toolbar">
    <input id="q" type="search" placeholder="搜索书名 / 作者 / 正文…">
    <button class="btn lf all active" onclick="setLang('all')">全部</button>
    <button class="btn lf zh" onclick="setLang('zh')">中文</button>
    <button class="btn lf en" onclick="setLang('en')">English</button>
    <button class="btn sort title active" onclick="setSort('title')">按书名</button>
    <button class="btn sort author" onclick="setSort('author')">按作者</button>
  </div>
  <div class="chips">{cat_chips}</div>
  <div class="count" id="cnt"></div>
</header>
<main>
  <ul class="booklist" id="list">
{list_html}
  </ul>
  <p id="empty" class="empty" style="display:none">没有匹配的书。</p>
</main>
<footer>由 build_site.py 生成 · 纯静态 · GitHub Pages 发布</footer>
<script src="assets/search.js"></script>
<script src="assets/app.js"></script>
"""
    return PAGE_HEAD.format(lang="zh", title="Z-Library 阅读站", css="assets/style.css") + body + "</body></html>"


def render_book(meta, content_html, toc):
    lang = "zh" if meta["language"] == "zh" else "en"
    badge = "中文" if meta["language"] == "zh" else "English"
    back = "../../index.html"
    author = meta.get("author") or ""
    cat = meta.get("category", "其他")
    if toc:
        toc_html = "<ol>" + "".join(
            f'<li class="lv{lv}"><a href="#{aid}">{html.escape(txt)}</a></li>' for lv, txt, aid in toc
        ) + "</ol>"
    else:
        toc_html = '<p class="empty-toc">（本书未检测到章节标题）</p>'
    meta_bits = [f'[{badge}]', f'主题：{cat}', f'来源：{meta["pipeline"]}', f'{meta["chars"]:,} 字',
                 f'校对：{"是" if meta.get("has_fixed") else "否"}']
    if author:
        meta_bits.insert(1, f'作者：{author}')
    body = f"""<nav class="toc">
  <h4>目录</h4>
  {toc_html}
</nav>
<div class="readcol">
  <div class="controls">
    <button class="btn" onclick="setFont(-1)">A−</button>
    <button class="btn" onclick="setFont(1)">A+</button>
    <button class="btn" onclick="setWidth(-80)">窄</button>
    <button class="btn" onclick="setWidth(80)">宽</button>
    <button class="btn" onclick="toggleDark()">夜间</button>
  </div>
  <div class="readwrap">
    <header class="bookhead">
      <p class="crumb"><a href="{back}">← 书架</a></p>
      <h1>{html.escape(meta["title"])}</h1>
      <p class="meta">{' · '.join(html.escape(m) for m in meta_bits)}</p>
    </header>
    <main class="reading">
{content_html}
    </main>
    <footer><a href="{back}">← 返回书架</a></footer>
  </div>
</div>
"""
    return PAGE_HEAD.format(lang=lang, title=html.escape(meta["title"]),
                            css="../../assets/style.css") + body + "</body></html>"


def build_search_index(manifest):
    """生成全文检索索引：每本书含标题/作者/主题/正文片段/章节。"""
    index = {}
    for b in manifest["books"]:
        slug = b["slug"]
        cp = os.path.join(config.BOOKS_DIR, slug, "content.md")
        raw = open(cp, "r", encoding="utf-8", errors="ignore").read() if os.path.exists(cp) else ""
        # 正文片段：去 markdown 标记后取前 1000 字
        intro = re.sub(r"^#.*$", "", raw, flags=re.MULTILINE)
        intro = re.sub(r"[*_`>#\-]+", " ", intro)
        intro = re.sub(r"\s+", " ", intro).strip()[:1000]
        headings = [ln.lstrip("# ").strip() for ln in raw.splitlines()
                    if re.match(r"^#{1,3}\s+", ln) and not re.match(r"^-+\s*Page", ln.strip()[2:])]
        index[slug] = {
            "title": b["title"], "author": b.get("author") or "",
            "category": b.get("category", "其他"), "intro": intro, "headings": headings,
        }
    return index


def main():
    config.ensure_dirs()
    manifest = json.load(open(config.BOOKS_MANIFEST, "r", encoding="utf-8"))

    # 样式 & 脚本
    os.makedirs(config.SITE_ASSETS_DIR, exist_ok=True)
    open(os.path.join(config.SITE_ASSETS_DIR, "style.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(config.SITE_ASSETS_DIR, "app.js"), "w", encoding="utf-8").write(JS_APP)
    open(os.path.join(config.SITE_ASSETS_DIR, "book.js"), "w", encoding="utf-8").write(JS_BOOK)

    open(os.path.join(config.SITE_DIR, "index.html"), "w", encoding="utf-8").write(render_index(manifest))

    ok = 0
    keep_slugs = set()
    for b in manifest["books"]:
        slug = b["slug"]
        keep_slugs.add(slug)
        cp = os.path.join(config.BOOKS_DIR, slug, "content.md")
        if not os.path.exists(cp):
            continue
        raw = open(cp, "r", encoding="utf-8", errors="ignore").read()
        html_out, toc = md_to_html(raw)
        out_dir = os.path.join(config.SITE_BOOKS_DIR, slug)
        os.makedirs(out_dir, exist_ok=True)
        try:
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
                fh.write(render_book(b, html_out, toc))
            # 每本书阅读页需要的脚本
            open(os.path.join(out_dir, "book.js"), "w", encoding="utf-8").write(JS_BOOK)
            ok += 1
        except (PermissionError, OSError) as e:
            print(f"  [跳过] 写入失败：{slug} — {e}", flush=True)

    # 阅读页脚本引用
    for slug in keep_slugs:
        p = os.path.join(config.SITE_BOOKS_DIR, slug, "index.html")
        if os.path.exists(p):
            s = open(p, "r", encoding="utf-8").read()
            if "assets/book.js" not in s:
                s = s.replace("</body>", '<script src="../../assets/book.js"></script></body>')
                open(p, "w", encoding="utf-8").write(s)

    # 全文检索索引
    idx = build_search_index(manifest)
    with open(os.path.join(config.SITE_ASSETS_DIR, "search.js"), "w", encoding="utf-8") as fh:
        fh.write("window.BOOK_INDEX = " + json.dumps(idx, ensure_ascii=False) + ";")

    # 清理失效页面
    import shutil
    for d in os.listdir(config.SITE_BOOKS_DIR):
        if d not in keep_slugs:
            shutil.rmtree(os.path.join(config.SITE_BOOKS_DIR, d), ignore_errors=True)

    print(f"站点生成完成：索引 1 页 + 阅读页 {ok} 页 + 检索索引 {len(idx)} 本", flush=True)


if __name__ == "__main__":
    main()
