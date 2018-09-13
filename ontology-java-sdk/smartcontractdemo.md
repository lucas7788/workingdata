## 智能合约调用demo

测试合约源代码见下面附件
测试合约的功能是：对相同的账户在两个不同的nep5合约中同时进行转账操作。
举例说明：部署nep5合约A和合约B，某一账户S在合约A中的余额是1000Atoken，在合约B中的余额是2000Bboken,
则测试合约可以实现账户S将100Atoken和100Btoken同时转给账户S2,

操作步骤是：
1. 部署合约Atoken和合约Btoken

```
ontSdk.vm().setCodeAddress(Address.AddressFromVmCode(code).toHexString());
Transaction tx = ontSdk.vm().makeDeployCodeTransaction(code, true, "name",
        "v1.0", "author", "email", "desp", account.getAddressU160().toBase58(),20600000,0);
ontSdk.signTx(tx, new Account[][]{{account}});
String txHex = Helper.toHexString(tx.toArray());
Object result = ontSdk.getConnect().syncSendRawTransaction(txHex);
System.out.println(result);
```

2. 执行测试合约中的SetContractHash方法，保存Atoken合约hash和Btoken的合约hash，通过key-value的形式进行保存，由于测试合约在通过Atoken的合约hash调用转账方法时，需要反转后的合约hash，
所以在执行SetContractHash时要对Atoken的合约hash进行反转。

javasdk调用合约示例代码：
```
Account account999 = new Account(Helper.hexToBytes(privatekey),SignatureScheme.SHA256WITHECDSA);
AbiInfo abiinfo = JSON.parseObject(swapAbi, AbiInfo.class);
String name = "SetContractHash";
AbiFunction func = abiinfo.getFunction(name);
func.setParamsValue("Atoken", Helper.reverse(Address.parse(AtokenContractHash).toArray()));//合约hash反转
boolean preExec = false;
Object obj =  ontSdk.neovm().sendTransaction(Helper.reverse(TestContractHash),adminAcct,adminAcct,20000,0,func, preExec);
System.out.println(obj);
Thread.sleep(6000);
System.out.println(ontSdk.getConnect().getSmartCodeEvent((String)obj));
```
3. 执行GetContractHash查询第一步是否执行成功，并且查看结果是不是反转后的合约hash。
javasdk调用合约示例代码：
```
AbiInfo abiinfo = JSON.parseObject(swapAbi, AbiInfo.class);
String name = "GetContractHash";
AbiFunction func = abiinfo.getFunction(name);
func.setParamsValue("Atoken");
boolean preExec = true;
Object obj =  ontSdk.neovm().sendTransaction(Helper.reverse(swapAddress2),null,null,20000,0,func, preExec);
System.out.println(obj);
```
4. 执行Transfer方法

```
String functionName = "Transfer";
//构造参数  请参考
List list = new ArrayList();
List list2 = new ArrayList();
list2.add("Atoken");
list2.add(100);
list.add(list2);
List list3 = new ArrayList();
list3.add("Btoken");
list3.add(100);
list.add(list3);

List list1 = new ArrayList();
list1.add(account.getAddressU160().toArray());//发送方
list1.add(Address.decodeBase58("AacHGsQVbTtbvSWkqZfvdKePLS6K659dgp").toArray());//接收方
list1.add(list);

List listF = new ArrayList<Object>();
listF.add(functionName.getBytes());
listF.add(list1);
byte[] params = BuildParams.createCodeParamsScript(listF);
Transaction tx = ontSdk.vm().makeInvokeCodeTransaction(Helper.reverse(contractHash),null,params,account3.getAddressU160().toBase58(),20000,0);
ontSdk.signTx(tx,new Account[][]{{account999}});
ontSdk.addSign(tx,account3);
System.out.println(tx.hash().toHexString());
ontSdk.getConnect().sendRawTransaction(tx);
Thread.sleep(6000);
System.out.println(ontSdk.getConnect().getSmartCodeEvent(tx.hash().toHexString()));
```
