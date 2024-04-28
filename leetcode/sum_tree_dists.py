from collections import deque, defaultdict
from typing import List


class Solution:
    @staticmethod
    def sum_of_distances_in_tree(n: int, edges: List[List[int]]) -> List[int]:
        nmap = defaultdict(set)

        for n1, n2 in edges:
            nmap[n1].add(n2)
            nmap[n2].add(n1)

        TREE_CACHE = {}
        SUM_CACHE = {}

        def get_tree_size(start, block=None):
            tree_key = (start, block)
            if tree_key in TREE_CACHE:
                return TREE_CACHE[tree_key]

            if block is not None:
                generic_key = (start, None)

                if generic_key in TREE_CACHE:
                    main_size = TREE_CACHE[generic_key]
                    cutoff_tree_size = get_tree_size(block, start)
                    size = main_size - cutoff_tree_size
                    TREE_CACHE[tree_key] = size
                    return size

            size = 1
            neighbors = nmap[start]

            for neighbor in neighbors:
                if neighbor == block:
                    continue

                sub_size = get_tree_size(neighbor, start)
                size += sub_size

            TREE_CACHE[tree_key] = size
            return size

        def get_sum_dist(start, block=None):
            sum_key = (start, block)
            print('KEY', sum_key, len(SUM_CACHE))

            if sum_key in SUM_CACHE:
                return SUM_CACHE[sum_key]

            if block is not None:
                generic_key = (start, None)

                if generic_key in SUM_CACHE:
                    main_sum = SUM_CACHE[generic_key]
                    sub_sum = get_sum_dist(block, start)
                    main_sum -= (
                        sub_sum + get_tree_size(block, start)
                    )
                    SUM_CACHE[sum_key] = main_sum
                    return main_sum

            total_sum = 0
            neighbors = nmap[start]

            for neighbor in neighbors:
                if neighbor == block:
                    continue

                sub_sum = get_sum_dist(neighbor, start)
                num_neighbors = get_tree_size(neighbor, start)
                total_sum += sub_sum + num_neighbors

            SUM_CACHE[sum_key] = total_sum
            return total_sum

        answers = []
        for k in range(n):
            dist = get_sum_dist(k)
            answers.append(dist)

        # print(TREE_CACHE, SUM_CACHE)
        return answers


if __name__ == '__main__':
    n = 30000
    edges = [[0, k] for k in range(n)]
    ans = Solution.sum_of_distances_in_tree(n, edges)
    print('ANS', ans)



