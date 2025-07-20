class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkpal(word):
            return word == word[::-1]

        ans=""
        for i in range(len(s)):
            for j in range(len(ans),len(s)):
                subpal=s[i:j+1]
                if checkpal(subpal) and len(subpal)>len(ans):
                    ans=subpal
        return ans