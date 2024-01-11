def fits_factors(n, arr):
    for num in arr:
        if num % n != 0:
            print('FF-FAIL', num, n)
            return False

    return True


def has_factors(n, arr):
    for num in arr:
        if n % num != 0:
            print('HF-FAIL', num, n)
            return False

    return True


def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)
    max_considered = min(b)
    min_considered = max(a)
    valid = 0

    for k in range(min_considered, max_considered + 1):
        # print('CONSIDER', k)
        if has_factors(k, a) and fits_factors(k, b):
            print('VALID', k)
            valid += 1

    # Write your code here
    return valid

# print(getTotalX([2,3], [2,4]))
print(getTotalX([2, 6], [24, 36]))