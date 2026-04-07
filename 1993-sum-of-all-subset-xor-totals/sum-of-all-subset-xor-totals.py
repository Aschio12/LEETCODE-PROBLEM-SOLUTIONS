class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        tot,n=0,len(nums)
        def back(idx,current):
            nonlocal tot
            if idx==n:
                tot+=current
                return
            back(idx+1,current^nums[idx])
            back(idx+1,current)

        back(0,0)
        return tot