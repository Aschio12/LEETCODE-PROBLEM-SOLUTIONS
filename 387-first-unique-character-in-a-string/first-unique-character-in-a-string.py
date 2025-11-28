class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for index,val in enumerate(s):
            if val not in d:
                d[val]=1
            else:
                d[val]+=1
        
        
        for i,ch in enumerate(s):
            if d[ch]==1:
                return i

        return  -1
