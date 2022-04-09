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
    if max_size == 0:
        return 0
    if sum(item_limits) == 0:
        return 0

    if item_limits[-1] == 0:
        return max_value(
            item_sizes, item_values, item_limits[::][:-1],
            max_size, max_items, cache=cache
        )

    # remove item from selection
    new_item_limits2 = item_limits[::]
    new_item_limits2[-1] -= 1

    item_value = item_values[-1]
    item_size = item_sizes[-1]

    p1 = max_value(
        item_sizes, item_values, item_limits[::][:-1],
        max_size, max_items
    )
    p2 = item_value + max_value(
        item_sizes, item_values, new_item_limits2,
        max_size-item_size, max_items - 1
    )

    return max(p1, p2)


if __name__ == '__main__':
    random.seed(42)
    sizes = generate()
    values = generate()
    inventory = generate(start=1, end=10)
    print(sizes, values, inventory)