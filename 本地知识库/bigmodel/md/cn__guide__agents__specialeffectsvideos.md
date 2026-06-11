<!-- source: https://docs.bigmodel.cn/cn/guide/agents/specialeffectsvideos -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 热门特效视频

热门特效视频是基于泛娱乐平台的热门玩法推出的视频模版智能体，能精准适配短视频创意生产需求。目前上线了法式热吻、转身热舞、变身比基尼/肌肉男三个特效模版，选择对应模版后，只需上传一张图像素材并输入对应的提示词即可生成特效视频。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/18446d4f3fb7">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=vidu_template_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

按调用次数后付费，**1.25 元/次**

## **接口请求**

| 传输方式   | https                                                                            |
| :----- | :------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 调用方式   | 异步调用，需通过查询接口获取结果                                                                 |
| 字符编码   | UTF-8                                                                            |
| 接口请求格式 | JSON                                                                             |
| 响应格式   | JSON                                                                             |
| 接口请求类型 | POST                                                                             |

## **请求参数**

| 参数名称              | 类型            | 是否必填 | 参数说明                                          |
| :---------------- | :------------ | :--- | :-------------------------------------------- |
| agent\_id         | String        | 是    | 固定值：`vidu_template_agent`                     |
| request\_id       | String        | 否    | 由用户端传参，需保证唯一性；用于区分每次请求的唯一标识，用户端不传时平台会默认生成     |
| messages          | List\<Object> | 是    | 会话消息体                                         |
| └─ role           | String        | 是    | 用户的输入 `role = user`                           |
| └─ content        | List\<Object> | 是    | 会话消息体                                         |
|     └─ type       | String        | 是    | 目前支持内容类型，支持 `text`、`image_url`                |
|     └─ text       | String        | 是    | 用户输入的文本内容                                     |
|     └─ image\_url | String        | 是    | 当 `type="image_url"` 时的URL；即参考图片URL           |
| custom\_variables | Object        | 否    | 智能体扩展参数                                       |
| └─ template       | String        | 是    | 视频特效模板，支持 `french_kiss`、`bodyshake`、`sexy_me` |

## **响应参数**

| 字段名称      | 字段类型   | 备注                                                   |
| :-------- | :----- | :--------------------------------------------------- |
| status    | String | 模型会话状态，`pending` - 视频特效任务创建成功, `failed` - 视频特效任务创建失败 |
| async\_id | String | 视频特效任务id                                             |
| agent\_id | String | 固定值：`vidu_template_agent`                            |
| error     | Object | 服务器错误信息                                              |
| └─ code   | String | 错误码                                                  |
| message   | String | 错误信息                                                 |
