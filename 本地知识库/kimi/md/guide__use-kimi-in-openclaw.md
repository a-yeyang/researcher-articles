<!-- source: https://platform.kimi.com/docs/guide/use-kimi-in-openclaw -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 OpenClaw 连接 Kimi 模型

> 使用 OpenClaw 和 Kimi K2.5 API 构建跨平台 AI 智能体。按照我们的指南安装 OpenClaw 并配置您的 Kimi API 密钥，实现在 Telegram、Discord、Slack 和 WhatsApp 上的无缝聊天。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/clawbot.jpeg?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=497a0d4a604b1cf34c88a20256ee1461" alt="openclaw" width="1018" height="407" data-path="assets/pics/openclaw/clawbot.jpeg" />

OpenClaw（前身为 Clawdbot 和 Moltbot）是一个开源的自托管 AI 智能体平台，可让您在本地运行 AI 助手。它集成了 WhatsApp、Telegram、Discord、Slack 和 Signal 等消息应用，将大语言模型连接到实际工作流程中。该平台支持多个 LLM 提供商、可扩展的技能，并让您完全掌控自己的数据和 API 密钥。

以下是如何在 OpenClaw 中使用 Kimi K2.5 模型的方法。Kimi 最新模型是 Kimi K2.6，最新模型的集成示例正在更新中。

## 第一步：创建 Kimi 开放平台 API Key

* 新注册的账户没有余额，请先完成组织认证，认证后的账号可以获得 15 元的免费代金券。但建议您充值50元以上升级到 tier1，以获得更流畅的使用体验。[前往充值](https://platform.kimi.com/console/pay)
* 创建并复制 API 密钥：[前往创建](https://platform.kimi.com/console/api-keys)

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/recharge_cn.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=f08034f02ad3dea2af45d4a5fb13e133" alt="recharge" width="2845" height="2174" data-path="assets/pics/openclaw/recharge_cn.png" />

## 第二步：安装 OpenClaw

在终端中运行以下命令。如果您已经安装了 OpenClaw，也请执行此命令以升级 OpenClaw。

**版本：强烈建议您升级到 2026.2.3 及以上版本。从 2.3 版本起，OpenClaw 已全面支持国内开放平台的 Kimi K2.5 模型选择。**

```curl theme={null}
curl -fsSL https://openclaw.ai/install.sh | bash
```

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/download.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=56645732e6534d6be08e66b3b4456593" alt="download" width="1594" height="484" data-path="assets/pics/openclaw/download.png" />

访问 OpenClaw 官方网站了解更多信息：[https://openclaw.ai/](https://openclaw.ai/)

如果安装成功，您会看到以下提示：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/success.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=d34a0980d651af2cd747238277027817" alt="success" width="1530" height="892" data-path="assets/pics/openclaw/success.png" />

选择 \[yes] 并继续安装：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/yes.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=eb1a0af7a05ef86e1dd6f7534df1671f" alt="yes" width="1346" height="268" data-path="assets/pics/openclaw/yes.png" />

选择 QuickStart 选项：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/quickstart.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=6a28d166677a1940d14fa20320435f4d" alt="quickstart" width="1296" height="306" data-path="assets/pics/openclaw/quickstart.png" />

## 第三步：设置 Kimi K2.5

* **第 1 步：Model.auth provider > 选择 Moonshot AI (Kimi K2.5)**
* **第 2 步：Model AI auth method（Kimi K2.5） > 选择 Kimi API key (.cn)**
* **第 3 步：Enter Moonshot API Key（.cn） > 输入您的 API Key**
* **第 4 步：Default model > 保持当前（moonshot/kimi-K2.5）**

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/1.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=67b1cc292b42a7b2f6e05295529544c9" alt="1" width="1564" height="612" data-path="assets/pics/openclaw/1.png" />

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/3_cn.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=a0ba1a4ac7ec2123225638c71083d5f7" alt="3" width="1646" height="318" data-path="assets/pics/openclaw/3_cn.png" />

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/models_cn.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=d0046b26525c36cee79e2bb71e2cac23" alt="models" width="1724" height="554" data-path="assets/pics/openclaw/models_cn.png" />

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/default_models.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=b6e06b47a0ff24546d8fa1738b8afcf6" alt="default_models" width="1746" height="239" data-path="assets/pics/openclaw/default_models.png" />

然后您会看到选择聊天工具的选项。您可以先选择 \[Skip for now]：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/4.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=990800b4ba46a786434af3e21a3db833" alt="4" width="1358" height="722" data-path="assets/pics/openclaw/4.png" />

其他配置，如 Gateway Port 设置，可以保持默认值 18789。对于 Skills 和包管理器，选择 npm 或其他选项，其余所有选项都可以选择 Yes。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/5.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=a8733c88e8e307d455504a958b2ded05" alt="5" width="1078" height="278" data-path="assets/pics/openclaw/5.png" />

对于 skills，您可以跳过此步骤，或使用空格键选择您需要的技能。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/6.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=f98fc9d45698942002f8db7c49a218a9" alt="6" width="1296" height="252" data-path="assets/pics/openclaw/6.png" />

对于其余的 API 密钥，如果您没有则选择 no：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/7.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=7faf267a0a0606868879789d2584cc9b" alt="7" width="880" height="288" data-path="assets/pics/openclaw/7.png" />

最后三个 hooks 可以启用，以执行内容指导日志和会话记录：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/8.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=200625309d1666df5584678c67444fb8" alt="8" width="1110" height="234" data-path="assets/pics/openclaw/8.png" />

安装完成后，您可以自动访问 [http://127.0.0.1:18789](http://127.0.0.1:18789) 打开聊天界面并开始使用。

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/openclaw/chat.jpeg?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=60d85b7adc13c4bc588b48be79acc514" alt="chat" width="1280" height="707" data-path="assets/pics/openclaw/chat.jpeg" />

## 一键安装包推荐

中国地区用户安装 OpenClaw 可能遇到网络下载缓慢的问题，推荐近期社区中好用的桌面端的 OpenClaw 一键安装包，[点此下载](https://claw.ver0.cn/)
