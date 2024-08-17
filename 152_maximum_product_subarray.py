from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # 53 was finding sum for a subarray.
        # this is the product.
        # We need to focus on cases when negative numbers are involved.
        # maxProd and minProd variable to store max and min products.
        # minProd is specially for cases when a negative number is followed
        # by another negative number.

        maxProd = nums[0]
        minProd = nums[0]
        totProd = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxProd, minProd = minProd, maxProd #flip max and min if there is a negative
    
            maxProd = max(num, num*maxProd)
            minProd = min(num, num*minProd)
            totProd = max(totProd, maxProd)    
            
        return totProd
