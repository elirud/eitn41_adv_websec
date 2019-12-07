from hashlib import sha1


zero_values = ["0" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
one_values = ["1" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
hash_lengths = [1, 2, 4, 8, 16, 32, 35, 64]
match_found_for_length = {}

for hash_length in hash_lengths:
    zero_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in zero_values]
    one_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in one_values]
    match_found = False
    for i in range(2 ** 16):
        if zero_hashes[i] in one_hashes:
            match_found = True
            break
    match_found_for_length.update({hash_length: match_found})

print(match_found_for_length)
