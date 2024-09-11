# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n

        #two pointer method - binary search
        while i < j:
            mid = (i + j) // 2

            if isBadVersion(mid) == True:
                j = mid
                
            elif isBadVersion(mid) == False:
                i = mid + 1

        return i
