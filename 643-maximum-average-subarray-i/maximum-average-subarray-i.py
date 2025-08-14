class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot=sum(nums[:k])
        current=tot
        for i in range(k,len(nums)):
            tot=tot-nums[i-k]+nums[i]
            current=max(current,tot)
        return current/k
