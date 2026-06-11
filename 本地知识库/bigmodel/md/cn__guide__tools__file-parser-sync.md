<!-- source: https://docs.bigmodel.cn/cn/guide/tools/file-parser-sync -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 新文件同步解析服务

## 产品简介

<Tip>
  文件解析服务能力升级：解析效果与 Prime 持平，速度更快，支持同步调用，用户可灵活选择，更高效、更全面！
</Tip>

**概述**：

智谱同步解析接口提供“一次请求即返回结果”的文件解析能力，支持多格式文档文本/表格/图片/版面结构识别，并输出纯文本或下载链接（图片+Markdown+布局JSON）。
支持多种复杂版式（双栏、混排、三栏等）

* 高精度解析图文、公式、段落、表格、页眉页脚等
* 适配复杂排版
* 精度表现优异，适合高解析要求

**适用场景**：

* 需要低延迟、即时拿到解析结果的在线处理链路（如用户上传后立刻问答、预览）。
* 单次文件不大、结构复杂度适中，或对纯文本抽取需求为主。

**不适用或建议改用异步的场景**：

* 超大文件、极复杂版面、并发量高且可后台处理的批量任务。此时建议使用 [异步接口](file-parser) ：创建任务 → 保存task\_id → 轮询查询结果。

<div className="table-container">
  |      服务类型      | 支持格式                                                                                                                                                        | 最大文件大小                                                                        | 解析结果                                                  | 计费方式                           |
  | :------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :---------------------------------------------------- | :----------------------------- |
  | **Prime-sync** | wps,pdf,doc,docx,<br />ppt,pptx,md,txt,<br />xls,xlsx,csv,html,<br />png,jpg,jpeg,bmp,<br />gif,webp,heic,eps,<br />icns,im,pcx,ppm,<br />tiff,xbm,heif,jp2 | WPS/PDF/DOC/DOCX/PPT/PPTX ≤100MB<br />MD/TXT/XLS/XLSX/CSV ≤10MB<br />其他 ≤20MB | 下载链接（图片 + Markdown 文件<br />+ 包含布局信息的<br />json文件）；纯文本 | 按解析页数消耗后付费<br />优惠后**0.12元/页** |
</div>

**字段属性**

| 字段名称       | 字段描述                                                                                                                            |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------ |
| file       | 本地待解析文件                                                                                                                         |
| tool\_type | 使用的解析工具类型: `prime-sync`                                                                                                         |
| file\_type | 文件类型: `WPS、PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、HTML、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2` |
| taskId     | 文件解析任务 ID                                                                                                                       |

## 调用示例

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl --location --request POST 'https://open.bigmodel.cn/api/paas/v4/files/parser/sync' \
    --header  'Authorization: Bearer your_api_token' \
    --form 'file=@example-file' \
    --form 'tool_type="prime-sync"' \
    --form 'file_type="PDF"'
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

    def file_parser_sync_example():
        """
        示例：提交文件解析任务并等待结果返回。
        """
        # 创建解析任务
        # 请修改为本地文件路径
        file_path = 'your file path'
        with open(file_path, 'rb') as f:
            print("正在提交文件解析任务 ...")
            response = client.file_parser.create_sync(
                file=f,
                file_type="pdf",
                tool_type="prime-sync",
            )
            print("任务创建成功，响应如下：")
            print(response)

        print("File parser demo completed.")

    if __name__ == "__main__":
        print("=== 文件同步解析快速演示（仅限 Prime） ===\n")
        file_parser_sync_example()
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
      import ai.z.openapi.service.fileparsing.FileParsingDownloadResponse;
      import ai.z.openapi.service.fileparsing.FileParsingUploadReq;
      import ai.z.openapi.utils.StringUtils;

      public class FileParsingSyncExample {

          public static void main(String[] args) {
              // 初始化客户端
              ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                  .apiKey("your api key")
                  .build();

              try {
                  System.out.println("=== 示例：创建文件解析任务 ===");

                  String filePath = "your file path";
                  FileParsingDownloadResponse result = syncFileParsingTaskExample(client, filePath, "pdf", "prime-sync");

                  System.out.println("解析任务创建成功，TaskId: " + result.getData().getTaskId());
                  System.out.println("文件内容: " + result.getData().getContent());
                  System.out.println("下载链接: " + result.getData().getParsingResultUrl());

              } catch (Exception e) {
                  System.err.println("发生异常: " + e.getMessage());
                  e.printStackTrace();
              }
          }

          /**
          * 示例方法：创建解析任务（上传文件并进行解析）
          *
          * @param client ZhipuAiClient 实例
          * @return 解析任务的 taskId
          */
          private static FileParsingDownloadResponse syncFileParsingTaskExample(ZhipuAiClient client, String filePath, String fileType, String toolType) {
              if (StringUtils.isEmpty(filePath)) {
                  System.err.println("文件路径无效。");
                  return null;
              }
              try {
                  FileParsingUploadReq uploadReq = FileParsingUploadReq.builder()
                          .filePath(filePath)
                          .fileType(fileType)  // 支持类型：pdf、docx 等
                          .toolType(toolType)  // 解析工具类型只支持：prime-sync
                          .build();

                  System.out.println("上传文件并创建解析任务...");
                  return client.fileParsing().syncParse(uploadReq);
              } catch (Exception e) {
                  System.err.println("文件解析任务出错: " + e.getMessage());
              }
              // 返回 null 表示任务创建失败
              return null;
          }


      }
    ```
  </Tab>

  <Tab title="响应示例">
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
