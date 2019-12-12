from hashlib import sha1
from math import ceil
import sys


def i20sp(x, xlen):
    if x >= 256**xlen:
        print("integer too large")
        sys.exit()
    temp_x = str(x).zfill(xlen)
    x = ''
    temp = 0
    for i in range(1, xlen + 1):
        x += temp_x[xlen - i] * 256**(xlen - i)

    return x


def mgf1(seed, mask_len):
    t = ''
    for i in range(ceil(mask_len / 20)):
        c = i20sp(i, 4)
        t += sha1((seed + c).encode()).hexdigest()

    return t[:2*mask_len]

print(mgf1("0123456789abcdef", 30))