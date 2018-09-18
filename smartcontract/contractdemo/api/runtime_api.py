
from boa.interop.System.Runtime import Notify, CheckWitness, Log, GetTime


def Main(operation, args):
    Notify(GetTime())
    user = bytearray([248, 142, 51, 220, 214, 177, 110, 235, 27, 218, 59, 86, 23, 47, 140, 20, 114, 119, 159, 152])
    CheckWitness(user)
    Notify("Hi BlockChain")
    Notify("s1", "s2", 1, 2, 3)
    Log("log message")