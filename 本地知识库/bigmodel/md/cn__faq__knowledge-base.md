<!-- source: https://docs.bigmodel.cn/cn/faq/knowledge-base -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 知识库

## 一、知识库 API 相关

**Q：知识库 API 有哪些接口？**

**A：** 目前知识库 API 包含以下接口：问答 Agent 对话（流式）、全模态知识库检索、知识库检索、知识库列表、创建知识库、知识库详情、编辑知识库、删除知识库、知识库使用量、文档列表、上传文件文档、上传 URL 文档、解析文档图片、文档详情、删除文档、重新向量化。详见：[知识库 API 文档](https://docs.bigmodel.cn/api-reference/%E7%9F%A5%E8%AF%86%E5%BA%93-api/%E5%85%A8%E6%A8%A1%E6%80%81%E7%9F%A5%E8%AF%86%E5%BA%93%E6%A3%80%E7%B4%A2)

***

**Q：体验中心的「知识问答」功能和直接调用知识库 API 有什么区别？**

**A：** 区别如下

* **知识问答（体验中心）：** 面向控制台页面操作，支持文本模型和视觉模型两种入口，无需编写代码，可实时调整检索参数（问题改写、Rerank、QA 干预等），视觉模型还支持「图文并茂」模式同时返回图片与文本。适合调试和体验。详见：[知识问答](https://docs.bigmodel.cn/cn/guide/tools/knowledge/q%26a)

* **API 调用：** 通过在 `tools` 参数中传入知识库 ID，以编程方式将知识库能力集成到自己的应用中，适合生产环境开发。详见：[对话调用知识库](https://docs.bigmodel.cn/cn/guide/tools/knowledge/retrieval)

***

**Q：问答 Agent 对话（流式）接口是什么，适合什么场景？**

**A：** [问答 Agent 对话（流式）](https://docs.bigmodel.cn/api-reference/agent-api/%E9%97%AE%E7%AD%94-agent-%E5%AF%B9%E8%AF%9D%EF%BC%88%E6%B5%81%E5%BC%8F%EF%BC%89)是基于 ReAct（Reasoning + Acting）推理引擎的流式对话接口，LLM 会根据用户问题自主决定是否调用工具（如知识检索、查询重写等），并通过 SSE 实时推送思考过程、工具调用和最终回答。适合需要实时反馈、多步推理的智能问答场景。

***

**Q：调用问答 Agent 对话接口时，如何指定检索的知识库？**

**A：** 在请求体的 `retrieval` 参数中传入 `know_ids`（知识库 ID 列表）即可。

<Tip>
  注意：需传入**知识库 ID**，不要传文档 ID。
</Tip>

***

**Q：知识库检索支持哪些检索方式？如何配置？**

**A：** 三个接口均支持以下检索类型，通过 `recall_method` 参数配置：

* `embedding`：向量化检索
* `keyword`：关键词检索
* `mixed`：混合检索（默认）

混合检索时可通过 `recall_ratio` 参数调整向量检索的权重（知识库检索接口取值范围 0-100，默认 80；全模态检索接口取值范围 0-1，默认 0.8）。

***

**Q：全模态知识库检索如何传入图片进行检索？**

**A：** 通过 `multimodal_parts` 参数传入图片 URL，文本查询（`query`）与多模态查询（`multimodal_parts`）必须传入其中之一。

***

**Q：问答 Agent 对话接口如何开启思考模式？**

**A：** 在请求体中设置 `enable_thinking: true` 即可开启思考模式。开启后模型会输出推理过程，通过 `reasoning` 事件类型在 SSE 流中实时返回。默认为 `false`（不开启）。

***

**Q：问答 Agent 对话（流式）接口返回的 SSE 事件有哪些类型？**

**A：** SSE 流式响应包含以下事件类型：

| 事件类型             | 说明               |
| :--------------- | :--------------- |
| session\_created | 会话创建             |
| reasoning        | 推理过程（开启思考模式时返回）  |
| thought          | 思考内容             |
| tool\_call       | 工具调用             |
| tool\_result     | 工具调用结果           |
| answer           | 最终回答             |
| done             | 完成（含 Token 用量信息） |
| error            | 错误               |

***

## 二、知识库版本 & 全模态知识库

**Q：知识库检索和全模态知识库检索有什么区别？**

**A：** 区别如下

* [知识库检索](https://docs.bigmodel.cn/api-reference/%E7%9F%A5%E8%AF%86%E5%BA%93-api/%E7%9F%A5%E8%AF%86%E5%BA%93%E6%A3%80%E7%B4%A2)：适用于文本检索，并支持查询重写、重排、QA 干预等高级功能。
* [全模态知识库检索](https://docs.bigmodel.cn/api-reference/%E7%9F%A5%E8%AF%86%E5%BA%93-api/%E5%85%A8%E6%A8%A1%E6%80%81%E7%9F%A5%E8%AF%86%E5%BA%93%E6%A3%80%E7%B4%A2)：支持文本、图片、视频等全模态内容检索，并支持查询重写、重排、QA 干预等高级功能，适合需要处理多种媒体格式内容的场景。

***

**Q：GLM 全模态知识库支持哪些文件格式？上传限制是什么？**

**A：** 支持以下格式导入：

* **文档：** pdf、docx、doc、pptx、ppt、txt、md、xlsx、xls、csv，单文件不超过 100MB
* **图片：** jpeg、png、webp，单张不超过 5MB
* **视频：** mp4、avi、mov，单条时长不超过 15 分钟
* **音频：** pcm、wav、mp3、ogg，单条时长不超过 30 分钟

除本地上传外，还支持通过 URL、飞书文档、问答对等方式导入。详见：[知识处理及检索](https://docs.bigmodel.cn/cn/guide/tools/knowledge/multimodal-retrieval)

***

**Q：全模态知识库支持对视频和音频内容检索吗？效果如何？**

**A：** 支持。系统会对视频和音频文件建立多模态索引：

* **视频检索：** 结果中显示视频缩略图及精确时间段（如 `00:22-00:38`），点击可在页面内直接播放对应片段
* **音频检索：** 结果中显示对应时间段与内容摘要，点击后展开播放控件直接收听相关片段

详见：[知识处理及检索](https://docs.bigmodel.cn/cn/guide/tools/knowledge/multimodal-retrieval)

***

**Q：知识库有哪几种版本？该如何选择？**

**A：** 创建知识库时，系统根据向量模型和导入格式自动区分为三种版本：

* **全模态版：** 选用全模态向量模型（如 Embedding-Multimodal），适合音视频、复杂图文、高精度语义问答等场景
* **文本版：** 选用文本向量模型，适合单一文本模态的信息查询
* **QA 版：** 导入内容为问答对格式时自动识别，适合精准问答和结构化知识体系

详见：[知识处理及检索](https://docs.bigmodel.cn/cn/guide/tools/knowledge/multimodal-retrieval)

***

## 三、知识库效果问题

**Q：上传文件后，为什么还无法检索到内容？**

**A：** 文件上传后需等待系统完成解析和向量索引构建，状态流转如下：**数据处理中 → 索引构建中 → 处理完成**。只有状态变为「**处理完成**」后才可以正常检索。大文件处理时间较长，请耐心等待。若状态显示「数据异常」，可点击刷新图标重试。

***

**Q：知识库检索结果不准确，有哪些方法可以提升效果？**

**A：** 可以尝试以下方式优化：

* 开启**问题改写**：自动扩展语义覆盖范围，口语化提问效果尤为明显
* 开启**Rerank 重排序**：对召回结果重新排序，提升精准度
* 开启 **QA 干预**：优先从 QA 知识库匹配精准问答对
* 调整**召回分数阈值**（默认 0.3）和**召回数量**（默认 8）
* 创建知识库时开启**上下文增强**：可提升复杂问答的平均召回率约 20%（该操作**不可逆**，且仅对文档类文件生效）

***

**Q：知识库 API 检索结果不准确，如何优化？**

**A：** 可以尝试以下方式：

* 开启**重排（Rerank）**：知识库检索接口设置 `rerank_status: 1`；全模态检索设置 `enable_rerank: true`。
* 开启**查询重写**（全模态检索接口）：设置 `enable_rewrite: true`，可结合 `messages` 实现多轮对话改写。
* 调整**相似度阈值**（`fractional_threshold` / `similarity_threshold`），过滤低质量切片。
* 开启**扩召**（全模态检索接口）：设置 `enable_expansion: true` 扩大召回范围。
* 检查上传的知识库内容是否与用户问题匹配，必要时优化文档切片。

***

**Q：什么是「上下文增强」功能，它有什么效果？**

**A：** 上下文增强是创建知识库时的可选增强设置，开启后系统会保留文档中的关键语义与指代信息，提升复杂问答和精确信息检索的效果。在高准确度场景下，**平均召回率可提升约 20%**，适用于复杂问答、精确信息检索等场景。需注意：此功能**不可逆**，一旦开启无法回退，且会增加 glm-4.5 的 Token 消耗。详见：[上下文增强技术报告](https://docs.bigmodel.cn/cn/guide/tools/knowledge/contextual)

***

## 四、费用问题

**Q：知识库服务如何计费？有免费额度吗？**

**A：** 知识库服务主要包含以下计费项：

| 功能                          | 价格              |
| :-------------------------- | :-------------- |
| 知识向量化（各 Embedding 模型）       | 0.5 元/百万 Tokens |
| 开启重排（GLM-rerank/rerank-pro） | 0.8 元/百万 Tokens |
| 深度解析                        | 0.12 元/页        |
| 上下文增强 / 图片理解 / AI 标签生成      | 免费              |
| 知识库存储（超出免费额度部分）             | 0.04 元/GB/小时    |

**存储免费额度：** 所有用户永久享有 1GB 免费存储空间，超出部分按量后付费。详见：[知识库服务计费](https://docs.bigmodel.cn/cn/guide/tools/knowledge/price)

***

**Q：知识库欠费后数据会被删除吗？**

**A：** 欠费处理分两个阶段：

* **欠费 1–7 天：** 知识库暂停服务，但数据安全保留。补缴欠款后服务自动恢复。
* **欠费超过 7 天：** 系统将数据列入删除计划，保留最近上传的 1GB 数据，并删除超出部分。数据删除前 24 小时会发送通知。**数据被删除后即使补缴欠款也无法恢复。**

建议存储用量超过 70% 时，及时清理无用文件或升级套餐。详见：[知识库服务计费](https://docs.bigmodel.cn/cn/guide/tools/knowledge/price)
