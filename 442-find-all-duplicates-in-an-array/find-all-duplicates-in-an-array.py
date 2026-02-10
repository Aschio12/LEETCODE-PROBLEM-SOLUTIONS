class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=set()
        for num in nums:
            index,val=abs(num)-1,abs(num)
            if nums[index]<0:
                ans.add(val)
            else:
                nums[index]*=-1
        return list(ans)