class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        num1="".join([chr(item) for item in nums1])
        num2="".join([chr(item) for item in nums2])
        l,ans=0,0
        for i in range(1,len(num1)+1):
            if num1[l:i] in num2:
                ans=max(ans,i-l)
            elif l<i:
                l+=1
        return ans