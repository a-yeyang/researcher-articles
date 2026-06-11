<!-- source: https://docs.bigmodel.cn/cn/coding-plan/tool/others -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 接入工具

<Tip>
  [**GLM Coding Plan 团队版**](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek) 已上线，让组织安全、可控地提升开发效率。

  统一管理团队成员、预算与权限，释放 AI 编程生产力。 [立即了解 → ](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek)
</Tip>

## 一、适用工具

GLM Coding Plan 仅限在以下官方支持的指定工具与产品环境中使用，用户不得将订阅权益用于以下范围之外的工具或场景。

### 1. Coding Agent 工具

点击并进入下方您想使用的工具文档，参考对应的接入文档接入即可。

<CardGroup cols={3}>
  <Card title="Claude Code" href="/cn/coding-plan/tool/claude" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    Anthropic 推出的 AI 编程助手，可理解代码库、跨文件修改代码，并支持运行命令与测试。
  </Card>

  <Card title="Claude for IDE" href="/cn/coding-plan/tool/claude-for-ide" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    Claude Code 的 IDE 插件，支持 VSCode 和 Jetbrains。
  </Card>

  <Card title="OpenCode" href="/cn/coding-plan/tool/opencode" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/globe.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=12c9d7a94bd8f6a6c5f3ef31568fdb36)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/globe.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=12c9d7a94bd8f6a6c5f3ef31568fdb36)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    面向开发者的开源 Coding Agent，在终端中提供代码生成、编辑与任务执行能力。
  </Card>

  <Card title="ZCode" href="/cn/coding-plan/tool/zcode" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/flask-solid.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=c6fc1fdd9c4b5cca3d0e26d7f15d5ccd)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/flask-solid.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=c6fc1fdd9c4b5cca3d0e26d7f15d5ccd)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    将最强大的 AI Agents 与现有工具链结合，让你在熟悉的流程中完成规划、编码、评审与上线。
  </Card>

  <Card title="TRAE" href="/cn/coding-plan/tool/trae" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/headset.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f42f526ce8d7b3098ec5c72bfe9a401a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/headset.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f42f526ce8d7b3098ec5c72bfe9a401a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    能独立完成各类开发任务的 AI 编辑器。
  </Card>

  <Card title="CodeBuddy" href="/cn/coding-plan/tool/codebuddy" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    基于 AI 的全流程智能编程工具。
  </Card>

  <Card title="Lingma" href="/cn/coding-plan/tool/lingma" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    你的智能编程助手。
  </Card>

  <Card title="Qoder" href="/cn/coding-plan/tool/qoder" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/cubes.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=68f7e70811d7c842eb5b9d34c8ce53ec)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/cubes.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=68f7e70811d7c842eb5b9d34c8ce53ec)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    面向真实软件的智能体编程平台。
  </Card>

  <Card title="Kilo" href="/cn/coding-plan/tool/kilo" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    高效的 VS Code 插件，用于代码生成和项目管理。
  </Card>

  <Card title="MonkeyCode" href="/cn/guide/develop/monkeycode" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/star.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b3c8448dccf8f96abadf9a72e51b3cca)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    在线 AI 开发平台，无需安装，内置云端开发环境。
  </Card>

  <Card title="Cline" href="/cn/coding-plan/tool/cline" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    VS Code 的 AI 编程插件，支持代码生成和文件操作。
  </Card>

  <Card title="Droid" href="/cn/coding-plan/tool/droid" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/helmet-safety.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6e68280ea52d21888fe2337a33e4bf95)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/helmet-safety.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6e68280ea52d21888fe2337a33e4bf95)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    企业级 AI 编码代理，运行在终端中处理端到端工作流。
  </Card>

  <Card title="Roo" href="/cn/coding-plan/tool/roo" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    智能的 VS Code 插件，用于项目的代码编写重构。
  </Card>

  <Card title="Crush" href="/cn/coding-plan/tool/crush" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    终端 AI 编程工具，支持 CLI 和 TUI 界面。
  </Card>

  <Card title="Goose" href="/cn/coding-plan/tool/goose" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    AI Agent 工具，支持本地运行和自动化工程任务。
  </Card>

  <Card title="Cursor" href="/cn/coding-plan/tool/cursor" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    AI 优先的代码编辑器，支持自定义模型配置。
  </Card>
</CardGroup>

### 2. 通用 Agent 工具

<Tip>
  GLM Coding Plan 大部分用户是在 Coding Agent 场景使用，我们优先保障编程任务请求。

  对于以下所支持的通用 Agent 工具，采用次级调度与尽力交付策略，Coding Agent 任务享有资源抢占优先权，高负载下以下通用 Agent 工具任务将自动触发包括动态排队、限流等公平使用策略。
</Tip>

<CardGroup cols={2}>
  <Card title="OpenClaw" href="/cn/coding-plan/tool/openclaw" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/J5fxbkS7zqFAL-67/resource/icon/lobster.svg?fit=max&auto=format&n=J5fxbkS7zqFAL-67&q=85&s=2401de6a8887835ce52b1a91f0596c6e)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/J5fxbkS7zqFAL-67/resource/icon/lobster.svg?fit=max&auto=format&n=J5fxbkS7zqFAL-67&q=85&s=2401de6a8887835ce52b1a91f0596c6e)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    可在本地设备运行的开源 AI 助手，支持多平台使用，并可通过 Skills 扩展能力。
  </Card>

  <Card title="Cherry Studio" href="/cn/coding-plan/tool/cherry-studio" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/window.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=ce809df2afccb242815db53bdf9452a1)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/window.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=ce809df2afccb242815db53bdf9452a1)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    AI 应用程序集成开发环境，支持多种模型接入。
  </Card>

  <Card title="Hermes Agent" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/shield.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a40f70c5bd3e70524784b04dcd0fe669)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/shield.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a40f70c5bd3e70524784b04dcd0fe669)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    开源自进化 AI 智能体，持久记忆越用越聪明。
  </Card>
</CardGroup>

## 二、编程端点

GLM Coding Plan 提供两种协议的端点，用于不同的编码工具：

`OpenAI Chat Completions` 协议端点地址：`https://open.bigmodel.cn/api/coding/paas/v4`

`Anthropic Messages` 协议端点地址：`https://open.bigmodel.cn/api/anthropic`

<Warning>
  请根据您使用的工具选择正确的端点地址。错误配置端点将导致无法使用 GLM Coding Plan 套餐额度。
</Warning>

## 三、配置示例

> 核心步骤：
>
> 1. 找到适配 OpenAI 协议的 Provider
> 2. 添加/替换 OpenAI Base URL 为 `https://open.bigmodel.cn/api/coding/paas/v4`
> 3. 输入 API Key 并选择 GLM 模型

下面以 **Cursor** 为例，注意 Cursor 高级版及以上才支持自定义配置，以下步骤展示了如何通过 OpenAI 协议接入 GLM 系列模型。类似地，其他支持 OpenAI 协议的工具也可以采用相同的配置方式。

### 1. 安装 Cursor

访问 Cursor 官网 下载并安装适合您的操作系统的版本。

### 2. 创建新 Provider/Model

在 Cursor 中，打开 “**Models**” 部分，并点击 “**Add Custom Model**” 按钮。

![Description](https://cdn.bigmodel.cn/markdown/176032162759420251013-100713.jpeg?attname=20251013-100713.jpeg)

* 选择 **OpenAI 协议**。
* 配置 **OpenAI API Key**。
  * 个人版套餐的用户，通过 [个人编程套餐 > 套餐概览](https://bigmodel.cn/coding-plan/personal/overview)，新建  API Key
  * 团队版套餐的成员，通过 [团队编程套餐 > 我的套餐](http://bigmodel.cn/coding-plan?z_plan=team)，获取  API Key（团队套餐 Key 与平台其他 API Key 不通用，使用团队额度请务必使用团队套餐 Key）
* 在 **Override OpenAI Base URL** 中，将默认 URL 替换为：`https://open.bigmodel.cn/api/coding/paas/v4`。
* 输入您希望使用的模型，如 `GLM-5.1`, `GLM-4.7` 或 `GLM-4.5-air`。
* 注意: 在 Cursor 中，需要输入模型的大写名称不能小写名称，如 `GLM-4.7`。

![Description](https://cdn.bigmodel.cn/markdown/176032171278120251013-100720.jpeg?attname=20251013-100720.jpeg)

### 3. 保存并切换模型

配置完成后，保存设置并在主页上选择您刚创建的 Provider。

### 4. 开始使用

通过该设置，您可以开始使用 GLM 系列模型进行代码生成、调试、任务分析等工作。

![Description](https://cdn.bigmodel.cn/markdown/176032176545720251013-100725.jpeg?attname=20251013-100725.jpeg)
