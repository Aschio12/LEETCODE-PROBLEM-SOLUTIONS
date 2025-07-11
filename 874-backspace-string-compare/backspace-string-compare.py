class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(arg):
            stack=[]
            for i in arg:
                if i=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)
        return(f(s)==f(t))

            
