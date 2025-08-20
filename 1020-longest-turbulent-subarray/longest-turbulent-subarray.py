class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,ans=0,0
        if len(arr)<=1:
            return len(arr)
        for r in range(1,len(arr)):
            if arr[r]==arr[r-1]:
                l=r
            elif (arr[r]>arr[r-1])==(arr[r-1]>arr[r-2]):
                l=r-1
            ans=max(ans,r-l+1)
                
            
        return ans

           
