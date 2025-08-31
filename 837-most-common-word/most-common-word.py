import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        counts = Counter(words)

        for b in banned:
            if b in counts:
                del counts[b]
        
        return max(counts, key=counts.get)
