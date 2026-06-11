<!-- source: https://platform.kimi.com/docs/guide/use-playground-to-debug-the-model -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Playground 调试模型

[Playground 开发工作台](https://platform.kimi.com/playground)是一个强大的模型调试和测试平台，提供了直观的界面来与 AI 模型进行交互和测试。通过这个工作台，您可以：

1. 调整观察模型在不同参数下的表现和输出效果
2. 通过使用 Kimi 开放平台内置的工具，体验模型的 tool calling 能力
3. 对比不同模型在相同参数下的效果
4. 监控 tokens 使用情况来优化成本

## 模型调试功能

**提示信息设置**

* 在最上方可以设置系统提示词（System Prompt），定义模型的行为规范指导模型输出
* 支持定义 system/user/assistant 三种角色的提示词

**模型配置**

* **模型选择**: 可选择不同的模型（如 Moonshot V1 系列/Kimi K2 系列/Kimi K2.6 等）
* **参数配置**：支持的参数和字段说明详见[请求参数说明](/api/chat)

**模型对话**

* 下方输入框可以进行聊天内容发送
* **Tool 调用显示**: 显示工具调用过程，包括调用 ID/工具参数/返回结果
* **查看代码**:可以查看当前会话的 API 调用代码并提供复制功能
* 底部统计信息：显示本次对话的输入/输出/总计的 tokens 消耗数量，包括上下文历史消息和 prompt 提示词信息

<img src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/prompt.png?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=11bbe1c6dcaa4b6e74b3b02d7cb42fae" alt="prompt" width="1916" height="1832" data-path="assets/pics/playground/prompt.png" />

## 工具调试

### 官方工具

* Kimi 开放平台提供了官方免费执行的工具，您可以在 playground 选择工具，模型会自动判断是否需要调用工具来完成您的指令，如果需要进行工具调用，模型会按照工具的要求生成参数调用工具，整合成最终的答案返回给您。
* **额度与限速**：Kimi 开放平台提供的工具是一个预构建的函数，可以在需要时快速在线执行无需您本地准备工具的执行环境，目前 Kimi 开放平台的工具执行限时免费，当工具负载达到容量上限时，可能会采取临时的限流措施。
* 目前支持的工具：日期时间工具/Excel 文件分析工具/联网搜索工具/随机数生成工具等
* 目前已支持通过 Kimi API 来调用工具，详见文档[如何在 Kimi API 中使用 Formula 工具](/guide/use-official-tools)
* 暂时不支持自定义工具上传执行。

### 使用 MCP 服务器

* 在 Kimi Playground 中，您可以配置 ModelScope MCP 服务器，使用 ModelScope 提供的工具。
  * 配置步骤请见[在 Playground 中配置 ModelScope MCP 服务器](/guide/configure-the-modelscope-mcp-server)
* 您也可以配置其他 MCP 服务器，通过添加 MCP 服务器功能，输入或选择 MCP 服务器的 URL /传输协议/认证方式，点击添加即可。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/playground/add-mcp-server-cn.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=8d6170ceecf46c2125e28ba768615bbd" alt="mcp" width="1896" height="1834" data-path="assets/pics/playground/add-mcp-server-cn.png" />

### Show Case1：今日新闻报告

* 场景说明：运用工具能力，请求模型搜索今日的新闻信息，并整理成 html 网页报告
* 工具选择：date 日期时间工具，web\_search 工具，rethink 想法整理工具
* 说明：web\_search 工具会调用 kimi 开放平台的联网搜索服务，单次联网搜索会进行计费，具体计费标准请见[计费](/pricing/tools#联网搜索计费逻辑)
* 点击页面 showcase 按钮，即可快速体验工具效果

<img src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/showcase-cn.png?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=c14e73f2d6d2bc10556b606cf277065b" alt="date" width="1898" height="1840" data-path="assets/pics/playground/showcase-cn.png" />

<img src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/news-cn.png?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=e5429cb18ce14e90084f0086bfd55dcf" alt="date" width="1904" height="1838" data-path="assets/pics/playground/news-cn.png" />

### Show Case2：表格分析工具

* 工具选择：excel 分析工具

<img src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/excel-cn.png?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=e41aad8f76d1874537b4d9cc57d6fd06" alt="excel" width="1894" height="1850" data-path="assets/pics/playground/excel-cn.png" />

## 模型对比

* 可以通过添加对话功能，创建新的对话，最多支持3个模型同时调用

<img src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/model-compare.png?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=d00a5eaa87bbf4af2cc36b79c8a0626b" alt="模型对比" width="1874" height="1808" data-path="assets/pics/playground/model-compare.png" />

## 分享对话

* **导出**: 导出当前对话内容，会将当前对话的全部配置和上下文导出 .json 格式文件。
* **导入**: 导入分享的或者历史导出的 .json 对话内容，playground 会将会话渲染到页面中。
* 注意：rerun 后的数据会重新生成覆盖之前的聊天内容。若导入的 case 包括上传过的文件，导入后的会话不能 rerun

<Frame>
  <video controls style={{ width: '100%', height: 'auto' }}>
    <source src="https://mintcdn.com/moonshotcn/7u71GHTjBBTV0Hno/assets/pics/playground/upload.mp4?fit=max&auto=format&n=7u71GHTjBBTV0Hno&q=85&s=87a15599e4aacd72f7bb9d453567b54f" type="video/mp4" data-path="assets/pics/playground/upload.mp4" />

    您的浏览器不支持视频播放。
  </video>
</Frame>
