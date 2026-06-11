<!-- source: https://docs.bigmodel.cn/cn/guide/agents/contract -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 合同解析

合同解析智能体是基于大语言模型开发的专业文档信息抽取工具，致力于解决企业在合同管理过程中面临的信息提取难题。无论是采购合同、劳务合同还是租赁合同，本智能体都能快速识别并提取关键信息，如合同名称、签约方、合同金额、签约日期等。支持PDF、Word等多种文档格式，用户还可以自定义提取字段和规则，满足不同业务场景需求。通过将非结构化的合同文本转化为结构化数据，显著提升合同审核、管理和分析效率，为企业决策提供数据支持。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/f1c6c086c3d1">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=contract_parser_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

按调用次数后付费，**0.2 元/次**

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

| 参数名称               | 类型            | 是否必填 | 参数说明                                       |
| :----------------- | :------------ | :--- | :----------------------------------------- |
| stream             | boolean       | 否    | 是否使用流式返回，默认为 `false`，表示非流式输出               |
| agent\_id          | String        | 是    | 智能体 ID：`contract_parser_agent`             |
| messages           | List\<Object> | 是    | 会话消息体                                      |
| └─ role            | String        | 是    | 用户的输入 `role = user`                        |
| └─ content         | List\<Object> | 是    | 会话消息体                                      |
|     └─ type        | String        | 是    | 目前支持内容类型，支持 `file_id`、`text`               |
|     └─ field\_id   | String        | 是    | 所上传合同文件的 ID                                |
| custom\_variables  | Object        | 是    | 智能体扩展参数                                    |
| └─ default\_fields | List\<String> | 否    | 默认字段提取配置。键为字段名称，值为 `True`（提取）或 `False`（忽略） |
| └─ custom\_fields  | List\<Object> | 否    | 自定义字段提取配置，格式同上，留空表示无自定义字段                  |
