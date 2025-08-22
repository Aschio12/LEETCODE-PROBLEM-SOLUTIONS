from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ss=defaultdict(int)
        tt=defaultdict(int)
        for i in t:
            tt[i]+=1
        count,l,start,min_len=len(tt),0,0,len(s)+1
        for r in range(len(s)):
            ss[s[r]]+=1
            if s[r] in tt and ss[s[r]]==tt[s[r]]:
                count-=1
            while count==0:
                if r-l+1<min_len:
                    min_len=r-l+1
                    start=l
                ss[s[l]]-=1
                if s[l] in tt and ss[s[l]]<tt[s[l]]:
                    count+=1
                l+=1
        return s[start:start+min_len] if min_len!=len(s)+1 else ""