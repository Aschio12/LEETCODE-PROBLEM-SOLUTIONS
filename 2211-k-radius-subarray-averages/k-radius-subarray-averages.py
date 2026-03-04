class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix,p=[nums[0]],0
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        
        ans=[]
        for i in range(len(prefix)):
            if i-k<0 or i+k>len(nums)-1:
                ans.append(-1)
            else:
                if i-k==0:
                    ans.append(int((prefix[i+k])/(2*k+1)))
                else:
                    ans.append(int((prefix[i+k]-prefix[i-k-1])/(2*k+1)))
        return ans 
        
        