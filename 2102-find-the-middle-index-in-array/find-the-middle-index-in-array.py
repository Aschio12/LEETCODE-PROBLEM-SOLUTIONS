class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum,tot=0,sum(nums)
        for i in range(len(nums)):
            if leftsum==tot-leftsum-nums[i]:
                return i
            leftsum+=nums[i]
        return -1
        

        