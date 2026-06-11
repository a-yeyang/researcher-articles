<!-- source: https://docs.bigmodel.cn/cn/guide/agents/aidrawing -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# AI绘图

通用高效的AI图像生成解决方案，支持通语言描述或关键词输入，快速生成高质量、风格统一、内容契合的图片，广泛适用于电商装修、内容创作、活动宣传等多种场景，显著提升视觉素材生产效率与表达效果。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/e7b00f3a326b">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=ai_drawing_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

按调用次数后付费，**0.4 元/次**

## **请求请求**

| 传输方式   | https                                                                            |
| :----- | :------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 字符编码   | UTF-8                                                                            |
| 接口请求格式 | JSON                                                                             |
| 响应格式   | JSON                                                                             |
| 接口请求类型 | POST                                                                             |
| 开发语言   | 任意可发起 http 请求的开发语言                                                               |

## **请求参数**

| 参数名称              | 类型            | 是否必填 | 参数说明                                                                                         |
| :---------------- | :------------ | :--- | :------------------------------------------------------------------------------------------- |
| agent\_id         | String        | 是    | 智能体 ID：`ai_drawing_agent`                                                                    |
| messages          | List\<Object> | 是    | 会话消息体                                                                                        |
| └─ role           | String        | 是    | 用户的输入 `role = user`                                                                          |
| └─ content        | List\<Object> | 是    | 会话消息体                                                                                        |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`                                                                           |
|     └─ text       | String        | 是    | 提示词                                                                                          |
| custom\_variables | Object        | 是    | 智能体扩展参数                                                                                      |
| └─ size           | String        | 是    | 分辨率。可选值: `1024*1024`, `768*1344`, `1344*768`, `864*1152`, `1152*864`, `1440*720`, `720*1440` |
