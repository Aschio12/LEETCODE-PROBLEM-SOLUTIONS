class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        ans,l=0,0
        for r,char in enumerate(s):
            if char in dic:
                l=max(l,dic[char]+1)
            dic[char]=r
            ans=max(ans,r-l+1)
        return ans
            
                
                

            