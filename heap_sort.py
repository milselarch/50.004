def children(index):
    return index * 2 + 1, index * 2 + 2


def get_max_child(index, array, size=None):
    if size is None:
        size = len(array)

    left, right = children(index)

    if right >= size:
        return left

    if array[left] > array[right]:
        return left

    return right


def parent(index):
    return (index - 1) // 2


def verify_heap(array):
    for k in range(len(array)):
        if k == 0:
            # root node 0 has no parent
            continue

        # parent node must have higher value than children
        assert array[parent(k)] >= array[k]


def max_heapify(array, index, size=None):
    if size is None:
        size = len(array)

    while True:
        child = get_max_child(index, array, size)
        if child >= size:
            return

        child_val = array[child]
        current_value = array[index]

        if child_val > current_value:
            array[child], array[index] = array[index], array[child]
            index = child
        else:
            return


def build_max_heap(array):
    # sort lowest level of tree first
    for k in range(len(array) // 2, -1, -1):
        max_heapify(array, k)


def heap_sort(array):
    build_max_heap(array)
    size = len(array) - 1

    while size > 0:
        print('PRE', array, array[:size + 1])
        array[0], array[size] = array[size], array[0]
        print('AFT', array, array[:size + 1])

        size -= 1
        # max_heapify(array[0: size+1], 0, size+1)
        max_heapify(array, 0, size+1)


array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_sort(array)
print(array)
assert array == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]