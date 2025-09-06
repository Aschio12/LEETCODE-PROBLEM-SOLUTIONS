class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        l,r=0,tot
        ans=[]
        for i in range(len(nums)):
            if i==0:
                l=0
                r-=nums[i]
            elif i==len(nums)-1:
                r=0
                l+=nums[i-1]
            else:
                l+=nums[i-1]
                r-=(nums[i])
            if l==r:
                ans.append(i)
        return ans[0] if ans else -1