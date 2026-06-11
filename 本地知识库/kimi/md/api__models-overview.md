<!-- source: https://platform.kimi.com/docs/api/models-overview -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 模型参数参考

export const DocTable = ({columns = [], rows = []}) => {
  return <div className="doc-table-wrap">
      <table className="doc-table">
        {columns.length > 0 ? <colgroup>
            {columns.map((column, index) => <col key={index} style={column.width ? {
    width: column.width
  } : undefined} />)}
          </colgroup> : null}
        <thead>
          <tr>
            {columns.map((column, index) => <th key={index}>{column.title}</th>)}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIndex) => <tr key={rowIndex}>
              {row.map((cell, cellIndex) => <td key={cellIndex}>{cell}</td>)}
            </tr>)}
        </tbody>
      </table>
    </div>;
};

不同模型系列对 Chat Completions API 参数有不同的默认值和约束。完整的模型列表请参阅[模型列表](/models)。

## 参数对比

<DocTable
  columns={[
{ title: "参数", width: "30%" },
{ title: "kimi-k2.6", width: "35%" },
{ title: "moonshot-v1 系列", width: "35%" },
]}
  rows={[
[<code>temperature</code>, <strong>不可修改</strong>, "0.0"],
[<code>top_p</code>, <>0.95 <strong>不可改</strong></>, "1.0"],
[<code>n</code>, <>1 <strong>不可改</strong></>, "1（最大 5）"],
[<code>presence_penalty</code>, <>0 <strong>不可改</strong></>, "0（可修改）"],
[<code>frequency_penalty</code>, <>0 <strong>不可改</strong></>, "0（可修改）"],
[<code>thinking</code>, "支持", "—"],
]}
/>

<Note>
  当 `temperature` 接近 0 时，`n` 只能为 1，否则将返回 `invalid_request_error`。
</Note>

## Kimi K2.6 — thinking 参数

Kimi K2.6 支持通过 `thinking` 参数控制是否启用深度思考。接受 `{"type": "enabled"}` 或 `{"type": "disabled"}`。

由于 OpenAI SDK 没有原生的 `thinking` 参数，需要使用 `extra_body` 传递：

<CodeGroup>
  ```python Python theme={null}
  completion = client.chat.completions.create(
      model="kimi-k2.6",
      messages=[
          {"role": "user", "content": "你好"}
      ],
      extra_body={
          "thinking": {"type": "disabled"}
      },
      max_tokens=1024*32,
  )
  ```

  ```bash cURL theme={null}
  curl https://api.moonshot.cn/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $MOONSHOT_API_KEY" \
    -d '{
      "model": "kimi-k2.6",
      "messages": [
        {"role": "user", "content": "你好"}
      ],
      "thinking": {"type": "disabled"}
    }'
  ```
</CodeGroup>
