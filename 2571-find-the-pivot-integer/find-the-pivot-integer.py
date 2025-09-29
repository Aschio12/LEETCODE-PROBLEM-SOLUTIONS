class Solution:
    def pivotInteger(self, n: int) -> int:
        arr,prefix,p=[],[],0
        for i in range(1,n+1):
            arr.append(i)
            p+=i
            prefix.append(p)
        tot=prefix[-1]
        for i in range(len(prefix)):
            if tot-prefix[i]+arr[i]==prefix[i]:
                return i+1
        return -1

