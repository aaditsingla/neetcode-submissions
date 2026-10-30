class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c ):
            q = deque()

            grid[r][c] = "0"
            q.append((r,c))
            while q:
                rw,cl = q.popleft()
                for rp, cp in directions:
                    if rw+rp < 0 or cl+cp < 0 or rw+rp >= len(grid) or cl+cp >= len(grid[0]) or grid[rw+rp][cl+cp] == "0":
                        continue
                   
                    grid[rw+rp][cl+cp]="0"
                    q.append((rw+rp,cl+cp))

            
            



        rows = len(grid)
        cols = len(grid[0])
        island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island +=1 
                
        return island
        