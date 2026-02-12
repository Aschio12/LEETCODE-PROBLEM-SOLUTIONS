class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d=defaultdict(int)
        for sub in responses:
            ss=set()
            for s in sub:
                ss.add(s)
            for el in ss:
                d[el]+=1
        c,ans=0,""
        for key,val in d.items():
            if val>c:
                c=val
                ans=key
            elif val==c:
                ans=min(ans,key)
        return ans
