<!-- source: https://platform.kimi.com/docs/api/files-content -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取文件内容

> 获取以 `file-extract` 用途上传的文件的提取文本内容。

<Accordion title="调用示例">
  <Tabs>
    <Tab title="python">
      ```python theme={null}
      # 注意，之前 retrieve_content api 在最新版本标记了 warning, 可以用下面这行代替
      # 如果是旧版本，可以用 retrieve_content
      file_content = client.files.content(file_id=file_object.id).text
      ```
    </Tab>

    <Tab title="curl">
      ```bash theme={null}
      curl https://api.moonshot.cn/v1/files/{file_id}/content \
        -H "Authorization: Bearer $MOONSHOT_API_KEY"
      ```
    </Tab>
  </Tabs>
</Accordion>


## OpenAPI

````yaml GET /v1/files/{file_id}/content
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
  /v1/files/{file_id}/content:
    get:
      tags:
        - Files
      summary: 获取文件内容
      description: 获取以 `file-extract` 用途上传的文件的提取文本内容。
      parameters:
        - name: file_id
          in: path
          required: true
          description: 文件标识符
          schema:
            type: string
      responses:
        '200':
          description: 提取的文件内容
          content:
            text/plain:
              schema:
                type: string
                description: 提取的文件内容（纯文本）
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