class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_brace=[]
        stack_star=[]
        for i,ele in enumerate(s):
            if ele == "(":
                stack_brace.append(i)
            elif ele == "*":
                stack_star.append(i)
            else:
                if stack_brace:
                    stack_brace.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
            
        while stack_brace and stack_star:
            if stack_brace[-1]<stack_star[-1]:
                stack_brace.pop()
                stack_star.pop()
            else:
                break
        return not stack_brace
