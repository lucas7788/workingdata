# ontid 合约

|参数名|参数说明|
|:--|:--|
|TxHash|交易hash|
|State|1表示成功，0表示失败|
|GasConsumed|该交易消耗的手续费|
|Notify|Notify事件|

* regIdWithPublicKey

注册ontid

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Register",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA" //注册ontid
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

* addKey

添加公钥

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "PublicKey",
        "add",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //ontid
        "022a06f7a4bfff93d9bbe31dfd70dbfb08263f1ea15db2ee9556688314e20e9dd7",//添加的公钥
        2, //公钥个数
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


* removeKey

删除公钥

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "PublicKey",
        "remove",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //ontid
        2, //公钥索引
        "022a06f7a4bfff93d9bbe31dfd70dbfb08263f1ea15db2ee9556688314e20e9dd7" //添加的公钥
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

* addRecovery

添加recovery地址

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Recovery",
        "add",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //ontid
        "d7239affb684c3c224476eb7bd52d9b2cb5e2aab" //recovery 地址
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

* changeRecovery

改变recovery地址

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Recovery",
        "change",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA", //ontid
        "d7239affb684c3c224476eb7bd52d9b2cb5e2aab" //recovery 地址
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

* regIDWithAttributes

注册ontid 附带属性信息

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Register",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA" //ontid
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

* addAttributes

添加属性

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Attribute",
        "add",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA" //ontid
        ["",""] //属性中的key字段的值
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

* removeAttribute

删除属性

Notify格式
```
{
  "TxHash":"",
  "State":1,
  "GasConsumed":10000000,
  "Notify":[
    {
      "ContractAddress": "0300000000000000000000000000000000000000",
      "States":[
        "Attribute",
        "remove",//方法名
        "did:ont:AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA" //ontid
        "", //属性中的key字段的值
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
