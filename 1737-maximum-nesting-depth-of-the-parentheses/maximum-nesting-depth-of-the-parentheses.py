class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count,ans=0,0
        for sy in s:
            if sy=="(":
                stack.append(sy)
                count+=1
            elif sy==")":
                stack.pop()
                count-=1
            ans=max(ans,count)
        return ans
