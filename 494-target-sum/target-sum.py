class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        @cache
        def backtrack(idx,current):
            if idx==n:
                if current==target:
                    return 1
                return 0
            
            left=backtrack(idx+1,current+nums[idx])
            right=backtrack(idx+1,current-nums[idx])

            return left+right

        return backtrack(0,0)