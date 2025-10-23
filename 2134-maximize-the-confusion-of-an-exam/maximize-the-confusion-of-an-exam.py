class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,window,ans=0,0,0
        d=defaultdict(int)
        for r in range(len(answerKey)):
            d[answerKey[r]]+=1
            minor=min(d["T"],d["F"])
            if minor<=k:
                window+=1
            else:
                d[answerKey[r-window]]-=1
            ans=max(ans,window)
        return (ans)
