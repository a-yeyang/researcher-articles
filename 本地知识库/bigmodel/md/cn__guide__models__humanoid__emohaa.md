<!-- source: https://docs.bigmodel.cn/cn/guide/models/humanoid/emohaa -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Emohaa

<Warning>
  Emohaa 模型虽然具备专业的心理支持能力，但不能替代专业的心理治疗。对于严重的心理健康问题，建议寻求专业心理医生的帮助。
</Warning>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-list.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=018c661d2efce849f51ad05afdb0f876)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 概览 </div>

Emohaa 是智谱AI 推出的专业心理咨询模型，学习了经典的 Hill 助人理论，拥有人类心理咨询师的专业话术能力。该模型具有较强的倾听、情感映射、共情等情绪支持能力，帮助用户了解自身想法和感受，学习应对情绪问题，帮助用户实现乐观、积极的心理和情感状态。

<CardGroup cols={3}>
  <Card title="价格" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/coins.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=d140ba7189994790a79f83f5a763f59a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/coins.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=d140ba7189994790a79f83f5a763f59a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    15 元 / 百万 Tokens
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
    提供专业的情感支持和心理陪伴，帮助用户缓解负面情绪，建立积极心态。
  </Accordion>

  <Accordion title="心理咨询">
    基于 Hill 助人理论，提供专业的心理咨询服务，帮助用户探索内心世界。
  </Accordion>

  <Accordion title="情绪管理">
    协助用户识别、理解和管理情绪，学习有效的情绪调节策略。
  </Accordion>

  <Accordion title="压力缓解">
    针对工作、学习、生活中的压力，提供专业的缓解建议和支持。
  </Accordion>

  <Accordion title="人际关系指导">
    帮助用户改善人际关系，提升沟通技巧和社交能力。
  </Accordion>
</AccordionGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 核心能力 </div>

<CardGroup cols={3}>
  <Card title="专业倾听" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/headset.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f42f526ce8d7b3098ec5c72bfe9a401a)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/headset.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f42f526ce8d7b3098ec5c72bfe9a401a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    具备专业心理咨询师的倾听技巧，能够深度理解用户的情感需求
  </Card>

  <Card title="情感映射" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    准确识别和映射用户的情感状态，提供针对性的支持
  </Card>

  <Card title="共情能力" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/users.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=450c463e81276d329696d13ac288effe)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/users.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=450c463e81276d329696d13ac288effe)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    强大的共情能力，能够与用户建立深度的情感连接
  </Card>

  <Card title="专业话术" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/feather.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=fe0922491e9f5f9c18209a21791882bc)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/feather.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=fe0922491e9f5f9c18209a21791882bc)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    掌握专业心理咨询话术，提供温暖而有效的沟通体验
  </Card>

  <Card title="Hill 助人理论" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=f9a867079d7ff6967277ded330e6a683)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    基于经典的 Hill 助人理论，提供科学系统的心理支持
  </Card>

  <Card title="积极引导" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/sparkles.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=33479426e22cd63fbda2dff6ad55670c)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/sparkles.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=33479426e22cd63fbda2dff6ad55670c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    引导用户建立乐观积极的心理状态和情感状态
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 使用资源 </div>

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
        "model": "emohaa",
        "messages": [
            {
                "role": "user",
                "content": "我最近工作压力很大，经常感到焦虑，不知道该怎么办"
            }
        ],
        "meta": {
            "user_info": "一位正在经历工作压力的职场人士",
            "bot_info": "专业的心理咨询师，擅长情绪支持和压力管理",
            "bot_name": "心理咨询师",
            "user_name": "用户"
        },
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
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="your-api-key")  # 填写您自己的 APIKey

    response = client.chat.completions.create(
        model="emohaa",
        messages=[
            {
                "role": "user",
                "content": "我最近工作压力很大，经常感到焦虑，不知道该怎么办"
            }
        ],
        meta={
            "user_info": "一位正在经历工作压力的职场人士",
            "bot_info": "专业的心理咨询师，擅长情绪支持和压力管理",
            "bot_name": "心理咨询师",
            "user_name": "用户"
        },
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
        model="emohaa",
        messages=[
            {
                "role": "user",
                "content": "我最近工作压力很大，经常感到焦虑，不知道该怎么办"
            }
        ],
        meta={
            "user_info": "一位正在经历工作压力的职场人士",
            "bot_info": "专业的心理咨询师，擅长情绪支持和压力管理",
            "bot_name": "心理咨询师",
            "user_name": "用户"
        },
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>
</Tabs>

<Note>
  为了获得最佳的使用效果，建议在 meta 参数中提供详细的用户信息和角色设定，这有助于模型更好地理解上下文并提供个性化的支持。
</Note>
