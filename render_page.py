#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把原 PDF 的某一页(或某页某区域)渲染为清晰 PNG，供目视精确转写公式/图表。
用法:
  python3 render_page.py <pdf> <page(从1起)> <out.png> [dpi=160]
  python3 render_page.py <pdf> <page> <out.png> <dpi> <x0> <y0> <x1> <y1>   # 仅渲染区域
"""
import sys, fitz
pdf = sys.argv[1]; page = int(sys.argv[2]) - 1; out = sys.argv[3]
dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 160
src = fitz.open(pdf); pg = src[page]
clip = None
if len(sys.argv) >= 9:
    clip = fitz.Rect(*map(float, sys.argv[5:9])) if len(sys.argv) == 9 else None
if len(sys.argv) == 10:  # dpi + 4 coords
    clip = fitz.Rect(*map(float, sys.argv[6:10]))
pg.get_pixmap(dpi=dpi, clip=clip).save(out)
print("WROTE", out, "dpi", dpi, "clip", clip)
