class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n,real_dif=len(nums),sum(nums)-x
        if real_dif==0:
            return n
        l,ans,current=0,0,0
        for r,val in enumerate(nums):
            current+=val
            while l<=r and current>real_dif:
                current-=nums[l]
                l+=1
            if current==real_dif:
                ans=max(ans,r-l+1)

        return n - ans if ans!=0 else -1


        

      