class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n,r,l,diff=len(nums),0,0,nums[-1]-nums[0]
        left,right=[0],[0]
        for i in range(1,n):
            l+=(nums[i]-nums[i-1])*i
            left.append(l)
            r+=(nums[n-i]-nums[n-i-1])*i
            right.append(r)
        right=right[::-1]
        return [left[i] + right[i] for i in range(n)]

        