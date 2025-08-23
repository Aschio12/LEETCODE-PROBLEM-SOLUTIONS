
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen,ans=set(),set()
        for l in range(len(s)-9):
            current=s[l:l+10]
            if current in seen:
                ans.add(current)
            seen.add(current)
        return list(ans)

