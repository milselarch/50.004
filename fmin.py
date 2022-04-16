def fmin(start, end, cache=None):
    cache_key = (start, end)
    if cache is None:
        cache = {}

    if cache_key in cache:
        return cache[cache_key]

    if start == end:
        return 1
    elif end == start + 1:
        return 2

    midpoint = (end + start) // 2
    min_trials = 1 + max(
        fmin(midpoint+1, end, cache),
        fmin(start, midpoint-1, cache)
    )

    cache[cache_key] = min_trials
    print(len(cache))
    return min_trials


if __name__ == '__main__':
    print(fmin(1, 1425))