def orangesRotting(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    q = []
    nOfOne = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 2:
                q.append([i, j])

            if grid[i][j] == 1:
                nOfOne += 1

    q.append(None)

    time = 0

    while q and q != [None]:
        s = q.pop(0)

        if s is None:
            time += 1
            q.append(None)
        else:
            # Top
            if s[0]-1 >= 0 and grid[s[0]-1][s[1]] == 1:
                grid[s[0]-1][s[1]] = 2
                q.append([s[0]-1, s[1]])
                nOfOne -= 1

            # Down
            if s[0]+1 < nrows and grid[s[0]+1][s[1]] == 1:
                grid[s[0]+1][s[1]] = 2
                q.append([s[0]+1, s[1]])
                nOfOne -= 1

            # Right
            if s[1]+1 < ncols and grid[s[0]][s[1]+1] == 1:
                grid[s[0]][s[1]+1] = 2
                q.append([s[0], s[1]+1])
                nOfOne -= 1

            # Left
            if s[1]-1 >= 0 and grid[s[0]][s[1]-1] == 1:
                grid[s[0]][s[1]-1] = 2
                q.append([s[0], s[1]-1])
                nOfOne -= 1

    if nOfOne > 0:
        return -1
    else:
        return time


n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
print(orangesRotting(grid))
