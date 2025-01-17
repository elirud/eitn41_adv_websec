import hashlib


def sha1_hash_hexadecimal_value(hstring):
    return hashlib.sha1(bytearray.fromhex(hstring)).hexdigest()


with open('testB3.txt', 'r') as f:
    data = f.read().splitlines()


built_hash = data[0]

for node in data[1:]:
    built_hash = sha1_hash_hexadecimal_value(node[1:] + built_hash) if node[0] == 'L' else sha1_hash_hexadecimal_value(built_hash + node[1:])

print(built_hash)
