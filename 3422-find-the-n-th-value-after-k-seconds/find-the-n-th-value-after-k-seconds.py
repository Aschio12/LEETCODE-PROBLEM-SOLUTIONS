class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr=[1]*n
        for i in range(k):
            for i in range(1,n):
                arr[i]+=arr[i-1]
        return arr[-1]%(10**9 + 7)