class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0:
            return(nums)
        temp=[0]*len(nums)
        i=0
        for t in range(len(nums)-k,len(nums)):
            temp[i]=nums[t]
            i+=1
        l=k
        for j in range(len(nums)-k):
            temp[l]=nums[j]
            l+=1
        for g in range(len(temp)):
            nums[g]=temp[g]
        