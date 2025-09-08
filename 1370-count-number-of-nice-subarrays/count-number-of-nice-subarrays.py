class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        f=defaultdict(int)
        f[0]=1
        prefix,count=0,0
        for num in nums:
            prefix+=1 if num%2==1 else 0
            if prefix-k in f:
                count+=f[prefix-k]
            f[prefix]+=1
        return count
        

