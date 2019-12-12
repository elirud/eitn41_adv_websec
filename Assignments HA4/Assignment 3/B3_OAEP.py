from hashlib import sha1
from math import ceil



def i20sp(x, xlen):
    temp = - 1
    x_array = [int(i) for i in str(x).zfill(xlen)]
    if x >= 256**xlen:
        print("integer too large")
        return temp
    temp = 0
    for i in range(1, xlen + 1):
        temp = temp + x_array[xlen - i] * 256**(xlen - i)

    return int(temp)




def mgf1(seed, mask_len):
    t = ''
    for i in range(ceil(mask_len / 20)):
        c = i20sp(i, 4)
        t += sha1((seed + c).encode()).hexdigest()

    return t[:2*mask_len]

print(mgf1("0123456789abcdef", 30))