class Solution:

    def countChars(self, s):
        count = {}

        for letters in s:
            count[letters] = count.get(letters, 0) + 1
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        count_1 = self.countChars(s)
        count_2 = self.countChars(t)

        return count_1 == count_2