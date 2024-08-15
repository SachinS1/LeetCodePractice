from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #array to store products left of the current elements
        leftProd = [1]*len(nums)
        #the first element is 1. No left elements before the first element.

        for i in range(1, len(nums)):
            leftProd[i] = leftProd[i-1] * nums[i-1]

        j = len(nums) - 1 
        rightProd = 1

        prod = [None] * len(nums)
        
        while(j >= 0):
            prod[j] = leftProd[j] * rightProd
            rightProd = rightProd * nums[j]
            j -= 1

        return prod