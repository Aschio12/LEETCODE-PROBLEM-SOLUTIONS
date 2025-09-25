class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[0]
        max_alt,current=arr[-1],0
        for i in gain:
            current+=i
            arr.append(current)
            max_alt=max(max_alt,current)
        return max_alt