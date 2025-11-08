class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """the intersection area i.e the one that is intersected with all regions in the cell is the one with most repeated larger elements becouse most opretion(adding one is performed there) so we find minimum row and minimu col becouse every operation starts from 0,0 to a,b where a,b is operation[i][j]"""
        min_row,min_col=m,n
        for a,b in ops:
            min_row=min(min_row,a)
            min_col=min(min_col,b)
        #number of elment in the subarray is num of row* num of col
        return min_row*min_col
        