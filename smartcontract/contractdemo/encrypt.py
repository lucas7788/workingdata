from boa.builtins import sha1, sha256, hash160, hash256


def Main(operation, args):
    sha1("123456789")
    sha256("123456789")
    hash160("123456789")
    hash256("123456789")
