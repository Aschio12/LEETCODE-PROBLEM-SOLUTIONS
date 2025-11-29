class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        num=[]
        for i in range(len(a)):
            if a[i] not in num:
                num.append(a[i])
        for i in range(len(num)):
            a[i]=num[i]
        for i in range(len(a)-len(num)):
            a.pop()
        return len(a)
