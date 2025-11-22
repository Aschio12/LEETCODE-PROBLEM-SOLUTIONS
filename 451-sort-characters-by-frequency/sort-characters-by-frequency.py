class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        val_reps=[]
        for key,val in c.items():
            val_reps.append((val,key))
        val_reps.sort(reverse=True)
        ans=""
        for toup in val_reps:
            ans+=(toup[1]*toup[0])
        return ans
