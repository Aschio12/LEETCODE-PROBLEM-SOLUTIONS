class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for op in ops:
            if op=="D":
                stack.append(2*stack[-1])
            elif op=="C":
                stack.pop()
            elif op=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))

        return sum(stack) if stack else 0