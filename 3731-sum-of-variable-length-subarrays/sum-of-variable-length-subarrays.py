class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            current=nums[max(0,i-nums[i]):i+1]
            ans+=sum(current)
        return ans