from hashlib import sha1
import matplotlib.pyplot as plt

zero_values = ["0" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
one_values = ["1" + bin(x).lstrip("0b").zfill(16) for x in range(2 ** 16)]
hash_lengths = [1, 2, 4, 8, 16, 24, 32, 35, 64]

probability_for_hash_length = {}

for hash_length in hash_lengths:
    zero_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in zero_values]
    one_hashes = [bin(int(sha1(x.encode()).hexdigest(), 16)).lstrip("0b")[:hash_length] for x in one_values]
    amount_of_matches = []
    for y in one_hashes:
        matches = [x for x in zero_hashes if x == y]
        if len(matches) != 0:
            amount_of_matches.append(len(matches))
    probability_for_hash_length.update({hash_length: ((2 ** 16 - len(amount_of_matches)) / (2 ** 16))})


fig = plt.figure()
plt.plot(*zip(*sorted(probability_for_hash_length.items())), marker='o')
fig.suptitle('Probability of breaking the concealing property', fontsize=20)
plt.xlabel('X-value', fontsize=18)
plt.ylabel('Probability', fontsize=16)
fig.savefig('graph_2.png')
plt.show()


print(probability_for_hash_length)
