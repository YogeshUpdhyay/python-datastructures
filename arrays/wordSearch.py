

def findnext(board, word, i, j, nrows, ncols):
    if word == "":
        return True

    # Checking right
    if j+1 < ncols and board[i][j+1] == word[0]:
        temp = board[i][j+1]
        board[i][j+1] = "$"
        if findnext(board, word[1:], i, j+1, nrows, ncols):
            return True
        else:
            board[i][j+1] = temp

    # Checking left
    if j-1 >= 0 and board[i][j-1] == word[0]:
        temp = board[i][j-1]
        board[i][j-1] = "$"
        if findnext(board, word[1:], i, j-1, nrows, ncols):
            return True
        else:
            board[i][j-1] = temp

    # Checking top
    if i-1 >= 0 and board[i-1][j] == word[0]:
        temp = board[i-1][j]
        board[i-1][j] = "$"
        if findnext(board, word[1:], i-1, j, nrows, ncols):
            return True
        else:
            board[i-1][j] = temp

    # Checking down
    if i+1 < nrows and board[i+1][j] == word[0]:
        temp = board[i+1][j]
        board[i+1][j] = "$"
        if findnext(board, word[1:], i+1, j, nrows, ncols):
            return True
        else:
            board[i+1][j] = temp

    return False


def exist(board, word):
    nrows = len(board)
    ncols = len(board[0])

    smap = {}
    for i in range(nrows):
        for j in range(ncols):
            if smap.get(board[i][j]) is None:
                smap[board[i][j]] = [[i, j]]
            else:
                smap[board[i][j]].append([i, j])

    for i in smap.get(word[0], []):
        temp = board[i[0]][i[1]]
        board[i[0]][i[1]] = "$"
        if findnext(board, word[1:], i[0], i[1], nrows, ncols):
            return True
        else:
            board[i[0]][i[1]] = temp

    return False


if __name__ == "__main__":
    nrows = int(input())
    board = []
    for i in range(nrows):
        board.append(list(input().split(" ")))

    word = input()

    print(exist(board, word))
