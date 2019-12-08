from hashlib import sha1
import matplotlib


zero_values = ["0" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
one_values = ["1" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
zero_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:16] for x in zero_values]
one_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:16] for x in one_values]

amount_of_matches = []
for y in one_hashes:
    matches = [x for x in zero_hashes if x == y]
    if len(matches) != 0:
        amount_of_matches.append(len(matches))

print(zero_hashes[0])
print(len(amount_of_matches))
print(amount_of_matches[:10])

