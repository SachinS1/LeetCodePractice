from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        out = []
        prefixXOR = [0] * len(arr)
        prefixXOR[0] = arr[0]
        for i in range(1, len(arr)):
            prefixXOR[i] = prefixXOR[i-1] ^ arr[i]

        for i, j in queries:
            if i == 0:
                out.append(prefixXOR[j])
            else:
                out.append(prefixXOR[j] ^ prefixXOR[i-1])        


        return out
