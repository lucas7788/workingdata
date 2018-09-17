# 合约代码概览

合约源代码请参考
https://github.com/lucas7788/fomo3d_clone

## 代码框架图
![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/fomo3d/contractuml.png)

通过上图，我们可以分析出：

* 1. 整个FoMo3D涉及8个合约的部署。具体就是图中标注出颜色的合约。蓝色指的是能看到代码的合约。红色的合约暂时还没看到代码。

* 2. Interface的大量使用，去拆解合约。通过传入合约地址的方式，实现合约的互调

* 3. FoMo3Dlong是主合约，玩家下注买key就是调用这个合约的接口操作。

* 4. PlayBook主要负责玩家数据的管理，特别是推广员系统，主要在这里面

* 5. TeamJust用作合约的权限控制，类似于以太猫的CEO，COO，CFO。具体原理后续在展开

* 6. Divies负责跟以前P3D的合约通信，把部分游戏的收益，返给P3D的持有者。从这里也可以看出以太坊作为游戏平台的魅力所在，可以把不同游戏的数据天然地打通。游戏与游戏之间不是生灭关系，能相互促进。
