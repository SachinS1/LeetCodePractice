from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        #sum of all rolls
        total_sum = (len(rolls) + n) * mean
        #sum of n rolls
        sum_n_rolls = total_sum - sum(rolls)
        
        
        #if sum of n rolls is greater than n * 6 or less than n return []
        #dice values can only be 1-6
        if sum_n_rolls > n * 6 or sum(rolls) > total_sum or sum_n_rolls < n:
            return []
        
        remainder = sum_n_rolls % n
        base_value = sum_n_rolls // n

        return [base_value + 1 if i < remainder else base_value for i in range(n)]

        #longer version of the same code
        # for _ in range(0, n):
        #     if 0 < sum_n_rolls//n + remainder < 7:
        #         number = sum_n_rolls//n + remainder
        #     else:
        #         number = sum_n_rolls//n
        #     remainder = sum_n_rolls % n
        #     sum_n_rolls -= number
        #     n -= 1
        #     m_observations.append(number)
            
        # return m_observations
