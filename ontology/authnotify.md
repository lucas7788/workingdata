
# auth合约

|参数名|参数说明|
|:--|:--|
|TxHash|交易hash|
|State|1表示成功，0表示失败|
|GasConsumed|该交易消耗的手续费|
|Notify|Notify事件|

* InitContractAdmin

初始化管理员信息

Notify格式

```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0600000000000000000000000000000000000000",
      "States":[
        "initContractAdmin",//方法名
        "调用者地址",
        "管理员ontid"
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "方法名",
        "调用者地址",
        "手续费接收地址",
        "数量"
      ]
    }
  ]
}
```

* Transfer

转移管理员权限

Notify格式

```json
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0600000000000000000000000000000000000000",
      "States":[
        "方法名",
        "合约地址",
        "成功或失败"
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "方法名",
        "调用者地址",
        "手续费接收地址",
        "数量"
      ]
    }
  ]
}
```
