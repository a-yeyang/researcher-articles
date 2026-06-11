<!-- source: https://docs.bigmodel.cn/cn/guide/agents/aicaricature -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# AI漫画

通过固定漫画核心特征来满足漫画生成结果的一致性和可控性，使用户能够自定义制作漫画。

* 角色高度一致性
* 低成本、高效率、定制化地创作漫画

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/ee4a85afc16b">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=cartoon_generator_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

按调用次数后付费，**0.06 元/次**

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

| 参数名称              | 类型            | 是否必填 | 参数说明                                      |
| :---------------- | :------------ | :--- | :---------------------------------------- |
| agent\_id         | String        | 是    | 智能体 ID：`cartoon_generator_agent`          |
| messages          | List\<Object> | 是    | 会话消息体                                     |
| └─ role           | String        | 是    | 用户的输入 `role = user`                       |
| └─ content        | List\<Object> | 是    | 会话消息体                                     |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`、`image_url`            |
|     └─ text       | String        | 是    | 提示词, 当 `type=text` 时填写                    |
|     └─ image\_url | String        | 是    | 参照图片URL, 当 `type="image_url"` 时填写，大小限制20M |
