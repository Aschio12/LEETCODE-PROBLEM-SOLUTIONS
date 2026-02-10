class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=set()
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
            if d[num]>1:
                ans.add(num)
        return list(ans)
