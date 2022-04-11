import random

from library import Array


def generate(n, max_val=100):
    blocks = [
        random.randint(0, max_val) for k
        in range(n)
    ]
    blocks[0] = 0
    return Array(blocks)


def max_points(arr, block_no=None, cap=None, cache=None):
    """
    likely O(n^2) as there are n numbers
    and each one has at most n possible score_caps associated
    """
    assert type(arr) is Array
    fresh = False

    if cache is None:
        fresh = True
        cache = {}

    if cap is None:
        cap = float('inf')
    if block_no is None:
        block_no = len(arr)

    if (block_no == 1) or (cap == 0):
        return 0

    key = (block_no, cap)
    if key in cache:
        return cache[key]

    if arr[block_no] > cap:
        return max_points(arr, block_no - 1, cap, cache=cache)

    block_points = arr[block_no]
    p1 = max_points(arr, block_no - 1, cap, cache=cache)
    p2 = block_points + max_points(
        arr, block_no - 1, block_points - 1, cache=cache
    )

    best_points = max(p1, p2)
    cache[key] = best_points

    if fresh:
        print(len(cache), cache)

    return best_points


if __name__ == '__main__':
    random.seed(422)
    a = generate(10)
    # a = [2 << k for k in range(10)]
    # random.shuffle(a)
    # a[0] = 0
    # a = Array(a)

    print(a)
    score = max_points(a)
    print(a)
    print(score)