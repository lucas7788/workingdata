from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, GetContext, Get, Delete

ctx = GetContext()


def Main(operation, args):
    if operation == "Test":
        return Test()


def Test():
    Put(ctx, "key", 100)
    v = Get(ctx, "key")
    Notify(v)

    Put(ctx, "key", "100")
    v = Get(ctx, "key")
    Notify(v)

    Delete(ctx, "key")
    Notify(Get(ctx, "key"))