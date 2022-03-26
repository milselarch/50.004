from random import randint
import random
import copy


def john_sort(c):
    arr = copy.deepcopy(c)
    for i in range(len(arr)-1, 0, -1):
        print(i, arr)

        for j in range(len(arr)-1, i, -1):
            # print(i,j)
            if arr[j] > arr[j-1]:
                assert j >= 1
                print(i, j, arr[j], arr[j-1])
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


def john_sort2(c):
    arr = copy.deepcopy(c)
    for i in range(len(arr)):
        # print(i, arr)
        print('ARD', i, arr)

        for j in range(len(arr)-1, i, -1):
            if arr[j] > arr[j-1]:
                assert j >= 1
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


def john_sort3(c):
    arr = copy.deepcopy(c)
    for i in range(len(arr)):
        # print(i, arr)
        for j in range(len(arr)-1, i, -1):
            # print(i,j, a[:j])
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


random.seed(23)
# randint(0, 40)
a = [randint(0, 20) for k in range(10)]
# a = [k for k in range(10)]
print('P1', a)


result = john_sort2(a)
print('P2', a)

bad_result = john_sort(a)

print()
print('a', a)
print('bad', bad_result)
print('john', result)