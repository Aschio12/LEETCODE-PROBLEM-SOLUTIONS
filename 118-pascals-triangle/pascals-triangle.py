class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        row=[1]
    
        for _ in range(numRows-1):
            new_row=[1]
            for i in range(1,len(row)):
                new_row.append(row[i]+row[i-1])
            new_row.append(1)
            ans.append(new_row)
            row=new_row

        return ans
