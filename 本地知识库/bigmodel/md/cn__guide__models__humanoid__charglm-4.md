<!-- source: https://docs.bigmodel.cn/cn/guide/models/humanoid/charglm-4 -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# CharGLM-4

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-list.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=018c661d2efce849f51ad05afdb0f876)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 概览 </div>

CharGLM-4 是智谱AI 推出的角色扮演专用模型，支持基于人设的角色扮演、超长多轮的记忆、千人千面的角色对话。该模型广泛应用于情感陪伴、游戏智能 NPC、网红/明星/影视剧 IP 分身、数字人/虚拟主播、文字冒险游戏等拟人对话或游戏场景。

<CardGroup cols={3}>
  <Card title="价格" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/coins.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=d140ba7189994790a79f83f5a763f59a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/coins.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=d140ba7189994790a79f83f5a763f59a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    1 元 / 百万 Tokens
  </Card>

  <Card title="输入模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    文本
  </Card>

  <Card title="输出模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    文本
  </Card>

  <Card title="上下文窗口" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-arrow-up.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=ccc051baa101b9a46d0d9bc5fad04877)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    8K
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 推荐场景 </div>

<AccordionGroup>
  <Accordion title="情感陪伴" defaultOpen="true">
    提供个性化的情感陪伴服务，支持长期的情感交流和心理支持。
  </Accordion>

  <Accordion title="游戏智能 NPC">
    为游戏创建具有独特个性和背景故事的智能 NPC，提升游戏体验的沉浸感。
  </Accordion>

  <Accordion title="IP 分身">
    创建网红、明星、影视剧角色的数字分身，实现粉丝互动和内容创作。
  </Accordion>

  <Accordion title="数字人/虚拟主播">
    为数字人和虚拟主播提供个性化的对话能力，支持直播互动和内容创作。
  </Accordion>

  <Accordion title="文字冒险游戏">
    创建沉浸式的文字冒险游戏体验，支持复杂的剧情发展和角色互动。
  </Accordion>

  <Accordion title="教育培训">
    扮演历史人物、文学角色等，为教育场景提供生动的互动体验。
  </Accordion>
</AccordionGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 核心能力 </div>

<CardGroup cols={3}>
  <Card title="角色扮演" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/square-user.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f2ec4e5b6ca0cd9c47255bcf8b22626b)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/square-user.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f2ec4e5b6ca0cd9c47255bcf8b22626b)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    基于人设进行深度角色扮演，保持角色一致性
  </Card>

  <Card title="超长记忆" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/database.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=93c0e1cf0ce93de9364ade5d1f49d992)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/database.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=93c0e1cf0ce93de9364ade5d1f49d992)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    支持超长多轮对话记忆，维持长期的角色关系
  </Card>

  <Card title="千人千面" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/users.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=450c463e81276d329696d13ac288effe)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/users.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=450c463e81276d329696d13ac288effe)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    支持创建多样化的角色，每个角色都有独特的个性
  </Card>

  <Card title="情感表达" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/sparkles.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=33479426e22cd63fbda2dff6ad55670c)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/sparkles.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=33479426e22cd63fbda2dff6ad55670c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    丰富的情感表达能力，支持复杂的情感交流
  </Card>

  <Card title="流式输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    支持实时流式响应，提升交互体验
  </Card>

  <Card title="上下文理解" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    深度理解对话上下文，保持对话连贯性
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 使用资源 </div>

[体验中心](https://bigmodel.cn/trialcenter??modelCode=charglm-4)：快速测试模型在业务场景上的效果<br />
[接口文档](/api-reference/%E6%A8%A1%E5%9E%8B-api/%E5%AF%B9%E8%AF%9D%E8%A1%A5%E5%85%A8)：API 调用方式<br />
[产品定价](https://bigmodel.cn/pricing)：查看模型定价信息

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 调用示例 </div>

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl -X POST "https://open.bigmodel.cn/api/paas/v4/chat/completions" \
    -H "Authorization: Bearer your_api_key" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "charglm-4",
        "messages": [
            {
                "role": "system",
                "content": "你乃苏东坡。人生如梦，何不活得潇洒一些？在这忙碌纷繁的现代生活中，帮助大家找到那份属于自己的自在与豁达，共赏人生之美好。"
            },
            {
                "role": "user",
                "content": "我最近工作不顺利，感到情绪低落"
            }
        ],
        "stream": true
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

    **调用示例**

    ```python theme={null}
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="your-api-key")  # 填写您自己的 APIKey

    response = client.chat.completions.create(
        model="charglm-4",
        messages=[
            {
                "role": "system",
                "content": "你乃苏东坡。人生如梦，何不活得潇洒一些？在这忙碌纷繁的现代生活中，帮助大家找到那份属于自己的自在与豁达，共赏人生之美好。"
            },
            {
                "role": "user",
                "content": "我最近工作不顺利，感到情绪低落"
            }
        ],
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>

  <Tab title="Python (旧)">
    **更新 SDK 至 2.1.5.20250726**

    ```bash theme={null}
    # 安装最新版本
    pip install zhipuai

    # 或指定版本
    pip install zhipuai==2.1.5.20250726
    ```

    ```python theme={null}
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key="your-api-key")  # 填写您自己的 APIKey

    response = client.chat.completions.create(
        model="charglm-4",
        messages=[
            {
                "role": "system",
                "content": "你乃苏东坡。人生如梦，何不活得潇洒一些？在这忙碌纷繁的现代生活中，帮助大家找到那份属于自己的自在与豁达，共赏人生之美好。"
            },
            {
                "role": "user",
                "content": "我最近工作不顺利，感到情绪低落"
            }
        ],
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>
</Tabs>
