#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def count_sort(arr):
    import copy
    arr = copy.deepcopy(arr[::])
    # Write your code here
    sort_map = {}

    for k, item in enumerate(arr):
        index, symbol = item
        # print('ITEM', item)

        if index not in sort_map:
            sort_map[index] = []

        if k < len(arr) // 2:
            sort_map[index].append('-')
        else:
            sort_map[index].append(symbol)

    indexes = sorted(list(sort_map.keys()))
    all_symbols = []

    for index in indexes:
        symbols = sort_map[index]
        # print('IDX', index, symbols)
        all_symbols.extend(symbols)

    return all_symbols


def count_sort_v2(arr):
    import copy
    arr = copy.deepcopy(arr[::])
    for i in range(len(arr) // 2):
        arr[i][1] = '-'

    arr.sort(key=lambda x: int(x[0]))
    all_symbols = [x[1] for x in arr]
    return all_symbols


if __name__ == '__main__':
    arr = open('input01.txt').read().rstrip().split('\n')[1:]
    arr = [item.split(' ') for item in arr]
    arr = [[int(item[0]), item[1]] for item in arr]
    # print(arr)

    output1 = count_sort(arr)
    output2 = count_sort_v2(arr)
    print('OUT1', output1)
    print('OUT2', output2)
    assert output1 == output2