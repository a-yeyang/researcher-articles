# SKILLRL：通过递归式技能增强强化学习实现智能体的自我演化

**SKILLRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning**

## 作者与机构

Peng Xia¹\* Jianwen Chen¹\* Hanyang Wang¹²\* Jiaqi Liu¹ Kaide Zeng¹ Yu Wang³ Siwei Han¹
Yiyang Zhou¹ Xujiang Zhao⁴ Haifeng Chen⁴ Zeyu Zheng⁵ Cihang Xie⁶ Huaxiu Yao¹

¹ UNC-Chapel Hill（北卡罗来纳大学教堂山分校） ² University of Chicago（芝加哥大学） ³ University of California San Diego（加州大学圣迭戈分校） ⁴ NEC Labs America（美国 NEC 实验室） ⁵ University of California Berkeley（加州大学伯克利分校） ⁶ University of California Santa Cruz（加州大学圣克鲁兹分校）

通讯作者：Peng Xia \<pxia@cs.unc.edu\>，Huaxiu Yao \<huaxiu@cs.unc.edu\>。

预印本。2026 年 2 月 10 日。

\* 表示同等贡献。

## 摘要

大语言模型（Large Language Model，LLM）智能体在复杂任务中已展现出令人瞩目的成果，但它们往往孤立地运行，无法从过往经验中学习。现有的基于记忆（memory-based）的方法主要存储原始轨迹（raw trajectories），而这些轨迹往往冗余且噪声繁多，这阻碍了智能体提取对泛化至关重要的高层、可复用的行为模式。本文提出 SKILLRL，一个通过自动技能发现（automatic skill discovery）与递归式演化（recursive evolution）来弥合原始经验与策略改进之间鸿沟的框架。我们的方法引入了一种基于经验的蒸馏（experience-based distillation）机制以构建层次化技能库 SKILLBANK，一种面向通用启发式与任务特定启发式的自适应检索策略，以及一种允许技能库在强化学习过程中与智能体策略协同演化（co-evolve）的递归式演化机制。这些创新在显著减少 token 占用的同时增强了推理效用。在 ALFWorld、WebShop 以及七项搜索增强（search-augmented）任务上的实验结果表明，SKILLRL 取得了当前最优（state-of-the-art）的性能，超越强基线达 15.3% 以上，并在任务复杂度提升时保持稳健。代码已开源于 https://github.com/aiming-lab/SkillRL 。

**图 1.** (a) SKILLRL 流程概览。与以往存储原始轨迹并丢弃失败案例的方法（灰色虚线）不同，SKILLRL 采用基于经验的蒸馏机制，将多样化的经验转化为结构化技能。(b) 在 ALFWorld 验证集（Shridhar et al.）上的性能。与原始 GRPO 及记忆增强的 RL 相比，SKILLRL 实现了更快的收敛和更高的成功率。

## 1. 引言

大语言模型（LLM）智能体（Yao et al., 2022b；Shinn et al., 2023）在各类复杂任务中展现出卓越的能力，例如网页导航（Google, 2025；OpenAI, 2025c）与深度研究（OpenAI, 2025b；Google, 2024；Team et al., 2025），它们通过自然语言与复杂环境进行交互来完成任务。尽管取得了这些进展，但每一次任务执行在很大程度上仍是孤立的（episodic）。当前的 LLM 智能体孤立地运行，无法从过往的成功或失败中学习（Zhang et al., 2025b），这极大地阻碍了它们的演化。因此，一个根本性的挑战依然存在：智能体如何才能高效地从经验中学习，并将这些知识迁移到其他任务上？

现有的面向 LLM 智能体的基于记忆的方法，主要是在采样过程中将原始轨迹直接保存到外部数据库中，以作为未来相似任务的参考（Shinn et al., 2023；Zhao et al., 2024）。这种做法虽然直观，但原始轨迹往往冗长，并包含大量冗余和噪声（Chhikara et al., 2025），使得模型难以提取关键信息。近期的工作尝试压缩轨迹，并通过在线训练（online training）更新记忆库（Zhang et al., 2025b；2026），从而提升记忆效率。然而，这些方法仅仅模仿过往的解决方案，无法提炼出核心原则，也无法调整智能体的内部策略以利用记忆来引导决策。如图 1(a) 中的虚线流程所示，此类方法常常在信息密度与噪声之间的权衡上举步维艰，导致性能次优甚至退化，如图 1(b) 所示。

我们认为，这些方法忽略了一个关键洞见：有效的经验迁移需要抽象（abstraction）。人类专家并不会记住每种情境下的每一个动作；相反，他们发展出技能（skills）（Anthropic, 2024）——紧凑且可复用的策略，这些策略捕捉了如何完成特定子任务的精髓。受此观察启发，我们提出了 SKILLRL，一个通过自动技能发现与递归式技能演化来弥合原始经验与高效策略改进之间鸿沟的框架。

SKILLRL 首先引入了一种基于经验的技能蒸馏（experience-based skill distillation）机制，它从环境 rollout 中收集多样化的轨迹，并施加差异化处理：成功的回合被保留为示范（demonstrations），而失败的回合则被综合为简洁的失败教训（failure lessons），以减轻上下文噪声。其次，我们将这些经验转化为层次化技能库 SKILLBANK，区分用于通用战略指导的通用技能（general skills）与用于任务级启发式的任务特定技能（task-specific skills）。这种抽象使得智能体能够在决策过程中自适应地检索相关技能，在显著减少 token 占用的同时增强推理效用。最后，SKILLRL 在强化学习（reinforcement learning，RL）过程中纳入了一种递归式技能演化机制，其中技能库被视为一个动态组件，而非静态的知识源。通过在每个验证轮次（validation epoch）后分析失败模式以生成新技能或精炼现有技能，我们的方法确保技能库与智能体策略协同演化，从而在任务复杂度提升时保持稳健。如图 1(b) 所示，SKILLRL 实现了显著更快的收敛和更高的渐近性能。

本文的主要贡献是 SKILLRL，一个使 LLM 智能体能够通过自动技能发现与递归式演化来弥合原始经验与策略改进之间鸿沟的框架。通过将冗余轨迹蒸馏进层次化的 SKILLBANK，我们的方法抽象出通用技能与任务特定技能，以高效地引导决策。此外，我们引入了一种递归式演化机制，确保技能库与智能体策略在强化学习过程中协同演化。在 ALFWorld、WebShop 以及七项搜索增强基准上的实验结果表明，SKILLRL 取得了当前最优性能，提升达 15.3%，在任务成功率和推理效用两方面均显著超越当前基于记忆的智能体调优基线。

## 2. 预备知识

**LLM 智能体。** 我们考虑一个在交互式环境 E 中运行的智能体。在每个时间步 t，智能体观察到状态 $o_t \in O$，选择一个动作 $a_t \in A$，并获得奖励 $r_t$ 与下一个观察 $o_{t+1}$。一条轨迹 $\tau = (o_0, a_0, r_0, \ldots, o_T, a_T, r_T)$ 捕捉了一个回合（episode）的交互。任务由自然语言描述 d 指定。一个由参数 θ 参数化的、基于 LLM 的智能体实现了一个策略 $\pi_\theta(a_t | o_{\le t}, d, c)$，其中 c 表示额外的上下文（例如技能、示范）。我们的目标是学习一个在上下文长度约束 $|c| \le L_{max}$ 下最大化期望回报的策略 $\max_\theta \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \gamma^t r_t \right]$。

**组相对策略优化（Group Relative Policy Optimization，GRPO）。** GRPO（Shao et al., 2024）是一种强化学习方法，它通过使用组内（intra-group）相对奖励来优化策略，从而避免训练评论家（critic）。对于每个查询 x，模型采样 G 个回复 $\{y^{(1)}, \ldots, y^{(G)}\}$，并对其评分以得到奖励 $\{R_1, \ldots, R_G\}$。GRPO 计算归一化优势（normalized advantages），并以 PPO 风格的裁剪目标（clipped objective）更新策略（Schulman et al., 2017）：

$$J_{GRPO}(\theta) = \mathbb{E}_{x, \{y_i\}} \left[ \frac{1}{G} \sum_{i=1}^G \min\left( r_i A_i, \text{clip}(r_i, 1-\epsilon, 1+\epsilon) A_i \right) - \beta D_{KL}(\pi_\theta \| \pi_{ref}) \right], \quad (1)$$

其中 $r_i = \frac{\pi_\theta(y_i|x)}{\pi_{old}(y_i|x)}$ 是重要性比率（importance ratio），$A_i = \frac{R_i - \text{mean}(\{R_j\}_{j=1}^G)}{\text{std}(\{R_j\}_{j=1}^G)}$ 是归一化优势，$\epsilon, \beta$ 是超参数，$\pi_{old}$ 是当前更新之前的策略。

## 3. SKILLRL

在本节中，如图 2 所示，我们提出 SKILLRL，一个旨在通过自动技能发现与递归式演化来弥合原始交互经验与策略改进之间鸿沟的框架。SKILLRL 由三个核心组件构成。首先，我们开发了一种基于经验的技能蒸馏机制，将冗余轨迹转化为简洁、可执行的知识。其次，我们将这些蒸馏出的经验组织进一个层次化技能库 S，从而实现对通用专长与任务特定专长的高效检索。最后，我们引入一种递归式技能演化机制，利用 RL 来与智能体策略同步地动态精炼技能库。我们详述这些组件如下：

**图 2.** SKILLRL 框架概览。我们使用基础模型（base model）收集轨迹，将其蒸馏进一个层次化技能库，执行冷启动 SFT（cold-start SFT）以使智能体能够利用技能，随后基于验证失败进行带有动态技能演化的 RL 训练。

### 3.1. 基于经验的技能蒸馏

从环境交互中收集到的原始轨迹 τ 是冗长的，包含探索性动作、回溯以及冗余步骤，这些会掩盖导向成功或失败的关键决策。为将这些经验转化为可执行的知识，我们采用一个教师模型（teacher model）$M_T$ 来将轨迹蒸馏为紧凑、可复用的技能。

具体而言，我们首先在目标环境 E 中部署一个基础 LLM 智能体 $\pi_{base}$ 以收集多样化的轨迹。与以往仅保留成功回合的方法不同，我们刻意同时保留成功轨迹 $T^+ = \{\tau_i : r(\tau_i) = 1\}$ 与失败轨迹 $T^- = \{\tau_i : r(\tau_i) = 0\}$，其中 $r(\tau)$ 表示二元的任务成功指示符。失败轨迹揭示了失败模式（failure modes）和边界条件（boundary conditions），即仅凭成功案例难以推断出的信息。

我们基于轨迹的结果施加差异化处理。对于成功轨迹 $\tau^+ \in T^+$，我们提取导向任务完成的战略模式：

$$s^+ = M_T(\tau^+, d). \quad (2)$$

教师模型识别关键决策点、正确动作背后的推理，以及可迁移到特定任务实例之外的可泛化模式。

对于失败轨迹 $\tau^- \in T^-$，由于其长度与噪声，直接纳入上下文是不可行的。相反，我们综合出简洁的失败教训：

$$s^- = M_T(\tau^-, d). \quad (3)$$

该分析识别出：(1) 失败的发生点，(2) 有缺陷的推理或动作，(3) 本应采取的做法，以及 (4) 用于防止类似失败的通用原则。这将冗长的失败回合转化为反事实（counterfactuals）。

### 3.2. 层次化技能库（SKILLBANK）的构建

遵循 Agent Skills（Anthropic, 2024）的设计原则，我们将蒸馏出的知识组织进一个层次化技能库 SKILLBANK，从而在决策过程中实现对相关专长的高效检索。

**技能组织（Skill Organization）。** 我们将 SKILLBANK 构造为两个层级：1) 通用技能 $S_g$ 捕捉在某一环境内适用于所有任务类型的普适战略原则。这些通常包括探索策略（例如系统化搜索模式、优先探索未访问的位置）、状态管理原则（例如在动作前验证前置条件）以及目标追踪启发式（例如维护进度计数器、仅在验证完成后才终止）。通用技能提供可跨不同任务类别迁移的基础性指导。2) 任务特定技能 $S_k$ 为任务类别 k 编码专门的知识。这些技能捕捉特定领域的动作序列、特定任务的前置条件与约束、任务类型特有的常见失败模式，以及利用任务结构的优化流程。通过在收集过程中按任务类型组织轨迹，我们得以提取细粒度的、类别特定的策略，以补充更宽泛的通用技能。

完整的技能库 SKILLBANK 为 $S_g \cup \bigcup_{k=1}^{S_K} S_k$。每个技能 $s \in$ SKILLBANK 由以下结构组成：一个简洁的名称（例如 systematic exploration）、一个描述策略的原则（principle），以及指定其适用性的应用条件（when to apply）。这种格式在实现高效检索的同时，为应用提供了清晰的指导。

**技能检索（Skill Retrieval）。** 在推理时，给定任务描述 d，智能体检索相关技能以增强其上下文。通用技能 $S_g$ 始终被纳入作为基础性指导。任务特定技能则通过语义相似度进行检索：

$$S_{ret} = \text{TopK}(\{s \in S_k : \text{sim}(e_d, e_s) > \delta\}, K), \quad (4)$$

其中 $e_d, e_s$ 分别是任务描述和技能的嵌入（embeddings），δ 是相似度阈值，K 控制被检索技能的数量。策略随后基于被检索的技能进行条件化：

$$a_t \sim \pi_\theta(a_t | o_{\le t}, d, S_g, S_{ret}). \quad (5)$$

值得注意的是，相比原始轨迹，技能蒸馏实现了 10–20× 的 token 压缩，同时增强而非削弱了原始经验的效用。这种压缩使智能体能够在有限的上下文窗口内利用丰富的经验性知识。

### 3.3. 递归式技能演化

静态的技能库无法预见智能体将遇到的所有场景。随着策略的改进与对新状态区域的探索，智能体会面临现有技能无法提供足够指导的情形。我们在强化学习过程中引入递归式技能演化以应对这一局限，使技能库与智能体策略能够协同演化。

**冷启动初始化（Cold-Start Initialization）。** 在 RL 训练之前，我们应对一个关键挑战：基础智能体尚未学会如何有效利用技能。仅仅向一个未经改变的模型提供技能，所带来的收益有限（Guo et al., 2025）。因此，我们执行一个冷启动监督微调（supervised fine-tuning，SFT）阶段（Ouyang et al., 2022），其中教师模型 $M_T$ 生成 N 条技能增强的推理轨迹 $D_{SFT} = \{(d_i, S_i, \tau_i^*)\}_{i=1}^N$，示范如何在决策过程中检索、解读并应用技能。随后基础模型在这些示范上进行微调：

$$\theta_{sft} = \arg\min_\theta L_{CE}(D_{SFT}; \theta), \quad (6)$$

其中 $L_{CE}$ 表示交叉熵损失（cross-entropy loss）。所得模型 $\pi_{\theta_{sft}}$ 既作为 RL 训练的起点，也作为用于 KL 正则化的参考策略 $\pi_{ref}$。

**递归式技能演化（Recursive Skill Evolution）。** 静态的技能库无法预见智能体将遇到的所有场景。随着策略的改进与对新状态区域的探索，智能体会面临现有技能无法提供足够指导的情形。我们引入递归式技能演化以应对这一局限。该过程始于一个包含基线任务-动作原则的初始技能库。

在每个验证轮次后，我们监测每个任务类别 C 的成功率 $\text{Acc}(C)$。为确保有针对性的增长，演化仅对 $\text{Acc}(C) < \delta$ 的类别触发。随后，我们使用一种多样性感知的分层采样（diversity-aware stratified sampling）策略来收集失败轨迹 $T_{val}^- = \{\tau_j : r(\tau_j) = 0\}_{j=1}^M$：轨迹按类别分组，按失败的严重程度（负奖励）排定优先级，并通过轮询（round-robin）采样进行选取以维持类别熵（categorical entropy）。然后我们将分析这些样本以识别差距：

$$S_{new} = M_T(T_{val}^-, \text{SKILLBANK}). \quad (7)$$

教师模型被提示去：(1) 识别当前技能未覆盖的失败模式，(2) 提出新技能以填补这些差距，以及 (3) 对被证明无效的现有技能提出精炼建议。随后技能库被更新：$\text{SKILLBANK} \leftarrow \text{SKILLBANK} \cup S_{new}$。

这形成了一个良性循环：随着智能体的改进，它会遇到新的挑战，这驱动技能库的扩展，进而促成进一步的改进。

**基于 RL 的策略优化。** 我们使用 GRPO 优化技能增强的策略。对于每个具有描述 d 的任务，智能体首先检索相关技能，然后从当前策略 $\pi_\theta$ 中采样 G 条完整轨迹 $\{\tau^{(1)}, \ldots, \tau^{(G)}\}$。每条轨迹 $\tau^{(i)}$ 获得一个二元奖励 $R_i = r(\tau^{(i)}) \in \{0, 1\}$，指示任务是否成功。每条轨迹的归一化优势计算为：

$$A_i = \frac{R_i - \text{mean}(\{R_j\}_{j=1}^G)}{\text{std}(\{R_j\}_{j=1}^G)}. \quad (8)$$

策略按下式更新：

$$J(\theta) = \mathbb{E}_{d, \{\tau^{(i)}\}} \left[ \frac{1}{G} \sum_{i=1}^G \min\left( \rho_i A_i, \text{clip}(\rho_i, 1-\epsilon, 1+\epsilon) A_i \right) - \beta D_{KL}(\pi_\theta \| \pi_{ref}) \right], \quad (9)$$

其中 $\rho_i = \frac{\pi_\theta(\tau^{(i)}|d, S_g, S_{ret})}{\pi_{old}(\tau^{(i)}|d, S_g, S_{ret})}$ 是在技能增强的上下文上计算的重要性比率。锚定到 $\pi_{ref} = \pi_{\theta_{sft}}$ 的 KL 惩罚确保 RL 优化在提升任务性能的同时，保留已习得的技能利用能力。完整的训练过程总结于算法 1。

### 算法 1 SKILLRL：递归式技能增强 RL

**Require:** 基础模型 $\pi_{base}$，教师 $M_T$，环境 E
**Ensure:** 训练后的策略 $\pi_{\theta^*}$，演化后的技能库 $\text{SKILLBANK}^*$

1: ▷ 基于经验的技能蒸馏
2: $T^+, T^- \leftarrow \text{Rollout}(\pi_{base}, E)$
3: **for all** $\tau^+ \in T^+$ **do**
4: &nbsp;&nbsp;&nbsp;&nbsp; $s^+ \leftarrow M_T(\tau^+)$
5: **end for**
6: **for all** $\tau^- \in T^-$ **do**
7: &nbsp;&nbsp;&nbsp;&nbsp; $s^- \leftarrow M_T(\tau^-)$
8: **end for**
9: ▷ 层次化技能库构建
10: $S_g \leftarrow$ 来自蒸馏经验的通用技能
11: **for all** 任务类型 k **do**
12: &nbsp;&nbsp;&nbsp;&nbsp; $S_k \leftarrow$ 类别 k 的任务特定技能
13: **end for**
14: $\text{SKILLBANK} \leftarrow S_g \cup \bigcup_k S_k$
15: ▷ 通过 RL 进行递归式技能演化
16: // 冷启动初始化
17: $D_{SFT} \leftarrow M_T(E, \text{SKILLBANK})$
18: $\theta \leftarrow \text{SFT}(\pi_{base}, D_{SFT})$；$\pi_{ref} \leftarrow \pi_\theta$
19: // 带有递归式演化的 RL
20: **for** epoch = 1 to N **do**
21: &nbsp;&nbsp;&nbsp;&nbsp; **for all** 任务 d **do**
22: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $S_{ret} \leftarrow \text{Retrieve}(d, \text{SKILLBANK})$
23: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 采样 $\{\tau^{(i)}\}_{i=1}^G \sim \pi_\theta(\cdot | d, S_g, S_{ret})$
24: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 计算 $\{R_i\}_{i=1}^G$ 并通过 GRPO 更新 θ
25: &nbsp;&nbsp;&nbsp;&nbsp; **end for**
26: &nbsp;&nbsp;&nbsp;&nbsp; **if** 验证轮次 **then**
27: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $T_{val}^- \leftarrow$ 失败的验证轨迹
28: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $S_{new} \leftarrow M_T(T_{val}^-, \text{SKILLBANK})$
29: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\text{SKILLBANK} \leftarrow \text{SKILLBANK} \cup S_{new}$
30: &nbsp;&nbsp;&nbsp;&nbsp; **end if**
31: **end for**
32: **return** $\pi_\theta$, SKILLBANK

## 4. 实验

我们在面向 LLM 智能体的九项具有挑战性的基准上评估 SKILLRL：ALFWorld、WebShop 以及七项搜索增强 QA 任务。我们的实验旨在回答以下问题：1) SKILLRL 与当前最优方法相比如何？2) 各组件的贡献是什么？3) 技能库在训练过程中如何演化？4) 技能是否加速了模型的收敛？

### 4.1. 实验设置

**环境。** ALFWorld（Shridhar et al.）是一个与 ALFRED 具身 AI 基准对齐的基于文本的游戏。智能体必须通过文本命令进行导航并与对象交互，以完成家庭任务。WebShop（Yao et al., 2022a）模拟网络购物。智能体在一个逼真的网络界面中导航，以查找并购买符合用户规格的商品。此外，我们还在搜索增强 QA 任务上评估 SKILLRL 的性能，包括单跳（single-hop）QA 数据集（NQ（Kwiatkowski et al., 2019）、TriviaQA（Joshi et al., 2017）和 PopQA（Mallen et al., 2023]））和多跳（multi-hop）QA 数据集（HotpotQA（Yang et al., 2018）、2Wiki（Ho et al., 2020）、MuSiQue（Trivedi et al., 2022）和 Bamboogle（Press et al., 2023]））。

**基线。** 我们将 SKILLRL 与四类有竞争力的方法进行比较。第一，我们纳入闭源 LLM，具体为 GPT-4o（OpenAI, 2024）和 Gemini-2.5-Pro（Comanici et al., 2025），它们代表了通用推理与指令遵循的当前最优水平。第二，我们评估基于提示（prompt-based）的智能体方法或基于记忆的方法，包括依赖上下文提示进行多步推理的 ReAct（Yao et al., 2022b）和 Reflexion（Shinn et al., 2023），以及利用外部记忆或经验池来引导行为而无需参数更新的 Mem0（Chhikara et al., 2025）、ExpeL（Zhao et al., 2024）和 MemP（Fang et al., 2025）。第三，我们考虑基于 RL 的方法，包括基于组（group-based）的在线 RL 算法，如 RLOO（Ahmadian et al., 2024）和 GRPO（Shao et al., 2024），它们通过在轨迹组上进行优势估计来优化策略。最后，我们与记忆增强的基于 RL 的方法进行比较，例如 EvolveR（Wu et al., 2025）、MemRL（Zhang et al., 2026），以及 Mem0+GRPO 与 SimpleMem（Liu et al., 2026）+GRPO 的组合，它们将持久化记忆机制直接集成到强化学习优化过程中以处理长期依赖。对于搜索增强 QA，我们将 SKILLRL 与 R1-Instruct、Search-o1（Li et al., 2025）、Search-R1（Jin et al., 2025）、ZeroSearch（Sun et al., 2025）和 StepSearch（Zheng et al., 2025）进行比较。

**实现细节。** 我们使用 Qwen2.5-7B-Instruct（Bai et al., 2023）作为基础模型，使用 OpenAI o3（OpenAI, 2025a）作为用于技能蒸馏和 SFT 数据生成的教师模型。对于 RL 训练，我们使用 GRPO，学习率为 $1 \times 10^{-6}$，batch size 为 16，组大小（group size）为 8，梯度累积步数为 4。我们设定任务特定技能检索的 $K = 6$，失败轨迹收集的 $\delta = 0.4$。关于训练超参数的更多细节，请参见附录 B.1。

### 4.2. 主要结果

**与基线的比较。** 我们将 SKILLRL 与各基线方法在两个基准上进行比较，如表 1 所示。我们的方法持续超越所有基线，关键观察如下：

1) **相对基于提示方法的显著增益。** SKILLRL 在 ALFWorld 上取得 89.9% 的成功率，在 WebShop 上取得 72.7%，大幅超越最优的基于提示的基线。这一差距表明，尽管上下文学习（in-context learning）能够利用过往经验，但它往往无法从冗长的轨迹中提炼出可执行的知识，也无法从根本上调整智能体的策略。

2) **相对原始 RL 的优越性。** RL 训练带来了可观的增益，但 SKILLRL 持续超越标准的 RL 基线。与 PPO、RLOO 和 GRPO 相比，SKILLRL 取得了最佳的总体性能。值得注意的是，由于 SKILLRL 采用 GRPO 作为其基础优化器，其在 ALFWorld 上相对 GRPO 的 12.3% 绝对提升（从 77.6% 到 89.9%）直接归功于我们的技能增强机制，而非算法上的方差。在 Cool 和 Pick2 等复杂子任务中，SKILLRL 分别以 23.0% 和 22.8% 超越 GRPO，证明结构化的技能先验（skill priors）能在稀疏奖励（sparse-reward）环境中有效加速并增强策略学习。

3) **相对记忆增强 RL 的优势。** SKILLRL 大幅超越现有的记忆增强 RL 框架，这些框架在管理和更新经验的方式上各有不同。MemRL 仅使用 RL 来更新其记忆库而保持策略冻结，无法适应复杂环境，在 ALFWorld 上仅取得 21.4%。EvolveR 联合更新策略与记忆库，显示出改进（43.8%），但仍受限于其对粗糙轨迹存储的依赖。为提供一个更具竞争力的基线，我们实现了 Mem0+GRPO，它将当前最优的基于提示的记忆机制与优化后的策略模型相结合。尽管这一混合方法将性能提升到 ALFWorld 上的 54.7% 和 WebShop 上的 37.5%，但它仍以很大差距落后于 SKILLRL（约 35.2% 的绝对成功率差距）。这些结果验证了我们的核心假设：有效的经验迁移需要高层的技能抽象和一个协同演化的库，而非简单的轨迹压缩或基于提示的记忆检索。

**与闭源模型的比较。** 值得注意的是，使用 Qwen2.5-7B-Instruct 的 SKILLRL 显著超越了规模大得多的闭源模型，如表 1 所示。在 ALFWorld 上，我们的方法以 41.9% 超越 GPT-4o（OpenAI, 2024），以 29.6% 超越 Gemini-2.5-Pro（Comanici et al., 2025）。这表明有效的技能学习能够弥补模型规模的差距，使更小的开源模型通过结构化的经验性知识取得更优的任务性能。

**搜索增强 QA 上的性能。** 如表 2 所示，SKILLRL 取得了 47.1% 的当前最优平均分，显著超越 Search-R1（38.5%）和 EvolveR（43.1%）。关键观察包括：1) **优越的多跳推理**：SKILLRL 在 Bamboogle 等复杂任务中表现出色，以 19.4% 超越 EvolveR。这表明层次化技能能有效引导多步信息综合。2) **强大的泛化能力**：尽管仅在有限的数据集（NQ、HotpotQA）上训练，SKILLRL 在 TriviaQA 和 2Wiki 等域外（OOD）任务上仍保持有竞争力的性能，证实了蒸馏出的搜索策略是任务无关的（task-agnostic）。

**表 1.** 在 ALFWorld 和 WebShop 上的性能。对于 ALFWorld，我们报告每个子任务的平均成功率（%）以及总体结果。对于 WebShop，我们同时报告平均分（Score）和平均成功率（Succ.，%）。∗ 表示从（Feng et al., 2025）复现的结果。最优结果和次优结果分别以红色和蓝色高亮。

| 方法 | Pick | Look | Clean | Heat | Cool | Pick2 | All | Score | Succ. |
|---|---|---|---|---|---|---|---|---|---|
| **闭源 LLM** | | | | | | | | | |
| GPT-4o | 75.3 | 60.8 | 31.2 | 56.7 | 21.6 | 49.8 | 48.0 | 31.8 | 23.7 |
| Gemini-2.5-Pro | 92.8 | 63.3 | 62.1 | 69.0 | 26.6 | 58.7 | 60.3 | 42.5 | 35.9 |
| **Qwen2.5-7B-Instruct** | | | | | | | | | |
| Qwen2.5 | 33.4 | 21.6 | 19.3 | 6.90 | 2.80 | 3.20 | 14.8 | 26.4 | 7.80 |
| **基于提示的智能体或基于记忆的方法** | | | | | | | | | |
| ReAct∗ | 48.5 | 35.4 | 34.3 | 13.2 | 18.2 | 17.6 | 31.2 | 46.2 | 19.5 |
| Reflexion∗ | 62.0 | 41.6 | 44.9 | 30.9 | 36.3 | 23.8 | 42.7 | 58.1 | 28.8 |
| Mem0 | 54.0 | 55.0 | 26.9 | 36.4 | 20.8 | 7.69 | 33.6 | 23.9 | 2.00 |
| ExpeL | 21.0 | 67.0 | 55.0 | 52.0 | 71.0 | 6.00 | 46.3 | 30.9 | 11.2 |
| MemP | 54.3 | 38.5 | 48.1 | 56.2 | 32.0 | 16.7 | 41.4 | 25.3 | 6.40 |
| SimpleMem | 64.5 | 33.3 | 20.0 | 12.5 | 33.3 | 3.84 | 29.7 | 33.2 | 8.59 |
| **基于 RL 的方法** | | | | | | | | | |
| RLOO∗ | 87.6 | 78.2 | 87.3 | 81.3 | 71.9 | 48.9 | 75.5 | 80.3 | 65.7 |
| GRPO∗ | 90.8 | 66.1 | 89.3 | 74.7 | 72.5 | 64.7 | 77.6 | 79.3 | 66.1 |
| **记忆增强的基于 RL 的方法** | | | | | | | | | |
| MemRL | 62.8 | 38.5 | 22.2 | 12.5 | 8.00 | 0.00 | 21.4 | 29.5 | 9.20 |
| EvolveR | 64.9 | 33.3 | 46.4 | 13.3 | 33.3 | 33.3 | 43.8 | 42.5 | 17.6 |
| Mem0+GRPO | 78.1 | 54.8 | 56.1 | 31.0 | 65.0 | 26.9 | 54.7 | 58.1 | 37.5 |
| SimpleMem+GRPO | 89.5 | 36.3 | 60.0 | 50.0 | 64.9 | 26.3 | 62.5 | 67.8 | 46.9 |
| **SKILLRL** | 97.9 | 71.4 | 90.0 | 90.0 | 95.5 | 87.5 | 89.9 | 85.2 | 72.7 |

**表 2.** 在搜索增强 QA 任务上的性能。SKILLRL 在 NQ 和 HotpotQA 上训练。† 和 ⋆ 分别表示域内（in-domain）和域外（out-of-domain）数据集。∗ 表示从（Sun et al., 2025）复现的结果。

| 方法 | NQ† | TriviaQA⋆ | PopQA⋆ | HotpotQA† | 2Wiki⋆ | MuSiQue⋆ | Bamboogle⋆ | Avg. |
|---|---|---|---|---|---|---|---|---|
| **Qwen2.5-7B-Instruct** | | | | | | | | |
| Qwen2.5∗ | 11.6 | 35.6 | 1.20 | 16.4 | 22.2 | 4.80 | 14.4 | 15.2 |
| CoT∗ | 12.8 | 35.6 | 3.80 | 16.2 | 22.6 | 6.60 | 24.0 | 17.4 |
| RAG∗ | 27.4 | 58.2 | 17.8 | 25.8 | 23.2 | 9.40 | 16.8 | 25.5 |
| Search-o1∗ | 19.4 | 40.6 | 11.4 | 17.0 | 27.0 | 8.60 | 30.4 | 22.1 |
| R1-Instruct | 21.0 | 44.9 | 17.1 | 20.8 | 27.5 | 6.00 | 19.2 | 22.4 |
| Search-R1 | 39.3 | 61.0 | 39.7 | 37.0 | 40.1 | 14.6 | 36.8 | 38.5 |
| ZeroSearch | 43.6 | 61.8 | 51.5 | 34.6 | 35.2 | 18.4 | 27.8 | 39.1 |
| StepSearch | - | - | - | 38.6 | 36.6 | 22.6 | 40.0 | - |
| EvolveR | 43.5 | 63.4 | 44.6 | 38.2 | 42.0 | 15.6 | 54.4 | 43.1 |
| **SKILLRL** | 45.9 | 63.3 | 45.9 | 43.2 | 40.3 | 20.2 | 73.8 | 47.1 |

### 4.3. 分析

在本节中，我们对每个模块的有效性以及技能演化动态提供详细分析。

**消融研究（Ablation Studies）。** 我们开展消融实验以评估每个组件的贡献，结果见表 3。根据结果：(1) 移除层次化结构（即仅保留任务特定技能）使 ALFWorld 上的性能下降 13.1%，WebShop 上下降 11.3%，表明普适的战略原则提供了至关重要的基础性指导。(2) 用原始轨迹替换技能库导致最大的退化（高达 25%），这直接支持了我们的动机，即抽象优于记忆。原始经验引入了显著的冗余和噪声，阻碍了有效的知识迁移。(3) 冷启动 SFT 被证明至关重要（缺失时下降 20%），确认了基础模型在进入 RL 阶段之前，需要一个初始的显式示范阶段来学习如何自适应地检索和利用抽象出的技能。(4) 动态演化贡献了 5.5% 的提升，确保技能库是一个动态组件而非静态数据库。这种协同演化使智能体能够通过应对初始技能集未覆盖的新兴失败模式，迭代地精炼其内部策略。

**表 3.** 消融研究结果。我们报告在 ALFWorld 和 WebShop 上的平均成功率（%）。

| 方法 | ALFWorld | WebShop |
|---|---|---|
| SKILLRL | 89.9 | 72.7 |
| **技能库消融** | | |
| 无层次化结构（w/o Hierarchical Structure） | 76.8 | 61.4 |
| 无技能库（原始轨迹）（w/o Skill Library, Raw Trajectories） | 61.7 | 50.2 |
| **训练流程消融** | | |
| 无冷启动 SFT（w/o Cold-Start SFT） | 65.2 | 46.5 |
| 无动态演化（w/o Dynamic Evolution） | 84.4 | 70.3 |

**ALFWorld 上的逐任务分析。** 表 1 按任务类型细分了 ALFWorld 性能。最大的增益出现在 PickTwo（+23%）、Cool（+22%）和 Heat（+15%）上，这些是最具挑战性、需要多步规划和状态追踪的任务。任务特定技能在此尤为宝贵，它们捕捉了诸如"在拿取两个对象时，先确认第一个已被妥善固定，再去寻找第二个"这类应对常见失败模式的策略。

**技能库的增长。** 图 3 展示了技能库在训练过程中如何演化。初始技能库包含 55 个技能（12 个通用，43 个任务特定）。通过动态演化，到训练结束时（Step 150）增长至 100 个技能。这一增长主要由任务特定技能驱动（从 43 增加到 80），而通用技能呈现更平稳的增长（从 12 到 20）。值得注意的是，我们观察到跨各任务类别的均衡扩展，确保智能体为每次环境 rollout 都发展出专门的专长。这一总体扩展反映了智能体不断提升的、精炼其技能库存（repertoire）并应对特定任务类型内多样场景的能力。

**图 3.** RL 训练期间技能库规模的演化。动态技能演化在验证检查点处添加技能。

**上下文效率。** 为评估技能抽象对推理开销的影响，我们在图 4 中将 SKILLRL 的平均提示长度与使用原始轨迹的记忆增强基线（Qwen2.5-7B with Raw Memory）进行比较。结果表明，尽管原始记忆方法的 token 占用既高又波动（平均约 1,450 tokens），SKILLRL 维持了显著更精简的提示（平均 \<1,300 tokens），实现了约 10.3% 的上下文长度缩减。这种效率源自我们的蒸馏机制，它将冗长的环境交互压缩为高密度、可执行的技能。值得注意的是，SKILLRL 在取得更优性能的同时所需的上下文比基于记忆的基线更少，证明技能抽象有效缓解了传统基于记忆的智能体中常见的上下文膨胀（context-bloat）问题。

**图 4.** 原始记忆检索与我们的蒸馏式技能抽象之间提示长度（tokens）的比较。SKILLRL 在维持推理效用的同时持续降低上下文开销。

**图 5.** ALFWorld 验证集上的成功率。递归式技能演化显著加速了收敛并提升了整体性能上限。

**演化动态。** 图 5 展示了带有和不带有递归式技能演化机制的强化学习训练曲线。我们观察到，尽管不带演化的 SKILLRL 显示出稳步改进，但带技能演化的 SKILLRL 表现出明显更高的学习速率和更优的渐近性能。具体而言，SKILLRL 在 60 个训练步内取得了超过 80% 的成功率，而基线则需要约 90 步才能达到一个更低的峰值。这种收敛加速表明，新技能的动态引入与现有技能的精炼，有效地为智能体提供了及时的战略指导以克服局部最优。此外，更高的性能上限验证了技能库与策略的协同演化使智能体能够适应日益复杂的任务场景，而静态记忆方法无法解决这些场景。

**定性分析。** 为进一步探究 SKILLRL 如何利用习得的知识，我们在图 6 中可视化了在 ALFWorld 和 WebShop 上的推理过程。案例研究表明，我们训练后的智能体能够有效地从 SKILLBANK 中检索并执行相关技能以引导其决策。例如，在 WebShop 任务中，智能体调用诸如"Prioritize Core Keywords"的通用策略，连同诸如"Focus Key Query"的任务特定启发式，以确保商品在有限预算内满足所有约束。类似地，在 ALFWorld 中，智能体协调层次化技能，即使用"Progressive Goal Decomposition"进行高层规划，并使用"No Appliance Before Object"以避免常见的逻辑陷阱。这种通用技能与特定技能的无缝整合证实，智能体并非仅仅记忆轨迹，而是对任务逻辑发展出结构化的理解，从而实现更稳健、更高效的问题求解。

**图 6.** SKILLRL 在 WebShop 和 ALFWorld 上的案例研究。这些示例说明了智能体如何在其推理过程中自适应地检索并整合通用技能（General Skills）与任务特定技能（Task-Specific Skills），以实现精确而高效的任务执行。

## 5. 相关工作

**LLM 智能体。** 有能力的 LLM 的出现催化了自主智能体系统的快速发展（Wei et al., 2026）。ReAct（Yao et al., 2022b）将推理与行动交错，实现思维链（chain-of-thought）风格的规划与交互过程中的规划；而 Reflexion（Shinn et al., 2023）通过对过往失败的自我反思引入了言语强化（verbal reinforcement）。AutoGen（Wu et al., 2024）和 CAMEL（Li et al., 2023）等框架展示了通用的多智能体能力，具备自动化编排和多样化工具集成的特征。尽管最初的努力聚焦于编码或基础算术等受限任务，这些方法主要依赖上下文学习（in-context learning，ICL）（Dong et al., 2024）。然而，随着任务变得更复杂，这些智能体难以扩展，因为它们将每次交互都视为孤立事件，且必须在没有任何先验知识的情况下从零开始处理每个新任务。

**智能体中的记忆机制。** 为克服有限上下文窗口的局限以及智能体无法从经验中学习的问题，外部记忆架构已成为智能体设计的基石（Hu et al., 2025；Wang, 2025）。早期系统主要利用静态的 RAG 范式或将原始轨迹存储为少样本（few-shot）示例（Wang et al.；Chhikara et al., 2025；Zhang et al., 2025a；Wang et al., 2024）。然而，原始轨迹往往 token 繁重，并包含显著的冗余和噪声，可能导致性能退化。当前研究已转向自我改进的记忆（self-improving memory），将交互蒸馏为更高层的洞见或程序性提示（Wang & Chen, 2025；Tang et al., 2025；Fang et al., 2025；Zhao et al., 2024；Ouyang et al., 2025；Wei et al., 2025）。尽管一些近期工作探索通过在线训练更新记忆库以提升效率（Zhang et al., 2025b；2026），许多现有方法仍难以区分高价值经验与噪声，或无法提炼出能引导内部决策的核心原则。

**智能体技能与强化学习的演化。** 智能体技能（agentic skills）（Anthropic, 2024）——紧凑、可复用、捕捉子任务精髓的策略——的发展，正日益从持续学习（Continual Learning，CL）与 RL 的视角来审视。传统的 CL（Parisi et al., 2019）聚焦于在预定义任务中保留知识，但自我演化的智能体（Gao et al., 2025；Xia et al., 2025；Liu et al., 2025）旨在于开放式（open-ended）环境中主动获取技能（Fang et al., 2025；Wang et al., 2025）。尽管 RL 被广泛用于对齐 LLM（Schulman et al., 2017；Ouyang et al., 2022），或通过基于规则的验证器（rule-based verifiers）改进推理（Shao et al., 2024），但由于稀疏奖励和长程（long horizons）问题，将其应用于智能体技能仍具挑战性。与以往将记忆视为静态或辅助源的记忆增强 RL 不同，近期趋势表明，高效经验迁移的关键在于抽象（Wu et al., 2025）。我们的工作在此基础上进一步发展，将技能库视为一个与智能体策略协同演化的动态组件，利用 RL 通过递归式失败分析来精炼结构化技能。

## 6. 结论

我们提出了 SKILLRL，一个面向 LLM 智能体的技能增强强化学习框架。通过将原始轨迹蒸馏为紧凑、可复用的技能，并在训练过程中实现动态技能演化，SKILLRL 在 ALFWorld 和 WebShop 上取得了当前最优性能，同时使用的上下文比基于记忆的方法少得多。我们的工作表明，从经验到技能的抽象是构建有能力、样本高效（sample-efficient）智能体的一个强有力的原则。

## 致谢

本工作部分由 Amazon Research Award、Cisco Faculty Research Award、NEC Laboratories America Research Grant 和 Coefficient Giving 支持。

## 参考文献

Ahmadian, A., Cremer, C., Gallé, M., Fadaee, M., Kreutzer, J., Pietquin, O., Üstün, A., and Hooker, S. Back to basics: Revisiting reinforce-style optimization for learning from human feedback in llms. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 12248–12267, 2024.

Anthropic. The claude 3 model family: Opus, sonnet, haiku, 2024. URL https://www.anthropic.com/news/claude-3-family.

Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F., et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.

Chhikara, P., Khant, D., Aryan, S., Singh, T., and Yadav, D. Mem0: Building production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413, 2025.

Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., Blistein, M., Ram, O., Zhang, D., Rosen, E., et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.

Dong, Q., Li, L., Dai, D., Zheng, C., Ma, J., Li, R., Xia, H., Xu, J., Wu, Z., Chang, B., et al. A survey on in-context learning. In Proceedings of the 2024 conference on empirical methods in natural language processing, pp. 1107–1128, 2024.

Fang, R., Liang, Y., Wang, X., Wu, J., Qiao, S., Xie, P., Huang, F., Chen, H., and Zhang, N. Memp: Exploring agent procedural memory. arXiv preprint arXiv:2508.06433, 2025.

Feng, L., Xue, Z., Liu, T., and An, B. Group-in-group policy optimization for llm agent training. arXiv preprint arXiv:2505.10978, 2025.

Gao, H.-a., Geng, J., Hua, W., Hu, M., Juan, X., Liu, H., Liu, S., Qiu, J., Qi, X., Wu, Y., et al. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046, 2025.

Google. Try deep research and our new experimental model in gemini, your ai assistant, 2024. URL https://blog.google/products/gemini/google-gemini-deep-research/.

Google. Introducing the gemini 2.5 computer use model, 2025. URL https://blog.google/technology/google-deepmind/gemini-computer-use-model/.

Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

Ho, X., Nguyen, A.-K. D., Sugawara, S., and Aizawa, A. Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps. In Proceedings of the 28th International Conference on Computational Linguistics, pp. 6609–6625, 2020.

Hu, Y., Liu, S., Yue, Y., Zhang, G., Liu, B., Zhu, F., Lin, J., Guo, H., Dou, S., Xi, Z., et al. Memory in the age of ai agents. arXiv preprint arXiv:2512.13564, 2025.

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., and Han, J. Search-r1: Training llms to reason and leverage search engines with reinforcement learning. arXiv preprint arXiv:2503.09516, 2025.

Joshi, M., Choi, E., Weld, D. S., and Zettlemoyer, L. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1601–1611, 2017.

Kwiatkowski, T., Palomaki, J., Redfield, O., Collins, M., Parikh, A., Alberti, C., Epstein, D., Polosukhin, I., Devlin, J., Lee, K., et al. Natural questions: a benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:453–466, 2019.

Li, G., Hammoud, H., Itani, H., Khizbullin, D., and Ghanem, B. Camel: Communicative agents for "mind" exploration of large language model society. Advances in Neural Information Processing Systems, 36:51991–52008, 2023.

Li, X., Dong, G., Jin, J., Zhang, Y., Zhou, Y., Zhu, Y., Zhang, P., and Dou, Z. Search-o1: Agentic search-enhanced large reasoning models. arXiv preprint arXiv:2501.05366, 2025.

Liu, J., Xiong, K., Xia, P., Zhou, Y., Ji, H., Feng, L., Han, S., Ding, M., and Yao, H. Agent0-vl: Exploring self-evolving agent for tool-integrated vision-language reasoning. arXiv preprint arXiv:2511.19900, 2025.

Liu, J., Su, Y., Xia, P., Han, S., Zheng, Z., Xie, C., Ding, M., and Yao, H. Simplemem: Efficient lifelong memory for llm agents. arXiv preprint arXiv:2601.02553, 2026.

Mallen, A., Asai, A., Zhong, V., Das, R., Khashabi, D., and Hajishirzi, H. When not to trust language models: Investigating effectiveness of parametric and non-parametric memories. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 9802–9822, 2023.

OpenAI. Gpt-4o system card, 2024. https://openai.com/index/gpt-4o-system-card/.

OpenAI. Introducing o3 and o4-mini, 2025a. https://openai.com/index/introducing-o3-and-o4-mini/.

OpenAI. Openai deep research system card, 2025b. URL https://openai.com/index/introducing-deep-research/.

OpenAI. Openai computer-using agent, 2025c. URL https://openai.com/index/computer-using-agent/.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems, 35:27730–27744, 2022.

Ouyang, S., Yan, J., Hsu, I., Chen, Y., Jiang, K., Wang, Z., Han, R., Le, L. T., Daruki, S., Tang, X., et al. Reasoningbank: Scaling agent self-evolving with reasoning memory. arXiv preprint arXiv:2509.25140, 2025.

Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., and Wermter, S. Continual lifelong learning with neural networks: A review. Neural networks, 113:54–71, 2019.

Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N. A., and Lewis, M. Measuring and narrowing the compositionality gap in language models. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 5687–5711, 2023.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and Yao, S. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36:8634–8652, 2023.

Shridhar, M., Yuan, X., Cote, M.-A., Bisk, Y., Trischler, A., and Hausknecht, M. Alfworld: Aligning text and embodied environments for interactive learning. In International Conference on Learning Representations.

Sun, H., Qiao, Z., Guo, J., Fan, X., Hou, Y., Jiang, Y., Xie, P., Zhang, Y., Huang, F., and Zhou, J. Zerosearch: Incentivize the search capability of llms without searching. arXiv preprint arXiv:2505.04588, 2025.

Tang, X., Qin, T., Peng, T., Zhou, Z., Shao, D., Du, T., Wei, X., Xia, P., Wu, F., Zhu, H., et al. Agent kb: Leveraging cross-domain experience for agentic problem solving. arXiv preprint arXiv:2507.06229, 2025.

Team, T. D., Li, B., Zhang, B., Zhang, D., Huang, F., Li, G., Chen, G., Yin, H., Wu, J., Zhou, J., et al. Tongyi deepresearch technical report. arXiv preprint arXiv:2510.24701, 2025.

Trivedi, H., Balasubramanian, N., Khot, T., and Sabharwal, A. Musique: Multihop questions via single-hop question composition. Transactions of the Association for Computational Linguistics, 10:539–554, 2022.

Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. Voyager: An open-ended embodied agent with large language models. Transactions on Machine Learning Research.

Wang, Y. From Static Parameters to Updatable Memory: Enabling Large Language Model Agents to Remember, Adapt, and Learn. PhD thesis, University of California, San Diego, 2025.

Wang, Y. and Chen, X. Mirix: Multi-agent memory system for llm-based agents. arXiv preprint arXiv:2507.07957, 2025.

Wang, Y., Takanobu, R., Liang, Z., Mao, Y., Hu, Y., McAuley, J., and Wu, X. Mem-{\alpha}: Learning memory construction via reinforcement learning. arXiv preprint arXiv:2509.25911, 2025.

Wang, Z. Z., Mao, J., Fried, D., and Neubig, G. Agent workflow memory. arXiv preprint arXiv:2409.07429, 2024.

Wei, T., Sachdeva, N., Coleman, B., He, Z., Bei, Y., Ning, X., Ai, M., Li, Y., He, J., Chi, E. H., et al. Evo-memory: Benchmarking llm agent test-time learning with self-evolving memory. arXiv preprint arXiv:2511.20857, 2025.

Wei, T., Li, T.-W., Liu, Z., Ning, X., Yang, Z., Zou, J., Zeng, Z., Qiu, R., Lin, X., Fu, D., et al. Agentic reasoning for large language models. arXiv preprint arXiv:2601.12538, 2026.

Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., et al. Autogen: Enabling next-gen llm applications via multi-agent conversations. In First Conference on Language Modeling, 2024.

Wu, R., Wang, X., Mei, J., Cai, P., Fu, D., Yang, C., Wen, L., Yang, X., Shen, Y., Wang, Y., et al. Evolver: Self-evolving llm agents through an experience-driven lifecycle. arXiv preprint arXiv:2510.16079, 2025.

Xia, P., Zeng, K., Liu, J., Qin, C., Wu, F., Zhou, Y., Xiong, C., and Yao, H. Agent0: Unleashing self-evolving agents from zero data via tool-integrated reasoning. arXiv preprint arXiv:2511.16043, 2025.

Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W., Salakhutdinov, R., and Manning, C. D. Hotpotqa: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 conference on empirical methods in natural language processing, pp. 2369–2380, 2018.

Yao, S., Chen, H., Yang, J., and Narasimhan, K. Webshop: Towards scalable real-world web interaction with grounded language agents. Advances in Neural Information Processing Systems, 35:20744–20757, 2022a.

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., and Cao, Y. React: Synergizing reasoning and acting in language models. In The eleventh international conference on learning representations, 2022b.

Zhang, G., Fu, M., Wan, G., Yu, M., Wang, K., and Yan, S. G-memory: Tracing hierarchical memory for multi-agent systems. arXiv preprint arXiv:2506.07398, 2025a.

Zhang, G., Ren, H., Zhan, C., Zhou, Z., Wang, J., Zhu, H., Zhou, W., and Yan, S. Memevolve: Meta-evolution of agent memory systems. arXiv preprint arXiv:2512.18746, 2025b.

Zhang, S., Wang, J., Zhou, R., Liao, J., Feng, Y., Zhang, W., Wen, Y., Li, Z., Xiong, F., Qi, Y., et al. Memrl: Self-evolving agents via runtime reinforcement learning on episodic memory. arXiv preprint arXiv:2601.03192, 2026.

Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J., and Huang, G. Expel: Llm agents are experiential learners. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 19632–19642, 2024.

Zheng, X., An, K., Wang, Z., Wang, Y., and Wu, Y. Stepsearch: Igniting llms search ability via step-wise proximal policy optimization. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 21816–21841, 2025.

## 附录

## A. 提示模板（Prompts）

在本节中，我们提供了在框架各阶段使用的完整提示模板。这些模板旨在确保智能体行为的一致性以及在各类环境中结构化数据生成的一致性。

### A.1. 智能体执行提示

以下提示用于在线推理阶段。这些模板为智能体提供当前任务描述、过往交互的历史，以及一组被检索的技能（经验）以引导其决策过程。这些提示明确强制在动作选择之前执行一个思维链（Chain-of-Thought，CoT）推理步骤。

**Prompt A.1：带技能的 ALFWorld 智能体执行**

System Prompt：
You are an expert agent operating in the ALFRED Embodied Environment. Your task is to: {task description}

\#\# Retrieved Relevant Experience
{retrieved memories}

\#\# Current Progress
Prior to this step, you have already taken {step count} step(s). Below are the most recent {history length} observations and the corresponding actions you took: {action history}
You are now at step {current step} and your current observation is: {current observation}
Your admissible actions of the current situation are: [{admissible actions}].

Now it's your turn to take an action. You should first reason step-by-step about the current situation. This reasoning process MUST be enclosed within \<think\> \</think\> tags. Once you've finished your reasoning, you should choose an admissible action for current step and present it within \<action\> \</action\> tags.

**Prompt A.2：带技能的 WebShop 智能体执行**

System Prompt：
You are an expert autonomous agent operating in the WebShop e-commerce environment. Your task is to: {task description}.

\#\# Retrieved Relevant Experience
{retrieved memories}

\#\# Current Progress
Prior to this step, you have already taken {step count} step(s). Below are the most recent {history length} observations and the corresponding actions you took: {action history}
You are now at step {current step} and your current observation is: {current observation}
Your admissible actions of the current situation are: [ {available actions} ].

Now it's your turn to take one action for the current step. You should first reason step-by-step about the current situation, then think carefully which admissible action best advances the shopping goal. This reasoning process MUST be enclosed within \<think\> \</think\> tags. Once you've finished your reasoning, you should choose an admissible action for current step and present it within \<action\> \</action\> tags.

### A.2. 技能生成与蒸馏提示

这些提示用于技能发现和库初始化阶段。它们引导一个高能力的教师模型分析交互轨迹、识别失败模式，并将可复用、可执行的技能蒸馏为结构化的 JSON 格式。

**Prompt B.1：从失败中进行动态技能发现**

Analyze these failed {env description} agent trajectories and suggest NEW skills to add.

FAILED TRAJECTORIES: {failure examples}
EXISTING SKILL TITLES: {existing titles}

Generate 1-3 NEW actionable skills that would help avoid these failures. Each skill must have: skill id, title (3-5 words), principle (1-2 sentences), when to apply. The skill id should be unique and follow the pattern: "dyn 001", "dyn 002", etc.

Return ONLY a JSON array of skills, no other text.

**Prompt B.2：初始技能蒸馏（ALFWorld）**

You are an expert at distilling agent behavior patterns into concise, actionable skills. Analyze these successful and failed trajectories from an embodied AI agent operating in household environments (ALFWorld).

SUCCESSFUL TRAJECTORIES: {success patterns}
FAILED TRAJECTORIES: {failure patterns}

Generate 8-12 GENERAL SKILLS that apply across ALL task types. These should be: 1. Concise; 2. Actionable; 3. Transferable; 4. Failure-aware. Focus on: Navigation, object manipulation, state tracking, error recovery, and container interaction rules.

Return ONLY the JSON array, no other text.

**Prompt B.3：初始技能蒸馏（WebShop）**

You are an expert at distilling agent behavior patterns into concise, actionable skills. Analyze these successful and failed trajectories from an AI agent operating in an online shopping environment (WebShop).

SUCCESSFUL TRAJECTORIES: {success patterns}
FAILED TRAJECTORIES: {failure patterns}

Generate 10-15 GENERAL SKILLS. Focus on: Search query formulation, product selection heuristics, option configuration (size, color, etc.), constraint verification, navigation patterns, and price handling.

Return ONLY the JSON array, no other text.

### A.3. 冷启动轨迹生成提示

为弥合基础模型与目标性能之间的差距，我们使用以下提示生成高质量的合成轨迹，用于监督微调（SFT）。这些提示指示教师模型在解决任务的同时显式地示范特定技能的应用，从而为学生模型（student model）提供清晰的学习信号。

**Prompt C.1：合成轨迹生成（ALFWorld）**

You are an expert agent in the ALFRED embodied environment. You will be given a task and relevant skills to apply. Your goal is to generate a successful trajectory that demonstrates proper use of these skills.

You should generate a step-by-step trajectory that:
1. Uses the provided skills appropriately;
2. Takes realistic actions in the environment;
3. Completes the task successfully;
4. Demonstrates good planning and systematic exploration.

For each step, you should:
• Think through the current situation using \<think\>\</think\> tags.
• Choose an appropriate action using \<action\>\</action\> tags.
• The action should be a simple command like "go to cabinet 1", "open drawer 2", "take apple 1", "put apple 1 in/on countertop 1".

Generate a complete trajectory from start to finish. Stop when the task is complete.

**Prompt C.2：合成轨迹生成（WebShop）**

You are an expert shopping agent in the WebShop e-commerce environment. You will be given a shopping task and relevant skills to apply. Your goal is to generate a successful trajectory that demonstrates proper use of these skills.

You should generate a step-by-step trajectory that:
1. Uses the provided skills appropriately;
2. Takes realistic actions in the WebShop environment;
3. Successfully finds and purchases the requested product;
4. Demonstrates good search strategies and product evaluation.

For each step, you should:
• Think through the current situation using \<think\>\</think\> tags.
• Choose an appropriate action using \<action\>\</action\> tags.
• Actions can be: search[query], click[element], or buy now.

Generate a complete trajectory from start to finish. Stop when the purchase is complete.

## B. 额外的实验细节

### B.1. 超参数

**表 4.** SKILLRL 的超参数。

| 超参数 | 值 |
|---|---|
| **冷启动 SFT（Cold-Start SFT）** | |
| 学习率（Learning rate） | $1 \times 10^{-4}$ |
| Batch size | 16 |
| Epochs | 3 |
| SFT 样本数（SFT examples） | 7,500（AlfWorld）/ 2,400（WebShop） |
| **RL 训练（RL Training）** | |
| 学习率（Learning rate） | $1 \times 10^{-6}$ |
| Batch size | 64 |
| KL 损失系数（KL loss Coef） | 0.01 |
| 无效动作惩罚系数（Invalid Action Penalty Coef） | 0.1 |
| 最大提示长度（Max Prompt Length） | 6,000 |
| 最大回复长度（Max Response Length） | 1,024 |
| Epoch | 150 |
| **技能检索（Skill Retrieval）** | |
| Top-K 检索（Top-K retrieval） | 6 |
| 验证间隔（Validation interval） | 5 Steps |
| 更新阈值 δ（Update Threshold δ） | 0.4 |
| 分析的最大失败数（Max failures analyzed） | 10（SR \< 0.4）/ 5（SR \> 0.4） |
| 每次演化的最大新技能数（Max new skills per evolution） | 3 |

### B.2. 计算资源

所有实验均在一个配备 8 块 NVIDIA H100 80GB GPU 的集群上进行。训练时间：

- 轨迹收集（Trajectory collection）：3 小时
- 技能蒸馏（Skill distillation）：0.5 小时
- 冷启动 SFT（Cold-start SFT）：2 小时
- RL 训练（RL training）：24 小时

**表 5.** 来自 SKILLBANK 的 ALFWorld 蒸馏技能示例（Shridhar et al.）。本表总结了从原始轨迹中导出的通用模式及应用逻辑。

| ID | 技能标题 | 原则（可执行模式） | 应用时机 |
|---|---|---|---|
| **通用探索与获取技能** | | | |
| gen 001 | Systematic Exploration | 在重访之前，对每个可能的表面或容器恰好搜索一次；优先选择未见过的位置。 | 任何目标数量未满足且仍有未探索区域时。 |
| gen 002 | Immediate Acquisition | 一旦所需对象变得可见且可触及，立即拿取。 | 在首次目视确认目标相关对象时。 |
| gen 003 | Destination First Policy | 拿起目标对象后，直接导航至已知的目标容器并放置。 | 持有任意目标对象且目标位置已确定时。 |
| **状态改变与空间关系技能** | | | |
| gen 005 | Use State-Changing Tools Early | 获取对象后，在放置前立即使用最近的合适器具（加热/冷却/清洁）。 | 拿起需要改变温度或清洁状态的对象后。 |
| gen 006 | Establish Spatial Relations | 先定位参照对象，必要时调整其状态，然后在指定区域内搜索或放置。 | 任务包含"under"、"inside"或"on"等介词时。 |
| **可靠性与错误恢复** | | | |
| gen 014 | Loop Escape Trigger | 若最近 3–5 个动作未改变状态，则切换到一个未尝试过的搜索分支或动作类型。 | 在连续若干次无进展的观察之后。 |
| gen 015 | Pre-Action Sanity Check | 在执行操作性命令前确认前置条件（空手、容量、电力）。 | 在发出任何可能合法失败的命令之前。 |

**表 6.** ALFWorld 常见的智能体失败及缓解策略。

| ID | 失败描述 | 根因（为何发生） | 缓解措施（如何避免） |
|---|---|---|---|
| err 001 | Redundant Revisit（冗余重访） | 缺乏对已探索区域的显式记忆；策略退化为局部循环。 | 维护一张探索地图；优先选择未访问的候选项。 |
| err 006 | Skipping State Changes（跳过状态改变） | 将对象存在与目标满足混为一谈；遗漏清洁/温度检查。 | 在放置前将状态前置条件检查整合进规划器。 |

总挂钟时间（wall-clock time）：每次实验约 30 小时。

## C. 技能库的图示

在本节中，我们为 ALFWorld 和 WebShop 两种环境提供一些蒸馏技能与错误分类法的示例目录。表 5 和表 7 分别详述了为具身操作和基于网络的购物蒸馏出的通用技能，凸显了系统化探索和约束满足所需的可执行原则。此外，我们在表 6 和表 8 中提供了对失败案例的结构化分析，对常见错误进行分类——从 ALFWorld 中的空间推理循环到 WebShop 中的价格变动疏忽——并给出其根因与提议的缓解策略。

**表 7.** WebShop 导航的蒸馏技能示例（Yao et al., 2022a）。这些技能代表了智能体用于处理大规模商品搜索和约束满足的战略模式。

| ID | 技能标题 | 原则（可执行模式） | 应用时机 |
|---|---|---|---|
| **搜索与查询工程** | | | |
| gen 001 | Prioritize Core Keywords | 包含商品类型、1-2 个功能性属性以及硬约束；省略次要的描述符。 | 在发出首次搜索或精炼过于具体的查询之前。 |
| gen 002 | Iterative Refinement | 调整关键词或应用站点过滤器，而非重复同一个失败的查询。 | 当结果无关或多次搜索后仍重复时。 |
| **商品评估与验证** | | | |
| gen 003 | Scan Before You Click | 在打开链接前阅读结果中的标题、缩略图和价格以确保合理性。 | 在搜索结果页选择下一个要查看的商品时。 |
| gen 004 | Verify Early, Abort Fast | 在商品页上立即检查类别、属性和价格；若任何约束被违反则离开。 | 在每个商品详情页的首个观察之内。 |
| gen 006 | Confirm Hidden Attributes | 打开 Description/Features 章节以确保非可见规格（如材质）满足约束。 | 当约束无法从标题或变体列表中明显看出时。 |
| **配置与交易** | | | |
| gen 005 | Set Mandatory Variants | 在评估价格或购买之前，总是先选择必需的选项（尺寸、颜色等）。 | 在确认商品匹配之后但在任何购买动作之前。 |
| gen 007 | Check Variant Pricing | 对于价格区间，选择确切的变体组合以验证具体价格在预算之内。 | 每当价格随变体选择而变化或显示为区间时。 |
| gen 013 | Purchase Decisively | 一旦某变体上的所有约束和价格被确认，立即执行 'Buy Now'。 | 在对当前商品变体验证完每一项约束之后。 |

**表 8.** 基于网络的购物任务中的常见失败。

| ID | 失败描述 | 根因 | 缓解策略 |
|---|---|---|---|
| err 001 | Missing Constraints in Query | 省略了尺寸或价格上限，导致结果集过于庞大或无关。 | 先组装完整的需求清单；确保每个硬约束都在查询字符串中。 |
| err 004 | Price Shift Oversight | 未能注意到在选择特定尺寸或颜色变体后的价格变化。 | 在每次选项变更后、进入结账前，重新阅读价格元素。 |
| err 005 | Premature Purchase | 在未设置必需变体的情况下点击"Buy Now"，导致错误或买错商品。 | 在购买前验证每个必需的下拉框/单选项都已被显式选中。 |
| err 009 | Ignoring Stock Status | 忽略禁用的按钮或缺货标签，试图购买缺货商品。 | 验证 'Add to Cart' 按钮已启用，且选择后无 'Out of Stock' 提示。 |
| err 011 | Sponsored Link Distraction | 点击松散匹配的广告，使工作流偏离自然的、合适的商品。 | 实现广告标签检测；优先选择自然列表（organic listings）以获得更高的约束可靠性。 |

## D. 额外案例

**Case 1：WebShop 鞋类（功能性约束）**

Task: I want a pair of men's black slip-resistant work shoes, size 10, rubber sole, price lower than $50.00.

- Skills: [foo 002] Verify features in description; [foo 004] Confirm price after variant selection.
- Avoid: [err 001] Omitting price cap; [err 003] Selecting wrong product category.

**带技能引导推理的智能体轨迹**

- **Step 1** — Obs: WebShop homepage.
  Think: Per [gen 001], I'll include key constraints (type, function, color, price) in the query.
  Action: search[men black slip resistant work shoes rubber sole under 50]
- **Step 2** — Obs: Results: [1] Chef Shoes $38.99; [2] Kitchen Shoes $42.50; [3] Steel Toe Boots $55.99.
  Think: [gen 003] Item [1] is under budget and matches function. Item [3] is over budget (skip).
  Action: click[Item 1]
- **Step 3** — Obs: Product page. Price: $35.99-$45.99. Colors: Black, White. Sizes: 7-12.
  Think: [foo 002] Description confirms rubber sole. Now selecting Black and Size 10 [foo 003].
  Action: click[Black] → click[10]
- **Step 5** — Obs: Selected: Black, Size 10. Price updated to $38.99.
  Think: [foo 004] $38.99 < $50. All constraints (color, size, function, price) are satisfied.
  Action: click[Buy Now]

Result: SUCCESS — Purchased at $38.99. Key Skills: [foo 002]（验证）, [foo 004]（价格检查）.

**Case 2：电子产品（带"中止并重试"的音箱）**

Task: I need a portable bluetooth speaker, waterproof, black color, price lower than $30.00.

- Skills: [ele 001] Constraint-rich search; [ele 004] Bail on mismatch fast; [gen 002] Iterative refinement.
- Avoid: [err 002] Overly specific variant names in search; [ele 006] Avoid click loops.

**智能体轨迹：处理缺失的约束**

- **Step 1** — Obs: WebShop homepage.
  Think: [ele 001] Packing all mandatory attributes: portable, bluetooth, waterproof, black, <$30.
  Action: search[portable bluetooth speaker waterproof black under 30]
- **Step 2** — Obs: Results: [1] Waterproof Speaker $28.99; [2] Mini LED Speaker $19.99; [3] 20W Speaker $35.50.
  Think: [ele 005] Item [1] matches most keywords and price.
  Action: click[Item 1]
- **Step 3** — Obs: Product page (Item 1). Colors: Blue, Red, Green, Army Green. Black unavailable.
  Think: [gen 004] Verify Early, Abort Fast: No black option! [ele 004] Bail immediately to find another candidate.
  Action: click[Back to Search]
- **Step 4** — Obs: Back on search results.
  Think: [gen 002] Iterative refinement. Item [2] $19.99 is the next best candidate.
  Action: click[Item 2]
- **Step 5** — Obs: Product page (Item 2). Colors: Black, Blue, Red. Specs: IPX5 Waterproof.
  Think: [ele 002] Black is available! IPX5 confirms waterproof. Selecting Black.
  Action: click[Black]
- **Step 6** — Obs: Black selected. Final price: $19.99.
  Think: [ele 003] $19.99 < $30. All specs (black, portable, waterproof) verified.
  Action: click[Buy Now]

Result: SUCCESS — 通过提前退出高效处理了属性不匹配。Key Skills Applied: [gen 004]（Abort Fast）, [ele 004]（Bail on Mismatch）.

**Case 1：ALFWorld 清洁任务（Lettuce → Sink → Countertop）**

Task: Clean some lettuce and put it in countertop.

- Core Skills: [cle 001] Phase-ordered plan (Locate → Clean → Place); [cle 006] Use location priors (Fridge for food).
- Mistakes Avoided: [err 002] Skipping closed containers; [err 003] Ignoring visible target objects.

- **Step 1-3** — Obs: Fridge 1 is closed. Action: open fridge 1 → take lettuce 1
  Reasoning: Per [cle 006], food is likely in the fridge. [gen 002] Grab lettuce immediately on sight.
- **Step 4-6** — Obs: Arrive at sinkbasin 1. Action: clean lettuce 1 with sinkbasin 1
  Reasoning: Per [cle 001] Phase 2: bring to water source. [cle 003] Go straight to sink.
- **Step 7** — Obs: Arrive at countertop 1. Action: put lettuce 1 in/on countertop 1
  Reasoning: Per [gen 003] Destination First: place cleaned object immediately to finish.

Result: SUCCESS (7 Steps) — Skills used: [gen 010]（Decomposition）, [cle 003]（Sink First）.

**Case 2：ALFWorld 加热任务（Egg → Microwave → Countertop）**

Task: Heat some egg and put it in countertop.

- Core Skills: [hea 001] Secure exact target first; [hea 003] Open-Place-Heat sequence; [hea 004] No appliance before object.

- **Step 1-3** — Obs: Countertop 1 (no egg) → Countertop 2 (egg found). Action: take egg 1
  Reasoning: [hea 004] Avoid microwave until object is held. [hea 002] Systematic search of surfaces.
- **Step 4-6** — Obs: Microwave 1 is closed. Action: open microwave 1 → heat egg 1
  Reasoning: [hea 003] Correct sequence: open door first, then initiate state change.
- **Step 7-8** — Obs: Egg is heated. Action: go to countertop 1 → put egg 1
  Reasoning: [hea 005] Direct Post-Heat Placement: move to target without detours.

Result: SUCCESS (8 Steps) — Skills used: [hea 001]（Target First）, [hea 004]（Sequence Control）.

**Case 3：ALFWorld 检视任务（Pencil ⊕ Desklamp → Success）**

Task: Look at pencil under the desklamp.

- Core Skills: [loo 001] Seek lamp surfaces (Desk/Sidetable); [loo 002] Switch lamp on; [exa 001] Pair objects early (Target & Tool co-location).
- Mistakes Avoided: [err 003] Ignoring reachable targets; [loo 005] Preventing action loops (Toggle only once).

**智能体轨迹：高效率的共位处理**

- **Step 1** — Obs: Mid-room. Visible: desk 1/2, drawer 1-3, sidetable 1, etc.
  Reasoning: [loo 001] Desklamps usually sit on desks. Prioritizing desk 1 to find both pencil and lamp in one go.
  Action: go to desk 1
- **Step 2** — Obs: On desk 1: alarmclock 1, desklamp 1, pencil 1.
  Reasoning: [exa 001] Successful co-location! Both objects are present. [exa 002] Pick up target first before interacting with the tool.
  Action: take pencil 1 from desk 1
- **Step 3** — Obs: Holding pencil 1.
  Reasoning: [loo 002] Toggle the lamp state to satisfy the "under light" condition. [exa 004] Single toggle rule ensures no repeated actions.
  Action: use desklamp 1

Result: SUCCESS (Optimal 3 Steps) — 展示了优越的空间推理和零浪费的导航。Key Skills: [exa 001]（Object Pairing）, [loo 001]（Spatial Priors）.
