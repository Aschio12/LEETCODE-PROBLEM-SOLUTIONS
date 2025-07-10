from collections import defaultdict
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dif=defaultdict(list)
        if x==0:
            return(arr[:k])
        for i in range(len(arr)):
            dif[abs(arr[i]-x)].append(arr[i])
        diff=dict(sorted(dif.items()))
        ans=[]
        for i in diff:
            ans+=diff[i]
        return(sorted(ans[:k]))
