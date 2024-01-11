# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def swap_index(string, index):
    return string[:index] + string[index + 1] + string[index] + string[index + 2:]


def swappable(string, index):
    return (int(string[index]) % 2) == (int(string[index + 1]) % 2)


def getLargestNumber(num, cache=None):
    cache = [] if cache is None else cache

    # Write your code here
    str_num = str(num)
    cache.append(str_num)

    for k in range(len(str_num) - 1):
        if not swappable(str_num, k):
            continue

        swapped_str_num = swap_index(str_num, k)
        if swapped_str_num in cache:
            continue

        getLargestNumber(swapped_str_num, cache)

    max_number = max(cache)
    print('MAX_IS', max_number)
    return max(max_number)