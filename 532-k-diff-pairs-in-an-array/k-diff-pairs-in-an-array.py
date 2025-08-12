from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dit=Counter(nums)
        n=list(set(nums))
        if k<0:
            return 0
        elif k==0:
            return sum(1 for count in dit.values() if count>=2)
        else:
            return sum(1 for num in n if num+k in n)

                   