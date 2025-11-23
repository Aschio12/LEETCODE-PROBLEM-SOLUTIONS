class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isdigit() and stack:
                stack.pop()
            else:
                stack.append(s[i])
        ans="".join(stack)
        return ans
