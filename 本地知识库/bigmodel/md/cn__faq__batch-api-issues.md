<!-- source: https://docs.bigmodel.cn/cn/faq/batch-api-issues -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch API

**Q：支持的 Batch API 模型有哪些？**

**A：** 支持的 Batch API 模型如下所示

* GLM-4-Flash
* GLM-4-Air
* GLM-3-Turbo
* Embedding-2
* Embedding-3
* GLM-4-0520
* GLM-4
* GLM-4-Plus
* Cogview-3
* CogVideoX
* GLM-4V
* GLM-4-Plus
* GLM-4-Air-250414
* GLM-4-Long
* GLM-4-FlashX-250414
* GLM-4V-Plus-0111
* CogView-4
* CogVideoX-2

***

**Q：Batch API 的价格如何？**

**A：** 价格是标准 API 的 50%。参考 [产品定价](https://open.bigmodel.cn/pricing)

***

**Q：Batch API 的并发限制是怎样的？**

**A：** Batch API 的并发限制与现有的每个模型并发限制是分开的。Batch API 引入了两种新的限制：

* 单个 Batch 文件中包含最多 50,000 个请求且不超过 100M。
* 每个模型的 Batch 有最大排队限制。当达到请求队列上限时，请等待当前任务完成后再提交新任务。
* 向量模型（Embedding-2、Embedding-3）Batch 文件请求数量限制为不超过 10,000 次。

| 模型               | Batch 队列限制      |
| :--------------- | :-------------- |
| GLM-4-Flash      | 1000 万次         |
| GLM-4-Air        | 1000 万次         |
| GLM-3-Turbo      | 200 万次          |
| Embedding-2      | 200 万次          |
| Embedding-3      | 200 万次          |
| GLM-4-Plus       | 200 万次          |
| GLM-4-0520       | 50 万次           |
| GLM-4            | 50 万次           |
| Cogview-3        | 3 万次            |
| CogVideoX        | 1 万次            |
| GLM-4V           | 1 万次            |

***

**Q：如何在调用 Batch API 前进行实名认证？**

**A：** 调用 Batch API 必须实名认证，请先前往 [实名认证](https://open.bigmodel.cn/usercenter/auth) 页面完成个人认证或企业认证，成功认证后，将免费获得 500 万 tokens。

***

**Q：Batch 的过期如何处理？**

**A：** 如果 Batch 未能及时完成，该批次将被标记为过期状态；批次中未完成的请求将被取消。对于批次中已完成的请求，用户可以通过文件获取，并且需要支付这些请求消耗的费用。

***

**Q：Batch 文件有哪些存储限制？**

**A：** Batch 文件最多上传 1000 个文件。系统只保留您的文件 30 天，过期后文件将自动删除，无法恢复。

***

**Q：如何删除Batch 文件？**

**A：** 请前往 [Batch 数据](/cn/guide/tools/batch) 页面进行删除、或通过调用接口删除。
