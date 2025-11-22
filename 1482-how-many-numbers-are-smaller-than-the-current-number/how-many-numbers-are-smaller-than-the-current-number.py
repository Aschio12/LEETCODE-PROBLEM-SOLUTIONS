class Solution:
    def smallerNumbersThanCurrent(self, num: List[int]) -> List[int]:
        less={}
        nums=sorted(num)
        for index,val in enumerate(nums):
                if val not in less:
                    less[val]=index
        ans=[0]*len(num)
        for i in range(len(num)):
            ans[i]=less[num[i]]
        return ans

                
                