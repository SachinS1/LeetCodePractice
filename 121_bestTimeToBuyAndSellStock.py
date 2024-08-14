from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 #initialize maximum profit in the beginning

        minPrice = prices[0] #track the minimum price

        for i in range(0, len(prices)):

            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
            elif prices[i]<minPrice:
                minPrice = prices[i]
            
        return maxProfit