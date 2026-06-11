<!-- source: https://platform.kimi.com/docs/introduction -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 主要概念

## 文本与多模态模型

`kimi-k2.6` 是 Kimi 当前最智能的模型，支持文本、图片和视频输入，以及思考与非思考模式，适用于对话、代码生成、视觉理解和 Agent 任务。对模型的输入通常称为 "prompt"，提供清晰的指令和必要示例，是获得稳定输出的关键。平台也提供其他模型，详见[模型列表](/models)。

## 语言模型推理服务

语言模型推理服务是一个基于我们（Moonshot AI）开发和训练的预训练模型的 API 服务。当前平台对外主要提供 Chat Completions 接口，用于对话、代码生成、视觉理解和 Agent 任务。模型本身默认不直接访问网络、数据库等外部资源，但您可以结合官方工具或自定义工具调用能力扩展模型的执行范围。

## Token

文本生成模型以 Token 为基本单位来处理文本。Token 代表常见的字符序列。例如，单个汉字"夔"可能会被分解为若干 Token 的组合，而像"中国"这样短且常见的短语则可能会使用单个 Token。大致来说，对于一段通常的中文文本，1 个 Token 大约相当于 1.5-2 个汉字。

需要注意的是，Input 和 Output 的总和长度不能超过所选模型的最大上下文长度。例如 `kimi-k2.6` 支持最高 256K 上下文窗口，其他模型的上下文长度请参考[模型列表](/models)。

## 速率限制

这些速率限制是如何工作的？

速率限制通过4种方式衡量：并发、RPM（每分钟请求数）、TPM（每分钟 Token 数）、TPD（每天 Token 数）。速率限制可能会在任何一种选项中达到，取决于哪个先发生。例如，你可能向 ChatCompletions 发送了 20 个请求，每个请求只有 100 个 Token ，那么你就达到了限制（如果你的 RPM 限制是 20），即使你在这些 20 个请求中没有发满 200k 个 Token （假设你的TPM限制是 200k）。

对网关，出于方便考虑，我们会基于请求中的 max\_completion\_tokens 参数来计算速率限制。这意味着，如果你的请求中包含了 max\_completion\_tokens 参数，我们会使用这个参数来计算速率限制。如果你的请求中没有包含 max\_completion\_tokens 参数，我们会使用默认的 max\_completion\_tokens 参数来计算速率限制。当你发出请求后，我们会基于你请求的 token 数量加上你 max\_completion\_tokens 参数的数量来判断你是否达到了速率限制。而不考虑实际生成的 token 数量。

而在计费环节中，我们会基于你请求的 token 数量加上实际生成的 token 数量来计算费用。

### 其他值得注意的重要事项：

* 速率限制是在用户级别而非密钥级别上实施的。
* 目前我们在所有模型中共享速率限制。

## 模型列表

查看所有可用模型及其能力说明，请访问[模型列表](/models)页面。

# 使用指南

## 获取 API 密钥

你需要一个 API 密钥来使用我们的服务。你可以在我们的[控制台](https://platform.kimi.com/console)中[创建一个 API 密钥](https://platform.kimi.com/console/api-keys)。

## 发送请求

你可以使用我们的 Chat Completions API 来发送请求。你需要提供一个 API 密钥和一个模型名称。你可以选择是否使用默认的 max\_completion\_tokens 参数，或者自定义 max\_completion\_tokens 参数。可以参考 [API 文档](/api/chat)中的调用方法。

## 处理响应

通常的，我们会设置一个 2 小时的超时时间。如果单个请求超过了这个时间，我们会返回一个 504 错误。如果你的请求超过了速率限制，我们会返回一个 429 错误。如果你的请求成功了，我们会返回一个 JSON 格式的响应。

如果是为了快速处理一些任务，你可以使用我们的 Chat Completions API 的非 streaming 模式。这种模式下，我们会在一次请求中返回所有的生成文本。如果你需要更多的控制，你可以使用 streaming 模式。在这种模式下，我们会返回一个 [SSE](https://kimi.moonshot.cn/share/cr7boh3dqn37a5q9tds0) 流，你可以在这个流中获取生成的文本，这样用户体验可能会更好，并且你也可以在任何时候中断请求，而不会浪费资源。
