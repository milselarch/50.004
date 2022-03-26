from hashmap import *


def search_divisible(arr, size=40):
    hm = HashMap(size=size)
    pairs = 0

    for k in range(len(arr)):
        value = arr[k]

        mod = value % size
        inv_mod = (size - mod) % size
        inv_hash_matches = hm[inv_mod]
        pairs += len(inv_hash_matches)

        if len(inv_hash_matches) > 0:
            print('PAIR', hm[inv_mod], mod)

        hm.add(mod, value)

    print(hm)
    return pairs


a = [4, 0, 28, 15, 34, 40, 64, 2, 12, 80, 120]
num_pairs = search_divisible(a, size=40)
print(f'there are {num_pairs} pairs')

a = [2, 12, 8, 18]
num_pairs = search_divisible(a, size=10)
print(f'there are {num_pairs} pairs')

