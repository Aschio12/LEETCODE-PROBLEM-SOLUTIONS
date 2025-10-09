class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"[":1,"{":1,"(":1}
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack and i=="]" and stack[-1]=="[":
                    stack.pop()
                elif stack and i=="}" and stack[-1]=="{":
                    stack.pop()
                elif stack and i==")" and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
        return not stack

