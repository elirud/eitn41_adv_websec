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

def bxor(b1, b2): # use xor for bytes
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return result

def OAEP_encode(message, seed):
    h_len = int(len(message)/2)
    l_hash = bytearray.fromhex(sha1('').hexdigest())
    ps = bytearray(128 - h_len - 40 - 2)
    db = l_hash + ps + b'\x01' + bytearray.fromhex(message)
    db_mask = bytearray.fromhex(mgf1(seed, 128 - h_len - 1))
    masked_db = bxor(db, db_mask)
    seedMask = mgf1(masked_db, h_len)
    masked_seed = bxor(bytearray.fromhex(seed) , seedMask)
    EM = "0x00" + str(masked_seed).lstrip('0x') + str(masked_db).lstrip('0x')

print(mgf1("0123456789abcdef", 30))
