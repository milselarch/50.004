from typing import List



class Solution:
    def max_profit(
        self, nums: List[int], n, start_rob=False, end_rob=False,
        cache=None
    ):
        cache = {} if cache is None else cache
        cache_key = (n, start_rob, end_rob)

        if cache_key in cache:
            return cache[cache_key]

        max_index = len(nums) - 1
        if n > max_index:
            return 0

        if n == 0:
            if start_rob or end_rob:
                return self.max_profit(
                    nums, n + 1, start_rob, end_rob, cache=cache
                )
            else:
                house_profit = nums[n]
                future_profit1 = self.max_profit(
                    nums, n + 2, start_rob=True, end_rob=end_rob, cache=cache
                )
                future_profit2 = self.max_profit(
                    nums, n + 1, start_rob, end_rob, cache=cache
                )
                max_profit = max(
                    house_profit + future_profit1, future_profit2
                )

                cache[cache_key] = max_profit
                return max_profit

        if (n == 1) and start_rob:
            return self.max_profit(
                nums, n + 1, start_rob, end_rob, cache=cache
            )
        if (n >= max_index - 1) and end_rob:
            return 0

        new_end_rob = False
        new_start_rob = False
        house_profit = nums[n]
        if n == max_index:
            new_end_rob = True
        if n == 0:
            new_start_rob = True

        future_profit1 = self.max_profit(
            nums, n + 2, start_rob=new_start_rob,
            end_rob=new_end_rob, cache=cache
        )
        future_profit2 = self.max_profit(
            nums, n + 1, start_rob=new_start_rob,
            end_rob=new_end_rob, cache=cache
        )
        max_profit = max(
            house_profit + future_profit1, future_profit2
        )

        cache[cache_key] = max_profit
        return max_profit

    def rob(self, nums: List[int]) -> int:
        return self.max_profit(nums=nums, n=0)