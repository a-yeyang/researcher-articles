<!-- source: https://platform.kimi.com/docs/pricing/limits -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 充值与限速

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

为了整体资源分配的公平性，同时防止恶意攻击，我们目前将基于账户的累计充值金额进行速率限制，具体如下表，如有更高需求请填写[提升速率表单](https://platform.kimi.com/contact-sales)：

<DocTable
  columns={[
{ title: "用户等级", width: "14%" },
{ title: "累计充值金额", width: "18%" },
{ title: "并发", width: "12%" },
{ title: "RPM", width: "12%" },
{ title: "TPM", width: "22%" },
{ title: "TPD", width: "22%" },
]}
  rows={[
["Tier0", "¥ 0", "1", "3", "500,000", "1,500,000"],
["Tier1", "¥ 50", "50", "200", "2,000,000", "Unlimited"],
["Tier2", "¥ 100", "100", "500", "3,000,000", "Unlimited"],
["Tier3", "¥ 500", "200", "5,000", "3,000,000", "Unlimited"],
["Tier4", "¥ 5,000", "400", "5,000", "4,000,000", "Unlimited"],
["Tier5", "¥ 20,000", "1,000", "10,000", "5,000,000", "Unlimited"],
]}
/>

## 限速概念解释

* 并发: 同一时间内我们最多处理的来自您的请求数
* RPM: requests per minute 指一分钟内您最多向我们发起的请求数
* TPM: tokens per minute 指一分钟内您最多和我们交互的token数
* TPD: tokens per day 指一天内您最多和我们交互的token数

其他细节请参考[速率限制](/introduction#速率限制)一节。

## 为什么要做限速？

速率限制是API接口的常见做法，主要有以下几个考量：

* 有助于防止滥用或误用API。例如，恶意行为者可能会通过大量请求来淹没API，试图使其过载或导致服务中断。通过设置速率限制，我们可以防范这样的行为。
* 速率限制有助于确保每个人都能公平地访问API。如果一个人或组织发出过多的请求，可能会拖慢所有人的API。通过限制单个用户可以发出的请求数量，那么尽可能多的人有机会使用API而不会遇到速度减慢的问题。
* 速率限制可以帮助我们管理集群总负载。如果对API的请求急剧增加，可能会给服务器带来压力并导致性能问题。通过设置速率限制将可以帮助为所有用户维护一个平稳且一致的体验。

## 特别说明

* 我们将全力保障用户的正常使用，但当集群负载达到容量上限时，我们可能会采取临时的限流措施，对各类限速进行调整。
* 代金券不计入累计充值总额
