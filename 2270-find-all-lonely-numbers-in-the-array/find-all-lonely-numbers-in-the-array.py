class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans,d=[],defaultdict(int)
        c=Counter(nums)
        for i in nums:
            if c[i]==1 :
                if (i+1 not in c) and (i-1 not in c): 
                    ans.append(i)

        return ans
