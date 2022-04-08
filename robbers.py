import random

from library import Array

def generate(n=10, start=0, end=100):
    return Array([
        random.randint(start, end) for _ in range(n)
    ])


cache = {}

def optimal_rob(houses, reset=True):
    length = len(houses)
    # print(length)
    global cache

    if reset:
        cache = {}

    if length == 0:
        return 0
    elif length in cache:
        return cache[length]

    h1 = houses[:-1]
    h2 = houses[:-2]
    c1 = optimal_rob(h1, False)
    c2 = optimal_rob(h2, False) + houses[-1]

    money = max(c1, c2)
    cache[length] = money
    return money

def generate_houses(n=10, start=0, end=100):
    return Array([
        Array([
            random.randint(start, end) for _ in range(n)
        ]) for _ in range(n)
    ])


def optimal_rob_square(
    houses, reset=True, i=None, j=None
):
    n = len(houses)
    global cache

    if reset:
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

    p1 = optimal_rob_square(houses, reset=False, i=i-1, j=j)
    p2 = optimal_rob_square(houses, reset=False, i=i, j=j-1)
    value = houses[i][j] + max(p1, p2)
    cache[i][j] = value
    return value


if __name__ == '__main__':
    random.seed(42)
    a = generate(9)
    print(a)
    print(optimal_rob(a))
    print(cache)

    houses = generate_houses()
    value = optimal_rob_square(houses)
    print(houses)
    print(cache)
    print(value)