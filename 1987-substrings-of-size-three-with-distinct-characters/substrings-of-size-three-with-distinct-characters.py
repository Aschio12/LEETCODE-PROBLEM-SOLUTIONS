class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for l in range(len(s)-2):
            current=s[l:l+3]
            if current[0]!=current[1] and current[0]!=current[-1] and current[1]!=current[-1]:
                count+=1

        return count
