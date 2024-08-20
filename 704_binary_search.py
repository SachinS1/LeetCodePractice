from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0 #left pointer
        j = len(nums) - 1 #right pointer

        
        while i <= j:
            mid = (i + j)//2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                i = mid + 1

            else:
                j = mid - 1
        
        return -1
