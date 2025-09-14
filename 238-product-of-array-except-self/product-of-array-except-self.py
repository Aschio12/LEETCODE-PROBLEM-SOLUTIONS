class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c0,prod=0,1
        for i in nums:
            if i!=0:
                prod*=i
            else:
                c0+=1
        ans=[]
        if c0==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    ans.append(prod)
                else:
                    ans.append(0)
        elif c0==0:
            for i in range(len(nums)):
                ans.append(prod//nums[i])
        else:
            ans=[0]*len(nums)
        return ans
