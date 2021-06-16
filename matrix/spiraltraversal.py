def spiral_traversal(matrix, r, c):
    ans = []
    left, top, right, bottom = 0, 0, c-1, r-1
    dir = 0
    while(left <= right and top <= bottom):
        if dir == 0:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1
            dir+=1
        if dir == 1:
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1
            dir+=1
        if dir == 2:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom-=1
            dir+=1
        if dir == 3:
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left+=1
        dir = (dir+1) % 4
    return ans

if __name__ == '__main__':
    r, c = map(int, input().strip().split(" "))
    matrix = []
    for i in range(r):
        row = list(map(int, input().strip().split(" ")))
        matrix.append(row)
    print(*spiral_traversal(matrix, r, c), sep=" ")
