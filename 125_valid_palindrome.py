class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for letters in s:
            
            if letters.isalpha():
                new_string += letters.lower()
        return new_string == new_string[::-1]
