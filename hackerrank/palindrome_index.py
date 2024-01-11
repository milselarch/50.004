#!/bin/python3

import math
import os
import random
import string
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # print("PRE_CHECK", s)
    # Write your code here
    left_shift = 0
    right_shift = 0
    l_index = 0
    r_index = 0
    k = 0

    while k < len(s) // 2:
        left_index = k + left_shift
        right_index = len(s) - 1 - k - right_shift
        if left_index >= right_index:
            break

        if s[left_index] == s[right_index]:
            k += 1
            continue

        # edge case where cutting out both from left and
        # right side causes next character to match on the other side
        l_cond = s[left_index + 1] == s[right_index]
        r_cond = s[left_index] == s[right_index - 1]
        temp_l_index = left_index
        temp_r_index = right_index
        # both_substitutable = False

        while l_cond and r_cond:
            left_index += 1
            right_index -= 1
            # both_substitutable = True

            l_cond = s[left_index + 1] == s[right_index]
            r_cond = s[left_index] == s[right_index - 1]

        # print('COND_TEST', k, s[left_index], s[right_index], l_cond, r_cond)

        if l_cond:
            left_shift += 1
            l_index = temp_l_index
        elif r_cond:
            right_shift += 1
            r_index = temp_r_index
        else:
            # print('TERM_D')
            return -1

        if left_shift + right_shift > 1:
            # print('TERM_E')
            return -1

    # print('SHIFTS', left_shift, right_shift)
    if left_shift + right_shift == 1:
        if left_shift == 1:
            return l_index
        else:
            return r_index

    # print('TERM_F', left_shift, right_shift)
    return -1


def generate(length=20):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    palindrome = result_str + result_str[::-1]
    chars = list(palindrome)

    index = random.choice(range(length * 2))
    rand_char = random.choice(letters)
    chars = chars[:index] + [rand_char] + chars[index:]
    return ''.join(chars)


random.seed(42)

# test_str = 'aaabaaa'
# test_str = 'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'

for k in range(10000):
    test_str = generate()
    print('TEST', test_str)

    result = palindromeIndex(test_str)
    assert (result != -1) or (test_str == test_str[::-1])
    print('RESULT', k, result)