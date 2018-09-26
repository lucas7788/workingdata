# 以太坊调研报告

* [1. 以太坊基本信息](#1.以太坊基本信息)
* [2. 以太坊dapp开发工具](#2.以太坊dapp开发工具)
   * [2.1 以太坊开发工具](#2.1以太坊开发工具)
   * [2.2 Truffle框架](#2.2Truffle框架)
   * [2.3 Embark框架](#2.3Embark框架)
* [3. 以太坊dapp](#3.以太坊dapp)
* [4. 总结](#4.总结)
* [5. 参考链接](#5.参考链接)

## 1.以太坊基本信息

* 项目git仓库地址: https://github.com/ethereum/go-ethereum
* 官方实现以太坊协议实现语言: golang
* 共识算法: casper （POW+POS）
* 性能: 每秒20笔
* 治理模型:
* Star人数: 20710
* Fork人数: 7094
* contributors人数: 330
* releases版本数:139
* 支持的客户端: go语言实现的Mist客户端，C++语言实现的Alethzero客户端, Python语言开发的Pythereum，Nodejs开发的Node-Ethereum，Java语言开发的Ethereumj
* 智能合约开发语言: solidity

以下结果来自以太坊社区调查报告:
全球开发者分布:
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/developer.png)
北美洲占43%，欧洲占40%，亚洲占10%，大洋洲占5%，南美洲占2%
* 以太坊社区透明度:良好
* 以太坊财务透明度:良好
* 以太坊在社会中的实际应用是否明确:较为明确
* 以太坊开发进度:以太坊开发者会及时公布开发进度（通过写博客或者交流的方式）

## 2. 以太坊dapp开发工具

### 2.1 以太坊开发工具

* Mist Mist的功能包括保存以太币、发送交易、部署合约等。你可以用它实现与区块链平台或测试网络
的交互。当你需要进行快速交易时超级有用
* Geth Geth除了实现Mist的全部功能，还包含一些额外的重要特性，例如提供RPC API接口给应用程序以便你的应用可以通过它连接如以太坊网络。
* Parity Parity是一个用Rust开发的以太坊节点软件，开发者是前以太坊CTO：Gavin Wood博士。Parity 的特点就是速度块、轻量化。Parity 还在本机的8080 端口提供了一个Web界面供你访问。
* MetaMask Chrome浏览器插件可以极大简化对你的DApp（去中心化应用：Decentralized Application）的访问
* Web3.js  Web3.js是web应用和区块链交互的桥梁
* Truffle 提供了快速创建、编译、部署和测试区块链应用的构建模块
* Solc 是以太坊智能合约编译器，可以把合约代码编译成以太坊字节码
* Solium solidity代码静态分析器，可以帮助开发者规范代码并发现安全隐患
* ether.camp 微软提供的在线全功能solidity集成开发环境
* BlockApps BlockApps提供了一些简洁的API来帮助你查看钱包余额、编写交易、读取合约状态等
* Embark Embark是另一个流行的开发框架，帮你轻松地构建、测试和部署DApp
* Zeppelin Zeppelin库用来编写安全的合约(类似于Java中的jar包，在合约中可以引入智能合约语言开发的工具库)

#### Mist介绍
Mist 主界面
1. 账户概览

2. 浏览器

3. 钱包

4. 合约信息

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/Mist1.jpg)

Mist 开发界面：
1. 集成了remix IDE开发工具
2. 可以显示日志文件
3. 以太坊节点
4. 网络配置等信息

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/Mist2.png)

Mist 浏览器界面：(ontology的owallet还没有该功能)

1. 提供dapp活跃度排名信息

2. dapp分类信息查询

3. 提供统计数据

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/Mist3.png)


#### parity介绍

parity主界面

该界面主要展示了parity支持的功能

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/parity1.png)

节点信息界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/parity2.png)

dapp 浏览器界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/parity3.png)

web3 console界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/paritycli.png)

交易队列界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/paritytxqueue.png)


#### MetaMask介绍

metamask 主界面
1. 网络配置 (ontology 的chrome插件把这部分放到了设置里面)
2. 账户地址
3. 余额信息
4. 交易记录

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/metamask2.jpg)

metamask add Token界面

该部分会显示用户的ERC20Token余额信息

目前ontology的chrome插件还不支持该功能

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/metamask.png)

metamask 点击交易记录跳转的页面
以太坊浏览器查询界面，交易记录显示的很详细，

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/metamask3.jpg)

#### OpenZeppelin库介绍

OpenZeppelin 项目结构图：

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/zeppelin.jpg)

### 2.2 Truffle框架

Truffle是一个世界级的开发环境，测试框架，以太坊的资源管理通道，致力于让以太坊上的开发变得简单，Truffle有以下特点：
* 内置的智能合约编译，链接，部署和二进制文件的管理
* 快速开发下的自动合约测试
* 脚本化的，可扩展的部署与发布框架
* 部署到不同的公网或私网的网络环境管理功能
* 使用EthPM&NPM提供的包管理，使用ERC190标准
* 与合约直接通信的直接交互控制台（写完合约就可以命令行里验证了）
* 可配的构建流程，支持紧密集成

下面数据来自git

|角度|人气|
|:--|:--|
|fork人数|926|
|star人数|6990|
|Watch人数|336|
|contributors人数|77|
|release数|102|
|commits|3283|

truflle dapp项目结构图：
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/truffle2.jpg)

`contracts` 文件夹存放的是项目合约文件

`migrations` 文件夹存放的是部署合约的js文件

`test` 文件夹存放的是合约的测试文件

`truffle.js` 用于配置以太坊节点网络

`truffle-config.js` 用于配置truffle配置

`client`文件夹用来存放js文件和网页文件等，支持流行的reactjs等

#### truffle客户端

适用于开发的客户端:
* EtherumJS TestRPC 当开发基于Truffle的应用时，我们推荐使用EthereumJS TestRPC。它是一个完整的在内存中的区块链仅仅存在于你开发的设备上。它在执行交易时是实时返回，而不等待默认的出块时间，这样你可以快速验证你新写的代码，当出现错误时，也能即时反馈给你。它同时还是一个支持自动化测试的功能强大的客户端。Truffle充分利用它的特性，能将测试运行时间提速近90%。
testrpc 一键式启动节点服务：
```
$ testrpc
```
testrpc 运行界面图：

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/testrpc.jpg)

适用于正式发布的客户端:
* Geth (go-ethereum)
* WebThree(cpp-ethereum)

#### ganache（ontology目前没有这样的工具）

Ganache是一个运行在个人桌面上的以太坊开发者的个人区块链。Ganache是Truffle Suite的一部分，通过把合约和交易放到前面来简化dapp的开发。通过使用Ganache，你可以快速的看到你的应用是如何影响区块链的。其中细节：如你的账户、余额、合约及Gas成本。你也可以调整Ganache的采矿控制来更好的适用你的应用。

ganache 主界面

可以看到账户地址，余额，交易数，以及以太坊网络的基本信息

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/ganache1.jpg)

ganache Blocks界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/ganache2.png)

ganache logs界面

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/ganache3.png)

详情请见：

https://truffleframework.com/ganache

#### box
Truffle 的盒子Boxs装有很多非常实用的项目样板，可以让你忽略一些环境配置问题，从而可以集中与开发你自己的DApp的业务唯一性。除此之外，Truffle Boxes能够容纳其他有用的组件、Solidity合约或者库，前后端视图等等。所有这些都是一个完整的实例Dapp程序。都可以下载下来逐一研究，寻找适合自己公司目前业务模型的组件。

truffle box案例：

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/truffle1.jpg)

### drizzle
Drizzle是前端库的集合，使得编写dapp前端更容易，更可预测。 Drizzle的核心是基于Redux商店，因此您可以访问Redux周围的壮观开发工具。 我们负责同步您的合同数据，交易数据等。
* drizzle 基于Redux store（前端的状态管理工具），可以很方便的同步合约中的数据、交易数据等
* 封装web3，可以方便的使用web3中的方法
* 方便和reducers、sagas集成
* 封装流行的js库例如reactjs，方便合约数据的展示

详情请见：
https://github.com/trufflesuite/drizzle

### 2.3 Embark框架
Embark 让开发者开发和部署以太坊dapp更容易，Embark当前集成了EVM区块链、去中心化存储IPFS、去中心化通信平台（Whisper和Orbit），支持swarm部署。
Embark框架链接 https://github.com/embark-framework/embark

下面数据来自git

|角度|人气|
|:--|:--|
|fork人数|344|
|star人数|2375|
|Watch人数|141|
|contributors人数|45|
|release数|92|
|commits|3587|

Embark框架特点

区块链（Ethereum）:

* 自动化的部署合约，方便js代码中调用。Embark可以自动监听合约的变化并重新部署变化后的合约。
* 合约可以通过js的promise调用
* 使用Javascript使用合约进行测试驱动开发。
* 追踪已经部署的合约，当合约更新的时候，会自动更新
* 管理不同链(testnet、private net,livenet)
* 轻松管理相互依赖合同的复杂系统

去中心化存储（IPFS）:

* 通过EmbarkJS轻松存储和检索DApp上的数据。 包括上传和检索文件。
* 将完整的应用程序部署到IPFS或Swarm。
去中心化通信（Whisper, Orbit）:
* 通过Whisper或Orbit轻松通过P2P渠道发送/接收消息。

web 技术:

* 与任何网络技术集成，包括React，Foundation等。
* 使用您想要的任何构建管道或工具，包括grunt，gulp和webpack。

embark 提供的图形化界面
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/dashboard.jpg)

### 2.4 智能合约IDE

Remix IDE：
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/remix.jpg)

* 左边一列是用文件夹的形式组织合约代码
* 中间一列是合约源代码
* 右边一列提供合约代码的编译、部署、运行、分析、调试等功能

## 3. 以太坊dapp
### 以太坊dapp基本信息
* dapp总数: 775，游戏类411,占比54%，竞猜类共152个，占比20%，交易市场占比4%，其他占比22%
* dapp占比图
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/ethereum/dapp.jpg)
* 累计交易笔数: 3亿
* 累计交易金额: 59亿ETH
* 用户数: 3587万人
* 日均活跃人数: 20万人

### dapp分类
* 游戏类: 以太小精灵，加密猫，
* 交易市场类: IDEX,Delta,Bancor,PoWH 3D
* 竞猜类: Fomo3D，FairDapp, Zethr
* 其他: Kyber,Ox协议，Livepeer,以太坊域名服务

### 比较火的dapp
#### 加密猫（游戏类）

应用原理：非同质代币ERC721标准(目前ontology还不支持)
另外还有非同质代币ERC875标准该标准支持一次买卖中只需要一次交易，也就只需要支付一次gas(通过magiclink的方式，实现了原子交易)
网址：https://www.cryptokitties.co/

#### 以德交易所（交易市场类）
基于以太坊的去中心化的交易所
实现数字资产的托管、交易、撮合、结算一体化功能
网址：https://etherdelta.com/

#### Fomo3D (竞猜类)

基于以太坊的乐透游戏，合约代码逻辑公开，没有人能够控制游戏的进程

网址 https://exitscam.me/

#### Bancor协议Token

oep4和nep5的缺点
1. 流通性不好（上交易所不容易）
2. 有割韭菜跑路的可能
3. 有庄家控盘的可能

Bancor Token
1. 连续的流动性，不需要买房和卖方
2. 即时调整价格，算法自动调整价格
3. 价格可预测，价格公式透明，
4. 无spread, 也就是不需要传统的做市商，使参与者收益

## 4. 总结

### 社区活跃度问题
ontology代码贡献者仅有42人，没有激发社区开发的力量参与进来，
dapp开发工具也需要社区的力量来推动

### ontology dapp开发工具问题

建议推出一个类似于truffle的dapp开发框架，最好拥有的功能是：
1. 有效的组织js、html、合约代码
2. 最好有类似于embark的图形化界面，实时监测合约状态，当合约代码有变动的时候能够自动化部署，并且方便和链交互
3. dapp开发框架集成目前比较流行的js框架 比如：reactjs,vue.js等
4. 应该提供dapp项目数据存储解决方案，IPFS或者数据库等
5. 应该多提供dapp 案例demo，可以通过社区开发者的力量贡献demo

### ontology chrome 钱包问题

目前的ontology chrome插件还不支持Token余额功能，以及Token交易记录查询等

### one blockchain 工具

ontology 缺少像testrpc 和 ganache这样的启动链的工具，终端形式或者图形化界面

### 智能合约开发
智能合约IDE：
目前smartx的功能还是比较有限
1. smartx报错 余额不够问题（亟待解决）
2. smartx debug功能（亟待解决）
3. smartx 可以增加类似于remix的代码分析功能
4. 建议集成通信功能(开发者通信或者数据交换功能)

智能合约相关的库类似于Zeppelin功能

## 5. 参考：
https://github.com/ethereum

http://www.wanbizu.com/xinbi/201503284872.html

https://www.jianshu.com/p/53fcdd255ef7
