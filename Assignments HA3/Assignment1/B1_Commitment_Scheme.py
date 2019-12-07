from hashlib import sha1


zero_values = ["0" + str(bin(x)).zfill(16) for x in range(2 ** 16 - 1)]
one_values = ["1" + str(bin(x)).zfill(16) for x in range(2 ** 16 - 1)]
zero_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:160] for x in zero_values]
one_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:160] for x in one_values]


print(zero_hashes[0])