import random

from library import Array


def generate(n=10, start=0, end=100):
    return Array([
        random.randint(start, end) for _ in range(n)
    ])


def max_value(
    item_sizes, item_values, item_limits, max_size,
    max_items, cache=None
):
    if cache is None:
        cache = {}

    if max_items == 0:
        return 0
    if len(item_limits) == 0:
        return 0

    item_no = len(item_limits)
    p1 = max_value(
        item_sizes, item_values, item_limits[:-1],
        max_size, max_items, cache=cache
    )

    if item_limits[-1] == 0:
        return p1
    elif max_size < item_sizes[item_no]:
        return p1
    else:
        for item_limit in item_limits:
            assert item_limit >= 0

    assert max_size >= 0
    assert max_items >= 0
    cache_key = item_limits.to_tuple() + (max_size, max_items)
    if cache_key in cache:
        return cache[cache_key]

    # remove item from selection
    # new_item_limits2 = item_limits.copy()
    # new_item_limits2.items[-1] -= 1

    item_value = item_values[item_no]
    item_size = item_sizes[item_no]

    assert max_size >= item_size
    p2 = item_value + max_value(
        item_sizes, item_values,
        item_limits[:-1] + [item_limits[-1]-1],
        max_size-item_size, max_items-1, cache=cache
    )

    loot_value = max(p1, p2)
    cache[cache_key] = loot_value
    # print(cache_key, loot_value)
    return loot_value


if __name__ == '__main__':
    random.seed(1223121122112222)
    sizes = generate()
    values = generate()
    inventory = generate(start=1, end=10)
    print(sizes, values, inventory)

    print('loot value =', max_value(
        sizes, values, inventory,
        max_size=1000, max_items=20
    ))