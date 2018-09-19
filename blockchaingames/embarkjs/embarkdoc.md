# Embark framework 调研报告

# 用法

1. 创建dapp
```
embark demo
```

2. 启动以太坊节点
```
embark blockchain
```
或者

启动以太坊模拟器
```
embark simulator
```

3. 启动dapp
```
embark run
```

4. embark提供界面功能

![avatar](https://github.com/lucas7788/workingdata/blob/master/blockchaingames/embarkjs/dashboard.jpg)

The dashboard will tell you the state of your contracts, the enviroment you are using, and what embark is doing at the moment.

* available services

Available Services will display the services available to your dapp in green, if one of these is down then it will be displayed in red.

* logs and console
There is a console at the bottom which can be used to interact with contracts or with embark itself. type help to see a list of available commands, more commands will be added with each version of Embark.

5. 创建一个干净的dapp
```
embark new AppName
```
项目目录结构
```
app/
  |___ contracts/ #solidity smart contracts
  |___ html/
  |___ css/
  |___ js/
config/
  |___ blockchain.json #rpc and blockchain configuration
  |___ contracts.json  #ethereum contracts configuration
  |___ storage.json  #ipfs configuration
  |___ communication.json  #whisper/orbit configuration
  |___ webserver.json  #dev webserver configuration
test/
  |___ #contracts tests
```

6. embark支持 自动化部署合约

7. 配置IPFS

```
{
  "default": {
    "enabled": true,
    "ipfs_bin": "ipfs",
    "provider": "ipfs",
    "available_providers": ["ipfs"],
    "host": "localhost",
    "port": 5001
  },
  "development": {
    "enabled": true,
    "provider": "ipfs",
    "host": "localhost",
    "port": 5001
  }
}
```

8. 提供Embarkjs
EmbarkJS is a javascript library meant to abstract and facilitate the development of DApps.
* promise

```
var myContract = new EmbarkJS.Contract({abi: abiObject, address: "0x123"});
myContract.get().then(function(value) { console.log("value is " + value.toNumber()) });
```

* deployment
```
SimpleStorage.deploy([args], {options}).then(function(anotherSimpleStorage) {});
```

* Storage
```
EmbarkJS.Storage.setProvider('ipfs',{server: 'localhost', port: '5001'})
```

* Communication(Whisper, Orbit)
initialization
```
EmbarkJS.Messages.setProvider('whisper')
```
listening to messages
```
EmbarkJS.Messages.listenTo({topic: ["topic1", "topic2"]}).then(function(message) { console.log("received: " + message); })
```
* sending messages
```
EmbarkJS.Messages.sendMessage({topic: "sometopic", data: 'hello world'})
```

9. Testing Ethereum Contracts
You can run specs with `embark test`, it will run any test files under `test/`.

Embark includes a testing lib to fastly run & test your contracts in a EVM.
```
# test/simple_storage_spec.js

var assert = require('assert');
var Embark = require('embark');
var EmbarkSpec = Embark.initTests();
var web3 = EmbarkSpec.web3;

describe("SimpleStorage", function() {
  before(function(done) {
    var contractsConfig = {
      "SimpleStorage": {
        args: [100]
      }
    };
    EmbarkSpec.deployAll(contractsConfig, done);
  });

  it("should set constructor value", function(done) {
    SimpleStorage.storedData(function(err, result) {
      assert.equal(result.toNumber(), 100);
      done();
    });
  });

  it("set storage value", function(done) {
    SimpleStorage.set(150, function() {
      SimpleStorage.get(function(err, result) {
        assert.equal(result.toNumber(), 150);
        done();
      });
    });
  });

});
```

10. Working with different chains
You can specify which environment to deploy to:
```
embark blockchain livenet
```

```
# config/blockchain.json
  ...
   "livenet": {
    "networkType": "livenet",
    "rpcHost": "localhost",
    "rpcPort": 8545,
    "rpcCorsDomain": "http://localhost:8000",
    "account": {
      "password": "config/livenet/password"
    }
  },
  ...
```

11. Structuring Application

Embark is quite flexible and you can configure you’re own directory structure using `embark.json`
```
# embark.json
{
  "contracts": ["app/contracts/**"],
  "app": {
    "css/app.css": ["app/css/**"],
    "images/": ["app/images/**"],
    "js/app.js": ["embark.js", "app/js/**"],
    "index.html": "app/index.html"
  },
  "buildDir": "dist/",
  "config": "config/",
  "plugins": {}
}
```

12. Deploying to IPFS

To deploy a dapp to IPFS, all you need to do is run a local IPFS node and then run embark upload ipfs. If you want to deploy to the livenet then after configuring you account on config/blockchain.json on the livenet environment then you can deploy to that chain by specifying the environment embark ipfs livenet.

13. Deploying to SWARM
To deploy a dapp to SWARM, all you need to do is run a local SWARM node and then run embark upload swarm

14. Extending functionality with plugins
* To add a plugin to embark:

1. Add the npm package to package.json e.g npm install embark-babel --save
2. Then add the package to plugins: in embark.json e.g "plugins": { "embark-babel": {} }

* Creating a plugin:
1. mkdir yourpluginname
2. cd yourpluginname
3. npm init
4. create and edit index.js
5. add the following code:
```
module.exports = function(embark) {
}
```

The embark object then provides an api to extend different functionality of embark.

14. Using Embark with Grunt

# 参考链接：
https://embark.readthedocs.io/en/2.6.6/usage.html
