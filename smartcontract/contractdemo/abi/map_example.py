
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash
from boa.interop.System.Runtime import Notify, Serialize, Deserialize
from boa.interop.System.Storage import GetContext, Put, Get

ctx = GetContext()
selfAddr = GetExecutingScriptHash()


def Main(operation, args):
    m = dict()
    m["k1"] = 100
    m["k2"] = 200
    Notify(m["k1"])
    Notify(m["k2"])
    b = Serialize(m)
    Put(ctx, "mapexample", b)

    v = Get(ctx, "mapexample")
    m2 = Deserialize(v)
    Notify(m2["k1"])
    Notify(m2["k2"])


