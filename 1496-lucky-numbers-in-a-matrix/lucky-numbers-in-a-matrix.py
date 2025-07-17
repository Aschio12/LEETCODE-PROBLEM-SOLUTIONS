class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = [min(row) for row in matrix]
        max_cols = [max(col) for col in zip(*matrix)]
        lucky = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_rows[i] and matrix[i][j] == max_cols[j]:
                    lucky.append(matrix[i][j])
        return lucky

