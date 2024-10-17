from typing import List
import heapq
from heapq import heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        elems = []

        for num in nums:
            heapq.heappush(elems, -num)

        for _ in range(k):
            element = heappop(elems)

        return element * -1

        #quickselect solution from neetcode.io

        # k = len(nums) - k

        # def quickSelect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p],nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k: return quickSelect(l, p - 1)
        #     elif p < k: return quickSelect(p+1, r)
        #     else:       return nums[p]
        
        # return quickSelect(0, len(nums) - 1)




        

         

        