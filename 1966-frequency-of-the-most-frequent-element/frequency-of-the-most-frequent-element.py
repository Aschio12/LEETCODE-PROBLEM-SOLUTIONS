class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,ans,p=0,0,0
        for r in range(len(nums)):
            p+=nums[r]
            while nums[r]*(r-l+1)-p>k:
                p-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans 
