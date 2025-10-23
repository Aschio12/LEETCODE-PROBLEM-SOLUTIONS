class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,window,ans=0,0,0
        d=defaultdict(int)
        for r in range(len(answerKey)):
            d[answerKey[r]]+=1
            while d["T"]>k and d["F"]>k:
                d[answerKey[l]]-=1
                window-=1
                l+=1
            window=r-l+1
            ans=max(ans,window)
        return (ans)
