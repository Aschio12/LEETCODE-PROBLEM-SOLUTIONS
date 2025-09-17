class Solution:
    def maxScore(self, s: str) -> int:
        ans,c0,c1,r=0,0,0,0
        right1=[]
        left0=[]
        l,r=0,len(s)-1
        while l<len(s)-1 and r>0:
            if int(s[l])==0:
                c0+=1
                left0.append(c0)
            else:
                left0.append(c0)
            if int(s[r])==1:
                c1+=1
                right1.append(c1)
            else:
                right1.append(c1)
            l+=1
            r-=1
        right1=right1[::-1]
        for i,j in zip(left0,right1):
            ans=max(ans,i+j)
        return ans
