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
    h_len = 20
    l_hash = sha1(b'').digest()
    ps = bytearray(128 - len(message) - 2 * h_len - 2)
    db = l_hash + ps + b'\x01' + message
    db_mask = bytearray.fromhex(mgf1(seed, 128 - h_len - 1))
    masked_db = bytes(a ^ b for a, b in zip(db, db_mask))
    seed_mask = bytearray.fromhex(mgf1(masked_db, h_len))
    masked_seed = bytes(a ^ b for a, b in zip(seed, seed_mask))
    em = b'\x00' + masked_seed + masked_db
    return em


def OAEP_decode(em):
    l_hash = sha1(b'').digest()
    y = em[0]
    masked_seed = em[1:21]
    masked_db = em[21:128]
    seed_mask = bytearray.fromhex(mgf1(masked_db, 20))
    seed = bytes(a ^ b for a, b in zip(masked_seed, seed_mask))
    db_mask = bytearray.fromhex(mgf1(seed, 107))
    db = bytes(a ^ b for a, b in zip(masked_db, db_mask))
    m = db[db.index(b'\x01', 21) + 1:]
    return m


print(mgf1(bytearray.fromhex("9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214"), 21))
em = OAEP_encode(bytearray.fromhex("c107782954829b34dc531c14b40e9ea482578f988b719497aa0687"), bytearray.fromhex("1e652ec152d0bfcd65190ffc604c0933d0423381"))
print("EM:", hexlify(em).decode())
m = OAEP_decode(bytearray.fromhex("0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f"))
print("M: ", hexlify(m).decode())

