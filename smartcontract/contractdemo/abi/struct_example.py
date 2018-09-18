from boa.interop.System.Runtime import Notify, Serialize, Deserialize


def Main(operation, args):
    if operation == "StructTest":
        return StructTest()
def StructTest():
    a = ["bob", 20]
    p = a
    Notify(p[0])
    Notify(p[1])
    b = Serialize(p)
    p2 = Deserialize(b)
    Notify(p2[0])
    Notify(p2[1])
    arr = {list("bob1", 21), list("bob2", 22)}
    return True
