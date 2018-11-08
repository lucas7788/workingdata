# punica-ts测试
## 问题1
文档中没有说明安装punica-ts 对npm版本的要求

## 问题2
文档中没有说明源码编译安装的操作步骤

##问题3
文档中没有说明安装失败的解决方案

##问题4
punica invoke 没有list子命令

##问题5
punica invoke --function functionName 执行成功
punica-ts invoke --function functionName 执行失败

失败截图：
![avatar](./pic/question5.jpg)
default-config配置截图
![avatar](./pic/question5a.jpg)

##问题6
asset transfer 交易 只打出了交易hash 没说明交易是否成功
![avatar](./pic/asset_transfer.jpg)

## 问题7
punica-ts wallet asset withdrawOng
必须指定钱包文件
![avatar](./pic/asset_withdrawOng.jpg)

## 问题8
punica-ts wallet ontid delete
提示信息有误
![avatar](./pic/ontid_delete.jpg)
执行报错
![avatar](./pic/ontid_delete2.jpg)

## 问题9
punica-ts unbox
提示信息有误
![avatar](./pic/unbox.jpg)

## 问题10
提示信息有误
![avatar](./pic/deploy.jpg)

# punica-ts wallet account 测试结果

## punica-ts asset

![avatar](./pic/account_add.jpg)

![avatar](./pic/account_list.jpg)

![avatar](./pic/account_delete.jpg)

![avatar](./pic/account_import.jpg)

## punica-ts wallet asset
![avatar](./pic/asset_balanceOf.jpg)
![avatar](./pic/asset_unbound.jpg)

## punica-ts wallet ontid

![avatar](./pic/ontid_list.jpg)

![avatar](./pic/ontid_add.jpg)

## punica-ts init

![avatar](./pic/init.jpg)

## punica-ts unbox --box_name tutorialToken

![avatar](./pic/unbox.jpg)

## punica-ts compile

![avatar](./pic/compile.jpg)

## punica-ts compile

![avatar](./pic/smartx.jpg)
