class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n_1 = len(word1)
        n_2 = len(word2)
        
        n = min(n_1, n_2)

        rslt = ""

        for i in range(0, n):
            rslt += word1[i] + word2[i]

        if n_1 > n_2:
            return rslt + word1[n_2:]
        
        else:
            return rslt + word2[n_1:]