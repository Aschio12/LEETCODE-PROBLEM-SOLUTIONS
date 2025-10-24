class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        popo=deque(popped)
        for r in range(len(pushed)):
            stack.append(pushed[r])
            while stack and stack[-1]==popo[0]:
                stack.pop()
                popo.popleft()
        return len(popo)==0