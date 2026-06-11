# 强化学习 × 智能体（RL + Agent）顶会论文 · 中文精读导读

本目录收录 **2024–2025 年「用强化学习训练/优化大模型智能体（agentic RL）」方向、顶会高引论文** 的 **中文精读导读**（每篇一份 PDF），并附一份总览调研报告。面向 AI 应用开发的初学者，用大白话讲清每篇的核心思想与实验。

> ⚠️ **版权声明（请先读）**
> - 本仓库内的「精读导读」是**转化性学习材料**：以中文讲解、转述、关键句翻译为主，**并非原文逐字全文翻译**。
> - 每份导读中**至多引用原论文 1 张架构图**用于教学说明，已标注出处；**不包含原始论文 PDF**——请通过下表「原文」链接到官方渠道获取。
> - 原始论文及其图表的版权归原作者/出版方所有。如有侵权请联系删除。

## 论文清单（引用数据：Semantic Scholar，查询日 2026-06-10）

### 2024 年（均发表于 ICLR/NeurIPS/ICML/AAAI/ACL/KDD）
| 论文 | 会议 | 引用 | 原文 | 代码 | 导读 PDF |
|---|---|--:|---|---|---|
| ETO（Trial and Error） | ACL 2024 | 181 | [arXiv 2403.02502](https://arxiv.org/abs/2403.02502) | [Yifan-Song793/ETO](https://github.com/Yifan-Song793/ETO) | `译文/ETO - Trial and Error.精读导读.pdf` |
| ArCHer | ICML 2024 | 180 | [arXiv 2402.19446](https://arxiv.org/abs/2402.19446) | [YifeiZhou02/ArCHer](https://github.com/YifeiZhou02/ArCHer) | `译文/ArCHer.精读导读.pdf` |
| DigiRL | NeurIPS 2024 | 177 | [arXiv 2406.11896](https://arxiv.org/abs/2406.11896) | [DigiRL-agent/digirl](https://github.com/DigiRL-agent/digirl) | `译文/DigiRL.精读导读.pdf` |
| StepCoder | ACL 2024 | — | [arXiv 2402.01391](https://arxiv.org/abs/2402.01391) | [Ablustrund/APPS_Plus](https://github.com/Ablustrund/APPS_Plus) | `译文/StepCoder.精读导读.pdf` |
| AGILE | NeurIPS 2024 | 49 | [arXiv 2405.14751](https://arxiv.org/abs/2405.14751) | [bytarnish/AGILE](https://github.com/bytarnish/AGILE) | `译文/AGILE.精读导读.pdf` |

### 2025–2026 年（含领域标杆）
| 论文 | 会议 | 引用 | 原文 | 代码 | 发表链接 | 导读 PDF |
|---|---|--:|---|---|---|---|
| Search-R1 | COLM 2025 | 1068 | [arXiv 2503.09516](https://arxiv.org/abs/2503.09516) | [PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1) | [COLM](https://arxiv.org/abs/2503.09516v5) | `译文/Search-R1.精读导读.pdf` |
| ReTool | **ICLR 2026** ✅ | 297 | [arXiv 2504.11536](https://arxiv.org/abs/2504.11536) | [ReTool-RL/ReTool](https://github.com/ReTool-RL/ReTool) | [OpenReview](https://openreview.net/forum?id=tRk1nofSmz) | `译文/ReTool.精读导读.pdf` |
| ToolRL | NeurIPS 2025 | 262 | [arXiv 2504.13958](https://arxiv.org/abs/2504.13958) | [qiancheng0/ToolRL](https://github.com/qiancheng0/ToolRL) | [OpenReview](https://openreview.net/forum?id=eOLdGbXT6t) | `译文/ToolRL.精读导读.pdf` |
| ~~UI-TARS~~ | ⚠️ **未发表**（arXiv） | 449 | [arXiv 2501.12326](https://arxiv.org/abs/2501.12326) | [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) | — | `译文/[未发表] UI-TARS.精读导读.pdf` |
| ~~RAGEN~~ | ⚠️ **未发表**（arXiv） | 229 | [arXiv 2504.20073](https://arxiv.org/abs/2504.20073) | [RAGEN-AI/RAGEN](https://github.com/RAGEN-AI/RAGEN) | — | `译文/[未发表] RAGEN.精读导读.pdf` |

> 说明：StepCoder 引用数查询当日因 API 限流未取到；GRPO（6757）、DeepSeek-R1（5387）引用更高，但属"推理 RL"而非智能体，未计入本榜（详见调研报告）。引用数随时间变化，仅供同年排序参考。
>
> ⚠️ **2026-06-10 清洗**：UI-TARS 与 RAGEN 截至查询日仍为 arXiv 预印本，未被任何顶会正式接收。ReTool 已确认发表于 ICLR 2026（此前标注为 arXiv）。

## 目录结构
- `RL-Agent顶会论文调研报告.md` —— 总览报告（领域扫盲 + 10 篇核心思想/实验 + 学习路线）
- `译文/*.精读导读.pdf` —— 10 篇中文精读导读
- `latex/<slug>/<slug>.tex` —— 各篇导读的 LaTeX 源码（XeLaTeX + ctexart）
- `assets/<slug>/` —— 各篇导读所用的那 1 张架构图（矢量裁切）

## 每篇导读包含什么
标题页与论文卡片 → 小白知识卡（背景概念）→ 摘要全译 → 逐节精读（关键句翻译 + 大白话讲解 + 公式逐符号拆解）→ 方法架构图讲解 → 实验解读（数据集/基线/结果表）→ 核心 takeaways 与对 AI 应用开发的启示。
