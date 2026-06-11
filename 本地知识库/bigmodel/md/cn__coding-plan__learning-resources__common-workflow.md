<!-- source: https://docs.bigmodel.cn/cn/coding-plan/learning-resources/common-workflow -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 常用工作流

> 介绍了日常开发中的一些实用工作流，可以根据自己的项目进行调整使用。

## 理解新的代码库

<Tabs>
  <Tab title="快速获取代码库概览">
    <Steps>
      <Step title="导航到项目根目录" titleSize="h3">
        ```bash theme={null}
        cd /path/to/project
        ```
      </Step>

      <Step title="启动 Coding Agent" stepNumber={2} titleSize="h3">
        ```bash theme={null}
        claude ## 以 claude 为例
        ```
      </Step>

      <Step title="请求高级概览" stepNumber={3} titleSize="h3">
        ```bash theme={null}
        give me an overview of this codebase
        ```
      </Step>

      <Step title="深入了解特定组件" stepNumber={3} titleSize="h3">
        ```bash theme={null}
        explain the main architecture patterns used here
        what are the key data models?
        how is authentication handled?
        ```
      </Step>
    </Steps>

    <Tip>
      **提示：**

      * 从广泛的问题开始，然后缩小到特定领域
      * 询问项目中使用的编码约定和模式
      * 请求项目特定术语的词汇表
    </Tip>
  </Tab>

  <Tab title="查找相关代码">
    <Steps>
      <Step title="要求 Coding Agent 查找相关文件" titleSize="h3">
        ```bash theme={null}
        find the files that handle user authentication
        ```
      </Step>

      <Step title="获取有关组件如何交互的上下文" stepNumber={2} titleSize="h3">
        ```bash theme={null}
        how do these authentication files work together?
        ```
      </Step>

      <Step title="理解执行流程" stepNumber={3} titleSize="h3">
        ```bash theme={null}
        trace the login process from front-end to database
        ```
      </Step>
    </Steps>

    <Tip>
      **提示：**

      * 明确说明需要查找的内容
      * 使用项目中的语言
    </Tip>
  </Tab>
</Tabs>

## 修复 bug

<Steps>
  <Step title="与 Coding Agent 分享错误" titleSize="h3">
    ```bash theme={null}
    I'm seeing an error when I run npm test
    ```
  </Step>

  <Step title="请求修复建议" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    suggest a few ways to fix the @ts-ignore in user.ts
    ```
  </Step>

  <Step title="应用修复" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    update user.ts to add the null check you suggested
    ```
  </Step>
</Steps>

<Tip>
  **提示：**

  * 告诉 Claude 重现问题的命令并获取堆栈跟踪
  * 提及重现错误的任何步骤
  * 让 Claude 知道错误是间歇性的还是持续的
</Tip>

## 重构代码

<Steps>
  <Step title="识别用于重构的遗留代码" titleSize="h3">
    ```bash theme={null}
    find deprecated API usage in our codebase
    ```
  </Step>

  <Step title="获取重构建议" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    suggest how to refactor utils.js to use modern JavaScript features
    ```
  </Step>

  <Step title="安全地应用更改" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    refactor utils.js to use ES2024 features while maintaining the same behavior
    ```
  </Step>

  <Step title="验证重构" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    run tests for the refactored code
    ```
  </Step>
</Steps>

<Tip>
  **提示：**

  * 要求 Coding Agent 解释现代方法的优势
  * 请求在需要时保持向后兼容性的更改
  * 以小的、可测试的增量进行重构
</Tip>

## 使用专门的 subagents

<Steps>
  <Step title="查看可用的 subagents" titleSize="h3">
    ```bash theme={null}
    /agents
    ```

    这显示所有可用的 subagents 并让您创建新的。
  </Step>

  <Step title="自动使用 subagents" stepNumber={2} titleSize="h3">
    Coding Agent 自动将适当的任务委派给专门的 subagents：

    ```bash theme={null}
    review my recent code changes for security issues
    run all tests and fix any failures
    ```
  </Step>

  <Step title="明确请求特定的 subagents" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    use the code-reviewer subagent to check the auth module
    have the debugger subagent investigate why users can't log in
    ```
  </Step>

  <Step title="为工作流创建自定义 subagents" stepNumber={4} titleSize="h3">
    ```bash theme={null}
    /agents
    ```

    然后选择 `Create New subagent` 并按照提示定义：

    * 描述 subagent 目的的唯一标识符（例如 `code-reviewer`、`api-designer`）。
    * Coding Agent 何时应该使用此代理
    * 它可以访问哪些工具
    * 描述代理角色和行为的系统提示
  </Step>
</Steps>

<Tip>
  **提示：**

  * 在 `.coding agent/agents/` 中创建项目特定的 subagents 以供团队共享
  * 使用描述性的 `description` 字段来启用自动委派
  * 限制工具访问权限为每个 subagent 实际需要的内容
</Tip>

## 使用 Plan Mode 进行安全的代码分析

**Plan Mode** 是一种工作模式，它会限制 Coding Agent 只使用 **只读操作（read-only tools）** 来分析代码库，从而先制定执行计划，而不会直接修改代码。这种模式适用于 **探索代码结构、规划复杂修改或进行安全的代码审查** 等场景。

以 **Claude Code** 为例，在 Plan Mode 下，Claude 会通过 `AskUserQuestion` 工具主动向用户提问，以进一步澄清需求。在充分理解目标之后，才会生成一份具体的执行计划。

### 什么时候应该使用 Plan Mode

* **复杂功能开发**：当一个任务涉及多个文件或多步修改时
* **代码库分析**：在动手修改代码之前，希望先系统地理解项目结构
* **方案讨论**：希望先与 Claude 反复确认需求和实现思路，再开始执行

### 如何使用 Plan Mode —— 以 Claude Code 为例

<Tabs>
  <Tab title="在会话中切换到 Plan Mode">
    在当前会话中，可以通过 **Shift + Tab** 在不同权限模式之间循环切换。

    如果当前处于 **Normal Mode**，按一次 **Shift + Tab** 会切换到 **Auto-Accept Mode**，终端底部会显示： `⏵⏵ accept edits on`

    再按一次 **Shift + Tab**，即可进入 **Plan Mode**，终端会显示： `⏸ plan mode on`
  </Tab>

  <Tab title="以 Plan Mode 启动新会话">
    如果希望从一开始就以 **Plan Mode** 运行 Claude，可以在启动时使用 `--permission-mode plan` 参数：

    ```bash theme={null}
    claude --permission-mode plan
    ```
  </Tab>

  <Tab title="在 Plan Mode 中运行无头模式查询">
    你也可以在 **Plan Mode** 下使用 `-p` 参数直接执行一次查询（即在 [无头模式](https://code.claude.com/docs/zh-CN/headless) 中运行）：

    ```bash theme={null}
    claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
    ```
  </Tab>
</Tabs>

### 示例：规划复杂的重构

```bash theme={null}
claude --permission-mode plan
```

```bash theme={null}
I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claude Code 将分析当前实现方法并创建全面的计划。通过后续问题进行细化：

```bash theme={null}
What about backward compatibility?
How should we handle database migration?
```

按 `Ctrl+G` 在默认文本编辑器中打开计划，您可以在 Claude 继续之前直接编辑它。

### 将 Plan Mode 配置为默认值

```bash theme={null}
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

## 编写测试用例

<Steps>
  <Step title="识别未测试的代码" titleSize="h3">
    ```bash theme={null}
    find functions in NotificationsService.swift that are not covered by tests
    ```
  </Step>

  <Step title="生成测试框架" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    add tests for the notification service
    ```
  </Step>

  <Step title="添加有意义的测试用例" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    add test cases for edge conditions in the notification service
    ```
  </Step>

  <Step title="运行并验证测试" stepNumber={4} titleSize="h3">
    ```bash theme={null}
    run the new tests and fix any failures
    ```
  </Step>
</Steps>

## 创建拉取请求

可以通过直接要求 Coding Agent 创建拉取请求（“create a pr for my changes”），或逐步指导 Coding Agent：

<Steps>
  <Step title="总结更改" titleSize="h3">
    ```bash theme={null}
    summarize the changes I've made to the authentication module
    ```
  </Step>

  <Step title="生成拉取请求" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    create a pr
    ```
  </Step>

  <Step title="审查和细化" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    enhance the PR description with more context about the security improvements
    ```
  </Step>
</Steps>

## 处理文档

<Steps>
  <Step title="识别未记录的代码" titleSize="h3">
    ```bash theme={null}
    find functions without proper JSDoc comments in the auth module
    ```
  </Step>

  <Step title="生成文档" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    add JSDoc comments to the undocumented functions in auth.js
    ```
  </Step>

  <Step title="审查和增强" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    improve the generated documentation with more context and examples
    ```
  </Step>

  <Step title="验证文档" stepNumber={4} titleSize="h3">
    ```bash theme={null}
    check if the documentation follows our project standards
    ```
  </Step>
</Steps>

<Tip>
  **提示：**

  * 指定您想要的文档样式（JSDoc、docstrings 等）
  * 请求文档中的示例
  * 请求公共 API、接口和复杂逻辑的文档
</Tip>

## 添加图像

如果你需要在对话中提供图像，并希望 Coding Agent 帮助分析图像内容，可以按照以下步骤操作。

<Steps>
  <Step title="将图像添加到对话中" titleSize="h3">
    可以使用以下任何方法：

    * 将图像拖放到 Coding Agent 窗口中
    * 复制图像并使用 ctrl+v 将其粘贴到 CLI 中（不要使用 cmd+v）
    * 向 Coding Agent 提供图像路径。例如 `Analyze this image: /path/to/your/image.png`
  </Step>

  <Step title="让 Coding Agent 分析图像" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    What does this image show?
    Describe the UI elements in this screenshot
    Are there any problematic elements in this diagram?
    ```
  </Step>

  <Step title="结合图像描述问题" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    Here's a screenshot of the error. What's causing it?
    This is our current database schema. How should we modify it for the new feature?
    ```
  </Step>

  <Step title="从视觉内容获取代码建议" stepNumber={4} titleSize="h3">
    ```bash theme={null}
    Generate CSS to match this design mockup
    What HTML structure would recreate this component?
    ```
  </Step>
</Steps>

## 引用文件和目录

使用 `@` 快速包含文件或目录，无需等待 Coding Agent 读取它们。

<Steps>
  <Step title="引用单个文件" titleSize="h3">
    ```bash theme={null}
    Explain the logic in @src/utils/auth.js
    ```

    这在对话中包含文件的完整内容。
  </Step>

  <Step title="引用目录" stepNumber={2} titleSize="h3">
    ```bash theme={null}
    What's the structure of @src/components?
    ```

    这提供了带有文件信息的目录列表。
  </Step>

  <Step title="引用 MCP 资源" stepNumber={3} titleSize="h3">
    ```bash theme={null}
    Show me the data from @github:repos/owner/repo/issues
    ```
  </Step>
</Steps>

## 学习资源

<CardGroup cols={2}>
  <Card title="Coding Agent 工作原理" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/plug.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=ee8b6362dc2efcf3b5e159abe7f85bc0)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/plug.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=ee8b6362dc2efcf3b5e159abe7f85bc0)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/coding-plan/learning-resources/how-coding-agent-works" />

  <Card title="Agentic 扩展组件" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/coding-plan/learning-resources/agentic-extension" />

  <Card title="记忆机制" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/coding-plan/learning-resources/memory-mechanism" />

  <Card title="最佳实践" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/coding-plan/learning-resources/best-practice" />
</CardGroup>
