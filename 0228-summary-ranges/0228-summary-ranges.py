class Solution(object):
    def summaryRanges(self, nums):
        result = []
        start = 0
        for end, n in enumerate(nums):
            if (end == len(nums) - 1 or nums[end + 1] - n != 1):
                if start == end:
                    result.append(str(n))
                else:
                    result.append(str(nums[start]) + "->" + str(n))
                start = end + 1
        return result