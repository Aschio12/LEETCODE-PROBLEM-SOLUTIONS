class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tot=sum(arr)
        if tot%3!=0:
            return False
        target,count,current=tot/3,0,0
        for num in arr:
            current+=num
            if current==target:
                count+=1
                current=0
        return count>=3

        