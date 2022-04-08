import random

from library import Array


def generate(n=10, start=0, end=100):
    return Array([
        random.randint(start, end) for _ in range(n)
    ])


def optimal_rob(houses, cache=None):
    length = len(houses)
    # print(length)

    if cache is None:
        cache = {}

    if length == 0:
        return 0
    elif length in cache:
        return cache[length]

    h1 = houses[:-1]
    h2 = houses[:-2]
    c1 = optimal_rob(h1, cache)
    c2 = optimal_rob(h2, cache) + houses[-1]

    money = max(c1, c2)
    cache[length] = money
    return money


def generate_houses_2d(n=10, start=0, end=100):
    return Array([
        Array([
            random.randint(start, end) for _ in range(n)
        ]) for _ in range(n)
    ])


def optimal_rob_square(
    houses, cache=None, i=None, j=None
):
    n = len(houses)

    if cache is None:
        cache = Array([
            Array([-1 for _ in range(n)])
            for _ in range(n)
        ])

    if i is None:
        i = n
    if j is None:
        j = n

    if (i == 1) or (j == 1):
        return houses[1][1]
    elif cache[i][j] != -1:
        return cache[i][j]

    p1 = optimal_rob_square(houses, cache, i=i-1, j=j)
    p2 = optimal_rob_square(houses, cache, i=i, j=j-1)
    value = houses[i][j] + max(p1, p2)
    cache[i][j] = value
    return value


def optimal_rob_st(
    houses, cache=None, i=None, j=None
):
    i = len(houses) if i is None else i
    j = len(houses[1]) if j is None else j

    cache_index = (i, j)
    cache = {} if cache is None else cache

    if (i < 1) or (j < 1):
        return 0
    elif cache_index in cache:
        return cache[cache_index]

    if cache is None:
        cache = {}
    elif cache_index in cache:
        return cache[cache_index]

    # rob current house
    top_left = optimal_rob_st(
        houses, cache=cache, i=i-1, j=j-1
    )
    # don't rob current house, go up one house
    top = optimal_rob_st(
        houses, cache=cache, i=i-1, j=j
    )
    # don't rob current house, go left one house
    left = optimal_rob_st(
        houses, cache=cache, i=i, j=j-1
    )

    house_loot = max(houses[i][j] + top_left, top, left)
    cache[cache_index] = house_loot
    return house_loot


if __name__ == '__main__':
    random.seed(42)
    a = generate(9)
    print(a)
    print(optimal_rob(a))

    h = generate_houses_2d()
    loot = optimal_rob_square(h)
    print(h)
    print(loot)

    loot = optimal_rob_st(h)
    print(h)
    print(loot)