class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split("/")
        stack=[]
        for ch in s:
            if ch=="..":
                if stack:
                    stack.pop()
            elif ch!="." and ch!="":
                stack.append(ch)
        return "/"+"/".join(stack)