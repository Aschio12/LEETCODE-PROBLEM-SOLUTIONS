class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current=defaultdict(int)
        ans=0
        l=0
        for r ,val in enumerate(s):
            current[val]+=1
            while current[val]>1:
                current[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans