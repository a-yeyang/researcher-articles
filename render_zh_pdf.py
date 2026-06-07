#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将翻译后的 Markdown 文本渲染为中文排版的 PDF。
用法: python3 render_zh_pdf.py input.md "输出标题" output.pdf
支持: # 一级标题  ## 二级  ### 三级  #### 四级
      普通段落、- 或 * 列表、1. 有序列表、> 引用、--- 分隔线
      **加粗**、*斜体*、`代码`
公式/英文术语原样保留。
"""
import sys, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                ListFlowable, ListItem, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---- 注册中文字体 ----
SONGTI = "/System/Library/Fonts/Songti.ttc"
HEITI  = "/System/Library/Fonts/STHeiti Medium.ttc"
try:
    pdfmetrics.registerFont(TTFont("Songti",  SONGTI, subfontIndex=0))
    BODY_FONT = "Songti"
except Exception:
    pdfmetrics.registerFont(TTFont("Songti", HEITI, subfontIndex=0))
    BODY_FONT = "Songti"
try:
    pdfmetrics.registerFont(TTFont("Heiti", HEITI, subfontIndex=0))
    HEAD_FONT = "Heiti"
except Exception:
    HEAD_FONT = BODY_FONT

styles = getSampleStyleSheet()
def mk(name, **kw):
    return ParagraphStyle(name, **kw)

TITLE  = mk("zhTitle", fontName=HEAD_FONT, fontSize=18, leading=26,
            alignment=TA_CENTER, spaceAfter=14, spaceBefore=6)
H1 = mk("zhH1", fontName=HEAD_FONT, fontSize=15, leading=22, spaceBefore=14, spaceAfter=8)
H2 = mk("zhH2", fontName=HEAD_FONT, fontSize=13, leading=20, spaceBefore=12, spaceAfter=6)
H3 = mk("zhH3", fontName=HEAD_FONT, fontSize=11.5, leading=18, spaceBefore=10, spaceAfter=5)
H4 = mk("zhH4", fontName=HEAD_FONT, fontSize=10.5, leading=16, spaceBefore=8, spaceAfter=4)
BODY = mk("zhBody", fontName=BODY_FONT, fontSize=10.5, leading=18,
          alignment=TA_JUSTIFY, spaceAfter=6, firstLineIndent=0)
QUOTE = mk("zhQuote", fontName=BODY_FONT, fontSize=10, leading=17,
           leftIndent=18, textColor="#444444", spaceAfter=6)
LISTSTY = mk("zhList", fontName=BODY_FONT, fontSize=10.5, leading=17, spaceAfter=2)

def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r'<font name="Courier">\1</font>', text)
    return text

def build(md_path, title, out_path):
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    story = []
    if title:
        story.append(Paragraph(inline(title), TITLE))
        story.append(HRFlowable(width="100%", thickness=0.8, color="#888888",
                                spaceBefore=2, spaceAfter=10))
    buf = []
    list_buf = []
    list_ordered = False

    def flush_para():
        if buf:
            story.append(Paragraph(inline(" ".join(buf).strip()), BODY))
            buf.clear()

    def flush_list():
        nonlocal list_buf, list_ordered
        if list_buf:
            items = [ListItem(Paragraph(inline(t), LISTSTY), leftIndent=14)
                     for t in list_buf]
            story.append(ListFlowable(
                items, bulletType=("1" if list_ordered else "bullet"),
                start=("1" if list_ordered else None),
                bulletFontName=BODY_FONT, leftIndent=16))
            list_buf = []

    for raw in lines:
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush_para(); flush_list(); continue
        if re.match(r"^#{1,6}\s", s):
            flush_para(); flush_list()
            level = len(s) - len(s.lstrip("#"))
            txt = s.lstrip("#").strip()
            story.append(Paragraph(inline(txt), {1:H1,2:H2,3:H3}.get(level, H4)))
            continue
        if s in ("---", "***", "___"):
            flush_para(); flush_list()
            story.append(HRFlowable(width="100%", thickness=0.5,
                                    color="#bbbbbb", spaceBefore=4, spaceAfter=8))
            continue
        m = re.match(r"^(\d+)[.)]\s+(.*)", s)
        if m:
            flush_para()
            if list_buf and not list_ordered:
                flush_list()
            list_ordered = True
            list_buf.append(m.group(2)); continue
        if re.match(r"^[-*+]\s+", s):
            flush_para()
            if list_buf and list_ordered:
                flush_list()
            list_ordered = False
            list_buf.append(re.sub(r"^[-*+]\s+", "", s)); continue
        if s.startswith(">"):
            flush_para(); flush_list()
            story.append(Paragraph(inline(s.lstrip(">").strip()), QUOTE)); continue
        # 普通段落行
        flush_list()
        buf.append(s)
    flush_para(); flush_list()

    doc = SimpleDocTemplate(out_path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm,
                            title=title)
    doc.build(story)
    print("WROTE", out_path)

if __name__ == "__main__":
    md, title, out = sys.argv[1], sys.argv[2], sys.argv[3]
    build(md, title, out)
