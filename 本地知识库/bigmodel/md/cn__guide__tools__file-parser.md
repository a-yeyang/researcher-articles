<!-- source: https://docs.bigmodel.cn/cn/guide/tools/file-parser -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 新文件解析服务

## 产品简介

<Tip>
  智谱文件解析API是一款面向开发者和企业的统一文件解析解决方案，实现了多格式文件解析、智能内容抽取、灵活结果输出的一站式服务。
</Tip>

该API支持主流办公文档（`PDF、Word、Excel、PPT`）、结构化/非结构化数据文件（`CSV、MD、TXT`）以及多种图片格式（`JPG、PNG`等），能够**快速提取文件中的文本、表格、图片和版面结构**，生成标准化输出，便于直接接入下游业务系统或大模型处理链路。

智谱文件解析API旨在帮助企业与开发者**降低接入成本、提升解析精度、优化调用体验**，实现从文件上传到结果获取的全链路高效处理。

<CardGroup cols={3}>
  <Card title="智能识别" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    自动识别并解析文件中的文本、表格、图片等内容。
  </Card>

  <Card title="灵活选择" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/function.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=a597d8cdc054b4c0e39c08295f570c86)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    按需选择不同解析服务类型，兼顾精度、速度和成本。
  </Card>

  <Card title="便捷获取" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrow-up.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2c1e1940f6d55086f84c6054cc093fac)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    灵活获取解析结果（完整下载链接或纯文本），方便后续大模型处理或二次加工。
  </Card>
</CardGroup>

## 产品定位

> 在多格式文件解析与内容抽取场景中，为大模型、知识管理系统、业务应用提供高精度、高可用、低成本的底层能力支持。

<Tabs>
  <Tab title="大模型前置解析">
    将PDF、Word、PPT等复杂文档解析为结构化文本或Markdown，减少手工清洗，直接作为大模型输入，提升问答与推理效果。

    **典型应用：** 智能问答系统、文档对话、内容生成等。
  </Tab>

  <Tab title="知识库构建管理">
    批量解析并标准化企业海量文档，形成结构化知识库，支持全文检索、语义搜索、知识问答等。

    **典型应用：** 企业内部知识管理、客服知识库、行业垂直知识图谱。
  </Tab>

  <Tab title="OCR识别及扫描件处理">
    对扫描版合同、财务报表、试卷、票据等非可编辑文件进行高精度识别，支持版面还原和图片提取。

    **典型应用：** 合同归档、档案数字化、试卷批改系统。
  </Tab>

  <Tab title="行业垂直解决方案">
    针对行业特定文档类型，提供高适配解析能力：

    * **教育行业：** 试题、讲义、教材解析入库
    * **金融行业：** 财报、招股书、研究报告结构化处理
    * **法律与合同管理：** 合同、协议、法律文书精确提取条款和内容
    * **出版与媒体：** 图文混排杂志、论文、新闻稿数字化处理
  </Tab>
</Tabs>

## 能力支持

<CardGroup cols={2}>
  <Card title="多样化解析能力整合" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/cubes.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=68f7e70811d7c842eb5b9d34c8ce53ec)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    一套API选择三种解析服务
  </Card>

  <Card title="多格式文件支持" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/images.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=5c7540ca4af57e6640b793cfd531ab54)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    涵盖主流文档及图片格式
  </Card>

  <Card title="多输出方式" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrows-rotate.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2b334fa767b3736a3afc9babb9c6d575)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    • `下载链接`：图片 + Markdown 文件 + 包含布局信息的json文件<br />
    • `纯文本`：适配大模型输入
  </Card>

  <Card title="文件大小灵活支持" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    不同服务最大可支持至 `100M` 文件
  </Card>

  <Card title="下载时效" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/clock.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=01942bdb6d8270b01215f52b5fe64363)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    解析结果下载有效期 `24` 小时
  </Card>
</CardGroup>

## 解析服务对比

### 基础信息对比

<div className="table-container">
  |    服务类型    | 支持格式                                                                                                                                              | 最大文件大小                                                                  | 解析结果                                        | 计费方式                                              |
  | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------- | :------------------------------------------ | :------------------------------------------------ |
  |  **Prime** | pdf,docx,doc,xls<br />xlsx,ppt,pptx,png<br />jpg,jpeg,csv,txt<br />md,html,bmp<br />gif,webp,heic,eps<br />icns,im,pcx,ppm<br />tiff,xbm,heif,jp2 | PDF/DOC/DOCX/PPT ≤100MB<br />XLS/XLSX/CSV ≤10MB<br />PNG/JPG/JPEG ≤20MB | 图片 + Markdown 文件<br />+ 包含布局信息的<br />json文件 | 按解析页数消耗后付费<br />优惠后**0.12元/页**                    |
  | **Expert** | pdf                                                                                                                                               | ≤100M                                                                   | 图片 + Markdown 文件                            | 按页数计费，限时 6 折优惠<br />优惠后**0.012元/页**               |
  |  **Lite**  | pdf,docx,doc,xls<br />xlsx,ppt,pptx,png<br />jpg,jpeg,csv,txt,md                                                                                  | ≤50M                                                                    | 纯文本（无图片）                                    | 按调用次数计费<br />**当前免费**<br /> 2025-10-08 起 0.01 元/次 |
</div>

### 解析耗时

解析时长与文档结构复杂度等因素密切相关，最终耗时以实际解析结果为准。

### 功能对比

<div className="table-container">
  | 服务类型       | 核心优势                                                                                          | 推荐场景                                                                |
  | :--------- | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
  | **Prime**  | - 支持多种复杂版式（双栏、混排、三栏等）<br />- 高精度解析图文、公式、段落、表格、页眉页脚等<br />- 多模态模型，适配复杂排版<br />- 精度表现优异，适合高要求场景 | - 科研出版：学术论文、技术书籍、会议资料<br />- 教育考试：试卷、教材、讲义<br />- 行业文档：合同、行业报告、白皮书  |
  | **Expert** | - PDF、图片适配能力突出<br />- 高精度识别 PDF 表格与公式<br />- 在科研、教辅、企业、财报、标准等多领域表现稳定<br />- 性价比高，适合大规模解析      | - 学术研究：论文、学术报告、专利<br />- 教育出版：教辅书籍、教育资料<br />- 商业金融：年报、财报、研究报告、国家标准 |
  | **Lite**   | - 全格式支持，覆盖常见办公文档<br />- 提供基本结构化解析，速度快<br />- 成本低，适合对版面还原要求不高的任务<br />- 精度表现优异，适合高要求场景         | - 办公场景：标准合同、规章制度、公告<br />- 批量解析：资料归档、文本抽取、快速预处理                     |
</div>

## 使用资源

[接口文档](/api-reference/%E5%B7%A5%E5%85%B7-api/%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90)：API调用方式

**接口使用方法**

1. 调用接口创建解析任务，获取 `task_id`；
2. 保存并记录下 `task_id`；
3. 使用该 `task_id` 轮询查询接口，获取解析结果。

**字段属性**

| 字段名称         | 字段描述                                                                                                                                                        |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file         | 本地待解析文件                                                                                                                                                     |
| tool\_type   | 使用的解析工具类型: `lite, expert, prime`                                                                                                                            |
| file\_type   | 文件类型: `PDF, DOCX, DOC, XLS, XLSX, PPT, PPTX, PNG, JPG, JPEG, CSV, TXT, MD, HTML, EPUB, BMP, GIF, WEBP, HEIC, EPS, ICNS, IM, PCX, PPM, TIFF, XBM, HEIF, JP2` |
| taskId       | 文件解析任务 ID                                                                                                                                                   |
| format\_type | 结果返回格式类型: `text, download_link`                                                                                                                             |

## 调用示例

> 调用示例里面的参数属性参考上方字段属性和对应的 API 文档。

### 创建文件解析任务

<Tabs>
  <Tab title="cURL">
    **创建文件解析任务**

    ```bash theme={null}
    curl --location --request POST 'https://open.bigmodel.cn/api/paas/v4/files/parser/create' \
    --header  'Authorization: Bearer your_api_token' \
    --form 'file=@example-file' \
    --form 'tool_type="prime"' \
    --form 'file_type="PDF"'
    ```

    **异步获取解析结果**

    ```bash theme={null}
    curl --request GET \
    --url https://open.bigmodel.cn/api/paas/v4/files/parser/result/{taskIid}/{format_type} \
    --header 'Authorization: Bearer your_api_token'
    ```
  </Tab>

  <Tab title="Python">
    ```bash theme={null}
    # 安装最新版本
    pip install zai-sdk

    # 或指定版本
    pip install zai-sdk==0.2.2
    ```

    ```python theme={null}
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="your api key")
    # 用于上传发起文件解析任务
    # 返回task_id
    response = client.file_parser.create(file=open('example.pdf', 'rb'), file_type='pdf', tool_type='lite')
    task_id = getattr(response, "task_id", None)

    # 获取文件内容抽取: format_type = text / download_link
    # text模式最长返回1m以内的文本内容，download_link响应更快
    res_response = client.file_parser.content(task_id=task_id, format_type="download_link")

    print(response.json())  # 新版推荐用法
    print(response.content.decode('utf-8')) # 旧版解码字节流用法依然支持
    ```
  </Tab>

  <Tab title="Python(旧)">
    **更新 SDK 至 2.1.5.20250825**

    ```bash theme={null}
    # 安装最新版本
    pip install zhipuai

    # 或指定版本
    pip install zhipuai==2.1.5.20250825
    ```

    ```python theme={null}
    from pathlib import Path
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key="your api key")
    # 用于上传发起文件解析任务
    # 返回task_id
    response = client.file_parser.create(file=open('example.pdf', 'rb'), file_type='pdf', tool_type='lite')
    print(response)

    # 获取文件内容抽取
    response = client.file_parser.content(task_id="your task_id", format_type="text")
    print(response.content.decode('utf-8'))
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

    ```java theme={null}
    import ai.z.openapi.ZhipuAiClient;
    import ai.z.openapi.service.fileparsing.FileParsingDownloadReq;
    import ai.z.openapi.service.fileparsing.FileParsingDownloadResponse;
    import ai.z.openapi.service.fileparsing.FileParsingResponse;
    import ai.z.openapi.service.fileparsing.FileParsingUploadReq;
    import ai.z.openapi.utils.StringUtils;

    public class FileParsingExample {

        public static void main(String[] args) {
            // 初始化客户端
            ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                 .apiKey("your api key")
                 .build();

            try {
                // 示例1: 创建解析任务
                System.out.println("=== 文件解析任务创建示例 ===");
                String filePath = "your file path";
                String taskId = createFileParsingTaskExample(client, filePath, "pdf", "lite");

                // 示例2: 获取解析结果
                System.out.println("\n=== 获取解析结果示例 ===");
                getFileParsingResultExample(client, taskId);

            } catch (Exception e) {
                System.err.println("发生异常: " + e.getMessage());
                e.printStackTrace();
            }
        }

        /**
        * 示例：创建解析任务（上传文件并解析）
        *
        * @param client ZhipuAiClient 实例
        * @return 解析任务的 taskId
        */
        private static String createFileParsingTaskExample(ZhipuAiClient client, String filePath, String fileType, String toolType) {
            if (StringUtils.isEmpty(filePath)) {
                System.err.println("无效的文件路径。");
                return null;
            }
            try {
                FileParsingUploadReq uploadReq = FileParsingUploadReq.builder()
                        .filePath(filePath)
                        .fileType(fileType)  // 支持: pdf, docx 等
                        .toolType(toolType) // 解析工具类型: lite, prime, expert
                        .build();

                System.out.println("正在上传并创建解析任务...");
                FileParsingResponse response = client.fileParsing().createParseTask(uploadReq);
                if (response.isSuccess()) {
                    if (null != response.getData().getTaskId()) {
                        String taskId = response.getData().getTaskId();
                        System.out.println("解析任务创建成功，TaskId: " + taskId);
                        return taskId;
                    } else {
                        System.err.println("解析任务创建失败: " + response.getData().getMessage());
                    }
                } else {
                    System.err.println("解析任务创建失败: " + response.getMsg());
                }
            } catch (Exception e) {
                System.err.println("文件解析任务错误: " + e.getMessage());
            }
            // 返回 null 表示创建失败
            return null;
        }

        /**
        * 示例：获取解析结果
        *
        * @param client ZhipuAiClient 实例
        * @param taskId 解析任务ID
        */
        private static void getFileParsingResultExample(ZhipuAiClient client, String taskId) {
            if (taskId == null || taskId.isEmpty()) {
                System.err.println("无效的任务ID，无法获取解析结果。");
                return;
            }

            try {
                int maxRetry = 100;      // 最多轮询100次
                int intervalMs = 3000;  // 每次间隔3秒
                for (int i = 0; i < maxRetry; i++) {
                    FileParsingDownloadReq downloadReq = FileParsingDownloadReq.builder()
                            .taskId(taskId)
                            .formatType("text")
                            .build();

                    FileParsingDownloadResponse response = client.fileParsing().getParseResult(downloadReq);

                    if (response.isSuccess()) {
                        String status = response.getData().getStatus();
                        System.out.println("当前任务状态: " + status);

                        if ("succeeded".equalsIgnoreCase(status)) {
                            System.out.println("解析结果获取成功！");
                            System.out.println("解析内容: " + response.getData().getContent());
                            System.out.println("内容下载链接: " + response.getData().getParsingResultUrl());
                            return;
                        } else if ("processing".equalsIgnoreCase(status)) {
                            System.out.println("解析进行中，请稍候...");
                            Thread.sleep(intervalMs);
                        } else {
                            System.out.println("解析任务异常，状态: " + status + "，消息: " + response.getData().getMessage());
                            return;
                        }
                    } else {
                        System.err.println("解析结果获取失败: " + response.getMsg());
                        return;
                    }
                }
                System.out.println("等待超时，请稍后自行查询解析结果。");
            } catch (Exception e) {
                System.err.println("获取解析结果时异常: " + e.getMessage());
            }
        }
    }
    ```
  </Tab>

  <Tab title="响应示例">
    **创建文件解析任务响应**

    ```
    {
        "message": "任务创建成功",
        "success": true,
        "task_id": "task_id"
    }
    ```

    **异步获取解析结果响应**

    ```
    {
        "status": "succeeded",
        "message": "结果获取成功",
        "content": "parsed result text",
        "task_id": "your task_id",
        "parsing_result_url": "download url"
    }
    ```
  </Tab>
</Tabs>

## 注意事项

* **文件大小限制：** 避免超出最大支持文件导致解析失败
* **优先选择适合场景的服务：** 复杂文档选择对应服务
* **下载结果后及时保存：** 下载链接24小时后失效
* **如需大模型处理：** 建议直接获取纯文本输出

## 常见问题（FAQ）

**Q1：解析结果能保留原始图片吗？**

A：Prime与Expert支持图片保留（打包下载），Lite服务不保留图片。

**Q2：下载链接失效怎么办？**

A：需重新调用解析API生成新链接。

**Q3：为什么我的复杂PDF解析效果不好？**

A：Lite服务不适合复杂排版和OCR场景，请使用Prime服务或Expert服务。

**Q4：活动价格多久有效？**

A：当前活动为 6折，截止至 2025 年 10 月 8 日，如有变更以平台公告为准。
