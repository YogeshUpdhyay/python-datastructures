def uniquePaths(m: int, n: int) -> int:
    mat = [[-1]*n for i in range(m)]
    mat[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                pass
            else:
                mat[i][j] = (mat[i-1][j] if i-1 >= 0 else 0) + \
                    (mat[i][j-1] if j-1 >= 0 else 0)

    return mat[m-1][n-1]


print(uniquePaths(m=3, n=7))
