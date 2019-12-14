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
    l_hash = bytearray.fromhex(sha1(b'').hexdigest())
    ps = bytearray(128 - h_len - 40 - 2)
    db = l_hash + ps + b'\x01' + bytearray.fromhex(message)
    db_mask = bytearray.fromhex(mgf1(seed, 128 - h_len - 1))
    masked_db = bytes(a ^ b for a, b in zip(db, db_mask))
    seed_mask = bytearray.fromhex(mgf1(masked_db, h_len))
    masked_seed = bytes(a ^ b for a, b in zip(seed, seed_mask))
    em = b"\x00" + masked_seed + masked_db
    return em

print(mgf1("0123456789abcdef", 30))
print(OAEP_encode("fd5507e917ecbe833878", "1e652ec152d0bfcd65190ffc604c0933d0423381"))
