from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d=defaultdict(int)
        l,count=0,0
        for r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            count=max(count,r-l+1)
        return count

