class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0
        s=""
        l,r=0,0
        while r<len(chars):
            if chars[l]==chars[r]:
                r+=1
                if r==len(chars):
                    if r-l>1:
                        s+=chars[l]+str(r-l)
                    else:
                        s+=chars[l]
                    
            else:
                if r-l>1:
                    s+=chars[l]+str(r-l)
                else:
                    s+=chars[l]
                l=r
        print(s)

                
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)
            
        