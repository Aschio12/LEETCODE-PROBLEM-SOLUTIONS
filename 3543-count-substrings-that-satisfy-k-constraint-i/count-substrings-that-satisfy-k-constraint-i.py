class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count1,count0=0,0
        l,ans=0,0
        for r in range(len(s)):
            if s[r]=="1":
                count1+=1
            else:
                count0+=1 
            while (count1>k and count0>k) and l<=r:
                if s[l]=="1":
                    count1-=1
                else:
                    count0-=1
                l+=1
            ans+=r-l+1
        return ans
                