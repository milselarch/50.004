import random

from library import *

def children(index):
    return index * 2, index * 2 + 1


def get_min_child(index, array: Array, size=None):
    assert isinstance(array, Array)

    if size is None:
        size = len(array)

    left, right = children(index)

    if right > size:
        if left > size:
            return None

        return left

    if array[left] < array[right]:
        return left

    return right


def get_max_child(index, array: Array, size=None):
    assert isinstance(array, Array)

    if size is None:
        size = len(array)

    left, right = children(index)

    if right > size:
        if left > size:
            return None

        return left

    if array[left] > array[right]:
        return left

    return right


def parent(index):
    return index // 2

def verify_min_heap(array):
    # print('length', len(array), array.items)

    for k in range(1, len(array) + 1):
        if k == 1:
            # root node 0 has no parent
            continue

        # parent node must have higher value than children
        # print(k, array[parent(k)], array[k])
        assert array[parent(k)] <= array[k]


def verify_max_heap(array):
    for k in range(len(array)):
        if k == 0:
            # root node 0 has no parent
            continue

        # parent node must have higher value than children
        assert array[parent(k)] >= array[k]


def min_heapify(array, index, size=None):
    if size is None:
        size = len(array)

    while True:
        child = get_min_child(index, array, size)
        if child is None:
            return

        child_val = array[child]
        current_value = array[index]

        if child_val < current_value:
            array[child], array[index] = array[index], array[child]
            index = child
        else:
            return

def max_heapify(array, index, size=None):
    if size is None:
        size = len(array)

    while True:
        child = get_max_child(index, array, size)
        if child is None:
            return

        child_val = array[child]
        current_value = array[index]

        if child_val > current_value:
            array[child], array[index] = array[index], array[child]
            index = child
        else:
            return

def build_min_heap(array):
    # sort lowest level of tree first
    for k in range(len(array) // 2 + 1, 0, -1):
        min_heapify(array, k)


if __name__ == '__main__':
    a = Array(list(range(10))[::-1])
    print(a)
    build_min_heap(a)
    print(a)

    verify_min_heap(a)
    random.seed(10)

    a = Array([
        random.randint(0, 100) for k in range(10)
    ])
    print(a)
    build_min_heap(a)
    print(a)

    verify_min_heap(a)