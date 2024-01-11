from typing import List


def longestConsecutive(nums: List[int]) -> int:
    hashset = set(nums)
    nums = list(hashset)
    if len(nums) <= 1:
        return len(nums)

    longest = 0
    for k in range(len(nums)):
        length = 0

        while nums[k + length] + 1 in hashset:
            length += 1

        longest = max(longest, length)

    return longest


if __name__ == '__main__':
    a = [-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]
    print(longestConsecutive(a))