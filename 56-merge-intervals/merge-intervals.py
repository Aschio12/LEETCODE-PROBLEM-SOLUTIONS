class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        start,end=intervals[0][0],intervals[0][1]
        for char in range(1,len(intervals)):
            left,right=intervals[char][0],intervals[char][1]
            if left<=end:
                end=max(end,right)
            else:
                ans.append([start,end])
                start,end = left,right
        ans.append([start,end])
                
        
        return ans


        