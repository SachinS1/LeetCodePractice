from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        # nums = [str(i) for i in range(1, n+1)]

        current_num = 1
        nums = []
        
        for _ in range(1, n+1):
            nums.append(current_num)
            if current_num * 10 <= n:
                current_num *= 10
            else:
                if current_num >= n:
                    current_num //= 10
                current_num += 1

                while current_num % 10 == 0:
                    current_num //= 10

        return nums

            
