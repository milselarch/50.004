def max_min(k, arr):
    # Write your code here
    arr = sorted(arr)
    print('SORTED', arr)
    best_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        unfairness = window[-1] - window[0]
        print('WINDOW', window)

        if unfairness < best_unfairness:
            best_unfairness = unfairness

    return best_unfairness


arr = [
    7, 3, 100, 200, 300, 350, 400,
    401, 402
]
print(max_min(3, arr))