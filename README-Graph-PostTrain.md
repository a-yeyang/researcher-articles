# 图 × 大模型 × 后训练：顶会论文中文精读导读（2024–2025）

本目录收录「大语言模型(LLM) × 图(Graph) × 后训练(SFT / DPO / RLHF / RL / PEFT)」方向、
来自六大顶会（ICLR / NeurIPS / ICML / AAAI / ACL / KDD）的高引代表论文的**中文精读导读**，
面向初学者用大白话讲清每篇的核心思想、方法（含公式逐条拆解）与实验。

> **版权说明**：本仓库仅收录**原创撰写的中文精读导读**（讲解 + 摘要与关键句翻译 +
> 用于讲解的少量配图 + 结果数据重述）及其 LaTeX 源码；**不收录受版权保护的原始论文 PDF
> 与整页渲染图**（见 `.gitignore`）。原文请通过下方 arXiv / 代码链接获取。
> 引用数为 2026 年中 Semantic Scholar 快照，仅供参考。

## 论文清单（10 篇）

| 论文 | 年 / 会议 | 引用 | 后训练手段 | 代码 | 导读 |
|---|---|---|---|---|---|
| **G-Retriever** | NeurIPS 2024 | ~279 | 图RAG + 软提示/LoRA | [code](https://github.com/XiaoxinHe/G-Retriever) | `译文/G-Retriever.精读导读.pdf` |
| **LLaGA** | ICML 2024 | 高 | 投影器对齐微调 | [code](https://github.com/VITA-Group/LLaGA) | `译文/LLaGA.精读导读.pdf` |
| **InstructGraph** | ACL 2024 (Findings) | ~73 | 指令微调 + DPO | [code](https://github.com/wjn1996/InstructGraph) | `译文/InstructGraph.精读导读.pdf` |
| **HiGPT** | KDD 2024 | ~70 | 异质图指令微调 | [code](https://github.com/HKUDS/HiGPT) | `译文/HiGPT.精读导读.pdf` |
| **GraphWiz** | KDD 2024 | ~65 | 指令微调 + DPO | [code](https://github.com/nuochenpku/Graph-Reasoning-LLM) | `译文/GraphWiz.精读导读.pdf` |
| **KG-Agent** | ACL 2025 | ~116 | 代码式指令微调（7B Agent） | — | `译文/KG-Agent.精读导读.pdf` |
| **UniGraph** | KDD 2025 | ~59 | LM + GNN 联合自监督 | [code](https://github.com/yf-he/UniGraph) | `译文/UniGraph.精读导读.pdf` |
| **G1** ★ | NeurIPS 2025 | 上升中 | **强化学习 (GRPO)** | [code](https://github.com/PKU-ML/G1) | `译文/G1.精读导读.pdf` |
| **SSQR**（KG×LLM） | ACL 2025 | ~18 | 结构量化 + 微调 | — | `译文/Self-Supervised-Quantized-Representation.精读导读.pdf` |
| **When Do LLMs Help…** | ICML 2025 | ~18 | 实证分析 | — | `译文/When-Do-LLMs-Help-Node-Classification.精读导读.pdf` |

## 五条技术路线（如何把"图"塞进 LLM 并后训练）

- **检索 + 轻量微调**：G-Retriever（图上 RAG + 软提示）
- **对齐 / 投影 / 量化**：LLaGA（投影器）、UniGraph（LM+GNN 联合预训练）、SSQR（结构量化进词表）
- **指令微调（±DPO）**：InstructGraph、HiGPT、GraphWiz、KG-Agent
- **强化学习**：G1（可验证奖励，2025 新路线 ★）
- **实证分析**：When Do LLMs Help with Node Classification（告诉你"何时该用、何时别用"）

## 每篇导读结构（统一 10 节）

论文卡片 → 解决什么问题 → 摘要中译 → 核心贡献 → 预备知识（小白补丁卡）→ 数据集/任务 →
**方法逐节精讲（架构图 + 公式逐条拆解）** → 实验与结果表解读 → 小白知识点速查卡 →
一句话总结与谱系定位。

## 关于 2026

截至 2026 年年中，六大顶会中仅 AAAI 2026、ICLR 2026 已召开，相关论文引用尚未积累
（如 GNN-as-Judge @ICLR 2026、GraphIF @AAAI 2026）。待下半年 ICML / KDD / NeurIPS / ACL 2026
召开、引用稳定后再补充正式榜单与导读。
