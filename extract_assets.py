#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
为单篇论文抽取"图/表"候选区域，裁切为无损矢量 PDF + 预览 PNG，
并渲染带编号候选框的整页 PNG 供 subagent 目视核对。

用法: python3 extract_assets.py <pdf路径> <slug>
产物目录: assets/<slug>/
  - manifest.json          候选清单(含 bbox/页码/类型/邻近标题文本)
  - _pages/pNN.png         整页(已叠加红色候选框+编号)
  - cand_pNN_kKK.pdf       候选区域矢量裁切(用于 \includegraphics)
  - cand_pNN_kKK.png       候选区域预览
另含工具脚本 crop_region.py 供按需重新裁切。
"""
import sys, os, json, re
import fitz

CAP_RE = re.compile(r'^\s*(Figure|Fig\.?|Table|TABLE|FIGURE|Algorithm|图|表|算法)\s*\.?\s*(\d+)', re.I)

def rects_overlap_ratio(a, b):
    inter = a & b
    if inter.is_empty:
        return 0.0
    ia = abs(inter)
    return ia / min(abs(a), abs(b)) if min(abs(a), abs(b)) else 0.0

def merge_candidates(cands):
    """合并高度重叠的候选框(保留较大者/取并集)。"""
    out = []
    used = [False]*len(cands)
    for i, c in enumerate(cands):
        if used[i]:
            continue
        r = fitz.Rect(c['bbox'])
        kind = c['kind']
        for j in range(i+1, len(cands)):
            if used[j]:
                continue
            r2 = fitz.Rect(cands[j]['bbox'])
            if rects_overlap_ratio(r, r2) > 0.45:
                r = r | r2  # 取并集
                used[j] = True
                if cands[j]['kind'] == 'table':
                    kind = 'table'
        used[i] = True
        out.append({'bbox': [round(v, 1) for v in r], 'kind': kind})
    return out

def detect(page):
    cands = []
    pr = page.rect
    page_area = abs(pr)
    # --- 表格 ---
    try:
        tf = page.find_tables()
        for t in tf.tables:
            r = fitz.Rect(t.bbox)
            if abs(r) > 0.003*page_area:
                cands.append({'bbox': list(r), 'kind': 'table'})
    except Exception:
        pass
    # --- 位图 ---
    try:
        for info in page.get_image_info():
            r = fitz.Rect(info['bbox'])
            if abs(r) > 0.01*page_area:
                cands.append({'bbox': list(r), 'kind': 'image'})
    except Exception:
        pass
    # --- 矢量图形聚类 ---
    try:
        clusters = page.cluster_drawings(x_tolerance=8, y_tolerance=8)
        for r in clusters:
            r = fitz.Rect(r)
            w, h = r.width, r.height
            # 过滤过小、过细(分隔线/下划线)的聚类
            if w < 50 or h < 28:
                continue
            if abs(r) < 0.01*page_area:
                continue
            cands.append({'bbox': list(r), 'kind': 'vector'})
    except Exception:
        pass
    return merge_candidates(cands)

def captions(page):
    caps = []
    d = page.get_text('dict')
    for b in d['blocks']:
        for l in b.get('lines', []):
            txt = ''.join(s['text'] for s in l['spans']).strip()
            m = CAP_RE.match(txt)
            if m:
                caps.append({'bbox': [round(v,1) for v in l['bbox']],
                             'text': txt[:200], 'label': f"{m.group(1)} {m.group(2)}"})
    return caps

def crop_vector(src, pageno, bbox, out_pdf, out_png, dpi=170):
    r = fitz.Rect(bbox)
    out = fitz.open()
    np = out.new_page(width=r.width, height=r.height)
    np.show_pdf_page(np.rect, src, pageno, clip=r)
    out.save(out_pdf)
    pix = out[0].get_pixmap(dpi=dpi)
    pix.save(out_png)
    out.close()

def render_overlay(src, pageno, cands, caps, out_png, dpi=130):
    # 在页面副本上画候选框与编号后渲染
    tmp = fitz.open()
    tmp.insert_pdf(src, from_page=pageno, to_page=pageno)
    pg = tmp[0]
    sh = pg.new_shape()
    for k, c in enumerate(cands):
        r = fitz.Rect(c['bbox'])
        sh.draw_rect(r)
        sh.finish(color=(1, 0, 0), width=1.2)
        pg.insert_text((r.x0+2, max(r.y0-2, pg.rect.y0+8)),
                       f"#{k}", fontsize=9, color=(1, 0, 0))
    for cp in caps:
        r = fitz.Rect(cp['bbox'])
        sh.draw_rect(r)
        sh.finish(color=(0, 0, 1), width=0.8)
    sh.commit()
    pg.get_pixmap(dpi=dpi).save(out_png)
    tmp.close()

def main():
    pdf, slug = sys.argv[1], sys.argv[2]
    base = os.path.join('assets', slug)
    pages_dir = os.path.join(base, '_pages')
    os.makedirs(pages_dir, exist_ok=True)
    src = fitz.open(pdf)
    manifest = {'pdf': pdf, 'slug': slug, 'page_count': src.page_count,
                'page_size': [round(src[0].rect.width,1), round(src[0].rect.height,1)],
                'pages': []}
    for pno in range(src.page_count):
        page = src[pno]
        cands = detect(page)
        caps = captions(page)
        # 裁切候选
        items = []
        for k, c in enumerate(cands):
            stem = f"cand_p{pno+1:02d}_k{k:02d}"
            try:
                crop_vector(src, pno, c['bbox'],
                            os.path.join(base, stem+'.pdf'),
                            os.path.join(base, stem+'.png'))
                items.append({'id': stem, 'kind': c['kind'],
                              'bbox': c['bbox'], 'pdf': stem+'.pdf'})
            except Exception as e:
                items.append({'id': stem, 'kind': c['kind'],
                              'bbox': c['bbox'], 'error': str(e)})
        overlay = os.path.join(pages_dir, f"p{pno+1:02d}.png")
        try:
            render_overlay(src, pno, cands, caps, overlay)
        except Exception as e:
            overlay = f"(overlay error: {e})"
        manifest['pages'].append({'page': pno+1, 'candidates': items,
                                  'captions': caps, 'overlay': overlay})
    with open(os.path.join(base, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    ncand = sum(len(p['candidates']) for p in manifest['pages'])
    ncap = sum(len(p['captions']) for p in manifest['pages'])
    print(f"[{slug}] pages={src.page_count} candidates={ncand} captions={ncap}")
    print(f"manifest: {os.path.join(base,'manifest.json')}")

if __name__ == '__main__':
    main()
