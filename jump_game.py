import random

from library import Array


def generate(n, max_val=100):
    blocks = [
        random.randint(0, max_val) for k
        in range(n)
    ]
    blocks[0] = 0
    return Array(blocks)


def max_score(arr, block_no=None, score_cap=None, cache=None):
    assert type(arr) is Array
    if cache is None:
        cache = {}

    if score_cap is None:
        score_cap = float('inf')
    if block_no is None:
        block_no = len(arr)

    if block_no == 1:
        return arr[block_no]

    key = (block_no, score_cap)
    if key in cache:
        return cache[key]

    if arr[block_no] > score_cap:
        return max_score(arr, block_no-1, score_cap)

    block_score = arr[block_no]
    p1 = max_score(arr, block_no-1, block_score-1, cache=cache)
    p2 = max_score(arr, block_no-1, score_cap, cache=cache)
    best_score = max(p1 + block_score, p2)
    cache[key] = best_score
    print(cache)
    return best_score


if __name__ == '__main__':
    random.seed(422)
    a = generate(10)
    print(a)
    score = max_score(a)
    print(a)
    print(score)