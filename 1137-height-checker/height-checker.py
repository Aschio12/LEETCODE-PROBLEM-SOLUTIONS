class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        inordered=0
        for i1,i2 in zip(expected,heights):
            if i1!=i2:
                inordered+=1
        return inordered

