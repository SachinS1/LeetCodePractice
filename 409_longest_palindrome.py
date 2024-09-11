class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_map = {}

        for letters in s:
            if letters in str_map:
                str_map[letters] += 1
            else:
                str_map[letters] = 1
        longest_palindrome = 0

        can_add_center = False

        for keys in str_map:
            if str_map[keys] % 2 == 0:
                longest_palindrome += str_map[keys]
            else:
                longest_palindrome += str_map[keys] - 1
                can_add_center = True
        
        if can_add_center:
            longest_palindrome += 1

        return longest_palindrome 