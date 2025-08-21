class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len,l,current=0,0,0
        for r in range(len(s)):
            current+=abs(ord(s[r])-ord(t[r]))
            while current>maxCost:
                current-=abs(ord(s[l])-ord(t[l]))
                l+=1
            max_len=max(max_len,r-l+1)

        return max_len
                