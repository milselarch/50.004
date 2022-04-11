import random

from library import Array


def generate(n=10, start=0, end=100):
    return Array([
        random.randint(start, end) for _ in range(n)
    ])


def max_sum(arr, m=None):
    m = len(arr) if m is None else m

    item_cache = {}
    cache = Array([0 for k in range(m)])
    cache[1] = arr[1]
    # print(arr)

    for k in range(2, m+1):
        # 2 to m inclusive
        # print(cache, m, arr[k])
        cache[k] = max(
            cache[k-1],
            max_item_sum(arr, k, item_cache)
        )

    # print('CACHE', cache)
    # print('ITEM_CACHE', item_cache)
    return cache[m]


def max_item_sum(arr, m=None, cache=None):
    m = len(arr) if m is None else m
    cache = {} if cache is None else cache

    if m in cache:
        return cache[m]

    # print(m)

    if m == 1:
        csum = arr[1]
        cache[m] = csum
        return csum

    if max_item_sum(arr, m-1, cache) <= 0:
        csum = arr[m]
        cache[m] = csum
        return csum
    else:
        csum = arr[m] + max_item_sum(arr, m-1, cache)
        cache[m] = csum
        return csum


def min_prod(A):
    m = len(A)
    min_cache = Array([0 for k in range(m)])
    min_cache[1] = A[1]
    cache = {}

    for k in range(2, len(A)+1):
        # for k from 2 to m (inclusive)
        min_cache[k] = min(
            min_cache[k-1], min_max_prod(
                A, k, cache=cache
            )[0]
        )

    return min_cache[m]


def min_max_prod(A, m=None, cache=None):
    m = len(A) if m is None else m
    cache = {} if cache is None else cache

    if m in cache:
        return cache[m]

    if m == 1:
        cache[1] = (A[m], A[m])
        return cache[1]
    else:
        prev_min, prev_max = min_max_prod(A, m-1, cache)
        prod_min = A[m] * min(prev_min, prev_max, 1)
        prod_max = A[m] * max(prev_min, prev_max, 1)
        cache[m] = (prod_min, prod_max)
        return cache[m]


def longest_coaster(A, m=None):
    m = len(A) if m is None else m
    rcache = Array([0 for k in range(m)])
    rcache[1] = 1
    cache = {}

    for k in range(2, m+1):
        rcache[k] = max(
            roller_coaster(A, k, cache=cache),
            rcache[k-1]
        )

    print(rcache, cache)
    return rcache[m]


def roller_coaster(A, m=None, cache=None):
    m = len(A) if m is None else m
    cache = {} if cache is None else cache
    print('AA', m, A[m - 1], A[m], cache)

    if m == 1:
        cache[1] = 1
        return cache[1]

    elif (abs(A[m-1]) > abs(A[m])) and (A[m] * A[m-1] < 0):
        print('ELIF')
        length = roller_coaster(A, m-1, cache) + 1
        cache[m] = length
        return length
    else:
        cache[m] = 1
        return 1


if __name__ == '__main__':
    random.seed(5324)
    a = Array([2, 3, -4, 2, 0, 1, -2, 3, 2, -3])
    prod_cache = {}

    print(a)
    print(min_max_prod(a, cache=prod_cache))
    print(prod_cache)
    print(min_prod(a))

    a = Array([2, 0, 3, -7, 6, -5, 1, -2])
    print(a)
    print(longest_coaster(a))
    # print(a, max_sum(a))
