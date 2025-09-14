class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_,conver,score=float("-inf"),0,0
        ans=[]
        prefix=[0]
        for i in range(len(nums)):
            max_=max(max_,nums[i])
            conver=nums[i]+max_
            score=conver+prefix[-1]
            prefix.append(score)
            ans.append(score)
        return ans