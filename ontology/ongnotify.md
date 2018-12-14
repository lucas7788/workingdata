# ong合约

* Transfer

转账

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
        "transfer",//方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//from地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//to地址
        100 //转账金额
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

* TransferFrom

从另一个地址把钱转到指定的地址

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
        "transfer",//方法名
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//from地址
        "AbPRaepcpBAFHz9zCj4619qch4Aq5hJARA",//to地址
        100 //转账金额
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
