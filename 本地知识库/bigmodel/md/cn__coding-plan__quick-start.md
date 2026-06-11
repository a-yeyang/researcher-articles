<!-- source: https://docs.bigmodel.cn/cn/coding-plan/quick-start -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

<Tip>
  本指南将帮助您快速上手 [GLM Coding Plan](https://zhipuaishengchan.datasink.sensorsdata.cn/t/Gd)，仅限在官方支持的[指定工具与产品环境](https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7)中使用 GLM 模型，只需几分钟即可完成。
</Tip>

<Warning>
  使用 GLM Coding Plan 时，需要配置专属的 Coding API 端点 [https://open.bigmodel.cn/api/coding/paas/v4](https://open.bigmodel.cn/api/coding/paas/v4) 而不是通用 API 端点
</Warning>

## 开始使用

<Steps>
  <Step title="注册账号">
    访问[智谱开放平台](https://open.bigmodel.cn)，点击右上角的「注册/登录」按钮，按照提示完成账号注册流程。

    <Frame>
      ![注册账号](https://cdn.bigmodel.cn/static/logo/register.png)
    </Frame>
  </Step>

  <Step title="订阅 GLM Coding Plan">
    登录后，前往 [套餐详情页](https://zhipuaishengchan.datasink.sensorsdata.cn/t/Gd) 选择适合您的订阅套餐：

    <Frame>
      ![Description](https://cdn.bigmodel.cn/markdown/1758212999196image.png?attname=image.png)
    </Frame>
  </Step>

  <Step title="获取 API Key">
    订阅套餐后:

    * 个人版套餐的用户，通过 [个人编程套餐 > 套餐概览](https://bigmodel.cn/coding-plan/personal/overview)，新建  API Key
    * 团队版套餐的成员，通过 [团队编程套餐 > 我的套餐](http://bigmodel.cn/coding-plan?z_plan=team)，获取  API Key（团队套餐 Key 与平台其他 API Key 不通用，使用团队额度请务必使用团队套餐 Key）

    <Warning>
      请妥善保管您的 API Key，不要泄露给他人，也不要直接硬编码在代码中。建议使用环境变量或配置文件来存储 API Key。
    </Warning>
  </Step>

  <Step title="选择编码工具">
    GLM Coding Plan 仅限在官方支持的[指定工具与产品环境](https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7)中使用，您可以根据自己的偏好选择：

    <CardGroup cols={3}>
      <Card title="Claude Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/claude">
        智能终端编码助手，支持自然语言编程
      </Card>

      <Card title="Cline" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/cline">
        VS Code 扩展，提供智能代码补全和调试
      </Card>

      <Card title="OpenCode" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/window.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=ce809df2afccb242815db53bdf9452a1)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/opencode">
        开源编码工具，支持多种编程语言
      </Card>

      <Card title="Roo Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/hammer.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f79760a2b8464f3d2cea1c006663f5f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/roo">
        轻量级编码助手，快速上手
      </Card>

      <Card title="Kilo Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/feather.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=fe0922491e9f5f9c18209a21791882bc)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/kilo">
        高效编码工具，专注性能优化
      </Card>

      <Card title="Cursor" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/cursor">
        AI 原生 IDE，智能代码编辑器
      </Card>

      <Card title="Crush" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/crush">
        高效 AI 编码助手
      </Card>

      <Card title="Goose" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/plug.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=ee8b6362dc2efcf3b5e159abe7f85bc0)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/goose">
        智能编码工具，灵活易用
      </Card>

      <Card title="其他工具" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
        其它 Coding 工具支持持续扩展中
      </Card>
    </CardGroup>
  </Step>

  <Step title="配置编码工具">
    以 Claude Code 为例，配置 GLM 模型：

    <Tabs>
      <Tab title="Claude Code">
        **1. 安装 Claude Code**

        前提条件：您需要安装 [Node.js 18 或更新版本](https://nodejs.org/en/download/)

        ```bash theme={null}
        # 进入命令行界面，安装 Claude Code
        npm install -g @anthropic-ai/claude-code

        # 创建您的工作目录，例如 `your-project`，使用 `cd` 命令导航到您的项目
        cd your-project

        # 安装完成，运行命令 `claude` 即可进入 Claude Code 交互界面
        claude
        ```

        **2. 配置环境变量**

        安装 Claude Code 后，通过在 Mac OS 终端或 Windows cmd 中输入以下命令，使用以下任意方法之一设置环境变量：

        <Tip>
          **注意**：设置环境变量时，终端不会返回任何输出。这是正常的，只要没有报错即代表成功。
        </Tip>

        **方式一：自动化助手**

        Coding Tool Helper 是一个编码工具助手，快速将您的 **GLM 编码套餐**加载到您喜爱的**编码工具**中。安装并运行它，按照界面提示操作即可自动完成工具安装，套餐配置，MCP服务器管理等。

        ```bash theme={null}
        # 进入命令行界面，执行如下运行 Coding Tool Helper
        npx @z_ai/coding-helper
        ```

        详细说明请参考 [Coding Tool Helper 文档](/cn/coding-plan/extension/coding-tool-helper)。

        **方式二：自动化脚本（支持 MacOS Linux）**

        在你的终端或 IDE 中运行以下命令，下载一个帮你自动配置环境变量的 shell 脚本，运行即可

        ```bash theme={null}
        curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
        ```

        **方式三：手动配置（支持 Windows MacOS Linux）**

        根据您的环境选择下面一种方式即可，配置后需新建命令行窗口生效

        <CodeGroup>
          ```bash MacOS & Linux theme={null}
          # 编辑或新增 Claude Code 配置文件 `~/.claude/settings.json`
          # 新增或修改里面的 env 字段
          # 注意替换里面的 `your_zhipu_api_key` 为您上一步获取到的 API Key
          {
              "env": {
                  "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
                  "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
                  "API_TIMEOUT_MS": "3000000",
                  "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
              }
          }
          ```

          ```cmd Windows Cmd theme={null}
          # 在 Cmd 中运行以下命令
          # 注意替换里面的 `your_zhipu_api_key` 为您上一步获取到的 API Key
          setx ANTHROPIC_AUTH_TOKEN your_zhipu_api_key
          setx ANTHROPIC_BASE_URL https://open.bigmodel.cn/api/anthropic
          setx CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 1
          ```

          ```powershell Windows PowerShell theme={null}
          # 在 PowerShell 中运行以下命令
          # 注意替换里面的 `your_zhipu_api_key` 为您上一步获取到的 API Key
          [System.Environment]::SetEnvironmentVariable('ANTHROPIC_AUTH_TOKEN', 'your_zhipu_api_key', 'User')
          [System.Environment]::SetEnvironmentVariable('ANTHROPIC_BASE_URL', 'https://open.bigmodel.cn/api/anthropic', 'User')
          [System.Environment]::SetEnvironmentVariable('CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC', '1', 'User')
          ```
        </CodeGroup>
      </Tab>

      <Tab title="其他工具">
        **通用配置方式**

        对于其他支持的编码工具，按以下方式配置：

        * **API Provider（供应商）**：选择 OpenAI Compatible
        * **Base URL**：输入 `https://open.bigmodel.cn/api/coding/paas/v4`
        * **API Key**：输入您的智谱 API Key
        * **Model**：选择 `GLM-4.7`

        具体配置步骤请参考各工具的详细文档。
      </Tab>
    </Tabs>
  </Step>

  <Step title="开始编码">
    配置完成后，您就可以开始使用 GLM 模型进行编码了！

    <Tabs>
      <Tab title="自然语言编程">
        ```
        # 在 Claude Code 中输入自然语言指令
        请帮我创建一个 React 组件，包含用户登录表单
        ```

        GLM 会自动：

        * 分析需求并制定实现计划
        * 生成完整的 React 组件代码
        * 包含表单验证和样式
        * 确保代码可以直接运行
      </Tab>

      <Tab title="代码调试">
        ```
        # 描述遇到的问题
        我的 API 请求返回 404 错误，请帮我检查代码
        ```

        GLM 会自动：

        * 分析您的代码库
        * 定位可能的问题原因
        * 提供具体的修复方案
        * 解释问题产生的原因
      </Tab>

      <Tab title="代码优化">
        ```
        # 请求代码优化
        这个函数性能不好，请帮我优化一下
        ```

        GLM 会自动：

        * 分析代码的性能瓶颈
        * 提供优化建议和重构方案
        * 保持代码功能不变
        * 提升执行效率
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 功能示例

<Card title="代码库问答" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  随时提出关于团队代码库的问题，保持全局理解。

  ```
  问：这个项目的用户认证是如何实现的？
  答：GLM-4.7 会分析您的代码库，详细解释认证流程和相关文件
  ```
</Card>

<Card title="自动化任务处理" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrows-rotate.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2b334fa767b3736a3afc9babb9c6d575)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  一键修复 lint 问题、解决合并冲突、生成发行说明。

  ```
  # 自动修复代码规范问题
  请修复所有的 ESLint 错误

  # 自动生成文档
  请为这个 API 生成详细的文档
  ```
</Card>

## 高级功能

<AccordionGroup>
  <Accordion title="视觉理解 MCP Server">
    套餐用户可以使用视觉理解 MCP Server，可以通过旗舰视觉推理模型 GLM-4.6V 来理解和分析图像内容。

    * 分析 UI 设计图并生成对应代码
    * 理解流程图和架构图
    * 从截图中提取文本和信息

    详细使用方法请参考 [视觉理解 MCP Server](/cn/coding-plan/mcp/vision-mcp-server) 文档。
  </Accordion>

  <Accordion title="网络搜索 MCP Server">
    套餐用户可以使用网络搜索 MCP Server，获取最新的技术信息。

    * 搜索最新的技术文档和 API 变更
    * 获取开源项目的最新信息
    * 查找解决方案和最佳实践

    详细使用方法请参考 [网络搜索 MCP Server](/cn/coding-plan/mcp/search-mcp-server) 文档。
  </Accordion>

  <Accordion title="网页读取 MCP Server">
    套餐用户可以使用网页读取 MCP Server，获取并解析网页内容。

    * 抓取任意网页的完整文本与链接
    * 提取标题、正文、元数据等结构化信息
    * 解析页面内链接列表，辅助知识提取

    详细使用方法请参考 [网页读取 MCP Server](/cn/coding-plan/mcp/reader-mcp-server) 文档。
  </Accordion>

  <Accordion title="开源仓库 MCP Server">
    套餐用户可以使用开源仓库 MCP Server，获取并解析网页内容。

    * Github 代码仓库检索文档、代码与注释
    * 获取 GitHub 仓库的目录结构和文件列表，快速掌握项目布局
    * 读取 GitHub 仓库中指定文件的完整代码内容，深入分析实现细节

    详细使用方法请参考 [开源仓库 MCP Server](cn/coding-plan/mcp/zread-mcp-server) 文档。
  </Accordion>
</AccordionGroup>

## 最佳实践

<Tip>
  查看我们的 [最佳实践](/cn/coding-plan/learning-resources/best-practice)，了解如何使用 GLM Coding Plan 高效完成复杂项目开发。
</Tip>

<Card title="项目开发流程" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
  1. **需求分析**：使用自然语言描述项目需求
  2. **架构设计**：让 GLM-5.1 帮助设计项目架构
  3. **代码实现**：逐步实现各个模块功能
  4. **测试调试**：自动生成测试用例并调试问题
  5. **优化部署**：优化性能并准备部署
</Card>

<Tip>
  如果您在使用过程中遇到任何问题，可以查阅开发者文档或联系我们的 [技术支持](https://bigmodel.cn/online-book/customerService)。
</Tip>
