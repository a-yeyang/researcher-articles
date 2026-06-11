<!-- source: https://docs.bigmodel.cn/cn/guide/agents/media -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 社交媒体翻译

社媒翻译智能体是基于先进大语言模型技术打造的专业翻译工具，专为社交媒体内容特点设计优化。它能够准确识别和处理网络流行语、表情符号、缩写词和平台特定表达，在保留原文风格、情感色彩的同时，提供地道自然的翻译结果。与传统翻译工具不同，本智能体深度理解多语言社交语境，能够处理非正式、口语化和文化引用表达，为用户提供跨文化交流的无缝体验，让国际社交变得轻松愉快。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/475a3cbfc308">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=social_translation_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

* **按 Token 后付费，5 元/百万 Tokens**
* 计量范围：智能体全任务流节点产生的 Tokens 总数

## **请求地址**

| 传输方式   | https                                                                            |
| :----- | :------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 字符编码   | UTF-8                                                                            |
| 接口请求格式 | JSON                                                                             |
| 响应格式   | JSON                                                                             |
| 接口请求类型 | POST                                                                             |
| 开发语言   | 任意可发起 http 请求的开发语言                                                               |

## **请求参数**

| 参数名称              | 类型            | 是否必填 | 参数说明                                     |
| :---------------- | :------------ | :--- | :--------------------------------------- |
| agent\_id         | String        | 是    | 智能体 ID：`social_translation_agent`        |
| messages          | List\<Object> | 是    | 会话消息体                                    |
| └─ role           | String        | 是    | 用户的输入 `role = user`                      |
| └─ content        | List\<Object> | 是    | 会话消息体                                    |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`                       |
|     └─ text       | String        | 是    | 提示词                                      |
| custom\_variables | Object        | 是    | 智能体扩展参数                                  |
| └─ source\_lang   | String        | 是    | 源语言目前仅支持英文、中文，`en` 表示英语， `zh-CN` 表示简体中文  |
| └─ target\_lang   | String        | 是    | 目标语言目前仅支持英文、中文，`en` 表示英语， `zh-CN` 表示简体中文 |
| └─ style          | String        | 是    | 翻译风格（如 `通用风格`，也可支持 `自动风格`、`鲁迅风格` ）       |
