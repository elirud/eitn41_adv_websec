from hashlib import sha1
from math import ceil
import sys


def i2osp(x, xlen):
    if x >= 256**xlen:
        print("integer too large")
        sys.exit()

    return hex(x).lstrip('0x').zfill(2 * xlen)


def mgf1(seed, mask_len):
    t = ''
    for i in range(ceil(mask_len / 20)):
        c = i2osp(i, 4)
        t += sha1(bytearray.fromhex(seed + c)).hexdigest()

    return t[:2*mask_len]

print(mgf1("0123456789abcdef", 30))