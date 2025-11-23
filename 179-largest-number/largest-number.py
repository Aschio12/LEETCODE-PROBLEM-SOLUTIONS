class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array=list(map(str,nums))
        array.sort(key=lambda x:x*10,reverse=True)
        largest="".join(array)
        return largest if largest[0]!="0" else "0"

       