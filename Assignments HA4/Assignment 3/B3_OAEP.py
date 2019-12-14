from hashlib import sha1
from math import ceil
from binascii import hexlify
import sys


def i2osp(x, xlen):
    if x >= 256**xlen:
        print("integer too large")
        sys.exit()

    return bytearray.fromhex(hex(x).lstrip('0x').zfill(2 * xlen))


def mgf1(seed, mask_len):
    t = ''
    for i in range(ceil(mask_len / 20)):
        c = i2osp(i, 4)
        t += sha1(seed + c).hexdigest()

    return t[:2*mask_len]


def OAEP_encode(message, seed):
    h_len = len(message)
    l_hash = sha1(b'').digest()
    ps = bytearray(128 - h_len - 40 - 2)
    db = l_hash + ps + b'\x01' + message
    db_mask = bytearray.fromhex(mgf1(seed, 128 - h_len - 1))
    masked_db = bytes(a ^ b for a, b in zip(db, db_mask))
    seed_mask = bytearray.fromhex(mgf1(masked_db, h_len))
    masked_seed = bytes(a ^ b for a, b in zip(seed, seed_mask))
    em = b"\x00" + masked_seed + masked_db
    return em


print(mgf1(bytearray.fromhex("0123456789abcdef"), 30))
em = OAEP_encode(bytearray.fromhex("fd5507e917ecbe833878"), bytearray.fromhex("1e652ec152d0bfcd65190ffc604c0933d0423381"))
print(hexlify(em).decode())
