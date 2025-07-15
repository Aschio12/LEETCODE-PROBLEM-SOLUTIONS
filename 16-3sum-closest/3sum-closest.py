class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closet=None
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if closet is None or abs(s-target)<abs(closet-target):
                    closet=s
                if s==target:
                    return s
                if s<target:
                    l+=1
                else:
                    r-=1
        return closet
