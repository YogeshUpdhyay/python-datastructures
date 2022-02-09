def isValidSudoku(board):
    used1 = [[0]*9 for i in range(9)]
    used2 = [[0]*9 for i in range(9)]
    used3 = [[0]*9 for i in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = int(board[i][j]) - 1
                k = (i//3) * 3 + (j // 3)
                if(used1[i][num] or used2[j][num] or used3[k][num]):
                    return False
                used1[i][num] = used2[j][num] = used3[k][num] = 1

    return True
