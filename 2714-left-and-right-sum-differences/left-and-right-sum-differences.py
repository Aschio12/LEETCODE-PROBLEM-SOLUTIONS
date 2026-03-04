class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre,post=[0],[]
        current,tot=nums[0],sum(nums)
        for i in range(1,len(nums)):
            pre.append(current)
            post.append(tot-current)
            current+=nums[i]
        post.append(tot-current)

        ans=[]
        for i in range(len(pre)):
            ans.append(abs(pre[i]-post[i]))
        return ans

        return pre
        
