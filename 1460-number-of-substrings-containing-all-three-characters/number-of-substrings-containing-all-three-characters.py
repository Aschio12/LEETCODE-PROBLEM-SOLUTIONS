class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=defaultdict(int)
        n,l,ans=len(s),0,0
        for r in range(len(s)):
            d[s[r]]+=1
            while len(d)==3:
                ans+=n-r
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
        return ans
