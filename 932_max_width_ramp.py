from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0
        #stores the max for the suffix
        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1

        rampWidth = 0

        l = 0

        for r in range(len(nums)):
            #sees if there is a number greater than the current one
            while nums[l] > max_right[r]:
                l += 1
            rampWidth = max(rampWidth, r - l)
        return rampWidth