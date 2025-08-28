class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count,l,tot=0,0,0
        for r in range(len(arr)):
            tot+=arr[r]
            if r-l+1==k:
                if tot/k>=threshold:
                    count+=1
                tot-=arr[l]
                l+=1
        return count