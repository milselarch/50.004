from library import Array


def min_jumps(A, index=1, j=3, backlog=(), calls=None):
    if index == len(A):
        print(len(backlog), backlog)
        return 0

    start = False
    if calls is None:
        calls = [1]
        start = True
    else:
        calls[0] += 1

    state = (index, j)
    if (state in backlog) or (j == 0):
        return -1

    new_indexes = index - j, index + j
    jumps_needed = float('inf')

    for new_index in new_indexes:
        if (new_index > len(A)) or (new_index <= 0):
            continue

        new_j = j + A[new_index]
        new_backlog = backlog + (state,)
        sub_min_jumps = min_jumps(
            A, new_index, new_j, new_backlog, calls=calls
        )

        if sub_min_jumps == -1:
            continue

        jumps = 1 + sub_min_jumps
        jumps_needed = min(jumps_needed, jumps)

    if jumps_needed == float('inf'):
        jumps_needed = -1

    if start:
        print(calls)

    return jumps_needed


if __name__ == '__main__':
    # a = Array([0, 0, 1, -1, 5, -2, -4, 0])
    a = Array([0, 0, 1, -1, 0, -2, 0])
    print(a)
    print(min_jumps(a))