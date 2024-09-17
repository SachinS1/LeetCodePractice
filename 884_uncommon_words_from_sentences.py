from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        combined = s1.split() + s2.split()
        freq = Counter(combined)

        return [word for word, count in freq.items() if count == 1]