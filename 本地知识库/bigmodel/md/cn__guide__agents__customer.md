<!-- source: https://docs.bigmodel.cn/cn/guide/agents/customer -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 客服话术质检

面向企业服务场景的客服质检智能体，精准提取对话关键信息，智能评估沟通表现并通过多维度质检与科学评分，助力企业快速定位服务短板。无论是优化客户体验流程，还是构建标准化服务管控体系，均可高效解决服务质量评估难题，显著提升企业服务形象与市场竞争力。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/b615ea387658">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=service_check_agent">
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

| 参数名称               | 类型            | 是否必填 | 参数说明                                                                                                                                                                                                                          |
| :----------------- | :------------ | :--- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agent\_id          | String        | 是    | 智能体 ID：`service_check_agent`                                                                                                                                                                                                  |
| messages           | List\<Object> | 是    | 会话消息体                                                                                                                                                                                                                         |
| └─ role            | String        | 是    | 用户的输入 `role = user`                                                                                                                                                                                                           |
| └─ content         | List\<Object> | 是    | 会话消息体                                                                                                                                                                                                                         |
|     └─ type        | String        | 是    | 目前支持内容类型，支持 `text`                                                                                                                                                                                                            |
|     └─ text        | String        | 是    | 客服对话记录文本                                                                                                                                                                                                                      |
| custom\_variables  | Object        | 是    | 扩展字段                                                                                                                                                                                                                          |
| └─ default\_fields | List\<String> | 是    | 内置质检维度。可选值：<br />• `customer_request`（客户诉求）<br />• `service_attitude`（服务态度）<br />• `communication`（沟通能力）<br />• `solution`（解决方案）<br />• `followup_needed`（是否需要跟进）<br />• `escalation_risk`（是否会有上升风险）<br />• `risk_type`（风险类型） |
| └─ custom\_fields  | List\<Object> | 否    | 自定义质检字段和说明。比如：<br />`[{"客户情绪":"从平静、生气、疑虑中选择"}]`                                                                                                                                                                               |
