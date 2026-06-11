<!-- source: https://docs.bigmodel.cn/cn/coding-plan/usage-notes -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用须知

## 并发限制

速率（并发数）限制与您的套餐等级相关，平台会根据资源进行动态调整，基本原则 **Max> Pro > Lite**。每个项目开发可使用 Subagent 等方式并发模型调用，我们的推荐使用项目数量如下：

* Lite ： 建议同时进行单个项目的开发
* Pro ： 建议同时进行 1-2 个项目的开发
* Max ：建议同时进行 2+ 个项目的开发

<Tip>
  套餐用户在低峰期将享有更高的并发权益（动态提升），能够支撑更高数量的项目开发。
</Tip>

## 账号使用规范

<Note>
  GLM Coding Plan 套餐为订阅人**专享使用**。 若因账号共享导致出现多人共用同一套餐的情况，我们可能会视为不当使用，并在必要时对订阅权益做出相应限制，严重时或将影响账号正常使用。
</Note>

<Note>
  GLM Coding Plan 仅限在官方支持的<a href="https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7">指定工具与产品环境</a>中使用。

  若系统检测到账号存在将 GLM Coding Plan 用于非支持工具的行为，平台有权基于保障系统公平性与服务稳定性的原则，对相关订阅权益采取必要的限制措施。
</Note>

* 为确保广大订阅用户权益，如您的账号因违反 [订阅及自动续费协议](https://docs.bigmodel.cn/cn/terms/subscription-agreement#%E5%85%AD%E3%80%81%E4%BD%BF%E7%94%A8%E8%A7%84%E8%8C%83)， 命中风控规则，将可能会被进行包括高强度限流、冻结、封禁等风控处置措施。
* 命中风控策略后您可以在 [套餐概览](https://www.bigmodel.cn/coding-plan/personal/overview) 页面查看风控提示，如认为判定有误，可发起申诉。3 次以上违反公平使用条款，将会被封禁处理。

## 管理订阅

您可以通过以下方式管理订阅、查看账单和取消计划：

1. 登陆 [Bigmodel 控制台](https://bigmodel.cn/console/overview)
2. 开启与关闭续订 -> [套餐概览](https://www.bigmodel.cn/coding-plan/personal/overview)
3. 查看套餐用量进度 -> [用量统计](https://www.bigmodel.cn/coding-plan/personal/usage)
4. 查看账单与明细  ->  [费用账单](https://bigmodel.cn/finance-center/bill/expensebill/list) ->  详情切换至费用明细

## 有效期与续费

* 订阅将在**每个计费周期结束时自动续费**，费用会从您绑定的支付方式中扣除。
* 系统会按照以下顺序扣费：

1. 优先使用平台账号内赠金余额。
2. 若赠金不足，则使用平台账号内现金余额。
3. 若以上余额不足，再从您绑定的第三方支付方式（如微信、支付宝）扣款。

* 如您需要取消订阅，可以在订阅管理页面取消订阅。请务必在下一个扣费日**至少 3 天前**取消，以避免自动续费。取消后，当前周期继续有效，到期后不再续费。

## 退款政策

请注意，订阅服务一经购买即视为确认，不支持退款。即使您未使用完套餐，费用也无法退回。我们建议您根据使用需求选择合适的订阅套餐和周期。
