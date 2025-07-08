from collections import defaultdict
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        d=defaultdict(list)
        for i,val in enumerate(s):
            d[val].append(i)
        index=d[c]
        ans=[]
        for i in range(len(s)):
            mini=float("inf")
            for j in index:
                mini=min(mini,abs(i-j))
            ans.append(mini)
        return ans
            