from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans,seen=[],defaultdict(int)
        for l in range(len(s)-9):
            current=s[l:l+10]
            seen[current]+=1

        for key,val in seen.items():
            if val>1:
                ans.append(key)
    
        return ans

