class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res=0
        i=1
        while i <len(arr)-1:
            c=False
            if arr[i-1]<arr[i]>arr[i+1]:
                l,r=i,i
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while  r+1<len(arr) and arr[r]>arr[r+1]:
                    r+=1
                    c=True
                res=max(res,(r-l+1))
            if c:
                i=r+1
            else:
                i+=1
        return res
            
                
           


