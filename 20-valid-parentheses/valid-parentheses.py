class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"]":"[","}":'{',")":'('}
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if not stack or stack[-1] != d[i] :
                    return False
                
                stack.pop()
                
        return not stack

