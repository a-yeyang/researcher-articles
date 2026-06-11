<!-- source: https://docs.bigmodel.cn/cn/coding-plan/overview -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 套餐概览

GLM Coding Plan 是专为 AI 编码打造的订阅套餐，仅需少量投入，即可为您带来智能、高速、稳定的编码体验。

<Tip>
  [**GLM Coding Plan 团队版**](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek) 已上线，让组织安全、可控地提升开发效率。

  统一管理团队成员、预算与权限，释放 AI 编程生产力。 [立即了解 → ](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek)
</Tip>

<Note>
  套餐仅限在官方支持的<a href="https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7">指定工具与产品环境</a>中使用。

  若系统检测到账号存在将 GLM Coding Plan 用于非支持工具的行为，平台有权基于保障系统公平性与服务稳定性的原则，对相关订阅权益采取必要的限制措施。
</Note>

## 应用场景

<AccordionGroup>
  <Accordion title="自然语言编程">
    通过对话描述需求，自动制定计划、生成代码、调试问题，并确保正常运行。
  </Accordion>

  <Accordion title="代码调试与修复">
    输入错误描述或报错信息，自动分析代码库、定位问题并提供修复方案。
  </Accordion>

  <Accordion title="代码库问答">
    随时提出关于团队代码库的问题，保持全局理解，并结合外部数据源给出精准解答。
  </Accordion>

  <Accordion title="自动化任务处理">
    一键修复 lint 问题、解决合并冲突、生成发行说明，让开发者专注核心逻辑。
  </Accordion>
</AccordionGroup>

## 独家优势

* **畅用智谱高智能模型**：GLM 模型上线时在推理、代码、智能体能力全面达到开源模型 SOTA，工具调用、复杂任务执行表现出色。
* **兼容多款编码工具**：支持 Claude Code、Kilo Code、OpenClaw、OpenCode、TRAE、CodeBuddy 等主流编码工具，灵活适配多种开发场景。
* **高额用量，普惠价格**：远超常规方案的调用额度，升级至 Pro、Max，即可轻松满足高频复杂项目需求。
* **扩展覆盖更多能力**：套餐包含专属图像视频理解、联网搜索、网页读取、开源仓库 MCP，最新上线 GLM in Excel (Beta) 权益，助力完成更广泛开发任务。

## 套餐权益

<p />

### 可用模型

* 所有套餐均支持 **GLM-5.1**、GLM-5-Turbo、GLM-4.7、GLM-4.5-Air。

### 用量说明

<Warning>
  团队版用量说明，请前往 [团队版权益](https://docs.bigmodel.cn/cn/coding-plan/team) 查看。
</Warning>

为了管理资源并确保所有用户的公平访问，我们进行每 5 小时的限额和每周使用额度限制，您可以在 [用量统计](https://www.bigmodel.cn/coding-plan/personal/usage) 中查看您的额度消耗进展。一次prompt指一次提问，每次 prompt 预计可调用模型 15-20 次。

**每月可用额度按 API 定价折算，相当于月订阅费用的 15–30 倍（已计入周限额影响）。**

|   套餐类型  | 每 5 小时限额<br />（动态刷新，额度在请求消耗 5 小时后刷新重置） | 每周限额<br />（自下单时开启，以 7 天为一个周期额度刷新重置） |
| :-----: | :------------------------------------: | :---------------------------------: |
| Lite 套餐 |            最多约 80 次 prompts            |          最多约 400 次 prompts          |
|  Pro 套餐 |            最多约 400 次 prompts           |          最多约 2000 次 prompts         |
|  Max 套餐 |           最多约 1600 次 prompts           |          最多约 8000 次 prompts         |

<Tip>
  上述次数为预估值，实际可用量会因项目复杂度、代码库大小以及是否启用自动接受等因素而有所不同。

  **GLM-5.1**、**GLM-5-Turbo** 作为高阶模型，对标 Claude Opus，调用时将按照 **“高峰期 3 倍，非高峰期 2 倍”** 系数消耗额度； 我们推荐您在复杂任务上切换至 GLM-5.1 处理，普通任务上继续使用 GLM-4.7，以避免套餐用量额度消耗过快。**（作为限时福利，GLM-5.1、GLM-5-Turbo 将在非高峰期仅作为 1 倍抵扣，持续到 6 月底）**

  注：高峰期为每日的 14:00～18:00 （UTC+8）
</Tip>

### 专属 MCP

<CardGroup cols={2}>
  <Card title="视觉理解 MCP" color="#ffffff" href="https://docs.bigmodel.cn/cn/coding-plan/mcp/vision-mcp-server" />

  <Card title="联网搜索 MCP" color="#ffffff" href="https://docs.bigmodel.cn/cn/coding-plan/mcp/search-mcp-server" />

  <Card title="网页读取 MCP" color="#ffffff" href="https://docs.bigmodel.cn/cn/coding-plan/mcp/reader-mcp-server" />

  <Card title="开源仓库 MCP" color="#ffffff" href="https://docs.bigmodel.cn/cn/coding-plan/mcp/zread-mcp-server" />
</CardGroup>

**调用额度说明：**

* **Lite 套餐**：联网搜索 MCP / 网页读取 MCP / 开源仓库 MCP 每月合计 100 次
* **Pro 套餐**：联网搜索 MCP / 网页读取 MCP / 开源仓库 MCP 每月合计 1000 次
* **Max 套餐**：联网搜索 MCP / 网页读取 MCP / 开源仓库 MCP 每月合计 4000 次

达到当月调用上限后，该类 MCP 当月将无法继续调用。

<Info>
  **视觉理解 MCP：** 所有套餐均与模型共享 5 小时最大 prompt 资源池，达到上限后将在 5 小时周期后自动恢复。
</Info>

### 适用工具

* 套餐仅限在官方支持的[指定工具与产品环境](https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7)中使用。在除规定工具外调用 API，不可享用 Coding 套餐的额度。
* 套餐支持 OpenClaw 使用，但采用次级调度与尽力交付策略，Coding Agent 任务享有资源抢占优先权，高负载下 OpenClaw 任务将自动触发包括动态排队、限流等公平使用策略。
* 订阅套餐后，在上述编程工具中调用 GLM 模型，按接入指南配置即可使用套餐额度。当套餐额度耗尽后，需要等待下一个 5 小时周期恢复额度，系统不会继续消耗您的其他资源包/账户余额。

## 下一步

* [快速开始](/cn/coding-plan/quick-start)：帮助您快速上手，从订阅套餐到在编码工具中使用，只需几分钟
* [使用须知](/cn/coding-plan/usage-notes)：快速了解账号使用规范、并发限制、退款政策等注意事项
* [常见问题](/cn/coding-plan/faq)：覆盖套餐相关的订阅、活动及使用过程中的常见问题

<CardGroup cols={2}>
  <Card title="GLM Coding 开发者社区" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book-open.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b5cd60a0c16c81255cbee52c2caf401)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="https://zhipu-ai.feishu.cn/wiki/TrlMwahsfihLrKkZsy0cpuTenCz?from=from_copylink">
    官方知识库

    * 入门指南
    * 实战教程
    * 应用案例
  </Card>

  <Card title="GLM Coding 用户交流群" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/globe.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=12c9d7a94bd8f6a6c5f3ef31568fdb36)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    飞书扫码入群

    <img src="https://cdn.bigmodel.cn/markdown/177909989899720260518-181434.png?attname=20260518-181434.png" alt="Main dashboard interface" style={{height: "100px", width: "100px"}} className="rounded-lg" />
  </Card>
</CardGroup>
