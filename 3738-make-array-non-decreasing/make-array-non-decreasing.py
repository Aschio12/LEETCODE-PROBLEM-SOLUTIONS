class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        prev,ans,stack=0,0,[]
        for num in nums:
            if num>=prev:
                ans+=1
                prev=num
        return ans
        