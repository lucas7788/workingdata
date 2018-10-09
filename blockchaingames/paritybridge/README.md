# Parity Bridge

DISCLAIMER: we recommend not using the bridge in "production" (to bridge significant amounts) just yet. it's missing a code audit and should still be considered alpha. we can't rule out that there are bugs that might result in loss of the bridged amounts. we'll update this disclaimer once that changes

parity-bridge is currently an
[ERC20 token](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)
contract on one ethereum-based blockchain that is backed by ether on **another** ethereum-based blockchain.

eventually parity-bridge will be able to pass arbitrary messages between
two ethereum-based blockchains.
in the future you'll be able to build the current ether-ERC20 bridge and any other
cross-chain application on top of the message passing bridge.

currently users can convert ether
on one chain into the same amount of ERC20 tokens on the other and back.
the bridge securely relays these conversions.

**the bridge can mitigate scaling issues:**
by deploying a [proof-of-authority](https://paritytech.github.io/wiki/Proof-of-Authority-Chains.html)
network and bridging it to the Ethereum Foundation network ('mainnet') users can convert their mainnet ether
into ERC20 tokens on the PoA chain
and there transfer them with much lower transaction fees,
faster block times and unaffected by mainnet congestion.

the users can withdraw their tokens worth of ether on the mainnet at any point.

parity is using the bridge project to prototype
the system that will eventually connect ethereum and other non-parachains to
[polkadot](https://polkadot.io/).

### current functionality

the bridge connects two chains `home` and `foreign`.

when users deposit ether into the `HomeBridge` contract on `home`
they get the same amount of ERC20 tokens on `foreign`.

[they can use `ForeignBridge` as they would use any ERC20 token.](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)

to convert their `foreign` ERC20 into ether on `home`
users can always call `ForeignBridge.transferHomeViaRelay(homeRecipientAddress, value, homeGasPrice)`.

`foreign` is assumed to use PoA (proof of authority) consensus.
relays between the chains happen in a byzantine fault tolerant way using the authorities of `foreign`.

### high level explanation of home ether -> foreign ERC20 relay

`sender` deposits `value` into `HomeBridge`.
the `HomeBridge` fallback function emits `Deposit(sender, value)`.

for each `Deposit` event on `HomeBridge` every authority executes
`ForeignBridge.deposit(sender, value, transactionHash)`.

once there are `ForeignBridge.requiredSignatures` such transactions
with identical arguments and from distinct authorities then
`ForeignBridge.balanceOf(sender)` is increased by `value`.

### high level explanation of foreign ERC20 -> home ether relay

`sender` executes `ForeignBridge.transferHomeViaRelay(recipient, value, homeGasPrice)`
which checks and reduces `ForeignBridge.balances(sender)` by `value` and emits `ForeignBridge.Withdraw(recipient, value, homeGasPrice)`.

for every `ForeignBridge.Withdraw`, every bridge authority creates a message containing
`value`, `recipient` and the `transactionHash` of the transaction referenced by the `ForeignBridge.Withdraw` event;
signs that message and executes `ForeignBridge.submitSignature(signature, message)`.
this collection of signatures is on `foreign` because transactions are free for the authorities on `foreign`,
but not free on `home`.

once `ForeignBridge.requiredSignatures` signatures by distinct authorities are collected
a `ForeignBridge.CollectedSignatures(authorityThatSubmittedLastSignature, messageHash)` event is emitted.

everyone (usually `authorityThatSubmittedLastSignature`) can then call `ForeignBridge.message(messageHash)` and
`ForeignBridge.signature(messageHash, 0..requiredSignatures)`
to look up the message and signatures and execute `HomeBridge.withdraw(vs, rs, ss, message)`
and complete the withdraw.

`HomeBridge.withdraw(vs, rs, ss, message)` recovers the addresses from the signatures,
checks that enough authorities in its authority list have signed and
finally transfers `value` ether ([minus the relay gas costs](#recipient-pays-relay-cost-to-relaying-authority))
to `recipient`.

### deposit
![deposit](https://github.com/lucas7788/parity-bridge/blob/master/res/deposit.png)
### withdraw
![deposit](https://github.com/lucas7788/parity-bridge/blob/master/res/withdraw.png)
