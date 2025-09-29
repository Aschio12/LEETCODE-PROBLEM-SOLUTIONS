class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix=[]
        for i in range(len(nums)):
            current=0
            for j in range(i,len(nums)):
                current+=nums[j]
                prefix.append(current)

        prefix.sort()
        return sum(prefix[left-1:right])%(10**9 + 7)
