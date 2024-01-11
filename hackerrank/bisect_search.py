def get_index(arr, score):
    left, right = 0, len(arr)

    while right - left > 1:
        # print('RL', right, left)
        mid = (left + right) // 2
        if arr[mid] > score:
            right = mid
        else:
            left = mid

    return left


a = list(range(20))
values = [4, 4.5, 5]

for value in values:
    index = get_index(a, value)
    print(value, a[index])