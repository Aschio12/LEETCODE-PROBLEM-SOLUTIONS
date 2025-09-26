class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        if len(shifts)==1:
            # Fixed: Proper modulo 26 and character wrapping
            a=chr((ord(s[0]) - ord('a') + shifts[0] % 26) % 26 + ord('a'))
            return a
        p,prefix=0,[]
        for i in shifts:
            p+=i
            prefix.append(p)
        shifting=[]
        pp=prefix[-1]
        shifting.append(pp%26)
        for i in range(len(shifts)-1):
            shifting.append((pp-prefix[i])%26)
        ans=""
        for i in range(len(shifting)):
            # Fixed: Proper character shifting with modulo 26
            current=((ord(s[i]) - ord('a') + shifting[i]) % 26 + ord('a'))
            ans+=chr(current)
        return ans