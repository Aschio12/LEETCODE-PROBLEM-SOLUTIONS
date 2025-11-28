class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for index,val in enumerate(s):
            last_index[val]=index
        start,end,ans=0,0,[]
        for i in range(len(s)):
            end=max(end,last_index[s[i]])
            if i==end:
                ans.append(end-start+1)
                start=i+1
        return ans
            