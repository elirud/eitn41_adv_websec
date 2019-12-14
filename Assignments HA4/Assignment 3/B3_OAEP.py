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


def OAEP_encode(message, seed):
    h_len = int(len(message)/2)
    l_hash = bytearray.fromhex(sha1('').hexdigest())
    ps = bytearray(128 - h_len - 40 - 2)
    db = l_hash + ps + b'\x01' + bytearray.fromhex(message)
    db_mask = bytearray.fromhex(mgf1(seed, 128 - h_len - 1))
    masked_db =
    masked_seed = bin(int(seed, 16)) ^

print(mgf1("0123456789abcdef", 30))
