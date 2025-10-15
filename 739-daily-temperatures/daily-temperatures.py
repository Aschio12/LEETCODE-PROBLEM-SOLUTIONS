class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(tem)
        for index,val in enumerate(tem):
            while stack and val>tem[stack[-1]]:
                prev=stack.pop()
                ans[prev]=index-prev
            stack.append(index)
        return ans
