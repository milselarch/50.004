from hashmap import HashMap

hm = HashMap(
    size=30, fill_all_keys=False, probing=True
)
hm.add_values(verbose=True, values=[
    2, 32, 62, 92, 122
])

print('final hashmap')
print(hm)

hm = HashMap(
    size=30, fill_all_keys=False, probing=True,
    hash_func=lambda size, k, i=0: ((k % size) + 1*i + 2*i**2) % size
)
hm.add_values(verbose=True, values=[
    2, 32, 62, 92, 122
])

print('final hashmap')
print(hm)

h1 = lambda k: (k % 30)
h2 = lambda k: (1 + k % 11)
h = lambda m,k,i: (h1(k) + i * h2(k)) % m

hm = HashMap(
    size=30, fill_all_keys=False, probing=True,
    hash_func=h
)
hm.add_values(verbose=True, values=[
    2, 32, 62, 92, 122
])

print('final hashmap')
print(hm)
