from hashlib import sha1
import matplotlib.pyplot as plt
import collections


zero_values = ["0" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
one_values = ["1" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
hash_lengths = [1, 2, 4, 8, 16, 32, 35, 64]
match_found_for_length = {}


for hash_length in hash_lengths:
    zero_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in zero_values]
    one_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in one_values]
    match_found = 0
    for i in range(2 ** 16):
        if zero_hashes[i] in one_hashes:
            match_found = 1
            break
    match_found_for_length.update({hash_length: match_found})


fig = plt.figure()
plt.plot(*zip(*sorted(match_found_for_length.items())), marker='o')
fig.suptitle('Probability of breaking the binding property', fontsize=20)
plt.xlabel('X-value', fontsize=18)
plt.ylabel('Probability', fontsize=16)
fig.savefig('graph.png')
plt.show()
print(match_found_for_length)
