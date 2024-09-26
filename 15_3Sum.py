from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        threeSum = set()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1

            while j < k:
                tot_sum = nums[i] + nums[j] + nums[k]
                if tot_sum == 0:
                    threeSum.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:    
                        k -= 1
                    j += 1
                    k -= 1
                elif tot_sum < 0:
                    j += 1
                else:
                    k -= 1
        
        return [list(triplet) for triplet in threeSum]