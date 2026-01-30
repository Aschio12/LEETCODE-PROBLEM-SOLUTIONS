class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        majority,counter=n/2,{}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
            if counter[num]>majority:
                    return num
        
        
