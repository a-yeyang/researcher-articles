<!-- source: https://docs.bigmodel.cn/cn/guide/agents/social -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 社科文学翻译

社科文学翻译智能体是基于大语言模型构建的专业翻译工具，针对社科与文学类文本进行风格保真、语义精准的端到端翻译。它适用于学术论文、社科著作、小说、诗歌、散文等高文体要求的文本场景，致力于在提升翻译效率的同时，保持原作语言风格与文化语境的准确传达。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/52df998146cb">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=social_literature_translation_agent">
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

| 参数名称              | 类型            | 是否必填 | 参数说明                                         |
| :---------------- | :------------ | :--- | :------------------------------------------- |
| agent\_id         | String        | 是    | 智能体 ID：`social_literature_translation_agent` |
| messages          | List\<Object> | 是    | 会话消息体                                        |
| └─ role           | String        | 是    | 用户的输入 `role = user`                          |
| └─ content        | String        | 是    | 会话消息体                                        |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`                           |
|     └─ text       | String        | 是    | 提示词                                          |
| custom\_variables | Object        | 是    | 智能体扩展参数                                      |
| └─ source\_lang   | String        | 是    | 源语言代码（支持 `en` 表示英语、 `zh-CN` 表示简体中文）          |
| └─ target\_lang   | String        | 是    | 目标语言代码支持 `en` 表示英语、 `zh-CN` 表示简体中文）          |
