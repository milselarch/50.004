import datetime
from line_profiler import LineProfiler

import math
import os
import random
import cProfile
import re
import sys

Datetime = datetime.datetime

MODULO = 10 ** 9 + 7

CACHE = {}
single_layer_combs = [1, 1, 2, 4] + [0] * 997
stack_total_combs = [0] * 1000
stack_total_combs_cache = {}

for layer_width in range(len(single_layer_combs)):
    if layer_width >= 4:
        current_layer_combs = sum(single_layer_combs[layer_width - 4:layer_width])
        single_layer_combs[layer_width] = current_layer_combs


EXP_CACHE = {}
def logexp(x, power):
    assert power >= 1

    if power == 1:
        return x

    cache_key = (x, power)
    if cache_key in EXP_CACHE:
        return EXP_CACHE[cache_key]

    l_power = power // 2
    r_power = power - l_power
    value = (logexp(x, l_power) * logexp(x, r_power)) % MODULO
    EXP_CACHE[cache_key] = value
    return value

"""
def get_stack_total_combs(n, m):
    key = (n, m)

    if key in stack_total_combs_cache:
        return stack_total_combs_cache[key]

    value = (single_layer_combs[m] ** n) % MODULO
"""


def legoBlocks(n, m):
    # n is height of wall, m is width of wall
    # number of ways to arrange a single layer of logo blocks
    # (ignoring the invalid combinations)
    # current_layer_width = max(list(single_layer_combs.keys()))

    """
    number of ways to fill a single layer of size n is the sum of:
    1. ways to fill size n - 1 and add a 1-width block at the end
    2. ways to fill size n - 2 and add a 2-width block at the end
    3. ways to fill size n - 3 and add a 3-width block at the end
    4. ways to fill size n - 4 and add a 4-width block at the end
    """

    """
    for layer_width in range(m+1):
        # number of ways to arrange a stack of logo blocks of height n
        # (ignoring the invalid combinations)
        stack_total_combs[layer_width] = (
            single_layer_combs[layer_width] ** n
        ) % MODULO
    """

    stack_valid_combs = [0] * (m + 1)  # {0: 0, 1: 0}
    # stack_invalid_combs = [0] * (m+1) # {0: 0, 1: 0}
    # print('STACK_TOTAL_COMBS', stack_total_combs)

    for layer_width in range(1, m + 1):
        current_invalid_combs = 0
        # print('LL', layer_width, stack_invalid_combs)
        for k in range(1, layer_width):
            # draw a vertical break at x-value k
            # get the number of combinations of lego bricks
            # where all sub-combinations to the left are valid
            # and everything to the right may or may not be valid
            # print('XX', layer_width, k, stack_total_combs[k], stack_invalid_combs[layer_width - k])
            current_invalid_combs += (
                stack_valid_combs[k] * stack_total_combs[layer_width - k]
            ) % MODULO

        stack_total_combs[layer_width] = (
            logexp(single_layer_combs[layer_width], n)
        ) % MODULO

        current_invalid_combs %= MODULO
        # stack_invalid_combs[layer_width] = current_invalid_combs
        stack_valid_combs[layer_width] = (
            stack_total_combs[layer_width] - current_invalid_combs
        ) % MODULO

    # print('SSL', single_layer_combs)
    return stack_valid_combs[m]

def compute():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lines = open('testcase7.txt').read().strip().split('\n')
    length = int(lines[0])
    numbers = [(int(x.split()[0]), int(x.split()[1])) for x in lines[1:]]

    for t_itr in range(length):
        n = int(numbers[t_itr][0])
        m = int(numbers[t_itr][1])
        result = legoBlocks(n, m)
        print(f'{t_itr} ({n},{m}) = {result}')

    # fptr.close()

def run_profile(func, filepath, *args, **kwargs):
    startTime = Datetime.now().timestamp()
    profiler = cProfile.Profile()
    profiler.enable()

    result = func(*args, **kwargs)

    profiler.disable()
    endTime = Datetime.now().timestamp()
    duration = endTime - startTime
    profiler.dump_stats(filepath)
    return result

if __name__ == '__main__':
    lp = LineProfiler()
    lp_wrapper = lp(compute)
    lp_wrapper()
    # lp_wrapper(959, 499)
    lp.print_stats()

    """
    res = run_profile(
        compute, 'lego.profile', # 959, 499
    )
    # fptr.close()
    print(res)"""