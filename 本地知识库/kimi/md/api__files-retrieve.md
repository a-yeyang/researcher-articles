<!-- source: https://platform.kimi.com/docs/api/files-retrieve -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取文件信息

> 获取指定已上传文件的元数据。

<Accordion title="调用示例">
  ```python theme={null}
  client.files.retrieve(file_id=file_id)
  # FileObject(
  #     id='clg681objj8g9m7n4je0',
  #     bytes=761790,
  #     created_at=1700815879,
  #     filename='xlnet.pdf',
  #     object='file',
  #     purpose='file-extract',
  #     status='ok', status_details='')
  ```
</Accordion>


## OpenAPI

````yaml GET /v1/files/{file_id}
openapi: 3.1.0
info:
  title: Moonshot AI API
  version: 1.0.0
  description: Moonshot AI / Kimi 大语言模型服务 API
servers:
  - url: https://api.moonshot.cn
    description: 生产环境
security: []
paths:
  /v1/files/{file_id}:
    get:
      tags:
        - Files
      summary: 获取文件信息
      description: 获取指定已上传文件的元数据。
      parameters:
        - name: file_id
          in: path
          required: true
          description: 文件标识符
          schema:
            type: string
      responses:
        '200':
          description: 文件元数据
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileObject'
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: 文件未找到
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: 服务器错误
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - bearerAuth: []
components:
  schemas:
    FileObject:
      type: object
      properties:
        id:
          type: string
          description: 文件唯一标识符
        object:
          type: string
          description: 对象类型
          example: file
        bytes:
          type: integer
          description: 文件大小（字节）
        created_at:
          type: integer
          description: 文件创建时的 Unix 时间戳
        filename:
          type: string
          description: 原始文件名
        purpose:
          type: string
          description: >-
            上传文件时指定的用途。file-extract：抽取文件内容；image：上传图片，用于视觉理解；video：上传视频，用于视频理解；batch：上传
            JSONL 文件，用于批处理任务
          enum:
            - file-extract
            - image
            - video
            - batch
        status:
          type: string
          description: 文件处理状态
          example: ready
        status_details:
          type: string
          description: 处理失败或返回警告时的额外状态详情
      required:
        - id
        - object
        - bytes
        - created_at
        - filename
        - purpose
        - status
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              description: 描述错误原因的错误消息
            type:
              type: string
              description: 错误类型
            code:
              type: string
              description: 错误码
          required:
            - message
      required:
        - error
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````