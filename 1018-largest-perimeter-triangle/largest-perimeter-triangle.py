class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        srt=nums.sort()
        ans=0
        for i in range(1,len(nums)-1):
            if nums[i-1]+nums[i]>nums[i+1]:
                ans=max(ans,nums[i-1]+nums[i]+nums[i+1])
        return ans