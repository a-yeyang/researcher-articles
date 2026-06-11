<!-- source: https://docs.bigmodel.cn/cn/guide/agents/bill -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 票据识别

等格式中高效提取简历内容，快速识别技能、经验、学历等核心信息。票据识别智能体专注于各类财务、保险与合规票据的自动识别与结构化解析。该智能体支持多种票据格式（如发票、收据、保单、费用单据等），用户可按需提取如发票抬头、金额、税号、保险条款、凭证编号等关键信息字段。

智能体具备高准确率、强泛化、可定制等能力，能够适配企业在不同业务流程中的票据处理需求，大幅提升票据审核、录入与归档的自动化程度。同时也能为求职者提供匹配建议，帮助优化简历、提升求职成功率，广泛适用于HR招聘增强与个人求职分析等多类应用场景。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/56169cdcac0d">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=receipt_recognition_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

* **按 Token 后付费，4 元/百万 Tokens**
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

| 参数名称            | 类型            | 是否必填 | 参数说明                               |
| :-------------- | :------------ | :--- | :--------------------------------- |
| agent\_id       | String        | 是    | 智能体 ID：`receipt_recognition_agent` |
| messages        | List\<Object> | 是    | 会话消息体                              |
| └─ role         | String        | 是    | 用户的输入 `role = user`                |
| └─ content      | List\<Object> | 是    | 会话消息体                              |
|     └─ type     | String        | 是    | 目前支持内容类型，支持 `file_id`、`text`       |
|     └─ text     | String        | 是    | 提示词                                |
|     └─ file\_id | String        | 是    | 所上传票据图像文件的 ID                      |
