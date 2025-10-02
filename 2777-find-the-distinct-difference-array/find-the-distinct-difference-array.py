from collections import defaultdict
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        ans,prefix=[],set()
        for j in range(len(nums)):
            prefix.add(nums[j])
            d[nums[j]]-=1
            if d[nums[j]]==0:
                del d[nums[j]]
            ans.append(len(prefix)-len(d))
        return ans
