from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d,current={0:1},0
        count=0
        for num in nums:
            current+=num
            if current-k in d:
                count+=d[current-k]
            if current in d:
                d[current]+=1
            else:
                d[current]=1
        return count
