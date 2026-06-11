<!-- source: https://docs.bigmodel.cn/cn/guide/agents/glm-ppt -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM PPT

GLM PPT 是面向职场人与创作者的新一代智能工具。基于 GLM 大模型深度驱动，区别于传统工程化拼接方案，实现从自然语言指令到可交互幻灯片的一键生成。深度融合内容生成与设计规范，可快速交付专业级作品，降低设计门槛，提升内容生产效率。

<CardGroup cols={2}>
  <Card title="详细说明" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://www.bigmodel.cn/marketplace/agent_detail/b2d182f15389">
    查看介绍、核心功能、适用场景
  </Card>

  <Card title=" Agent API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D">
    查看完整的 API 文档
  </Card>

  <Card title="体验中心" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://bigmodel.cn/trialcenter/apptrial/agent?agentId=slides_glm_agent">
    点击立即体验
  </Card>
</CardGroup>

## **价格**

* **按 Tokens 消耗后付费，5 元/百万 Tokens**
* 计量范围：智能体全任务流节点产生的 Tokens 总数

### 用户并发权益

API 调用会受到速率限制，当前我们限制的维度是请求并发数量（在途请求任务数量）。不同等级的用户并发保障如下。

| V0 | V1 | V2 | V3 |
| :- | :- | :- | :- |
| 10 | 15 | 20 | 30 |

## GLM PPT

### **接口请求**

| 传输方式   | https                                                                            |
| :----- | :------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 调用方式   | 同步调用，等待模型完成执行并返回最终结果或使用SSE调用                                                     |
| 字符编码   | UTF-8                                                                            |
| 接口请求格式 | JSON                                                                             |
| 响应格式   | JSON 或标准 Stream Event                                                            |
| 接口请求类型 | POST                                                                             |
| 开发语言支持 | 任意可发起 http 请求的开发语言                                                               |

#### **请求参数**

| 参数名称             | 类型            | 是否必填 | 参数说明                            |
| :--------------- | :------------ | :--- | :------------------------------ |
| agent\_id        | String        | 是    | 智能体 ID：`slides_glm_agent`       |
| messages         | List\<Object> | 是    | 会话消息体                           |
| conversation\_id | String        | 否    | 会话id                            |
| stream           | String        | 是    | 目前只支持流式，必须传 `true`              |
| └─ role          | String        | 是    | 用户的输入 `role = user`             |
| └─ content       | List\<Object> | 是    | 会话内容                            |
|     └─ type      | String        | 是    | 目前支持内容类型，目前仅支持 `text`           |
|     └─ text      | String        | 是    | 具体内容，例如："帮我生成一个关于人工智能技术发展的市场调研" |

#### 响应参数

| 字段名称                      | 字段类型          | 备注                                                                                                                                                                                    |
| :------------------------ | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id                        | String        | 请求唯一ID                                                                                                                                                                                |
| agent\_id                 | String        | 当前 agent id                                                                                                                                                                           |
| conversation\_id          | String        | 当前对话的唯一ID                                                                                                                                                                             |
| choices                   | List\<Object> | 智能体响应选项                                                                                                                                                                               |
| └─ index                  | Number        | 事件编号，单调递增                                                                                                                                                                             |
| └─ messages               | List\<Object> | 智能体响应消息体                                                                                                                                                                              |
|     └─ role               | String        | 智能体的角色 `role = assistant`                                                                                                                                                             |
|     └─ phase              | String        | 当前角色的状态：思考-`thinking`、<br />使用工具-`tool`、回答-`answer`                                                                                                                                   |
|     └─ content            | List\<Object> | 智能体响应内容                                                                                                                                                                               |
|         └─ type           | String        | 响应内容类型：文本-`text`、对象-`object`                                                                                                                                                          |
|         └─ tag\_cn        | String        | 标签（中文），例如：插入幻灯片                                                                                                                                                                       |
|         └─ tag\_en        | String        | 标签（英文），例如：Insert Page                                                                                                                                                                 |
|         └─ text           | String        | 如果 `type = text`，则这个字段以<br />字符串格式给出具体内容                                                                                                                                              |
|         └─ object         | Object        | 如果 `type = object`，则这个字段<br />以对象格式给出具体内容                                                                                                                                             |
|             └─ tool\_name | String        | 工具唯一标识，例如：`search`、`insert_page`                                                                                                                                                      |
|             └─ input      | String        | 调用工具的输入。<br />例如，搜索时，此字段给出了具体的搜索词                                                                                                                                                     |
|             └─ output     | String        | 工具执行后的输出。<br />例如，生成幻灯片时，HTML 内容通过此字段输出                                                                                                                                               |
|             └─ position   | List\<Number> | 如果工具涉及到 PPT 的操作，`position` 字段指明具体操作哪几页 slides；<br />例如：<br />• 当用户输入「在第二页之后插入一张幻灯片」，则 `position = [3]`，`output` 是第三页幻灯片的 HTML 内容<br />• 当用户输入「请删除第四、五、六页幻灯片」，则 `position = [4, 5, 6]` |

#### 请求示例

```shell theme={null}
curl --location --request POST 'https://open.bigmodel.cn/api/v1/agents' \
--header 'Authorization: {{api-key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "agent_id": "slides_glm_agent",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "帮我生成一个游戏主机市场发展调研"
                }
            ]
        }
    ]
}'
```

#### 响应示例

```JSON theme={null}
// 第一次 event
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 0,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "我需要为"
                        }
                    ],
                    "phase": "thinking" 
                }
            ]
        }
    ]
}

// 第二次 event
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 1,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "用户生成一个"
                        }
                    ],
                    "phase": "thinking"
                }
            ]
        }
    ]
}

// 命中工具
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 2,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "object",
                            "object": {
                                "tool_name" : "search",
                                "input" : "搜索词"
                            },
                            "tag_cn": "搜索",
                            "tag_en": "Search"
                        }
                    ]
                    "phase": "tool"
                }
            ]
        }
    ]
}

// 命中工具
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 3,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "object",
                            "object": {
                                "tool_name" : "search",
                                "output" : "搜索结果"
                            },
                            "tag_cn": "搜索",
                            "tag_en": "Search"
                        }
                    ],
                    "phase": "tool"
                }
            ]
        }
    ],
}

// 命中工具
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 4,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "object",
                            "object": {
                                "tool_name" : "insert_page",
                                "input": "创建中国游戏主机市场现状与机遇页，详细介绍中..."
                            },
                            "tag_cn": "插入幻灯片",
                            "tag_en": "Insert Page"
                        }
                    ],
                    "phase": "tool"
                }
            ]
        }
    ]
}

// 命中工具
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 5,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "object",
                            "object": {
                                "tool_name" : "insert_page",
                                "output" : "html doc",
                                "position": [1],
                                "title":"标题"
                            },
                            "tag_cn": "添加幻灯片",
                            "tag_en": "Insert Page"
                        }
                    ],
                    "phase": "tool"
                }
            ]
        }
    ],
}

// 命中工具
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 5,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "object",
                            "object": {
                                "tool_name" : "remove_slides",
                                "position": [1,2,3]
                            },
                            "tag_cn": "删除幻灯片",
                            "tag_en": "Remove Pages"
                        }
                    ],
                    "phase": "tool"
                }
            ]
        }
    ],
}

// assistant answer
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 6,
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "文案"
                        }
                    ],
                    "phase": "answer"
                }
            ]
        }
    ]
}

// 最后一次 event
{
    "id": "202507221412023db1a56fc77943d8",
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 123,
            "finish_reason": "stop"
            "messages": [
                ...
            ],
        }
    ],
    "usage": {
        "prompt_tokens": 100,
        "completion_tokens": 200,
        "total_tokens": 300
    },
    // 如果 finish_reason != stop，出现 error 字段；
    "error": {
        "code": "1301",
        "message": "系统检测到输入或生成内容可能包含不安全或敏感内容"
    }
}
```

## 导出PDF

### **接口请求**

| 传输方式   | https                                                                                                        |
| :----- | :----------------------------------------------------------------------------------------------------------- |
| 请求地址   | [https://open.bigmodel.cn/api/v1/agents/conversation/](https://open.bigmodel.cn/api/v1/agents/conversation/) |
| 调用方式   | 同步调用，等待模型完成执行并返回最终结果或使用SSE调用                                                                                 |
| 字符编码   | UTF-8                                                                                                        |
| 接口请求格式 | JSON                                                                                                         |
| 响应格式   | JSON                                                                                                         |
| 接口请求类型 | POST                                                                                                         |
| 开发语言支持 | 任意可发起 http 请求的开发语言                                                                                           |

#### 请求参数

| 字段名称              | 字段类型    | 是否必填 | 备注                            |
| :---------------- | :------ | :--- | :---------------------------- |
| agent\_id         | String  | 是    | 智能体 ID，ID值：slides\_glm\_agent |
| conversation\_id  | String  | 是    | 当前对话的唯一ID                     |
| custom\_variables | Object  | 否    | 自定义参数                         |
| └─ include\_pdf   | Boolean | 否    | 是否导出 PDF 文件                   |
| └─ include\_html  | Boolean | 否    | 是否导出 HTML 文件                  |

#### 响应参数

| 字段名称                  | 字段类型          | 备注                                                |
| :-------------------- | :------------ | :------------------------------------------------ |
| agent\_id             | String        | 固定值：slides\_glm\_agent                            |
| conversation\_id      | String        | 当前对话的唯一ID                                         |
| choices               | List\<Object> | 智能体响应选项                                           |
| └─ messages           | List\<Object> | 智能体响应消息体                                          |
|     └─ role           | String        | 智能体的角色 `role = assistant`                         |
|     └─ content        | List\<Object> | 智能体响应内容                                           |
|         └─ type       | String        | 响应内容类型：文件下载链接-`file_url`、<br />图片下载链接-`image_url` |
|         └─ tag\_cn    | String        | 标签（中文），例如：市场调研.pdf                                |
|         └─ tag\_en    | String        | 标签（英文），例如：market research.pdf                     |
|         └─ file\_url  | String        | 如果 `type = file_url`，<br />则这个字段给出文件的具体下载链接       |
|         └─ image\_url | String        | 如果 `type = image_url`，<br />则这个字段给出图片的具体下载链接      |

#### 请求示例

```JSON theme={null}
{
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "custom_variables": {
        "include_pdf": true
    }
}
```

#### 响应示例

```JSON theme={null}
{
    "agent_id": "slides_glm_agent",
    "conversation_id": "1750756263-a0e8bc1e2ee14879810025009e2ff693",
    "choices": [
        {
            "index": 0,
            "finish_reason": "stop",
            "messages": [
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "file_url",
                            "file_url": "https://xxx.cn",
                            "tag_cn": "市场调研.pdf",
                            "tag_en": "market research.pdf"
                        }                        
                    ],
                    "phase": "answer"
                }
            ]
        }
    ]
}
```
