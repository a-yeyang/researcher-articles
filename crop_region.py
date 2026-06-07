#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按指定坐标把原 PDF 某页的矩形区域裁切为无损矢量 PDF(+预览PNG)。
用法: python3 crop_region.py <pdf> <page(从1起)> <x0> <y0> <x1> <y1> <out.pdf>
坐标为 PDF 点坐标(原点左上)。可在 manifest.json / 整页 PNG 上读取参考。"""
import sys, fitz
pdf, page = sys.argv[1], int(sys.argv[2])-1
x0,y0,x1,y1 = map(float, sys.argv[3:7])
out_pdf = sys.argv[7]
src = fitz.open(pdf)
r = fitz.Rect(x0,y0,x1,y1)
out = fitz.open(); np = out.new_page(width=r.width, height=r.height)
np.show_pdf_page(np.rect, src, page, clip=r)
out.save(out_pdf)
png = out_pdf.rsplit('.',1)[0]+'.png'
out[0].get_pixmap(dpi=170).save(png)
print('WROTE', out_pdf, '+', png)
