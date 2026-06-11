<!-- source: https://docs.bigmodel.cn/cn/guide/models/vlm/glm-ocr -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM-OCR

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-list.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=018c661d2efce849f51ad05afdb0f876)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 概览 </div>

GLM-OCR  是一款轻量级的专业 OCR 模型，参数仅为0.9B，但多项能力达到了SOTA水平，以 “小尺寸、高精度” 实现文档解析能力新标杆。其核心要点如下：

* **性能 SOTA**：在模型发布时以 94.62 分登顶 OmniDocBench V1.5，并在表格、公式等多项主流文档理解基准中取得当前最佳表现；
* **针对真实业务场景优化**：在代码文档、复杂表格、印章等复杂场景中表现稳定且精度领先，即使在版式复杂、字体多样或图文混排情况下，识别准确度依旧出色；
* **高效高性价比**：仅 0.9B 参数规模，支持 VLLM 和 SGLang 部署，显著降低推理延迟与算力开销,成本约为传统 OCR 方案的 1/10。

<CardGroup cols={3}>
  <Card title="输入模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    - PDF、图片（JPG、PNG）
    - 单图 ≤ 10 MB，PDF ≤ 50 MB
    - 最大支持 100 页
  </Card>

  <Card title="输出模态" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    文本、图片链接、md 文档
  </Card>

  <Card title="支持的语言" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    中文、英文、法语、西班牙语、俄罗斯语、德语、日语、韩语等……
  </Card>
</CardGroup>

<Tip>
  GLM-OCR 价格详情请前往[价格界面](https://open.bigmodel.cn/pricing)
</Tip>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/bolt.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=69a953a610be765badc883ce49686389)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 能力支持 </div>

<CardGroup cols={3}>
  <Card title="结构化输出" href="/cn/guide/capabilities/struct-output" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/maximize.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=743c202becf04d91d943f9014a3fe67f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    返回符合预定义格式的 JSON 数据
  </Card>

  <Card title="文档解析" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/eye.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b122d35262105038324f60f9e09612e)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/eye.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b122d35262105038324f60f9e09612e)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
    高精度的文档信息识别能力
  </Card>
</CardGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/stars.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=eefc5fa680420566b18e2c3c1d30bb3d)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 推荐场景 </div>

<AccordionGroup>
  <Accordion title="通用文本识别" defaultOpen="true">
    GLM-OCR 支持照片、截图、扫描件、文档输入，能够识别手写体、印章、代码等特殊文字，可广泛应用于教育、科研、办公等场景。
  </Accordion>

  <Accordion title="复杂表格解析">
    针对合并单元格、多层表头等复杂结构，模型能精准理解并直接输出 HTML 代码。无需二次制表，识别结果即可用于网页展示或数据处理，大幅提升表格录入与转换效率。
  </Accordion>

  <Accordion title="信息结构化提取">
    GLM-OCR 可从各类卡证、票据、表格中智能提取关键字段，并输出标准的 JSON 格式，无缝对接银行、保险、政务及物流等行业系统。
  </Accordion>

  <Accordion title="批量处理与RAG支持">
    GLM-OCR 支持大批量文档的识别与解析，其高精度的识别能力和规整的输出格式，可为检索增强生成（RAG）提供坚实基础。
  </Accordion>
</AccordionGroup>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-up.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2c1e1940f6d55086f84c6054cc093fac)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 详细介绍 </div>

<Steps>
  <Step title="性能SOTA、精准干活儿" stepNumber={1} titleSize="h3">
    得益于自研 CogViT 视觉编码器与深度场景优化，GLM-OCR 实现了“小尺寸，高精度”。
    GLM-OCR 参数量仅 0.9B，但模型发布时在权威文档解析榜单 OmniDocBench V1.5 中以 94.6 分取得SOTA。在文本、公式、表格识别及信息抽取四大细分领域的表现优于多款OCR专项模型，性能接近 Gemini-3-Pro 。

    ![Description](https://cdn.bigmodel.cn/markdown/1770049137241img_v3_02uh_8e984807-871e-45eb-8ea2-706fb275cf3g.png?attname=img_v3_02uh_8e984807-871e-45eb-8ea2-706fb275cf3g.png)

    除了公开榜单，我们还针对真实业务中的六大核心场景进行了内部测评。结果显示，在模型发布时GLM-OCR 在代码文档、真实场景表格、手写体、多语言、印章识别、票据提取等维度均取得显著优势。

    ![Description](https://cdn.bigmodel.cn/markdown/1770049153590img_v3_02uh_b3aff49e-f980-4bf4-9dfb-20c7bbce04bg.png?attname=img_v3_02uh_b3aff49e-f980-4bf4-9dfb-20c7bbce04bg.png)
  </Step>

  <Step title="更快、更便宜" stepNumber={2} titleSize="h3">
    速度方面，我们对比了在相同硬件环境与测试条件下（单副本，单并发），分别以图像文件和 PDF 文件为输入，不同 OCR 方法完成解析并导出 Markdown 文件的速度差异。结果显示，GLM-OCR 处理 PDF 文档的吞吐量达 1.86 页/秒，图片达 0.67 张/秒，速度显著优于同类模型。

    ![Description](https://cdn.bigmodel.cn/markdown/1770038561894img_v3_02uh_e883d08f-9ebf-4438-90e0-ab741438ff6g.png?attname=img_v3_02uh_e883d08f-9ebf-4438-90e0-ab741438ff6g.png)

    <Info>
      提示：实际性能受文件质量、网络及并发数影响，建议以实际接入测试为准。
    </Info>

    <Check>
      **想要更快？** 推荐以下用法：

      * 使用图片传入替代文件上传
      * 多页 PDF 拆页并行调用
    </Check>

    价格方面，API输入输出同价，仅需 0.2元/百万Tokens。1 元即可处理约 2000 张 A4 大小扫描图片或 200 份 10 页简单排版PDF，成本约为传统 OCR 方案的 1/10。
  </Step>
</Steps>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/ballot.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=62ff21df625f3b2407e77a4106317317)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 应用示例 </div>

<Tabs>
  <Tab title="手写字识别">
    <CardGroup cols={2}>
      <Card title="输入" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        ![Description](https://cdn.bigmodel.cn/markdown/1770033643596image.png?attname=image.png)<br />
      </Card>

      <Card title="输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        六国灭亡了，天下统一了，蜀地的山秃了，阿房宫建成了。 它覆盖三百多里地，遮蔽天日。阿房宫从骊山北边建起，折而向西，一直通向咸阳。
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="表格识别">
    <CardGroup cols={2}>
      <Card title="输入" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        ![Description](https://cdn.bigmodel.cn/markdown/1770033857500image.png?attname=image.png)
      </Card>

      <Card title="输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        ![Description](https://cdn.bigmodel.cn/markdown/1770033891518image.png?attname=image.png)
      </Card>
    </CardGroup>
  </Tab>

  <Tab title="信息结构化提取">
    <CardGroup cols={2}>
      <Card title="输入" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-down-right.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=088a58fa0b1a4048d5c6fab7841133c8)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        ![Description](https://cdn.bigmodel.cn/markdown/1770033970153image.png?attname=image.png)
        **prompt**

        请按下列JSON格式输出图中信息:

        ```bash theme={null}
        {
            "标题": "",
            "发票号码": "",
            "开票日期": {
            "年": "",
            "月": "",
            "日": ""
        },
            "购买方信息": {
            "名称": "",
            "统一社会信用代码/纳税人识别号": ""
        },
            "销售方信息": {
            "名称": "",
            "统一社会信用代码/纳税人识别号": ""
        },
            "项目名称": "",
            "单价": "",
            "数量": "",
            "金额": "",
            "税率/征收率": "",
            "税额": "",
            "金额合计": "",
            "税额合计": "",
            "出行人": "",
            "有效身份证件号": "",
            "出行日期": "",
            "出发地": "",
            "到达地": "",
            "等级": "",
            "交通工具类型": "",
            "价税合计（大写）": "",
            "价税合计（小写）": "",
            "备注": "",
            "开票人": "",
            "印章": []
        }
        ```
      </Card>

      <Card title="输出" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/Skp28ct-clfAIOZo/resource/icon/arrow-down-left.svg?fit=max&auto=format&n=Skp28ct-clfAIOZo&q=85&s=1ed65b58aa7a484b387f01be25d99278)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />}>
        ```bush theme={null}
        {
            "标题": "电子发票（普通发票）",
            "发票号码": "25127000000102638675",
            "开票日期": {
            "年": "2025",
            "月": "04",
            "日": "08"
        },
            "购买方信息": {
            "名称": "深圳市百川数安科技有限公司",
            "统一社会信用代码/纳税人识别号": "91440300MA5GUFD LXF"
        },
            "销售方信息": {
            "名称": "天津鞍马出行科技有限公司",
            "统一社会信用代码/纳税人识别号": "91120106MACB2BWC1M"
        },
            "项目名称": "*运输服务*客运服务费",
            "单价": "8.74",
            "数量": "1",
            "金额": "8.74",
            "税率/征收率": "3%",
            "税额": "0.26",
            "金额合计": "¥8.74",
            "税额合计": "¥0.26",
            "出行人": "",
            "有效身份证件号": "",
            "出行日期": "",
            "出发地": "",
            "到达地": "",
            "等级": "",
            "交通工具类型": "",
            "价税合计（大写）": "⊗玖圆整",
            "价税合计（小写）": "¥9.00",
            "备注": "",
            "开票人": "刘薇",
            "印章": [
            "全国统一发票监制章\n国家税务总局\n天津市税务局"
            ]
        }
        ```
      </Card>
    </CardGroup>
  </Tab>
</Tabs>

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/gauge-high.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=11e017cb0ce99d3d70ab7310e8728e18)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 使用资源 </div>

[体验中心](https://www.bigmodel.cn/trialcenter/modeltrial/visual?modelCode=glm-ocr)：快速测试模型在业务场景上的效果<br />
[接口文档](/api-reference/%E6%A8%A1%E5%9E%8B-api/%E6%96%87%E6%A1%A3%E8%A7%A3%E6%9E%90)：API 调用方式

## <div className="flex items-center"> <svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} /> 调用示例 </div>

以下是完整的调用示例，帮助您快速上手 GLM-OCR 模型。

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl --location --request POST 'https://open.bigmodel.cn/api/paas/v4/layout_parsing' \
    --header 'Authorization: your_api_key' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "model": "glm-ocr",
      "file": "https://cdn.bigmodel.cn/static/logo/introduction.png"
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

    # 初始化客户端
    client = ZhipuAiClient(api_key="your-api-key")

    image_url = "https://cdn.bigmodel.cn/static/logo/introduction.png"

    # 调用布局解析 API
    response = client.layout_parsing.create(
        model="glm-ocr",
        file=image_url
    )

    # 输出结果
    print(response)
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
    import ai.z.openapi.service.layoutparsing.LayoutParsingCreateParams;
    import ai.z.openapi.service.layoutparsing.LayoutParsingResponse;
    import ai.z.openapi.service.layoutparsing.LayoutParsingResult;

    public class LayoutParsing {
        public static void main(String[] args) {
            // 初始化客户端
            ZhipuAiClient client = ZhipuAiClient.builder()
                .ofZHIPU()
                .apiKey("your-api-key")
                .build();

            String model = "glm-ocr";
            String file = "https://cdn.bigmodel.cn/static/logo/introduction.png";

            // 创建布局解析请求
            LayoutParsingCreateParams params = LayoutParsingCreateParams.builder()
                .model(model)
                .file(file)
                .build();

            // 发送请求
            LayoutParsingResponse response = client.layoutParsing().layoutParsing(params);

            // 处理响应
            if (response.isSuccess()) {
                System.out.println("解析结果: " + response.getData());
            } else {
                System.err.println("错误: " + response.getMsg());
            }
        }
    }
    ```
  </Tab>
</Tabs>
