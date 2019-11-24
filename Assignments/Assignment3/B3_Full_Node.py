import hashlib
import math


def calc_parents(children):
    parents = []

    for leaf in children[::2]:
        parents.append(sha1_hash_hexadecimal_value(leaf + children[children.index(leaf) + 1]))

    return parents


def sha1_hash_hexadecimal_value(hstring):
    return hashlib.sha1(bytearray.fromhex(hstring)).hexdigest()


with open('testB3_2.txt', 'r') as f:
    data = f.read().splitlines()


n_leaf = int(data[0])
n_sibling_depth = int(data[1])
depth = int(math.ceil(math.log2(len(data[2:]))))
leaves = data[2:]
merkle_path = []
merkle_node_at_depth = None


for i in range(depth):
    if len(leaves) % 2 != 0:
        leaves.append(leaves[len(leaves) - 1])
    if (n_leaf + 1) % 2 == 0:
        merkle_path.append('L' + leaves[n_leaf - 1])
    else:
        merkle_path.append('R' + leaves[n_leaf + 1])
    if (depth - i) == n_sibling_depth:
        merkle_node_at_depth = merkle_path[len(merkle_path) - 1]
    leaves = calc_parents(leaves)
    n_leaf = int(math.floor(n_leaf / 2))

print("-----Merkle Path-----")
for sibling in merkle_path:
    print(sibling)
print("---------------------")


print("-----Merkle Node-----")
print(merkle_node_at_depth)
print("---------------------")


print("-----Merkle Root-----")
print(leaves)
print("---------------------")
