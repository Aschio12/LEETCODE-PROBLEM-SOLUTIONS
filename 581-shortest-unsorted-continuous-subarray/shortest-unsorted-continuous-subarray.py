class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        l,r=len(nums),float("-inf")
        for i in range(len(nums)):
            if nums[i]!=nums2[i]:
                l=min(l,i)
                r=max(r,i)
        return 0 if l==len(nums) else r-l+1
