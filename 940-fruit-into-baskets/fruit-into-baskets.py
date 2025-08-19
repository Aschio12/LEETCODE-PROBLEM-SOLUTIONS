from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count,ans,l=2,0,0
        d=defaultdict(int)
        for r in range(len(fruits)):
            if d[fruits[r]]==0:
                count-=1
            d[fruits[r]]+=1
            while count==-1:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    count+=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
                
