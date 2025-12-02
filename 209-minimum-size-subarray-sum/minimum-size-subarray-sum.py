class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def twoSum(arr,targ):
            left=0
            tot,length=0,float("inf")
            for right in range(len(arr)):
                tot+=arr[right]       
                while tot>=targ:
                    length=min(length,right-left+1)
                    tot-=arr[left]
                    left+=1
            return(length if length!=float("inf") else 0)
        return twoSum(nums,target)