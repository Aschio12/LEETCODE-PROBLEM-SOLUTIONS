class Solution:
    def findIndices(self, nums: List[int], index: int, value: int) -> List[int]:
        i,j=0,index
        while i<len(nums):
            while j<len(nums):
                if abs(nums[i]-nums[j])>=value:
                    return([i,j])
                j+=1
            i+=1
            j=i+index
        return([-1,-1])
        
