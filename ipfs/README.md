# IPFS

* [ipfs介绍](ipfs介绍)
* [ipfs安装](ipfs安装)
* [ipfs使用](ipfs使用)
* [ipfs搭建私网](ipfs搭建私网)

## ipfs介绍

IPFS（InterPlanetary File System）是一个点对点的分布式超媒体分发协议，它整合了过去几年最好的分布式系统思路，为所有人提供全球统一的可寻址空间，包括Git、自证明文件系统SFS、BitTorrent和DHT，同时也被认为是最有可能取代HTTP的新一代互联网协议。

IPFS用基于内容的寻址替代传统的基于域名的寻址，用户不需要关心服务器的位置，不用考虑文件存储的名字和路径。我们将一个文件放到IPFS节点中，将会得到基于其内容计算出的唯一加密哈希值。哈希值直接反映文件的内容，哪怕只修改1比特，哈希值也会完全不同。当IPFS被请求一个文件哈希时，它会使用一个分布式哈希表找到文件所在的节点，取回文件并验证文件数据。

IPFS是通用目的的基础架构，基本没有存储上的限制。大文件会被切分成小的分块，下载的时候可以从多个服务器同时获取。IPFS的网络是不固定的、细粒度的、分布式的网络，可以很好的适应内容分发网络的要求。这样的设计可以很好的共享各类数据，包括图像、视频流、分布式数据库、整个操作系统、模块链、8英寸软盘的备份，还有静态网站。

IPFS提供了一个友好的WEB访问接口，用户可通过 http://ipfs.io/hash  获取IPFS网络中的内容，也许在不久的将来，IPFS协议将会彻底替代传统的HTTP协议。

## ipfs 安装

[ipfs git地址](https://github.com/ipfs)

* System Requirements
IPFS can run on most Linux, macOS, and Windows systems. We recommend running it on a machine with at least 2 GB of RAM (it’ll do fine with only one CPU core), but it should run fine with as little as 1 GB of RAM. On systems with less memory, it may not be completely stable.

[go-ipfs下载地址](https://github.com/ipfs/go-ipfs/releases)

## ipfs使用

1. ipfs 基本命令

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfs1.jpg)

2. 在本地建立一个IPFS节点
```
ipfs init
```

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfsinit.jpg)

3. 启动ipfs服务
```
ipfs daemon
```
![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfs2.jpg)

4. 查看节点信息
```
ipfs id
```
![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfs3.jpg)

5. ipfs跨域资源共享CORS配置

当使用ipfs上传数据添加的时候，会发生拒绝访问的错误，必须要进行跨域的配置才可以。

先关掉ipfs服务，然后进行如下配置

mac进行跨域配置的命令
```
localhost:ipfs-http-demo yuechunli$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "GET", "POST", "OPTIONS"]'

localhost:ipfs-http-demo yuechunli$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'

localhost:ipfs-http-demo yuechunli$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Credentials '["true"]'

localhost:ipfs-http-demo yuechunli$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Headers '["Authorization"]'

localhost:ipfs-http-demo yuechunli$ ipfs config --json API.HTTPHeaders.Access-Control-Expose-Headers '["Location"]'
```

windows进行跨域配置的命令
```
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods "[\"PUT\", \"GET\", \"POST\", \"OPTIONS\"]"

ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin "[\"*\"]"

ipfs config --json API.HTTPHeaders.Access-Control-Allow-Credentials "[\"true\"]"

ipfs config --json API.HTTPHeaders.Access-Control-Allow-Headers "[\"Authorization\"]"

ipfs config --json API.HTTPHeaders.Access-Control-Expose-Headers "[\"Location\"]"
```
6. 跨域配置好后，启动ipfs
```
ipfs daemon
```
然后点击 http://localhost:5001/webui 查看官方ipfs webui例子

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfszhuye.jpg)

7. 使用ipfs新增文件
```
ipfs add file.txt
```

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfsadd.jpg)

ipfs 查看新增加的文件
```
ipfs cat 文件hash
```

在网页看文件内容
```
http://localhost:8080/ipfs/文件hash
```

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfsadd2.jpg)

8. ipns

什么是ipns呢，ipns又有什么作用呢。我们应该知道，本地通过ipfs daemon创建的节点是唯一的，但是我们的文件只要内容改变了就会产生不同的hash，ipns的作用就是将内容和本地的节点绑定，这样更新内容的时候我们就可以绑定本地节点，然后通过ipns+本地的节点来访问网站了，网站的网址也不用随着文件内容改变而改变了 那么怎么绑定：

```
ipfs name publish 你的上传的文件的hash
```
在网页中访问的方法
```
http://localhost:8080/ipns/节点id/
```

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfsns.jpg)

由于节点id是唯一的，如何实现多个保留多个这样的映射

其实ipns的映射关系除了节点ID<->文件内容，还有一种是key<->文件内容
![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfskey.jpg)

可以看到，节点默认具有一个名为self的key，它的值正是节点ID。

而在ipfs name publish命令的完整形式是
```
ipfs name publish [--resolve=false] [--lifetime=<lifetime> | -t] [--ttl=<ttl>] [--key=<key> | -k] [--] <ipfs-path>
```
注意其中的key，如果不带这个参数，那么久表示使用默认的key,　也就是节点ID。

可以使用`ipfs key gen`创建新的key，这里创建一个名为another的key

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfskey2.jpg)

尝试用新的key，映射一个ipfs文件内容
![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfskey3.jpg)

通过网页访问
![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfsns3.jpg)

## ipfs搭建私网
1. ipfs初始化
```
ipfs init
```
执行完成后会生成.ipfs的文件夹

2. 生成共享key
因为我们要组建的是私有网络，所有节点需要使用相同的私有key来加入网络中，我们使用go-ipfs-swarm-key-gen工具来生成共享key
```
#编译工具
go get github.com/Kubuxu/go-ipfs-swarm-key-gen
cd $GOPATH
cd src/github.com/Kubuxu/go-ipfs-swarm-key-gen/ipfs-swarm-key-gen/
go build
# 生成key
./ipfs-swarm-key-gen > /root/.ipfs/swarm.key
```

将生成的swarm.key拷贝到另一台机器的.ipfs目录

注意： 私网的所有节点的.ipfs文件夹下面都要拷贝一份swarm.key
3. 移除默认的boostrap节点
```
# ipfs bootstrap rm --all
```

4. 启动服务
首先启动一个节点
```
ipfs daemon
```
我们的私有网络中已经有了第一个ipfs节点，现在需要将第二个节点加入网络中，在启动第二个节点的服务前，需要先将第一个启动节点的信息作为作为第二个节点的boostrap的信息

```
# 添加boostrap信息
ipfs bootstrap add /ip4/192.168.1.63/tcp/4001/ipfs/QmTks2mpdcTJnaLLtjGkyqPWxuMy6WvZbDzkG6XTGRfYA3

# 然后启动该节点
ipfs daemon
```

![avatar](https://github.com/lucas7788/workingdata/blob/master/ipfs/picture/ipfssiwang.jpg)

至此私网搭建成功

4 测试
在其中一个节点上添加文件到ipfs网络,会产生文件id
```
ipfs add file.txt
```

在另一个节点上查询
```
ipfs cat 文件id
```
