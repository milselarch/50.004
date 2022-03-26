from hashmap import HashMap

hm = HashMap(size=5, max_load_factor=0.8)
hm.add_values([
    2, 3, 6, 7, 10, 21, 24, 28, 30, 32, 35, 39
], verbose=True)

print('final hashmap')
print(hm)
