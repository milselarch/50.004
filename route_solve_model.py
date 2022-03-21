from library import Array
from HashMap import HashMapUnchain as HashMap

# question 5 python code
def hash_state(state):
    i, j, n = state
    return i * n + (j-1)

def min_jumps(
    A: Array, j: int, index=1, backlog: HashMap = None
):
    if index == len(A):
        print(len(backlog), backlog)
        return 0

    n = len(A)
    state = (index, j, n)
    if backlog is None:
        backlog = HashMap(size=2 * n**2, hash_func=hash_state)
    if (j == 0) or (backlog[state] is not None):
        return -1

    new_indexes = index - j, index + j
    jumps_needed = float('inf')
    for new_index in new_indexes:
        if (new_index > len(A)) or (new_index <= 0):
            continue

        new_j = j + A[new_index]
        backlog[state] = 1
        sub_min_jumps = min_jumps(
            A, new_j, index=new_index, backlog=backlog
        )

        backlog[state] = None
        if sub_min_jumps == -1:
            continue

        jumps = 1 + sub_min_jumps
        jumps_needed = min(jumps_needed, jumps)

    if jumps_needed == float('inf'): jumps_needed = -1
    return jumps_needed


if __name__ == '__main__':
    # a = Array([0, 0, 1, -1, 5, -2, -4, 0])
    a = Array([0, 0, 1, -1, 0, -2, 0])
    print(a)
    print(min_jumps(a, j=3))
