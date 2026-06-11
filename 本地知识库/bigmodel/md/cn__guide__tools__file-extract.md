<!-- source: https://docs.bigmodel.cn/cn/guide/tools/file-extract -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# (旧)文件内容抽取

> 从文件中提取文本信息，可用于文件问答等 AI 服务。文件管理请参考文件 API。

## 接口请求

* **传输方式**: `https`
* **请求地址**: `https://open.bigmodel.cn/api/paas/v4/files/{file_id}/content`
* **调用方式**:  同步调用，等待返回结果
* **字符编码**: `UTF-8`
* **请求格式**: `JSON`
* **响应格式**: `JSON`
* **接口请求类型**: `GET`

详细调用方法请参考：

<Card title=" 文件 API 文档" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", WebkitMaskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"} />} href="/api-reference/%E6%96%87%E4%BB%B6-api/%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9" />

<Tab title="Python SDK(旧)">
  **安装 SDK**

  ```bash theme={null}
  # 安装最新版本
  pip install zhipuai

  # 或指定版本
  pip install zhipuai==2.1.5.20250726
  ```

  **验证安装**

  ```python theme={null}
  import zhipuai
  print(zhipuai.__version__)
  ```

  **使用示例**

  ```python theme={null}
  from pathlib import Path
  from zhipuai import ZhipuAI

  client = ZhipuAI(
     api_key="您的 API Key",
     base_url="https://open.bigmodel.cn/api/paas/v4"
  )
  # 用于上传文件
  # 格式限制：PDF、DOCX、DOC、XLS、XLSX、PPT、PPTX、PNG、JPG、JPEG、CSV
  # 文件大小不超过 50M，图片大小不超过 5M、总数限制为 100 个文件
  file_object = client.files.create(file=Path("本地文件地址"), purpose="file-extract")

  # 文件内容抽取
  file_content = client.files.content(file_id=file_object.id).content.decode()
  print(file_content)
  ```

  **响应示例**

  ```json theme={null}
  {
      "content": "文档内容",
      "file_type": "application/pdf",
      "filename": "文档名称.pdf",
      "title": "",
      "type": "file"
  }
  ```
</Tab>
