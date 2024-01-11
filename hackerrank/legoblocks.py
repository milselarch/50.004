#!/bin/python3

import math
import os
import random
import re
import sys

import pstats
import cProfile

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

MODULO = 10 ** 9 + 7


def legoBlocks(n, m):
    # n is height of wall, m is width of wall
    # number of ways to arrange a single layer of logo blocks
    # (ignoring the invalid combinations)
    single_layer_combs = [1,1,2,4] + [0]*(m-3)
    # current_layer_width = max(list(single_layer_combs.keys()))
    stack_total_combs = [0] * (m+1) # {}

    """
    number of ways to fill a single layer of size n is the sum of:
    1. ways to fill size n - 1 and add a 1-width block at the end
    2. ways to fill size n - 2 and add a 2-width block at the end
    3. ways to fill size n - 3 and add a 3-width block at the end
    4. ways to fill size n - 4 and add a 4-width block at the end
    """

    stack_valid_combs = [0] * (m+1) # {0: 0, 1: 0}
    stack_invalid_combs = [0] * (m+1) # {0: 0, 1: 0}
    # print('STACK_TOTAL_COMBS', stack_total_combs)

    for layer_width in range(0, m + 1):
        if layer_width >= 4:
            current_layer_combs = sum(single_layer_combs[layer_width-4:layer_width])
            single_layer_combs[layer_width] = current_layer_combs

        # number of ways to arrange a stack of logo blocks of height n
        # (ignoring the invalid combinations)
        stack_total_combs[layer_width] = (
             single_layer_combs[layer_width] ** n
        ) % MODULO

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
            )

        current_invalid_combs %= MODULO
        stack_invalid_combs[layer_width] = current_invalid_combs
        stack_valid_combs[layer_width] = (
            stack_total_combs[layer_width] - current_invalid_combs
        ) % MODULO

    print('SSL', single_layer_combs)
    return stack_valid_combs[m]

combs = legoBlocks(4, 4)
print('COMBS', combs)
