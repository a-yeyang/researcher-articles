<!-- source: https://docs.bigmodel.cn/cn/guide/start/quick-start -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

<Tip>
  本指南将帮助您快速上手智谱开放平台，从注册账号到发起第一次 API 调用，只需几分钟即可完成。
</Tip>

## 开始使用

<Steps>
  <Step title="注册账号">
    访问[智谱开放平台](https://open.bigmodel.cn)，点击右上角的「注册/登录」按钮，按照提示完成账号注册流程。

    <Frame>
      ![注册账号](https://cdn.bigmodel.cn/static/logo/register.png)
    </Frame>
  </Step>

  <Step title="获取API Key">
    登录后，在个人中心页面，点击 [API Keys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)，创建一个新的 API Key。

    <Warning>
      请妥善保管您的 API Key，不要泄露给他人，也不要直接硬编码在代码中。建议使用环境变量或配置文件来存储 API Key。
    </Warning>

    <Frame>
      ![Description](https://cdn.bigmodel.cn/markdown/1775643006211img_v3_0210i_e555ce4e-a817-431c-8bc8-f3a9ebbf2f3g.jpg?attname=img_v3_0210i_e555ce4e-a817-431c-8bc8-f3a9ebbf2f3g.jpg)
    </Frame>
  </Step>

  <Step title="选择模型">
    平台提供多种模型，您可以根据自己的需求选择合适的模型。详细的模型介绍请参考[模型概况](/cn/guide/start/model-overview)。

    <CardGroup cols={2}>
      <Card title="GLM-5.1" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book-open.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b5cd60a0c16c81255cbee52c2caf401)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/models/text/glm-5.1">
        通用旗舰大语言模型
      </Card>

      <Card title="GLM-5V-Turbo" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/eye.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b122d35262105038324f60f9e09612e)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/models/vlm/glm-5v-turbo">
        多模态 Coding 基座模型
      </Card>

      <Card title="GLM-Image" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/image.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e08359b6e7da6742ec2d4e6e9b7bc438)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/models/image-generation/glm-image">
        图像生成模型，文字渲染更稳更准
      </Card>

      <Card title="CogVideoX-3" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/video.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=54282ae2b5141037a874a54cba2bc15d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/models/video-generation/cogvideox-3">
        视频生成模型，新增首尾帧生成
      </Card>
    </CardGroup>
  </Step>

  <Step title="选择开发方式">
    平台提供多种开发方式，您可以根据项目需求和技术栈选择最适合的方式：

    <CardGroup cols={2}>
      <Card title="HTTP API" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/globe.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=12c9d7a94bd8f6a6c5f3ef31568fdb36)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/develop/http/introduction">
        标准 RESTful API，支持所有编程语言和开发框架
      </Card>

      <Card title="Python SDK" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/python.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=41127f670b5a754e1b5096914dac2a31)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/develop/python/introduction">
        官方 Python 开发工具包，提供完整的类型提示和异步支持
      </Card>

      <Card title="Java SDK" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/java.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=546388e0636f3e7e74cc27ca041d0289)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/develop/java/introduction">
        企业级 Java 开发工具包，支持高并发和高可用性
      </Card>

      <Card title="API 参考文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/api/introduction">
        完整的 API 接口文档和参数说明
      </Card>
    </CardGroup>
  </Step>

  <Step title="发起调用">
    准备好 `API Key` 和选择模型后，您可以开始发起调用。以下是使用 `curl` 和 `Python SDK` `Java SDK` 的示例：

    <Tabs>
      <Tab title="cURL">
        <Warning>
          注意：使用 [GLM 编码套餐](/cn/coding-plan/overview) 时，需要配置专属的 \
          Coding 端点 - [https://open.bigmodel.cn/api/coding/paas/v4](https://open.bigmodel.cn/api/coding/paas/v4) \
          而非通用端点 - [https://open.bigmodel.cn/api/paas/v4](https://open.bigmodel.cn/api/paas/v4) \
          注意：Coding API 端点仅限 Coding 场景，并不适用通用 API 场景，请区分使用。
        </Warning>

        ```bash theme={null}
        curl -X POST "https://open.bigmodel.cn/api/paas/v4/chat/completions" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -d '{
            "model": "glm-5.1",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个有用的AI助手。"
                },
                {
                    "role": "user",
                    "content": "你好，请介绍一下自己。"
                }
            ],
            "temperature": 1.0,
            "stream": true
        }'
        ```
      </Tab>

      <Tab title="Python SDK">
        **安装 SDK**

        ```bash theme={null}
        # 安装最新版本
        pip install zai-sdk

        # 或指定版本
        pip install zai-sdk==0.2.2
        ```

        **验证安装**

        ```python theme={null}
        import zai
        print(zai.__version__)
        ```

        **使用示例**

        ```python theme={null}
        from zai import ZhipuAiClient

        # 初始化客户端
        client = ZhipuAiClient(api_key="YOUR_API_KEY")

        # 创建聊天完成请求
        response = client.chat.completions.create(
            model="glm-5.1",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个有用的AI助手。"
                },
                {
                    "role": "user",
                    "content": "你好，请介绍一下自己。"
                }
            ],
            temperature=0.6
        )

        # 获取回复
        print(response.choices[0].message.content)
        ```
      </Tab>

      <Tab title="Java SDK">
        **安装 SDK**

        **Maven**

        ```xml theme={null}
        <dependency>
            <groupId>ai.z.openapi</groupId>
            <artifactId>zai-sdk</artifactId>
            <version>0.3.3</version>
        </dependency>
        ```

        **Gradle (Groovy)**

        ```groovy theme={null}
        implementation 'ai.z.openapi:zai-sdk:0.3.3'
        ```

        **使用示例**

        ```java theme={null}
        import ai.z.openapi.ZhipuAiClient;
        import ai.z.openapi.service.model.*;
        import java.util.Arrays;

        public class QuickStart {
            public static void main(String[] args) {
                // 初始化客户端
                ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                    .apiKey("YOUR_API_KEY")
                    .build();

                // 创建聊天完成请求
                ChatCompletionCreateParams request = ChatCompletionCreateParams.builder()
                    .model("glm-5.1")
                    .messages(Arrays.asList(
                        ChatMessage.builder()
                            .role(ChatMessageRole.USER.value())
                            .content("Hello, who are you?")
                            .build()
                    ))
                    .stream(false)
                    .temperature(0.6f)
                    .maxTokens(1024)
                    .build();

                // 发送请求
                ChatCompletionResponse response = client.chat().createChatCompletion(request);

                // 获取回复
                System.out.println(response.getData().getChoices().get(0).getMessage());
            }
        }
        ```
      </Tab>

      <Tab title="Python SDK(旧)">
        **安装 SDK**

        ```bash theme={null}
        # 安装最新版本
        pip install zhipuai

        # 或指定版本
        pip install zhipuai==2.1.5.20250726
        ```

        **验证安装**

        ```python theme={null}
        import zhipuai
        print(zhipuai.__version__)
        ```

        **使用示例**

        ```python theme={null}
        from zhipuai import ZhipuAI

        client = ZhipuAI(api_key="YOUR_API_KEY")
        response = client.chat.completions.create(
            model="glm-5.1",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个有用的AI助手。"
                },
                {
                    "role": "user",
                    "content": "你好，请介绍一下自己。"
                }
            ]
        )
        print(response.choices[0].message.content)
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 探索更多功能

<Card title="流式输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/water.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=2caefb923998df348ec0d0f367ebacbc)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  启用流式输出，获得更自然的对话体验。

  ```json theme={null}
  {
      "model": "glm-5.1",
      "messages": [
          {
              "role": "user",
              "content": "你好，请介绍一下自己。"
          }
      ],
      "stream": true
  }
  ```
</Card>

<Card title="多模态输入" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/images.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=5c7540ca4af57e6640b793cfd531ab54)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  使用 GLM-4.6V 模型处理图像和文本的混合输入。

  ```json theme={null}
  {
      "model": "glm-4.6v",
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "这张图片是什么?"
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "data:image/jpeg;base64,..."
                      }
                  }
              ]
          }
      ]
  }
  ```
</Card>

<Card title="函数调用" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/function.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a597d8cdc054b4c0e39c08295f570c86)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  使用函数调用功能，让模型调用您定义的函数。

  ```json theme={null}
  {
      "model": "glm-5.1",
      "messages": [
          {
              "type": "text",
              "text": "帮我查询从2024年1月20日，从北京出发前往上海的航班"
          }
      ],
      "tools": [
          {
              "type": "function",
              "function": {
                  "name": "get_flight_number",
                  "description": "根据始发地、目的地和日期，查询对应日期的航班号",
                  "parameters": {
                      "type": "object",
                      "properties": {
                          "departure": {
                              "description": "出发地",
                              "type": "string"
                          },
                          "destination": {
                              "description": "目的地",
                              "type": "string"
                          },
                          "date": {
                              "description": "日期",
                              "type": "string"
                          }
                      },
                      "required": ["departure", "destination", "date"]
                  }
              }
          }
      ]
  }
  ```
</Card>

## 常见问题

<AccordionGroup>
  <Accordion title="如何处理API调用错误？">
    当 API 调用出现错误时，服务器会返回相应的 HTTP 状态码和错误信息。常见的错误包括：

    * **401 Unauthorized**: API Key 无效或已过期
    * **400 Bad Request**: 请求参数错误
    * **429 Too Many Requests**: 超出 API 调用频率限制
    * **500 Internal Server Error**: 服务器内部错误

    建议实现适当的错误处理和重试机制，特别是对于 429 和 500 错误。
  </Accordion>

  <Accordion title="如何优化API调用成本？">
    以下是一些优化 API 调用成本的建议：

    1. 选择适合任务的模型，不同模型的价格不同
    2. 减少不必要的上下文信息，降低 token 消耗
    3. 使用缓存机制，避免重复调用
    4. 设置合理的 max\_tokens 参数，避免生成过长的回复
    5. 在开发阶段使用较小的模型进行测试
  </Accordion>

  <Accordion title="如何处理长文本输入？">
    对于超过模型上下文窗口大小的长文本，可以采用以下策略：

    1. 使用 GLM-4-Long 等支持更长上下文的模型
    2. 对文本进行分段处理，然后合并结果
    3. 使用文本嵌入模型进行相关性检索，只保留最相关的部分
    4. 对文本进行摘要，提取关键信息后再输入模型
  </Accordion>
</AccordionGroup>

<Tip>
  如果您在使用过程中遇到任何问题，可以查阅 [完整文档](/cn/faq/api-code) 或联系我们的 [技术支持](https://bigmodel.cn/online-book/customerService) 。
</Tip>
