from boa.interop.Ontology import Contract


def Main(operation, args):
    if operation == "Destroy":
        return DestroyContract()
    if operation == "Migrate":
        code = args[0]
        return Migrate(code)


def DestroyContract():
    Contract.Destroy()
    return True


def Migrate(code):
    Contract.Migrate(code, True, "", "", "", "", "")
    return True