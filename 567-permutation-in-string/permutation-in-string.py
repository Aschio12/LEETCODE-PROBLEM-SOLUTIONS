class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count_s1=[0]*26
        count_s2=[0]*26
        l,r=0,len(s1)-1
        for i in range(len(s1)):
            count_s1[ord(s1[i])-97]+=1
            count_s2[ord(s2[i])-97]+=1
        while r<len(s2):
            if count_s2==count_s1:
                return True
            count_s2[ord(s2[l])-97]-=1
            l+=1
            r+=1
            if r<len(s2):
                count_s2[ord(s2[r])-97]+=1
        return False