class Solution:

    #memoization technique with recursion
    def __init__(self):
        self.memoize = {}

    def climbStairs(self, n: int) -> int:
        
        #base case
        if n == 1 or n == 2:
            return n

        if n in self.memoize:
            return self.memoize[n]
        else:
            result = self.climbStairs(n-2) + self.climbStairs(n-1)
        self.memoize[n] = result

        return result

    #bottoms up dynamic programming
    def climbStairs_dp(self, n: int) -> int:
        #base case
        if n == 1 or n == 2:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]