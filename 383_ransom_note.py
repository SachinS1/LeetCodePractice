from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazine_count = {}

        # for letters in magazine:
        #     if letters not in magazine_count:
        #         magazine_count[letters] = 1
        #     else:
        #         magazine_count[letters] += 1
        
        magazine_count = Counter(magazine) #using counter from collections

        for letters in ransomNote:
            if letters not in magazine_count or magazine_count[letters] == 0:
                return False
            else:
                magazine_count[letters] -= 1
            
        return True