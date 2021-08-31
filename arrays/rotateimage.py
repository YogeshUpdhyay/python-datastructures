def rotate(matrix):
    n = len(matrix)
    if n == 1:
        return

    for i in range(n//2):
        j = i
        while j < n-i-1:
            matrix[j][n-i-1], matrix[n-i-1][n-1-j], matrix[n-1-j][i], matrix[i][j] = matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-1-j], matrix[n-1-j][i] 
            j += 1
    
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
for i in matrix:
    print(*i, sep=" ")