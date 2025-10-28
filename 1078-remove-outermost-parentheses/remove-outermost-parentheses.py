class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=""
        for i in range(len(s)):
            if s[i]=="(":
                if stack:
                    ans+=s[i]
                stack.append(s[i])
            else:
                stack.pop()
                if stack:
                    ans+=s[i]
                
            
        return ans