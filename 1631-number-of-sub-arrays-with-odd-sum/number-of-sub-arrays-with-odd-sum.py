class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans,odd,even,current=0,0,0,0
        for i in arr:
            current+=i
            if current%2!=0:
                ans+=even+1
                odd+=1
            else:
                ans+=odd
                even+=1
        return ans%(10**9 + 7)
            
