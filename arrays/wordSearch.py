def findmatch(mat, pat, x, y,
              nrow, ncol, level) :
 
    l = len(pat)
 
    # Pattern matched
    if (level == l) :
        return True
 
    # Out of Boundary
    if (x < 0 or y < 0 or
        x >= nrow or y >= ncol) :
        return False
 
    # If grid matches with a letter
    # while recursion
    if (mat[x][y] == pat[level]) :
 
        # Marking this cell as visited
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")
 
        # finding subpattern in 4 directions
        res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1))
 
        # marking this cell as unvisited again
        mat[x].replace(mat[x][y], temp)
        return res
     
    else : # Not matching then false
        return False
 
# Function to check if the word
# exists in the grid or not
def checkMatch(board, word) :
 
    l = len(word)
    nrow = len(board)
    ncol = len(board[0])
 
    # if total characters in matrix is
    # less then pattern lenghth
    if (l > nrow * ncol) :
        return False
 
    # Traverse in the grid
    for i in range(nrow) :
        for j in range(ncol) :
 
            # If first letter matches, then
            # recur and check
            if (board[i][j] == word[0]) :
                if (findmatch(board, word, i, j,
                              nrow, ncol, 0)) :
                    return True
    return False