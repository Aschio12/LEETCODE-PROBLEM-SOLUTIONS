class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found=False
        for i in range(len(nums)):
            if nums[i]==0 and not found:
                found=True
                holder=i
            elif nums[i]!=0:
                if found:
                    nums[i],nums[holder]=nums[holder],nums[i]
                    while nums[holder]!=0 and holder<i:
                        holder+=1
                    
                
        