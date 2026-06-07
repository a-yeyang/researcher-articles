# 论文 LaTeX 无损中文重排规范（subagent 必读）

目标：把一篇英文论文**完整重建**为中文 LaTeX 文档（XeLaTeX+ctex），做到
**图、表、公式、版面无损**，正文译为规范中文。

## 0. 你已拥有的输入（均在 /Users/yye/project/论文 下）
- 原文 PDF：`<原文件名>.pdf`
- 文本：先运行 `pdftotext -layout "<原文件名>.pdf" /tmp/<slug>.txt` 再用 Read 读全文。
- 资产清单：`assets/<slug>/manifest.json`，含每页的：
  - `candidates`：自动识别的图/表候选，字段 `id`（如 `cand_p03_k00`）、`kind`
    (`image`/`vector`/`table`)、`bbox`（PDF 点坐标 [x0,y0,x1,y1]）、`pdf`（无损矢量裁切文件名）。
  - `captions`：识别到的图表题注（`label` 如 "Figure 1"/"Table 2"、`text`、`bbox`）。
  - `overlay`：整页 PNG（红框=候选、蓝框=题注），路径 `assets/<slug>/_pages/pNN.png`。
- 翻译规范：`译文/_md/TRANSLATION_GUIDE.md`（术语/公式/引用处理规则，必须遵守）。

## 1. 工作流程
1. 读 `TRANSLATION_GUIDE.md` 和本文件。
2. `pdftotext -layout` 提取全文并 Read。
3. **看图理解版面**：用 Read 打开需要的 `assets/<slug>/_pages/pNN.png`（整页）与候选预览
   `assets/<slug>/<id>.png`，弄清每页有哪些图/表/公式、它们与正文的对应关系。
4. 写 `latex/<slug>/<slug>.tex`（见模板）。
5. 编译：`bash compile_tex.sh latex/<slug>/<slug>.tex`，按报错修改，直到输出 `PASS`。
6. 拷贝结果：`cp "latex/<slug>/<slug>.pdf" "译文/<输出名>.中文.pdf"`（覆盖旧版纯文字 PDF）。
7. 用 `python3 render_page.py latex/<slug>/<slug>.pdf <页> /tmp/chk.png` 抽查几页，Read 确认中文/图表正常。

## 2. 文档模板（直接复制，按需增删宏包）
```latex
\documentclass[11pt,UTF8,fontset=fandol]{ctexart}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx,float,caption,subcaption}
\usepackage{booktabs,array,multirow,makecell}
\usepackage{geometry,enumitem,xcolor}
\usepackage[hidelinks]{hyperref}
\usepackage{url}
\geometry{margin=2.3cm}
\graphicspath{{/Users/yye/project/论文/assets/<slug>/}}   % 绝对路径，务必改成本篇 slug
\captionsetup{font=small,labelfont=bf}
\setlength{\parskip}{0.4em}
\title{\textbf{<中文主标题>}}
\author{<作者，姓名机构不译，可括注中文>}
\date{}
\begin{document}
\maketitle
\begin{abstract}
<摘要中文译文>
\end{abstract}
% ... 正文 ...
\end{document}
```

## 3. 图（Figure）
- 在 manifest 里按页找到对应候选，用其 `pdf`（矢量无损）嵌入：
```latex
\begin{figure}[H]\centering
  \includegraphics[width=0.85\linewidth]{cand_p03_k00.pdf}
  \caption{<译后题注，如：Transformer 的整体架构。>}
  \label{fig:1}
\end{figure}
```
- 一张图被拆成多个候选（如 Figure 2 左右两半）时，**重新裁一个并集区域**：
  先在整页 PNG 上估读包住整图的坐标，再
  `python3 crop_region.py "<pdf>" <页> x0 y0 x1 y1 assets/<slug>/fig2.pdf`，
  然后 Read `fig2.png` 确认裁切完整，再 `\includegraphics{fig2.pdf}`。
- **图内文字保持原文**（坐标轴/图例等不改），这是"无损还原"的要求。
- 图的位置尽量还原原文（紧邻首次引用处）。宽度按版面调（`0.6~1.0\linewidth`）。

## 4. 表（Table）
按情况二选一：
- **简单/无边框的数值表**（多数性能表）：用 booktabs **重排为 LaTeX 表格**，
  表头译中文、数字与数学符号原样保留、术语按规范括注英文。例：
```latex
\begin{table}[H]\centering\caption{<译后题注>}
\begin{tabular}{lccc}
\toprule 模型 & BLEU & 参数量 & 训练成本 \\ \midrule
Transformer (base) & 27.3 & 65M & $3.3\times10^{18}$ \\ \bottomrule
\end{tabular}\end{table}
```
- **结构复杂/含合并单元格/排版难以复刻**的表：当作图处理——
  用 manifest 的 table 候选 `pdf`，或 `crop_region.py` 裁切原表区域后 `\includegraphics`，
  题注译中文。确保不丢任何数据。
- 不论哪种，表内**数据一字不差**。

## 5. 公式
- 行内 `$...$`，独立公式 `\[...\]` 或 `equation`/`align`。
- pdftotext 对公式会错乱：**务必用 `render_page.py` 渲染该页/该区域 PNG，Read 后照着原样转写**为
  正确 LaTeX，核对每个上下标、希腊字母、求和/积分号、矩阵。
- 编号公式可保留原编号（用文字或 `\tag{3}`）。
- 实在过于复杂、无把握转写正确的公式，**裁切为图片嵌入**（同图处理），保证无损。

## 6. 特殊字符转义（极易导致编译失败，务必处理）
正文中的这些字符必须转义：`% -> \%`，`& -> \&`，`# -> \#`，`_ -> \_`，
`$ -> \$`（指货币/字面美元，数学环境内不转），`{ } -> \{ \}`，`~ -> \textasciitilde{}`，
`^ -> \textasciicircum{}`，反斜杠 `-> \textbackslash{}`。
网址用 `\url{...}`。引用标记 `[1]`、`[2,3]` 原样保留为普通文本。

## 7. 参考文献
- 小标题译为"参考文献"（`\section*{参考文献}`）。
- 条目**保留英文原文**，用 `\begin{enumerate}[leftmargin=2em]` 列出或逐条 `\par`；
  注意转义条目中的 `%&#_` 等字符，网址用 `\url`。不必翻译。

## 8. 完整性与质量
- **全文翻译，不得省略/概括**：标题、作者机构、摘要、所有章节小节、脚注、附录、所有图表题注。
- 章节层级用 `\section`/`\subsection`/`\subsubsection` 还原。
- 术语全文统一；模型/数据集/方法专名保留英文；首次出现的中文术语括注英文原文。
- 反复编译直到 `PASS`，且抽查页面渲染正常（无缺字、图表完整）。
