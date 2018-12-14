# governance合约

|参数名|参数说明|
|:--|:--|
|TxHash|交易hash|
|State|1表示成功，0表示失败|
|GasConsumed|该交易消耗的手续费|
|Notify|Notify事件|

* RegisterCandidate

注册成为候选人

Notify格式

```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0100000000000000000000000000000000000000",
      "States":[
        "transfer",//方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//from 地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA"// to 地址
        100 //转账的数量
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer",//方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//from 地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA"// to 地址
        100 //转账的数量
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

* UnRegisterCandidate

取消注册

Notify格式

```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
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

* QuitNode

退出节点

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
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

* AuthorizeForPeer

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress":"0100000000000000000000000000000000000000",
      "State":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//from 地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//to 地址
        10000000 //转账的数量
      ]
    },
    {
      "ContractAddress":"0200000000000000000000000000000000000000",
      "State":[
        "transfer", //方法名
        "AFsAKgywkKtrLWoEdWNe8BWRutojP1KEFw",//from 地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//to 地址
        10000000 //转账的数量
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

* UnAuthorizeForPeer

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
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

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0100000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//治理合约地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//用户地址
        10000000 //
      ]
    },
    //withdrawTotalStake
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//治理合约地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//用户地址
        10000000 //
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

* WithdrawOng

提取ong

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0100000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//治理合约地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//用户地址
        1 //
      ]
    },
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV",//ONT合约地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//用户地址
        10000000 //
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

* AddInitPos

增加初始化权益

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0100000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//用户地址
        "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",//治理合约地址
        1000 //
      ]
    },
    //depositTotalStake
    {
      "ContractAddress": "0200000000000000000000000000000000000000",
      "States":[
        "transfer", //方法名
        "AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV",//ONT合约地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//用户地址
        10000000 //
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

* ReduceInitPos

减少初始权益

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
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
