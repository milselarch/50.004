import copy
import random

from library import FixedArray
from library import Queue


def scramble(string):
    char_arr = copy.deepcopy(list(string.items))
    random.shuffle(char_arr)
    return FixedArray(char_arr)


def swap(s: FixedArray, k):
    print(s, k, s[k+1], s[k], s[k+2:])
    return s[:k-1] + FixedArray(s[k + 1], s[k]) + s[k + 2:]


def min_swaps(scrambled, original):
    distance_cache = {}
    n = len(original)

    queue = Queue()
    distance_cache[scrambled] = 0
    queue.put(scrambled)

    while True:
        word = queue.pop()
        distance = distance_cache[word]
        print(word, distance)

        if word == original:
            print(len(distance_cache))
            return distance

        for k in range(1, n):
            # for k from 1 to n - 1 (inclusive)
            swapped = swap(word, k)
            if swapped in distance_cache:
                continue

            distance_cache[swapped] = distance + 1

            # print(swapped)
            assert len(swapped) == n
            queue.put(swapped)


if __name__ == '__main__':
    random.seed(22232)
    target_word = FixedArray(list('potato'))
    new_word = scramble(target_word)
    # print(target_word, new_word)

    distance = min_swaps(new_word, target_word)
    # print(distance)