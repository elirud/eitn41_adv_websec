from hashlib import sha1


def i20sp(x, xlen):
    return str(int(x, 256)).zfill(xlen)


