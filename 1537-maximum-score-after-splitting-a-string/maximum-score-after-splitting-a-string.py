class Solution:
    def maxScore(self, s: str) -> int:
        ans,c0,c1,r=0,0,0,0
        if int(s[r])==0:
            c0+=1
        r+=1
        for i in range(1,len(s)):
            if int(s[i])==1:
                c1+=1
        ans=max(ans,c0+c1)
        while r<len(s)-1:
            if int(s[r])==0:
                c0+=1
            else:
                c1-=1
            ans=max(ans,c0+c1)
            r+=1
        return ans
            
        
        
