from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        biggestSum = nums[0]

        for num in nums:

            if runningSum < 0:
                runningSum = num
            else:
                runningSum += num
            
            biggestSum = max(runningSum, biggestSum)
            
        return biggestSum
        
        # #this approach outputs the subarray and the sum
        # #sum of the subarray
        # runningSum = 0
        # subarray = []
        # biggestSum = nums[0]

        # for i in range(0, len(nums)):

        #     if runningSum < 0:
        #         #clear the subarray
        #         subarray.clear()
        #     subarray.append(nums[i])

        #     runningSum = sum(subarray)

        #     if runningSum > biggestSum:
        #         biggestSum = runningSum
            
        # return biggestSum