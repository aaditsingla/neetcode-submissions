class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c ):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)



        rows = len(grid)
        cols = len(grid[0])
        island = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island +=1 
                
        return island
        