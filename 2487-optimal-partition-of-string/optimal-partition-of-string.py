class Solution:
    def partitionString(self, s: str) -> int:
        seen,count=set(),1
        for ch in s:
            if ch in seen:
                count+=1
                seen=set()
            seen.add(ch)


        return count