class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        found=False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    s_r,s_c=i,j
                    found=True
                    break
            if found:
                break
        else:
            return 0

        visited=set()
        p=0
       
        def dfs(r,c):
            nonlocal p,visited
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
                return

            if (r,c) not in visited and grid[r][c]==1:
                visited.add((r,c))
                if (r-1>=0 and grid[r-1][c]==0) or r==0:
                    p+=1
                if c-1>=0 and grid[r][c-1]==0 or c==0:
                    p+=1
                if (r+1<len(grid) and grid[r+1][c]==0) or r==len(grid)-1:
                    p+=1
                if c+1<len(grid[0]) and grid[r][c+1]==0 or c==len(grid[0])-1:
                    p+=1
            else:
                return
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)

        dfs(s_r,s_c)
        return p