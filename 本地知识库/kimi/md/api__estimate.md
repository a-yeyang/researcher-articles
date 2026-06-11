<!-- source: https://platform.kimi.com/docs/api/estimate -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 计算 Token

> 估算给定消息和模型所需的 Token 数量。输入结构与聊天补全几乎相同。

estimate-token-count 的输入结构体和 chat completion 基本一致。

<Accordion title="纯文本调用示例">
  ```bash theme={null}
  curl 'https://api.moonshot.cn/v1/tokenizers/estimate-token-count' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $MOONSHOT_API_KEY" \
    -d '{
      "model": "kimi-k2.6",
      "messages": [
          {
              "role": "system",
              "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
          },
          {
              "role": "user",
              "content": "你好，我叫李雷，1+1等于多少？"
          }
      ]
  }'
  ```
</Accordion>

<Accordion title="包含视觉的调用示例">
  ```python theme={null}
  import os
  import base64
  import json
  import requests

  api_key = os.environ.get("MOONSHOT_API_KEY")
  endpoint = "https://api.moonshot.cn/v1/tokenizers/estimate-token-count"
  image_path = "image.png"

  with open(image_path, "rb") as f:
      image_data = f.read()

  # 我们使用标准库 base64.b64encode 函数将图片编码成 base64 格式的 image_url
  image_url = f"data:image/{os.path.splitext(image_path)[1].lstrip('.')};base64,{base64.b64encode(image_data).decode('utf-8')}"

  payload = {
      "model": "kimi-k2.6",
      "messages": [
          {
              "role": "system",
              "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": image_url,
                      },
                  },
                  {
                      "type": "text",
                      "text": "请描述图片的内容。",
                  },
              ],
          }
      ]
  }

  response = requests.post(
      endpoint,
      headers={
          "Authorization": f"Bearer {api_key}",
          "Content-Type": "application/json"
      },
      data=json.dumps(payload)
  )

  print(response.json())
  ```
</Accordion>

当没有 error 字段，可以取 `data.total_tokens` 作为计算结果。


## OpenAPI

````yaml POST /v1/tokenizers/estimate-token-count
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
  /v1/tokenizers/estimate-token-count:
    post:
      tags:
        - Utilities
      summary: 估算 Token 数量
      description: 估算给定消息和模型所需的 Token 数量。输入结构与聊天补全几乎相同。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EstimateTokenRequest'
      responses:
        '200':
          description: Token 数量估算结果
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EstimateTokenResponse'
        '400':
          description: 请求错误 - 参数无效
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失
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
    EstimateTokenRequest:
      type: object
      properties:
        model:
          type: string
          description: 模型 ID
          default: kimi-k2.5
          enum:
            - kimi-k2.6
            - kimi-k2.5
            - kimi-k2-0905-preview
            - kimi-k2-0711-preview
            - kimi-k2-turbo-preview
            - moonshot-v1-8k
            - moonshot-v1-32k
            - moonshot-v1-128k
            - moonshot-v1-auto
            - moonshot-v1-8k-vision-preview
            - moonshot-v1-32k-vision-preview
            - moonshot-v1-128k-vision-preview
        messages:
          type: array
          description: >-
            包含迄今为止对话的消息列表。每个元素格式为 {"role": "user", "content": "你好"}。role 支持
            system、user、assistant 其一，content 不得为空
          items:
            $ref: '#/components/schemas/Message'
      required:
        - model
        - messages
    EstimateTokenResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            total_tokens:
              type: integer
              description: 估算的总 Token 数量
              example: 80
          required:
            - total_tokens
      required:
        - data
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
    Message:
      type: object
      properties:
        role:
          type: string
          enum:
            - system
            - user
            - assistant
          description: 消息发送者的角色
        content:
          oneOf:
            - type: string
            - type: array
              items:
                oneOf:
                  - title: text
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - text
                      text:
                        type: string
                    required:
                      - type
                      - text
                  - title: image_url
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - image_url
                      image_url:
                        oneOf:
                          - type: object
                            properties:
                              url:
                                type: string
                            required:
                              - url
                          - type: string
                    required:
                      - type
                      - image_url
                  - title: video_url
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - video_url
                      video_url:
                        oneOf:
                          - type: object
                            properties:
                              url:
                                type: string
                            required:
                              - url
                          - type: string
                    required:
                      - type
                      - video_url
          description: 消息内容。可以是纯文本字符串，也可以是包含 text/image_url/video_url 类型的对象数组（用于多模态输入）
        name:
          type: string
          default: null
          description: 消息发送者的名称（可选）
        partial:
          type: boolean
          default: false
          description: 在最后一条 assistant 消息中设置为 true 以启用 Partial Mode
      required:
        - role
        - content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````