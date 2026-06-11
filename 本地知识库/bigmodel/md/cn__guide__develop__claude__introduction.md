<!-- source: https://docs.bigmodel.cn/cn/guide/develop/claude/introduction -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude API 兼容

智谱提供与 Claude API 兼容的接口，这意味着您可以使用现有的 Anthropic SDK 代码，只需要简单修改 API 密钥和基础 URL，就能无缝切换到智谱的模型服务。

### 核心优势

<CardGroup cols={2}>
  <Card title="零学习成本" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    如果您已经熟悉 Anthropic SDK，可以立即上手使用
  </Card>

  <Card title="快速迁移" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrows-rotate.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2b334fa767b3736a3afc9babb9c6d575)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    现有 Claude 应用如 Claude Code 等可以快速迁移到智谱平台
  </Card>

  <Card title="极速访问" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    无障碍极速访问智谱模型的强大能力
  </Card>

  <Card title="持续更新" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-up.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2c1e1940f6d55086f84c6054cc093fac)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    跟随 Anthropic SDK 更新，保持最新功能支持
  </Card>
</CardGroup>

<Warning>
  某些场景下智谱与 Claude 接口仍存在差异，但不影响整体兼容性。
</Warning>

## 从 Claude 迁移至智谱

如果您已经在使用 Claude API，迁移到智谱非常简单。

* 替换您访问的 `base_url` 为 `https://open.bigmodel.cn/api/anthropic`
* 在 [智谱开放平台](https://bigmodel.cn/usercenter/proj-mgmt/apikeys) 申请您的 `api_key`
* 调用时使用智谱模型编码即可

```python theme={null}
# 原来的 Claude 代码
import anthropic

client = anthropic.Anthropic(
    base_url="your-base-url",
    api_key="your-api-key",
)

# 迁移到智谱，只需要修改三个地方
client = anthropic.Anthropic(
    api_key="your-zhipuai-api-key",  # 替换为智谱 API Key
    base_url="https://open.bigmodel.cn/api/anthropic"  # 配置智谱 base_url
)

# 模型编码使用 智谱模型，其他代码保持不变
message = client.messages.create(
    model="glm-5.1",  # 使用智谱模型
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**推荐模型**

| 模型编码                                     | 定位    | 特点                                   | 上下文  | 最大输出 |
| :--------------------------------------- | :---- | :----------------------------------- | :--- | :--- |
| [glm-5.1](/cn/guide/models/text/glm-5.1) | 高智能旗舰 | - 旗舰性能 <br />- 长程任务显著提升，可自主工作长达 8 小时 | 200K | 128K |
| [glm-5](/cn/guide/models/text/glm-5)     | 高智能基座 | - 擅长 Agentic 长程规划与执行                 | 200K | 128K |
| [glm-4.7](/cn/guide/models/text/glm-4.7) | 高智能模型 | - 强大的推理能力、代码生成能力以及工具调用能力             | 200K | 128K |

## 详细步骤

### 获取 API Key

1. 访问 [智谱开放平台](https://bigmodel.cn)
2. 注册并登录您的账户
3. 在 [API Keys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys) 管理页面创建 API Key
4. 复制您的 API Key 以供使用

<Tip>
  建议将 API Key 设置为环境变量：`export ANTHROPIC_API_KEY=your-api-key` 替代硬编码到代码中，以提高安全性。
</Tip>

### 代码示例

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl https://open.bigmodel.cn/api/anthropic/v1/messages \
         --header "x-api-key: your-zhipuai-api-key" \
         --header "content-type: application/json" \
         --data \
    '{
        "model": "glm-5.1",
        "max_tokens": 1024,
        "stream": true,
        "messages": [
            {"role": "user", "content": "Hello, ZHIPU"}
        ]
    }'
    ```
  </Tab>

  <Tab title="Python">
    **安装 SDK**

    ```bash theme={null}
    pip install anthropic
    ```

    详细安装可参考 [Anthropic SDK 官方文档](https://docs.anthropic.com/en/api/client-sdks)

    **调用示例**

    ```python theme={null}
    import anthropic

    client = anthropic.Anthropic(
        api_key="your-zhipuai-api-key",
        base_url="https://open.bigmodel.cn/api/anthropic"
    )

    message = client.messages.create(
        model="glm-5.1",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, ZHIPU"}
        ]
    )
    print(message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    **安装 SDK**

    ```bash theme={null}
    npm install @anthropic-ai/sdk
    ```

    详细安装可参考 [Anthropic SDK 官方文档](https://docs.anthropic.com/en/api/client-sdks)

    **调用示例**

    ```typescript theme={null}
    import Anthropic from '@anthropic-ai/sdk';

    const anthropic = new Anthropic({
      apiKey: 'your-zhipuai-api-key',
      baseURL: 'https://open.bigmodel.cn/api/anthropic',
    });

    const msg = await anthropic.messages.create({
      model: 'glm-4.7',
      max_tokens: 1024,
      messages: [{ role: 'user', content: 'Hello, ZHIPU' }],
    });
    console.log(msg);
    ```
  </Tab>

  <Tab title="Java">
    **安装 SDK**

    Maven:

    ```xml theme={null}
    <dependency>
        <groupId>com.anthropic</groupId>
        <artifactId>anthropic-java</artifactId>
        <version>2.6.0</version>
    </dependency>
    ```

    Gradle:

    ```gradle theme={null}
    implementation 'com.anthropic:anthropic-java:2.6.0'
    ```

    详细安装可参考 [Anthropic SDK 官方文档](https://docs.anthropic.com/en/api/client-sdks)

    **调用示例**

    ```java theme={null}
      import com.anthropic.client.*;
      import com.anthropic.models.*;

      public class Chat {
          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.builder()
                  .apiKey("your_zhipuai_api_key")
                  .baseUrl("https://open.bigmodel.cn/api/anthropic")
                  .build();
              MessageCreateParams params = MessageCreateParams.builder()
                  .model("glm-5.1")
                  .maxTokens(1024)
                  .addUserMessage("Hello, ZHIPU")
                  .build();
              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
    ```
  </Tab>
</Tabs>

## 更多资源

<CardGroup cols={2}>
  <Card title="畅玩 Claude Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/guide/develop/claude">
    Claude Code 接入智谱随心畅玩
  </Card>

  <Card title="智谱 API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/api/introduction">
    查看智谱完整的 API 文档
  </Card>

  <Card title="Claude 官方文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/link.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=20fe7d23601cbb2a6bf65dc78ab4ebc3)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://docs.anthropic.com/en/api/messages">
    参考 Claude 官方文档了解更多
  </Card>
</CardGroup>

<Note>
  智谱致力于保持与 Claude API 的兼容性，如果您在迁移过程中遇到任何问题，请联系我们的[技术支持团队](https://bigmodel.cn/online-book/customerService)。
</Note>
