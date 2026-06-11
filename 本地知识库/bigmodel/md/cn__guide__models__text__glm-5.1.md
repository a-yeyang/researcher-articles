<!-- source: https://docs.bigmodel.cn/cn/guide/models/text/glm-5.1 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM-5.1

<Tip>
  [**GLM Coding Plan 团队版**](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek) 已上线，让组织安全可控地提升开发效率，释放 AI 编程生产力。 →[立即了解](https://zhipuaishengchan.datasink.sensorsdata.cn/t/ek)
</Tip>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-list.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=018c661d2efce849f51ad05afdb0f876)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 概览 </div>

**GLM-5.1** 是智谱最新旗舰模型，代码能力大大增强，**长程任务**显著提升，能够在单次任务中持续、自主地工作长达 8 小时，完成从规划、执行到迭代优化的完整闭环，交付工程级成果。<br />在综合能力与 Coding 能力上，GLM-5.1 整体表现对齐 Claude Opus 4.6，并在**长程自主执行、复杂工程优化与真实开发**场景中展现出更强的持续工作能力，是构建 Autonomous Agent 与长程 Coding Agent 的理想基座。

<CardGroup cols={3}>
  <Card title="定位" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    旗舰基座模型
  </Card>

  <Card title="输入模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    文本
  </Card>

  <Card title="输出模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    文本
  </Card>

  <Card title="上下文窗口" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-arrow-up.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=ccc051baa101b9a46d0d9bc5fad04877)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-arrow-up.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=ccc051baa101b9a46d0d9bc5fad04877)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    200K
  </Card>

  <Card title="最大输出 Tokens" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    128K
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 能力支持 </div>

<CardGroup cols={3}>
  <Card title="思考模式" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/guide/capabilities/thinking-mode">
    提供多种思考模式，覆盖不同任务需求
  </Card>

  <Card title="流式输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/guide/capabilities/streaming">
    支持实时流式响应，提升用户交互体验
  </Card>

  <Card title="Function Call" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/function.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a597d8cdc054b4c0e39c08295f570c86)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/function.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a597d8cdc054b4c0e39c08295f570c86)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/guide/capabilities/function-calling">
    强大的工具调用能力，支持多种外部工具集成
  </Card>

  <Card title="上下文缓存" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/database.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=93c0e1cf0ce93de9364ade5d1f49d992)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/database.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=93c0e1cf0ce93de9364ade5d1f49d992)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/guide/capabilities/cache">
    智能缓存机制，优化长对话性能
  </Card>

  <Card title="结构化输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/cn/guide/capabilities/struct-output">
    支持 JSON 等结构化格式输出，便于系统集成
  </Card>

  <Card title="MCP" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    可灵活调用外部 MCP 工具与数据源，扩展应用场景
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 推荐场景 </div>

<AccordionGroup>
  <Accordion title="Agentic Coding">
    针对 Claude Code、OpenClaw 等典型 Agentic Coding 场景进一步优化，具备更强的长程规划、分步执行、过程调整与结果交付能力，在长程开发任务和复杂编程问题上的表现显著提升，适合多阶段、强依赖关系的真实工程任务。
  </Accordion>

  <Accordion title="通用对话">
    在开放式问答、复杂指令理解与多轮交流场景中表现更稳，回复维度更丰富、内容更完整，具备更强的指令遵循能力与长上下文理解能力，适合高质量日常助手与复杂信息交互场景。
  </Accordion>

  <Accordion title="创意写作">
    在文学化表达、情节延展、人物刻画与语言风格控制方面进一步增强，适用于小说片段、故事设定、文案创作等对表达力与一致性要求较高的写作任务。
  </Accordion>

  <Accordion title="Artifacts / 前端开发">
    适合网页、交互页面与前端原型生成场景，生成结果进一步减少模板感，视觉表达更多样，前端任务整体完成度更高，可更高效地支持从需求到可用产物的快速落地。
  </Accordion>

  <Accordion title="Office 生产力">
    在 PPT、Word、PDF、Excel 等文档生产任务上整体提升，能够完成更复杂的内容组织、版式设计与结构化输出，默认审美与成品质量显著增强，适合长文档、报告、教材、论文等高强度生产场景。
  </Accordion>
</AccordionGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 详细介绍 </div>

<Steps>
  <Step title="综合与 Coding 能力：对齐全球顶尖水平" stepNumber={1} titleSize="h3">
    GLM-5.1 在综合能力与 Coding 能力上达到全球第一梯队，整体表现对齐 Claude Opus 4.6，并在多个关键评测中位居前列。

    ![Description](https://cdn.bigmodel.cn/markdown/1775571965455img_v3_0210h_e53bcf0a-11aa-481c-aa2b-896e1b902eeg.png?attname=img_v3_0210h_e53bcf0a-11aa-481c-aa2b-896e1b902eeg.png)

    在 SWE-Bench Pro 基准测试中，GLM-5.1 取得 **58.4** 的成绩，超过 GPT-5.4、Claude Opus 4.6 和 Gemini 3.1 Pro，刷新全球最佳表现。同时，在覆盖推理、编程、Agent、工具调用与浏览等 12 项代表性基准上，GLM-5.1 也展现出全面、均衡的能力结构。

    ![Description](https://cdn.bigmodel.cn/markdown/1775572152820img_v3_0210h_7e69658d-d027-40da-b7e5-da12c080e41g.png?attname=img_v3_0210h_7e69658d-d027-40da-b7e5-da12c080e41g.png)

    这表明 GLM-5.1 的提升并非单点突破，而是在**通用智能、真实编程与复杂任务执行**三个维度上同步增强，更适合作为通用 Agent 系统与工程生产场景的基础模型。
  </Step>

  <Step title="长程任务能力：迈向 8 小时级持续工作" stepNumber={2} titleSize="h3">
    GLM-5.1 长程任务（Long Horizon Task）显著提升，重点提升模型在复杂目标下的**持续执行、闭环优化与工程交付能力**。相较于以分钟级交互为主的模型，GLM-5.1 能在单次任务中持续、自主地工作长达 8 小时，完成从规划、执行、测试到修复和交付的完整流程。

    在同等评估标准下，GLM-5.1 是少数具备 8 小时级持续工作能力的模型之一，也是中国模型中率先达到这一水平的代表。模型能力的衡量标准，正在从“单轮更聪明”进一步演进为“长程任务中能稳定工作多久、交付什么”。

    这类能力并不只是更长上下文，而是要求模型在长时间执行中**持续保持目标一致性，减少策略漂移、错误累积和无效试错**，真正具备面向复杂工程任务的自主执行能力。
  </Step>

  <Step title="工程交付能力：从代码生成向全自治智能体进化" stepNumber={3} titleSize="h3">
    GLM-5.1 的核心突破之一，是在长程任务中形成“**实验—分析—优化**”的自主闭环，而不是停留在一次性代码生成层面。模型能够主动运行 benchmark、识别瓶颈、调整策略，并在多轮迭代中持续提升结果质量。

    在典型案例中，GLM-5.1 可在 8 小时内从零构建完整 Linux 桌面系统；自主进行 655 轮迭代，完成整条优化链路，让向量数据库的查询吞吐提升到初始正式版本的 6.9倍；在 KernelBench Level 3 优化基准上，完成千轮工具调用优化真实机器学习模型负载，实现 3.6 倍几何平均加速比，远超 torch.compile max-autotune 模式的 1.49 倍。

    这些结果说明，GLM-5.1 已具备在复杂工程环境中自主探索、持续改进和稳定交付的能力，能够胜任系统构建、性能优化与长程 Coding Agent 等更高价值任务。
  </Step>
</Steps>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 使用资源 </div>

[体验中心](https://bigmodel.cn/trialcenter/modeltrial/text?modelCode=glm-5.1)：快速测试模型在业务场景上的效果<br />
[接口文档](/api-reference/%E6%A8%A1%E5%9E%8B-api/%E5%AF%B9%E8%AF%9D%E8%A1%A5%E5%85%A8)：API 调用方式

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 调用示例 </div>

以下是完整的调用示例，帮助您快速上手 GLM-5.1 模型。

<Tabs>
  <Tab title="cURL">
    **基础调用**

    ```bash theme={null}
    curl -X POST "https://open.bigmodel.cn/api/paas/v4/chat/completions" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer your-api-key" \
        -d '{
            "model": "glm-5.1",
            "messages": [
                {
                    "role": "user",
                    "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"
                },
                {
                    "role": "assistant",
                    "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"
                },
                {
                    "role": "user",
                    "content": "智谱AI 开放平台"
                }
            ],
            "thinking": {
                "type": "enabled"
            },
            "max_tokens": 65536,
            "temperature": 1.0
        }'
    ```

    **流式调用**

    ```bash theme={null}
    curl -X POST "https://open.bigmodel.cn/api/paas/v4/chat/completions" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer your-api-key" \
        -d '{
            "model": "glm-5.1",
            "messages": [
                {
                    "role": "user",
                    "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"
                },
                {
                    "role": "assistant",
                    "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"
                },
                {
                    "role": "user",
                    "content": "智谱开放平台"
                }
            ],
            "thinking": {
                "type": "enabled"
            },
            "stream": true,
            "max_tokens": 65536,
            "temperature": 1.0
        }'
    ```
  </Tab>

  <Tab title="Python">
    **安装 SDK**

    ```bash theme={null}
    # 安装最新版本
    pip install zai-sdk
    # 或指定版本
    pip install zai-sdk==0.2.2
    ```

    **验证安装**

    ```python theme={null}
    import zai
    print(zai.__version__)
    ```

    **基础调用**

    ```python theme={null}
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="your-api-key")  # 请填写您自己的 API Key

    response = client.chat.completions.create(
        model="glm-5.1",
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱开放平台"}
        ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        max_tokens=65536,          # 最大输出 tokens
        temperature=1.0           # 控制输出的随机性
    )

    # 获取完整回复
    print(response.choices[0].message)
    ```

    **流式调用**

    ```python theme={null}
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="your-api-key")  # 请填写您自己的 API Key

    response = client.chat.completions.create(
        model="glm-5.1",
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱开放平台"}
        ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        stream=True,              # 启用流式输出
        max_tokens=65536,          # 最大输出tokens
        temperature=1.0           # 控制输出的随机性
    )

    # 流式获取回复
    for chunk in response:
        if chunk.choices[0].delta.reasoning_content:
            print(chunk.choices[0].delta.reasoning_content, end='', flush=True)

        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end='', flush=True)
    ```
  </Tab>

  <Tab title="Java">
    **安装 SDK**

    **Maven**

    ```xml theme={null}
    <dependency>
        <groupId>ai.z.openapi</groupId>
        <artifactId>zai-sdk</artifactId>
        <version>0.3.3</version>
    </dependency>
    ```

    **Gradle (Groovy)**

    ```groovy theme={null}
    implementation 'ai.z.openapi:zai-sdk:0.3.3'
    ```

    **基础调用**

    ```java theme={null}
    import ai.z.openapi.ZhipuAiClient;
    import ai.z.openapi.service.model.ChatCompletionCreateParams;
    import ai.z.openapi.service.model.ChatCompletionResponse;
    import ai.z.openapi.service.model.ChatMessage;
    import ai.z.openapi.service.model.ChatMessageRole;
    import ai.z.openapi.service.model.ChatThinking;
    import java.util.Arrays;

    public class BasicChat {
        public static void main(String[] args) {
            // 初始化客户端
            ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                .apiKey("your-api-key")
                .build();

            // 创建聊天完成请求
            ChatCompletionCreateParams request = ChatCompletionCreateParams.builder()
                .model("glm-5.1")
                .messages(Arrays.asList(
                    ChatMessage.builder()
                        .role(ChatMessageRole.USER.value())
                        .content("作为一名营销专家，请为我的产品创作一个吸引人的口号")
                        .build(),
                    ChatMessage.builder()
                        .role(ChatMessageRole.ASSISTANT.value())
                        .content("当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息")
                        .build(),
                    ChatMessage.builder()
                        .role(ChatMessageRole.USER.value())
                        .content("智谱开放平台")
                        .build()
                ))
                .thinking(ChatThinking.builder().type("enabled").build())
                .maxTokens(65536)
                .temperature(1.0f)
                .build();

            // 发送请求
            ChatCompletionResponse response = client.chat().createChatCompletion(request);

            // 获取回复
            if (response.isSuccess()) {
                Object reply = response.getData().getChoices().get(0).getMessage();
                System.out.println("AI 回复: " + reply);
            } else {
                System.err.println("错误: " + response.getMsg());
            }
        }
    }
    ```

    **流式调用**

    ```java theme={null}
    import ai.z.openapi.ZhipuAiClient;
    import ai.z.openapi.service.model.ChatCompletionCreateParams;
    import ai.z.openapi.service.model.ChatCompletionResponse;
    import ai.z.openapi.service.model.ChatMessage;
    import ai.z.openapi.service.model.ChatMessageRole;
    import ai.z.openapi.service.model.ChatThinking;
    import ai.z.openapi.service.model.Delta;
    import java.util.Arrays;

    public class StreamingChat {
        public static void main(String[] args) {
            // 初始化客户端
            ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                .apiKey("your-api-key")
                .build();

            // 创建流式聊天完成请求
            ChatCompletionCreateParams request = ChatCompletionCreateParams.builder()
                .model("glm-5.1")
                .messages(Arrays.asList(
                    ChatMessage.builder()
                        .role(ChatMessageRole.USER.value())
                        .content("作为一名营销专家，请为我的产品创作一个吸引人的口号")
                        .build(),
                    ChatMessage.builder()
                        .role(ChatMessageRole.ASSISTANT.value())
                        .content("当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息")
                        .build(),
                    ChatMessage.builder()
                        .role(ChatMessageRole.USER.value())
                        .content("智谱开放平台")
                        .build()
                ))
                .thinking(ChatThinking.builder().type("enabled").build())
                .stream(true)  // 启用流式输出
                .maxTokens(65536)
                .temperature(1.0f)
                .build();

            ChatCompletionResponse response = client.chat().createChatCompletion(request);

            if (response.isSuccess()) {
                response.getFlowable().subscribe(
                    // Process streaming message data
                    data -> {
                        if (data.getChoices() != null && !data.getChoices().isEmpty()) {
                            Delta delta = data.getChoices().get(0).getDelta();
                            System.out.print(delta + "\n");
                        }
                    },
                    // Process streaming response error
                    error -> System.err.println("\nStream error: " + error.getMessage()),
                    // Process streaming response completion event
                    () -> System.out.println("\nStreaming response completed")
                );
            } else {
                System.err.println("Error: " + response.getMsg());
            }
        }
    }
    ```
  </Tab>

  <Tab title="Python(旧)">
    **更新 SDK 至 2.1.5.20250726**

    ```bash theme={null}
    # 安装最新版本
    pip install zhipuai

    # 或指定版本
    pip install zhipuai==2.1.5.20250726
    ```

    **基础调用**

    ```python theme={null}
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key="your-api-key")  # 请填写您自己的 API Key

    response = client.chat.completions.create(
        model="glm-5.1",
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱开放平台"}
        ],
        thinking={
            "type": "enabled",
        },
        max_tokens=65536,
        temperature=1.0
    )

    # 获取完整回复
    print(response.choices[0].message)
    ```

    **流式调用**

    ```python theme={null}
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key="your-api-key")  # 请填写您自己的 API Key

    response = client.chat.completions.create(
        model="glm-5.1",
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱开放平台"}
        ],
        thinking={
            "type": "enabled",
        },
        stream=True,              # 启用流式输出
        max_tokens=65536,
        temperature=1.0
    )

    # 流式获取回复
    for chunk in response:
        if chunk.choices[0].delta.reasoning_content:
            print(chunk.choices[0].delta.reasoning_content, end='', flush=True)

        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end='', flush=True)
    ```
  </Tab>
</Tabs>
