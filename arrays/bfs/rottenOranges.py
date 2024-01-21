# def orangesRotting(grid):
#     nrows = len(grid)
#     ncols = len(grid[0])

#     q = []
#     nOfOne = 0
#     for i in range(nrows):
#         for j in range(ncols):
#             if grid[i][j] == 2:
#                 q.append([i, j])

#             if grid[i][j] == 1:
#                 nOfOne += 1

#     q.append(None)

#     time = 0

#     while q and q != [None]:
#         s = q.pop(0)

#         if s is None:
#             time += 1
#             q.append(None)
#         else:
#             # Top
#             if s[0]-1 >= 0 and grid[s[0]-1][s[1]] == 1:
#                 grid[s[0]-1][s[1]] = 2
#                 q.append([s[0]-1, s[1]])
#                 nOfOne -= 1

#             # Down
#             if s[0]+1 < nrows and grid[s[0]+1][s[1]] == 1:
#                 grid[s[0]+1][s[1]] = 2
#                 q.append([s[0]+1, s[1]])
#                 nOfOne -= 1

#             # Right
#             if s[1]+1 < ncols and grid[s[0]][s[1]+1] == 1:
#                 grid[s[0]][s[1]+1] = 2
#                 q.append([s[0], s[1]+1])
#                 nOfOne -= 1

#             # Left
#             if s[1]-1 >= 0 and grid[s[0]][s[1]-1] == 1:
#                 grid[s[0]][s[1]-1] = 2
#                 q.append([s[0], s[1]-1])
#                 nOfOne -= 1

#     if nOfOne > 0:
#         return -1
#     else:
#         return time


# n = int(input())
# grid = [list(map(int, input().split())) for i in range(n)]
# print(orangesRotting(grid))


class Solution:
    def orangesRotting(self, grid) -> int:
        q = []
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        # preprocessing
        # this creates the initial queue for the bfs algo and keep a count of 
        # the fresh oranges to see if all the fresh ranges after the bfs have becom rotten or not
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r, c])

        

        # bfs logic
        directions = [[0, 1], [0, -1], [1,0], [-1, 0]]
        while q and fresh > 0:

            for i in range(len(q)):                
                r, c = q.pop(0)
                for dr, dc in directions:

                    row, col = dr + r, dc + c

                    # out of bounds condition and if not a fresh orange
                    if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1:
                        continue


                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1

        
        return time if fresh == 0 else -1

sol = Solution()
print(sol.orangesRotting([[1],[2],[1],[2]]))