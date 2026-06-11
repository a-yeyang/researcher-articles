<!-- source: https://docs.bigmodel.cn/cn/guide/agents/winningbidder -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 中标解析

在竞争激烈的市场中，快速获取和分析中标信息是企业制定战略、评估对手、发现合作伙伴的关键。中标解析智能体是一款基于智造大语言模型的专业级文本分析工具，它能模拟行业分析师的审查和提炼能力，自动处理各类中标信息。无论是政府官网发布的中标公告，还是企业内部归档的中标结果文件，本智能体都能提供高效、精准、结构化的信息提取服务，为市场分析、商务拓展等提供高质量的数据支持。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/2029a6c1b5f3">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=bidwin_parser_agent">
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

| 参数名称              | 类型            | 是否必填 | 参数说明                            |
| :---------------- | :------------ | :--- | :------------------------------ |
| agent\_id         | String        | 是    | 智能体 ID：`bidwin_parser_agent`    |
| messages          | List\<Object> | 是    | 会话消息体                           |
| └─ role           | String        | 是    | 用户的输入 `role = user`             |
| └─ content        | List\<Object> | 是    | 会话消息体                           |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`              |
|     └─ text       | String        | 是    | 招标公告HTML文本                      |
| custom\_variables | Object        | 是    | 智能体扩展参数                         |
| └─ custom\_fields | List\<Object> | 否    | 自定义字段提取说明，每项是一个键值对，键为字段名，值为提取规则 |
