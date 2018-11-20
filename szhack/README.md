# 2018年11月17号，深圳马拉松开发者问题整理

1. cyyano chrome下载不了，
直接从github上下载release版本，windows 和mac 安装没有提供解决方法。

2. smartx run, 配置参数太麻烦，每次替换要执行的函数，都需要重新配置参数。

3. smartx, test 界面，add account功能，使用私钥添加，但是不知道怎么获得私钥

4. 开发者对钱包有惯性思维，不是很清楚ontid的概念。不知道ontid可以做啥。

7. crynao mac上偶尔会出现卡死的情况

8. smartx number是正序的应该改成反序

9. solo chain 在Windows平台不稳定

10. TSSDK访问ontology本地节点的问题

新建了rpcclient,无法访问getblockcount, getblockheight等API

11. smartx访问本地节点，IP地址不要端口号的，几乎所有的开发者都会遇到这个问题

12. dApi 存在 chrome is not defined 的错误

13. smartx 编译的pyhton合约和c#合约  生成的abi文件结构不一样。python合约编译生成的abi文件abi对应的值少了hash，和entryentrypoint
