class Solution:
    def numIslands(self, grid) -> int:
        dp = [[False] * len(grid[0]) for _ in range(len(grid))]

        rows, cols = len(grid), len(grid[0])
        def bfs(i, j):
            if grid[i][j] == '1' and dp[i][j] is False:
                dp[i][j] = True
                
                # checking down
                if i + 1 < rows: bfs(i + 1, j)
                
                # checking up
                if i - 1 >= 0: bfs(i-1, j)
                
                # checking right
                if j + 1 < cols: bfs(i, j + 1)
                
                # checking left
                
                if j - 1 >= 0: bfs(i, j -1)
            else:
                pass
                

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and dp[i][j] is False:
                    # if it is an unseend island
                    bfs(i, j)
                    count += 1

        return count
    
sol = Solution()
print(sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))