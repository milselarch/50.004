import random

from library import Array


def generate(n=10, start=0, end=100):
    return Array([
        random.randint(start, end) for _ in range(n)
    ])


def optimal_rob(houses, cache=None):
    """
    if we're using cache
    2 calls to T(n-2) that are cached the second time
    likely linear as T(n) = T(n-2) + c
    if we're not using cache
    T(n) = T(n) + T(n-1) + c
    """
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
    """
    O(n^2)
    n rows, n columns, we decrease 1 row / column each time
    """
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

    if (i == 1) and (j == 1):
        return houses[1][1]
    elif cache[i][j] != -1:
        return cache[i][j]

    if i == 1:
        return max(
            houses[i][j],
            optimal_rob_square(houses, cache, i=i, j=j-1)
        )
    if j == 1:
        return max(
            houses[i][j],
            optimal_rob_square(houses, cache, i=i-1, j=j)
        )

    p1 = optimal_rob_square(houses, cache, i=i-1, j=j)
    p2 = optimal_rob_square(houses, cache, i=i, j=j-1)
    p3 = houses[i][j] + optimal_rob_square(houses, cache, i=i-1, j=j-1)
    value = max(p1, p2, p3)
    cache[i][j] = value
    return value


def optimal_rob_st(
    houses, cache=None, i=None, j=None
):
    """
    O(n^2)?
    n rows, n columns, we decrease 1 row
    AND 1 column each time,
    but we do have to scan row / column in worst case
    T(n) = O(2n) + T(n-1)
    """
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


def optimal_rob_st2(
    houses, cache=None,
    x0=None, y0=None, x1=None, y1=None
):
    cache_index = (x0, y0, x1, y1)
    cache = {} if cache is None else cache
    x1 = len(houses) if x1 is None else x1
    y1 = len(houses) if y1 is None else y1
    x0 = 1 if x0 is None else x0
    y0 = 1 if y0 is None else y0

    if (x0 == x1) and (y0 == y1):
        return houses[y0][x0]

    if (x0 > x1) or (y0 > y1):
        return float('-inf')

    if cache is None:
        cache = {}
    elif cache_index in cache:
        return cache[cache_index]

    best_loot = 0
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            house_loot = houses[y][x]
            top_left = optimal_rob_st2(
                houses, cache, x0, y0, x-1, y-1
            )
            bottom_right = optimal_rob_st2(
                houses, cache, x+1, y+1, x1, y1
            )

            best_loot = max(
                house_loot + top_left + bottom_right,
                best_loot
            )

    return best_loot


def optimal_rob_st3(
    houses, cache=None,
    x0=None, y0=None, x1=None, y1=None
):
    cache_index = (x0, y0, x1, y1)
    cache = {} if cache is None else cache
    x1 = len(houses) if x1 is None else x1
    y1 = len(houses) if y1 is None else y1
    x0 = 1 if x0 is None else x0
    y0 = 1 if y0 is None else y0

    if (x0 == x1) and (y0 == y1):
        return houses[y0][x0]

    if (x0 > x1) or (y0 > y1):
        return float('-inf')

    if cache is None:
        cache = {}
    elif cache_index in cache:
        return cache[cache_index]

    # rob bottom right house
    bottom_right = optimal_rob_st3(
        houses, cache=cache,
        x0=x0, y0=y0, x1=x1-1, y1=y1-1
    ) + houses[y1][x1]
    # rob top left house
    top_left = optimal_rob_st3(
        houses, cache=cache,
        x0=x0+1, y0=y0+1, x1=x1, y1=y1
    ) + houses[y0][x0]

    # don't rob current house, go up one house
    bottom_up = optimal_rob_st3(
        houses, cache=cache,
        x0=x0, y0=y0, x1=x1, y1=y1-1
    )
    bottom_left = optimal_rob_st3(
        houses, cache=cache,
        x0=x0, y0=y0, x1=x1-1, y1=y1
    )

    # don't rob current house, go right one house
    top_right = optimal_rob_st3(
        houses, cache=cache,
        x0=x0+1, y0=y0, x1=x1, y1=y1
    )
    top_down = optimal_rob_st3(
        houses, cache=cache,
        x0=x0, y0=y0+1, x1=x1, y1=y1
    )

    best_loot = max(
        bottom_right, top_left,
        bottom_up, bottom_left,
        top_right, top_down
    )
    cache[cache_index] = best_loot
    return best_loot


if __name__ == '__main__':
    random.seed(11122211223312)
    a = generate(53)
    # print(a)
    # print(optimal_rob(a))

    # h = generate_houses_2d()
    h = Array(
        Array([0, 0, 0, 0, 0]),
        Array([0, 0, 4, 0, 0]),
        Array([0, 0, 0, 0, 0]),
        Array([0, 9, 0, 0, 0]),
        Array([0, 0, 0, 2, 2])
    )

    while True:
        h = generate_houses_2d(6)

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