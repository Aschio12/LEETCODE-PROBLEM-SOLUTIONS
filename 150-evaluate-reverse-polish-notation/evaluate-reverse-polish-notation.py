class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t in "+-*/":
                r_operand=stack.pop()
                l_operand=stack.pop()
                if t=="+":
                    stack.append(l_operand+r_operand)
                elif t=="-":
                    stack.append(l_operand-r_operand)
                elif t=="*":
                    stack.append(l_operand*r_operand)
                elif t=="/":
                    stack.append(int(l_operand/r_operand))
            else:
                stack.append(int(t))
        return stack[0]
