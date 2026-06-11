<!-- source: https://platform.kimi.com/docs/api/files-delete -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除文件

> 删除一个已上传的文件。

<Accordion title="调用示例">
  ```python theme={null}
  client.files.delete(file_id=file_id)
  ```
</Accordion>


## OpenAPI

````yaml DELETE /v1/files/{file_id}
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
    delete:
      tags:
        - Files
      summary: 删除文件
      description: 删除一个已上传的文件。
      parameters:
        - name: file_id
          in: path
          required: true
          description: 文件标识符
          schema:
            type: string
      responses:
        '200':
          description: 删除结果
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileDeleteResponse'
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
    FileDeleteResponse:
      type: object
      properties:
        id:
          type: string
          description: 已删除文件的标识符
        object:
          type: string
          example: file
        deleted:
          type: boolean
          description: 文件是否删除成功
      required:
        - id
        - object
        - deleted
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