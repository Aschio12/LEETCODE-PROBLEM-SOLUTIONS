class Solution:
    def decrypt(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            current=0
            if k>0:
                l=(i+1)%n
                for j in range(abs(k)):
                    current+=nums[l%n]
                    l+=1
                ans.append(current)
            elif k<0:
                l=(i-1)%n
                for j in range(abs(k)):
                    current+=nums[l%n]
                    l-=1
                ans.append(current)
            else:
                ans.append(0)
        return ans