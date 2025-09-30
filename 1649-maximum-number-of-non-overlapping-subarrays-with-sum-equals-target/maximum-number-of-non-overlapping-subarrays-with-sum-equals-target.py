from collections import defaultdict
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        remainder=defaultdict(int)
        remainder[0]=-1
        right,p,ans=-1,0,0
        for r in range(len(nums)):
            p+=nums[r]
            if p-target in remainder and remainder[p-target]>=right:
                ans+=1
                right=r
            remainder[p]=r
        return ans
