<!-- source: https://docs.bigmodel.cn/cn/guide/agents/sale -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 销售质检

面向销售沟通场景的话术质检智能体，支持自动分析通话录音文本，实现跨场景、跨业务的话术标准化评估与精准打分。无论是企业质检部门批量审核通话记录，还是一线销售团队实时优化话术策略，均可高效集成解决话术偏差、合规风险等难题，显著提升沟通效率与成单转化率。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/8d97b500411c">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=sales_check_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

* **按 Token 后付费，5 元/百万 Tokens**
* 计量范围：智能体全任务流节点产生的 Tokens 总数

## **接口请求**

| 传输方式   | https                                                                            |
| :----- | :------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 字符编码   | UTF-8                                                                            |
| 接口请求格式 | JSON                                                                             |
| 响应格式   | JSON                                                                             |
| 接口请求类型 | POST                                                                             |
| 开发语言   | 任意可发起 http 请求的开发语言                                                               |

## **请求参数**

| 参数名称               | 类型            | 是否必填 | 参数说明                                                                                                                                                                                                                                                             |
| :----------------- | :------------ | :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agent\_id          | String        | 是    | 智能体 ID：`sales_check_agent`                                                                                                                                                                                                                                       |
| messages           | List\<Object> | 是    | 会话消息体                                                                                                                                                                                                                                                            |
| └─ role            | String        | 是    | 用户的输入 `role = user`                                                                                                                                                                                                                                              |
| └─ content         | List\<Object> | 是    | 会话消息体                                                                                                                                                                                                                                                            |
|     └─ type        | String        | 是    | 目前支持内容类型，支持 `text`                                                                                                                                                                                                                                               |
|     └─ text        | String        | 是    | 客服对话记录文本                                                                                                                                                                                                                                                         |
| custom\_variables  | Object        | 是    | 智能体扩展参数                                                                                                                                                                                                                                                          |
| └─ default\_fields | List\<String> | 是    | 内置质检维度。可选值：<br />• `self_intro`（自我介绍）<br />• `state_intent`（表明来意）<br />• `need_dig`（需求挖掘）<br />• `highlight`（介绍产品优点）<br />• `historical`（询问历史渠道）<br />• `cite`（成功案例引用）<br />• `deal`（优惠活动）<br />• `action`（引导行动）<br />• `contact`（添加联系方式）<br />• `summary`（通话总结） |
| └─ custom\_fields  | List\<Object> | 否    | 自定义质检字段和说明                                                                                                                                                                                                                                                       |
| └─ rate            | String        | 是    | 评分方式，可选值：`基础评分` 和 `阶梯评分`                                                                                                                                                                                                                                         |
