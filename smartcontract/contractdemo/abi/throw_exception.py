from boa.interop.System.Runtime import CheckWitness, Notify
from boa.builtins import concat
from boa.interop.System.Storage import Delete, Put, Get, GetContext

ctx = GetContext()
TRANSFER_PREFIX = bytearray(b'\x01')
APPROVE_PREFIX = bytearray(b'\x02 ')


def Main(operation, args):
    if operation == "transferMulti":
        return TransferMulti(args)
    return False


def TransferMulti(args: list):
    for p in (args):
        if len(p) != 3:
            return False
        if Transfer(p[0], p[1], p[2]) == False:
            raise Exception("Transfer failed.")
        return True


def Transfer(from_acct,to_acct,amount):

    if from_acct == to_acct:
        return True
    if amount == 0:
        return True
    if amount < 0 :
        return False
    if  CheckWitness(from_acct) == False:
        return False
    if len(to_acct) != 20:
        return False
    fromKey = concat(TRANSFER_PREFIX,from_acct)
    fromBalance = Get(ctx, fromKey)
    if fromBalance < amount:
        return False
    if fromBalance == amount:
        Delete(ctx,fromKey)
    else:
        Put(ctx, fromKey, fromBalance - amount)

    tokey = concat(TRANSFER_PREFIX, to_acct)
    toBalance = Get(ctx, tokey)

    Put(ctx, tokey, toBalance + amount)
    Notify(['transfer',from_acct,to_acct,amount])
    return True
