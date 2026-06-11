<!-- source: https://platform.kimi.com/docs/guide/configure-the-modelscope-mcp-server -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Playground 中配置 ModelScope MCP 服务器

Kimi 开放平台 与 ModelScope 魔搭达成官方合作，简化了 Kimi 开放平台 Playground 添加 MCP 服务器的操作步骤，同时可以在 ModelScope 社区发现海量 MCP 服务器。下面我们来看下如何在 Kimi Playground 中使用 ModelScope MCP 服务。

## 在 Kimi Playground 中配置 ModelScope MCP 同步

首先，登录 Kimi Playground：[https://platform.kimi.com/playground](https://platform.kimi.com/playground) 确保可以使用 Kimi K2 模型进行基本对话。

在 Kimi Playground 中启用 MCP 服务，需要在「MCP 服务器设置」中添加 MCP 服务配置。进入后，您会看到 Kimi Playground 默认选中 ModelScope 作为 MCP 服务提供商。Kimi Playground 与 ModelScope（魔搭）达成合作，您只需输入您的魔搭 API 令牌，即可一键同步您魔搭账号下所有已配置托管的 MCP 服务配置。如果您之前未使用过 ModelScope MCP 广场，建议参考 [ModelScope 官方文档](https://modelscope.cn/mcp/kimi-playground)，选择并托管您的 MCP 服务。

### 第一步：点击配置按钮

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/config.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=fc006cb865dabb5c768b3994d94937f8" alt="mcp-server-setting" width="1280" height="1210" data-path="assets/pics/modelscope/config.png" />

### 第二步：同步外部平台

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/syc.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=0df616e043a5211396fbed093511e032" alt="syc" width="1280" height="1038" data-path="assets/pics/modelscope/syc.png" />

其中 API 令牌可以通过访问[魔搭首页-访问令牌](https://modelscope.cn/my/myaccesstoken)页面获取

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/get-keys.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=49ec6e6279e9ca620973394bd4aa586b" alt="keys" width="1280" height="1117" data-path="assets/pics/modelscope/get-keys.png" />

在获取 ModelScope API 令牌后，粘贴到步骤 3 的空格中，并点击「开始同步」按钮。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/start-syc.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=8860fe307c651ba0dc3b403acc88038d" alt="start-syc" width="1280" height="1093" data-path="assets/pics/modelscope/start-syc.png" />

您将看到所有已配置连接的魔搭 Hosted MCP 服务已成功同步至 Kimi Playground 的可用 MCP 服务列表中.

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/mcp-list.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=abb50a339f3dd82192b00c2de2c999d1" alt="mcp-list" width="1280" height="1151" data-path="assets/pics/modelscope/mcp-list.png" />

然后您可以愉快地在 Kimi Playground 中体验 AI 助手调用 MCP 服务完成任务～

### 增量更新

如果后续在 ModelScope MCP 广场新增或删除托管 MCP 服务，您可以在"设置-MCP 服务器-同步服务器"中点击同步按钮进行增量更新。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/add-mcp.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=d1a9195291d0ba2382ec62095d9ad019" alt="add-mcp" width="1280" height="1058" data-path="assets/pics/modelscope/add-mcp.png" />

## 在 Kimi Playground 中结合模型与 MCP 的使用

同步 MCP 服务后，您将在 Kimi Playground 平台页面的左侧看到之前同步操作已导入的的 "MCP 服务列表"。在该列表中，您可以多选并启用您希望在本次对话中使用的 MCP 服务。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/manage-mcp.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=c03d77ddcf9117e64a95a082663190ee" alt="manage-mcp" width="1280" height="1206" data-path="assets/pics/modelscope/manage-mcp.png" />

例如，以高德地图为例，您可以在此列表中选择启用相关的 MCP 服务。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/maps.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=639a21d90b7d21f5736bd5ce64a236da" alt="maps" width="1280" height="1234" data-path="assets/pics/modelscope/maps.png" />

轻松 get 您的专属行程助理！
