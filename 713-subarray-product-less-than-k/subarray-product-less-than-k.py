class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        current,count,l=1,0,0

        for r in range(len(nums)):
            current*=nums[r]
            while current>=k and l<r:
                current/=nums[l]
                l+=1
            if current<k:
                count+=(r-l+1)
        return count
            