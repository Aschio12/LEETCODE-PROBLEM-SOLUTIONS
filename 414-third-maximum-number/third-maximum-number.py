class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp=list(set(nums))
        temp.sort(reverse=True)
        if len(temp)>=3:
            return(temp[2])
        else:
            return(temp[0])