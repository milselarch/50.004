from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = list(set(nums))
    if len(nums) <= 1:
        return len(nums)

    sorted_nums = sorted(nums)
    consec_mapping = {}

    for k in range(len(nums) - 1):
        if sorted_nums[k] + 1 == sorted_nums[k + 1]:
            consec_mapping[sorted_nums[k]] = True
            consec_mapping[sorted_nums[k + 1]] = True

    consec_nums = sorted(list(consec_mapping.keys()))
    print(consec_nums)
    consec_length, max_consec_length = 1, 1

    for k in range(1, len(consec_nums)):
        if consec_nums[k] == consec_nums[k - 1] + 1:
            consec_length += 1
        else:
            consec_length = 1

        max_consec_length = max(
            consec_length, max_consec_length
        )

    return max_consec_length


if __name__ == '__main__':
    a = [-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]
    print(longestConsecutive(a))