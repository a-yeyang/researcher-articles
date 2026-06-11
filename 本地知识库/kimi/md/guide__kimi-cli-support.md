<!-- source: https://platform.kimi.com/docs/guide/kimi-cli-support -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Kimi CLI 调用 Kimi 大模型

Kimi CLI 是 Moonshot AI 自研的命令行通用智能体工具，它可以帮助你快速完成各种各样的编程和文件处理等任务。

> Kimi CLI 目前还在 Technical Preview 阶段，如遇到 bug 或有任何意见或建议，欢迎通过 [https://github.com/MoonshotAI/kimi-cli/issues](https://github.com/MoonshotAI/kimi-cli/issues) 提交反馈！

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/hello.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=ef3f3ae202d9e08b2cd286692396ff1b" alt="" width="1546" height="1156" data-path="assets/pics/kimi-cli/hello.png" />

## 安装

Kimi CLI 支持 macOS 和 Linux 系统，要求使用 uv 包管理器安装。

如果你的系统中还没有安装 uv，请先参考 [uv 安装说明](https://docs.astral.sh/uv/getting-started/installation/) 进行安装。通常，在 macOS 和 Linux 系统中，可使用以下命令安装 uv：

```sh theme={null}
curl -LsSf https://astral.sh/uv/install.sh | sh
```

安装 uv 后，使用以下命令安装 Kimi CLI：

```sh theme={null}
uv tool install --python 3.13 kimi-cli
```

运行以下命令检查是否安装成功：

```sh theme={null}
kimi --version
```

> 由于 macOS 的安全校验机制，在 macOS 上第一次运行可能需要较长时间，请耐心等待。可以尝试将你所使用的终端工具添加到「系统设置」-「隐私与安全性」-「开发者工具」中，以信任终端上运行的程序。

## 升级

使用以下命令升级 Kimi CLI：

```sh theme={null}
uv tool upgrade kimi-cli --no-cache
```

## 使用

在命令行中进入你想要 Kimi CLI 操作的项目目录，运行 `kimi` 命令，即可启动 Kimi CLI。例如：

```sh theme={null}
cd my-project
kimi
```

首次运行时，Kimi CLI 会提示没有配置模型，需输入 `/setup` 元命令，进入配置流程：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/setup.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=f0cd02610e40af7695a5bfdd66ec7829" alt="" width="1588" height="1124" data-path="assets/pics/kimi-cli/setup.png" />

* Kimi For Coding 会员权益用户，选择第一个「Kimi For Coding 」，在随后的提示中，输入在会员页面获得的 API Key，并选择 `kimi-for-coding` 模型；Moonshot AI 开放平台用户，根据提示选择对应的平台，输入 API Key 并选择想要使用的模型。[查看 Kimi For Coding 会员权益说明](https://www.kimi.com/coding/benefits.html)
* 使用开放平台 API Key 的用户，请选择第二个 「Moonshot AI 开放平台」,然后配置在开放平台创建的 API Key [创建 API Key](https://platform.kimi.com/console/api-keys)，请确保 API Key 有足够的余额，否则可能会出现 API 调用失败的情况。

配置完成后，即可开始使用 Kimi CLI，例如：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/2048-game.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=9fec90dd073a0aa647f8ec40e608ee43" alt="" width="1588" height="2084" data-path="assets/pics/kimi-cli/2048-game.png" />

## Shell 模式

Kimi CLI 不仅仅是一个编程智能体，还可以通过 Ctrl-K 快捷键切换到 shell 模式。通过该模式，你可以在不离开 Kimi CLI 的情况下，直接执行 shell 命令，方便进行文件操作和查看结果。例如：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/shell-mode.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=681de8e3862c51f61ecf9fecd35455fe" alt="" width="1574" height="1540" data-path="assets/pics/kimi-cli/shell-mode.png" />

## 搭配 Zsh 使用

Zsh 用户可以搭配 [zsh-kimi-cli](https://github.com/MoonshotAI/zsh-kimi-cli) 插件，在 shell 中快速调用 Kimi CLI。

使用如下命令安装（以 oh-my-zsh 为例，其它包管理请参考仓库 README）：

```sh theme={null}
git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli
```

然后在 `~/.zshrc` 中启用该插件：

```sh theme={null}
plugins=(... kimi-cli)
```

重新启动 Zsh 之后，即可在 Zsh 中通过 Ctrl-K 进入 Kimi CLI 模式：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/zsh-integration.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=19768b47048052dbad69f35c8db936e7" alt="" width="1546" height="1124" data-path="assets/pics/kimi-cli/zsh-integration.png" />

目前 zsh-kimi-cli 插件还在持续更新中，请定期前往 `custom/plugins/kimi-cli` 目录通过 `git pull` 拉取更新。

## 搭配 Zed 编辑器使用

Kimi CLI 原生提供 [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol) 支持，可以搭配任何 ACP 客户端使用，例如 [Zed 编辑器](https://zed.dev/)。

> ACP 是 Zed 编辑器推出的一种通用智能体协议，使智能体的核心功能（服务端）和用户界面（客户端）解耦，用户可以自由选择不同的智能体服务端和客户端进行搭配使用。

要在 Zed 中使用 Kimi CLI，首先需确保已经安装并配置好 Kimi CLI，然后在 Zed 配置文件（`~/.config/zed/settings.json`）中添加以下内容：

```json theme={null}
{
  "agent_servers": {
    "Kimi CLI": {
      "command": "kimi",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

随后即可在 Zed 侧边栏创建 Kimi CLI Thread：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/kimi-cli/zed-new-thread.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=a169d4ef1283c9e77a5e8e0708006a6c" alt="" width="1050" height="560" data-path="assets/pics/kimi-cli/zed-new-thread.png" />

## 接入 MCP 工具

Kimi CLI 支持广泛采用的 MCP 配置格式指定 MCP 工具。例如：

```json theme={null}
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

启动时，通过 `--mcp-config-file` 参数指定 MCP 配置文件路径即可。例如：

```sh theme={null}
kimi --mcp-config-file /path/to/mcp.json
```

## Kimi CLI 更多用法

除了上述功能，还可以通过 `kimi --help` 查看 Kimi CLI 的更多用法。或者访问 Kimi CLI 官方网站了解更多 [Kimi CLI 文档](https://github.com/MoonshotAI/kimi-cli)。

## Kimi Agent SDK

Kimi Agent SDK 提供了以编程方式与 Kimi CLI 交互的接口，支持在代码中集成 Kimi 智能体能力。通过 SDK，你可以：

* **构建自定义应用** - 将 Kimi Agent 集成到自己的工具和流程中
* **自动化任务** - 编写复杂的多轮对话脚本
* **扩展功能** - 注册自定义工具供模型调用
* **处理审批** - 程序化响应权限请求

SDK 目前支持以下语言：

* **Go** - [go](https://github.com/MoonshotAI/kimi-agent-sdk/tree/main/go)
* **Node.js** - [node/agent\_sdk](https://github.com/MoonshotAI/kimi-agent-sdk/tree/main/node/agent_sdk)
* **Python** - [python](https://github.com/MoonshotAI/kimi-agent-sdk/tree/main/python)

详细信息请查看 [Kimi Agent SDK GitHub 仓库](https://github.com/MoonshotAI/kimi-agent-sdk)。
