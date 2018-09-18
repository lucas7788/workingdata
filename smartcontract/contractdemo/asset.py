from boa.interop.Ontology.Native import Invoke

OntContract = "AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV".ToScriptHash()
OngContract = "AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ".ToScriptHash()


def Main(operation, args):
    if operation == "RecycleAsset":
        return RecycleAsset()


def RecycleAsset(from_acct: bytearray, to_acct: bytearray, ont: int, ong: int):
    ret = bytearray()
    transfer = state(from_acct, to_acct, ont)
    ret = Invoke(0, OntContract, "transfer", [transfer])
    if ret != b'\x01':
        raise Exception("tansfer ont error.")
    transfer = state(from_acct, to_acct, ong)
    ret = Invoke(0, OngContract, "transfer", [transfer])
    if ret != b'\x01':
        raise Exception("tansfer ont error.")
    return True