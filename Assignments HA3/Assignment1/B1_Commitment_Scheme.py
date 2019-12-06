import hashlib
hash = hashlib.sha1()

hashlib.sha1(b"Nobody inspects the spammish repetition").hexdigest()

k_combinations = (2**16 - 1) * 2
X0_size = 16
X1_size = 24
X2_size = 32
X4_size = 40