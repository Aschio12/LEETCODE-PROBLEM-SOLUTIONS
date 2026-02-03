class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        while i>-1:
            if digits[i]==9:
                # print("in here")
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                return digits   
        # print(digits)
        digits.append(0)
        digits[0]=1
        return digits