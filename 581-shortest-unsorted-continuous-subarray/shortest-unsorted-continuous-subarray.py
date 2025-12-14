class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n,stack=len(nums),[]
        l=n
        mx=float("-inf")
        for index,val in enumerate(nums):
            while stack and stack[-1][1]>val:
                tup=stack.pop()
                l=min(l,tup[0])
                mx=max(mx,tup[1])
            stack.append((index,val))
        if l==n:
            return 0 
        end=0
        for i in range(n-1,-1,-1):
            if nums[i]<mx:
                end=i
                break
        return end-l+1
            


