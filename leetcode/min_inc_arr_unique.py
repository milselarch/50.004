from typing import List


class Solution:
    @staticmethod
    def min_increment_for_unique(nums: List[int]) -> int:
        nums = sorted(nums)
        unique_nums = set()
        prev_num = float('-inf')
        moves = 0

        for orig_num in nums:
            if prev_num < orig_num:
                carry = 0
            else:
                print("OP", orig_num, prev_num)
                assert prev_num >= orig_num
                carry = 1 + prev_num - orig_num

            num = carry + orig_num
            unique_nums.add(num)
            prev_num = num
            moves += carry

        return moves


if __name__ == '__main__':
    # test = [1, 2, 2]
    test = [3, 2, 1, 2, 1, 7]
    solution = Solution()
    moves = solution.min_increment_for_unique(test)
    print(moves)
