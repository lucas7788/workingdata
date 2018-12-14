
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
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//调用者合约地址
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA"//管理员ontid
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```

* Transfer

转移管理员权限

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
        "transfer",//方法名
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//合约地址
        true //执行结果，true表示成功，false表示失败
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```


* AssignFuncsToRole

分配函数到角色

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
        "assignFuncsToRole",//方法名
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//合约地址
        true //执行结果，true表示成功，false表示失败
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```

* AssignOntIDsToRole

分配角色给ontid

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
        "assignOntIDsToRole",//方法名
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//合约地址
        true //执行结果，true表示成功，false表示失败
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```

* Delegate

将权限委托给ontid

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
        "delegate",//方法名
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//合约地址
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //from ontid
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//to ontid
        true //执行结果，true表示成功，false表示失败
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```

* Withdraw

撤回委托的权限

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
        "withdraw",//方法名
        "ea1e2adf8c19f5a7e877860264ebf326e8c3aa5a",//合约地址
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //委托者ontid
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//代理人ontid
        true //执行结果，true表示成功，false表示失败
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//调用者合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//手续费接收地址
        10000000 //支付的手续费数量，精度是9
      ]
    }
  ]
}
```
