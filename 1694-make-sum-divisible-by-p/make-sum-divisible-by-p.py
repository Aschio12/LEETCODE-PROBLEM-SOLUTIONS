class Solution:
    def minSubarray(self, nums: List[int], l: int) -> int:
        rem=sum(nums)%l
        print(sum(nums),rem)
        ans,p,d=float("inf"),0,defaultdict(int)
        d[0]=-1
        if rem==0:
            return 0
        if sum(nums)<l:
            return -1
        for r in range(len(nums)):
            p=(p+nums[r])%l
    
            if (p-rem)%l in d:
                ans=min(ans,r-d[(p-rem)%l])
            d[p]=r
        return ans if ans < len(nums) else -1

            
