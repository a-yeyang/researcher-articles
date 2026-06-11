<!-- source: https://platform.kimi.com/docs/api/list-models -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出模型

> 列出当前可用的所有模型。

列出当前可用的所有模型。


## OpenAPI

````yaml GET /v1/models
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
  /v1/models:
    get:
      tags:
        - Models
      summary: 列出模型
      description: 列出当前可用的所有模型。
      responses:
        '200':
          description: 模型列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    example: list
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: 模型 ID
                          example: kimi-k2.5
                        object:
                          type: string
                          example: model
                        created:
                          type: integer
                          description: 创建时间戳
                        owned_by:
                          type: string
                          example: moonshot
                        context_length:
                          type: integer
                          description: 最大上下文长度（tokens）
                        supports_image_in:
                          type: boolean
                          description: 是否支持图片输入
                        supports_video_in:
                          type: boolean
                          description: 是否支持视频输入
                        supports_reasoning:
                          type: boolean
                          description: 是否支持深度思考
        '401':
          description: 未授权 - API 密钥无效或缺失
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