#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Kimi / DeepSeek / BigModel 三个在线文档站爬成 PDF + Markdown 本地知识库。"""
import os, re, sys, time, json, subprocess, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from markdownify import markdownify as md

ROOT = "/Users/yye/project/论文/本地知识库"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HDR = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
WORKERS = 5

SITES = {
    "kimi":     {"sitemap": "https://platform.kimi.com/docs/sitemap.xml", "strip": "/docs/"},
    "deepseek": {"sitemap": "https://api-docs.deepseek.com/zh-cn/sitemap.xml", "strip": "/zh-cn/"},
    "bigmodel": {"sitemap": "https://docs.bigmodel.cn/sitemap.xml", "strip": "/"},
}

def get_urls(sitemap):
    r = requests.get(sitemap, headers=HDR, timeout=30)
    r.encoding = "utf-8"
    return sorted(set(re.findall(r"<loc>(.*?)</loc>", r.text)))

def slug(url, strip):
    path = urllib.parse.urlparse(url).path
    path = urllib.parse.unquote(path)
    if strip != "/" and path.startswith(strip):
        path = path[len(strip):]
    path = path.strip("/")
    if not path:
        path = "index"
    return path.replace("/", "__")

def render_pdf(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 5000:
        return "skip"
    if os.path.exists(out):
        os.remove(out)
    prof = "/tmp/cprofile/" + re.sub(r"[^a-zA-Z0-9]", "_", out)[-60:]
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--no-pdf-header-footer", "--no-first-run", "--disable-background-networking",
           "--disable-extensions", "--user-data-dir=" + prof,
           "--virtual-time-budget=9000", "--run-all-compositor-stages-before-draw",
           "--print-to-pdf=" + out, url]
    # Chrome 写完 PDF 后常因后台网络服务不退出，故启动后轮询文件、写好即杀进程
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    last = -1
    stable = 0
    for _ in range(45):  # 最多 ~22.5s
        if p.poll() is not None:  # 自己退出了
            break
        time.sleep(0.5)
        if os.path.exists(out):
            sz = os.path.getsize(out)
            if sz > 5000 and sz == last:
                stable += 1
                if stable >= 2:  # 连续 1s 大小不变 = 写完
                    break
            else:
                stable = 0
            last = sz
    try:
        p.kill()
        p.wait(timeout=5)
    except Exception:
        pass
    return "ok" if os.path.exists(out) and os.path.getsize(out) > 5000 else "empty"

def fetch_md(url, out, site):
    if os.path.exists(out) and os.path.getsize(out) > 50:
        return "skip"
    try:
        if site in ("kimi", "bigmodel"):
            r = requests.get(url + ".md", headers=HDR, timeout=30)
            if r.status_code == 200 and "markdown" in r.headers.get("content-type", ""):
                text = r.text
            else:
                return "no-md"
        else:  # deepseek: 从 HTML 提取正文转 markdown
            r = requests.get(url, headers=HDR, timeout=30)
            r.encoding = "utf-8"
            m = re.search(r"<article[^>]*>(.*?)</article>", r.text, re.S)
            html = m.group(1) if m else r.text
            text = md(html, heading_style="ATX", strip=["nav", "script", "style"])
        open(out, "w", encoding="utf-8").write("<!-- source: %s -->\n\n" % url + text)
        return "ok"
    except Exception as e:
        return "err:" + str(e)[:40]

def work(site, url, cfg):
    s = slug(url, cfg["strip"])
    pdf = f"{ROOT}/{site}/pdf/{s}.pdf"
    mdf = f"{ROOT}/{site}/md/{s}.md"
    rp = render_pdf(url, pdf)
    rm = fetch_md(url, mdf, site)
    return (site, s, rp, rm)

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs("/tmp/cprofile", exist_ok=True)
    jobs = []
    for site, cfg in SITES.items():
        if only and site != only:
            continue
        for d in ("pdf", "md"):
            os.makedirs(f"{ROOT}/{site}/{d}", exist_ok=True)
        urls = get_urls(cfg["sitemap"])
        manifest = [{"url": u, "slug": slug(u, cfg["strip"])} for u in urls]
        json.dump(manifest, open(f"{ROOT}/{site}/manifest.json", "w"), ensure_ascii=False, indent=2)
        print(f"[{site}] {len(urls)} pages", flush=True)
        for u in urls:
            jobs.append((site, u, cfg))

    total = len(jobs)
    done = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = [ex.submit(work, s, u, c) for s, u, c in jobs]
        for f in as_completed(futs):
            site, s, rp, rm = f.result()
            done += 1
            el = int(time.time() - t0)
            print(f"  ({done}/{total}) [{el}s] {site}/{s}  pdf={rp} md={rm}", flush=True)
    print(f"DONE {total} pages in {int(time.time()-t0)}s", flush=True)

if __name__ == "__main__":
    main()
