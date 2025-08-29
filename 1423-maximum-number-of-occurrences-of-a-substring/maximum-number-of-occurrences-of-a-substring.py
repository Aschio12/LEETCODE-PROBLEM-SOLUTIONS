from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans=defaultdict(int)
        d=defaultdict(int)
        l,count=0,0
        for r in range(len(s)):
            d[s[r]]+=1
            while r-l+1>maxSize:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            while r-l+1>=minSize and r-l+1<=maxSize:
                if len(d)<=maxLetters:
                    ans[s[l:r+1]]+=1
                else:
                    d[s[l]]-=1
                    if d[s[l]]==0:
                        del d[s[l]]
                    l+=1
                    break
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
                
        return max(ans.values()) if ans else 0
