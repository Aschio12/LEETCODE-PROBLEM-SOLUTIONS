class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average=[]
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            average.append((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return min(average)