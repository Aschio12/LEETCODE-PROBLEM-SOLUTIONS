class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr=[]
        nums.sort()
        for i in range(len(nums)+1):
            if i>len(nums)-1 or i!=nums[i]:
                return i
        