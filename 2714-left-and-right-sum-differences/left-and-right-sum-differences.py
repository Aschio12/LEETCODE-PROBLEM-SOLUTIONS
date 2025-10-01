class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        p,m,ans=0,sum(nums),[]
        for i in range(len(nums)):
            p+=nums[i]
            ans.append(abs((m-p)-(p-nums[i])))
        return ans
        
