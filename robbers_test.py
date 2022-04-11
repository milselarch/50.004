from robbers import *

h = Array(
    Array([0, 0, 0, 0, 11]),
    Array([0, 0, 0, 0, 0]),
    Array([0, 0, 55, 0, 0]),
    Array([0, 0, 0, 0, 0]),
    Array([12, 0, 0, 0, 1])
)

loot1 = optimal_rob_square(h)
print(h)
print('SQUARE', loot1)

loot = optimal_rob_st(h)
print(h)
print('LOOT1', loot)

loot = optimal_rob_st2(h)
print(h)
print('LOOT2', loot)

loot = optimal_rob_st3(h)
print(h)
print('LOOT3', loot)
assert loot == loot1