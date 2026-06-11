<!-- source: https://api-docs.deepseek.com/zh-cn/api/get-user-balance -->

* API 文档
* 其它
* 查询余额

# 查询余额

```
GET

## /user/balance
```

查询账号余额

## Responses[​](#responses "Responses的直接链接")

* 200

OK, 返回用户余额详情

* application/json

* Schema
* Example (from schema)
* Example

**Schema**

**is\_available** boolean

当前账户是否有余额可供 API 调用

**balance\_infos**

object[]

* Array [

**currency** string

**Possible values:** [`CNY`, `USD`]

货币，人民币或美元

**total\_balance** string

总的可用余额，包括赠金和充值余额

**granted\_balance** string

未过期的赠金余额

**topped\_up\_balance** string

充值余额

* ]

```
{  
  "is_available": true,  
  "balance_infos": [  
    {  
      "currency": "CNY",  
      "total_balance": "110.00",  
      "granted_balance": "10.00",  
      "topped_up_balance": "100.00"  
    }  
  ]  
}
```

```
{  
  "is_available": true,  
  "balance_infos": [  
    {  
      "currency": "CNY",  
      "total_balance": "110.00",  
      "granted_balance": "10.00",  
      "topped_up_balance": "100.00"  
    }  
  ]  
}
```

Loading...