class Solution:
    def rob(self, nums: list[int]) -> int:
        def dp(i: int, memo=None):
            if memo is None:
                memo = {}

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]

            curr_left = nums[i - 1]
            curr_right = nums[i]

            memo[i] = max(
                dp(i - 2, memo) + curr_right,
                dp(i - 3, memo) + curr_left,
            )

            return memo[i]

        return dp(len(nums) - 1)