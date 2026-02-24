class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        ans=""
        for i in range(len(dictionary)):
            current=dictionary[i]
            c,ss=0,0
            while c<len(current) and ss<len(s):
                if current[c]==s[ss]:
                    c+=1
                    ss+=1
                else:
                    ss+=1
            if c==len(current):
                if len(current)>len(ans):
                    ans=current
                elif len(current)==len(ans):
                    ans=min(ans,current)
        return ans
            

