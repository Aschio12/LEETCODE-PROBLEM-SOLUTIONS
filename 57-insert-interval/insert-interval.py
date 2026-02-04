class Solution:
    def insert(self, interval: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i,ans=0,[]
        n=len(interval)
        while i<n and interval[i][1]<newInterval[0]:
            ans.append(interval[i])
            i+=1
        while i<n and newInterval[1]>=interval[i][0]:
            newInterval[0]=min(newInterval[0],interval[i][0])
            newInterval[1]=max(newInterval[1],interval[i][1])
            i+=1
        ans.append(newInterval)
        while i<n:
            ans.append(interval[i])
            i+=1
        return ans
        
        

        
            




