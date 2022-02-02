def findNoofAdjOnes(i, j, nrows, ncols, board):
    count = 0
    # Above row
    if i-1 >= 0:
        if j-1 >= 0 and board[i-1][j-1] == 1:
            count += 1
        if board[i-1][j] == 1:
            count += 1
        if j+1 < ncols and board[i-1][j+1] == 1:
            count += 1

    # Level
    if j-1 >= 0 and board[i][j-1] == 1:
        count += 1

    if j+1 < ncols and board[i][j+1] == 1:
        count += 1

    # Below row

    if i+1 < nrows:
        if j-1 >= 0 and board[i+1][j-1] == 1:
            count += 1
        if board[i+1][j] == 1:
            count += 1
        if j+1 < ncols and board[i+1][j+1] == 1:
            count += 1

    return count


def gameOfLife(board):

    nrows = len(board)
    ncols = len(board[0])

    chgMat = [[-1]*ncols for i in range(nrows)]

    # Finding adjacent ones
    for i in range(nrows):
        for j in range(ncols):
            nones = findNoofAdjOnes(i, j, nrows, ncols, board)
            chgMat[i][j] = nones

    # Replacing the board
    for i in range(nrows):
        for j in range(ncols):
            if board[i][j] == 0 and chgMat[i][j] == 3:
                board[i][j] = 1

            if board[i][j] == 1:
                if chgMat[i][j] < 2:
                    board[i][j] = 0

                if chgMat[i][j] > 3:
                    board[i][j] = 0

    return


n = int(input().strip())
board = [list(map(int, input().split())) for i in range(n)]
gameOfLife(board)
print(board)
