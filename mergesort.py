import random


def merge(a, b):
    merged_arr = []
    a_index, b_index = 0, 0
    comparisons = 0

    for k in range(len(a) + len(b)):
        if a_index == len(a):
            merged_arr.append(b[b_index])
            b_index += 1
            continue
        elif b_index == len(b):
            merged_arr.append(a[a_index])
            a_index += 1
            continue

        comparisons += 1

        if a[a_index] < b[b_index]:
            merged_arr.append(a[a_index])
            a_index += 1
        else:
            merged_arr.append(b[b_index])
            b_index += 1

    return merged_arr, comparisons


def merge_five(a, b, c, d, e):
    result, c1 = merge(a, b)
    result, c2 = merge(result, c)
    result, c3 = merge(result, d)
    result, c4 = merge(result, e)
    print(c1, c2, c3, c4, c1 + c2 + c3 + c4)
    return result


random.seed(1000)
lengths = [20, 24, 30, 35, 50]
arrays = []

for k in range(5):
    arr = sorted([100 - i + k for i in range(lengths[k])])
    arrays.append(arr)

merged = merge_five(*arrays)
print(arrays)

assert sum([len(arr) for arr in arrays]) == len(merged)
assert merged == sorted(merged)
print(merged, len(merged))