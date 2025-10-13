class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        check=[]
        for i in range(1,n+1):
            if target==check:
                break
            if i in target:
                stack.append("Push")
                check.append(i)
            else:
                stack.append("Push")
                stack.append("Pop")
        return stack

        