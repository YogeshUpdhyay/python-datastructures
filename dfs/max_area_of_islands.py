from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        visited = set()
        def bfs(r ,c):
            q = deque()

            q.append((r,c))
            area = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()

                    if (r,c) in visited:
                        continue 

                    area += 1
                    visited.add((r,c))

                    for dr, dc in [[0,1], [0, -1], [1,0], [-1,0]]:
                        cur_r, cur_c = dr + r, dc + c

                        if cur_c >= 0 and cur_c < COLS and cur_r >= 0 and cur_r < ROWS and grid[cur_r][cur_c]:
                            q.append((cur_r, cur_c))

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = bfs(i , j)
                    max_area = max(max_area, area)

        return max_area
    
sol = Solution()
print(sol.maxAreaOfIsland([[1,1]]))