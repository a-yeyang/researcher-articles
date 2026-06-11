<!-- source: https://docs.bigmodel.cn/cn/guide/agents/clothes -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 衣物识别

衣物识别智能体是一款基于多模态大模型（图像+文本）能力构建的智能信息提取工具，专注于图像中衣物属性的精准识别与结构化输出。该智能体能够从服饰类图片中自动提取衣物的多维度信息，包括但不限于品类、颜色、材质、款式、版型、图案、风格、品牌、衣领、口袋等关键属性。

智能体具备高度的通用性与定制能力，可根据不同行业场景、业务需求进行模型微调与标签体系扩展，适配复杂多变的衣物识别任务。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/326942e63ef2">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/trialcenter/agent?agentId=clothes_recognition_agent">
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

| 参数名称             | 类型            | 是否必填 | 参数说明                               |
| :--------------- | :------------ | :--- | :--------------------------------- |
| agent\_id        | String        | 是    | 智能体 ID：`clothes_recognition_agent` |
| messages         | List\<Object> | 是    | 会话消息体                              |
| └─ role          | String        | 是    | 用户的输入 `role = user`                |
| └─ content       | List\<Object> | 是    | 会话消息体                              |
|     └─ type      | String        | 是    | 目前支持内容类型，支持 `file_id`、`text`       |
|     └─ text      | String        | 是    | 提示词                                |
|     └─ field\_id | String        | 是    | 所上传衣物图像文件的ID                       |
