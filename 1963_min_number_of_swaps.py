class Solution:
    def minSwaps(self, s: str) -> int:

        counter = 0
        swaps = 0

        for brackets in s:
            if brackets == '[':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                swaps += 1
                counter += 2
        
        return swaps