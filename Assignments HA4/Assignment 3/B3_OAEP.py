from hashlib import sha1
from math import ceil



def i20sp(x, xlen):



def mgf1(seed, mask_len):
    t = ''
    for i in range(ceil(mask_len / 20)):
        c = i20sp(i, 4)
        t += sha1((seed + c).encode()).hexdigest()

    return t[:2*mask_len]

print(mgf1("0123456789abcdef", 30))