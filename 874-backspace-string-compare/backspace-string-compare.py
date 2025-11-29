class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
            stack_s,stack_t=[],[]
            for ss in s:
                if ss!="#":
                    stack_s.append(ss)
                else:
                    if stack_s:
                        stack_s.pop()
            for tt in t:
                if tt!="#":
                    stack_t.append(tt)
                else:
                    if stack_t:
                        stack_t.pop()
            return stack_s==stack_t
            
                
