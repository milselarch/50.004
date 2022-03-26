from LinkedList import LinkedList


def kth_last_element(arr, k=3):
    cache = [0] * k
    i = 0

    while True:
        if i >= len(arr):
            break

        value = arr[i]
        cache[i % k] = value
        i += 1

    if k > i:
        return None

    inv_index = (i - k) % k
    return cache[inv_index]


def kth_last_element_v2(L: LinkedList, k=3):
    n = 0
    i = 0

    is_scouting = True
    scout_node = L.head
    search_node = L.head

    while True:
        if scout_node.next is None:
            is_scouting = False

        if is_scouting:
            scout_node = scout_node.next
            n += 1
            continue

        print(i, n-k+1)
        if i == n - k + 1:
            break
        if k > n:
            return None

        search_node = search_node.next
        i += 1

    return search_node


print(kth_last_element([1, 2, 3, 24, 4, 6, 7, 8], k=5))

data = LinkedList([1, 2, 3, 24, 4, 6, 7, 8])
print(data)
print(kth_last_element_v2(data, k=9))
