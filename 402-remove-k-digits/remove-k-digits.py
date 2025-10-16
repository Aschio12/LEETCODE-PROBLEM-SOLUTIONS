class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums=list(map(int,num))
        stack=[nums[0]]
        for i in range(1,len(nums)):
            while stack and nums[i]<stack[-1] and k>0:
                stack.pop()
                k-=1
            stack.append(nums[i])
        while k>0 and stack:
            stack.pop()
            k-=1
        while stack and stack[0]==0:
            stack.pop(0)

        return "".join(list(map(str,stack))) if stack else "0"
        
        
            
