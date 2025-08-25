
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l,ans=0,0
        nums.sort()
        for r in range(1,len(nums)):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                ans=max(ans,r-l+1)
        return ans
